#!/usr/bin/env python3
"""Post-build SEO validation for the Real-World Japanese static site.

Runs against a built `dist/` directory and checks the integrity of the SEO
plumbing that the source can't guarantee on its own:

  (a) hreflang    — alternates are absolute, self-referencing, reciprocal, and
                    every target actually exists in dist (no 404 alternates).
  (b) orphans     — article pages with zero in-content inbound internal links.
  (c) dates       — JSON-LD dateModified/​datePublished matches sitemap lastmod,
                    and lastmod isn't a single build-time value stamped on all.
  (d) velocity    — too many articles published in the trailing 7 days (per
                    language) trips a scaled-content-abuse guard.
  (e) robots      — reports nosnippet/max-snippet directives and checks
                    robots.txt for accidental crawler blocking.
  (f) translation — source-side gate: non-draft articles still marked
                    humanReviewed: false are awaiting native review.

Standard library only; targets Python 3.9+.

Usage:
    python3 scripts/validate_seo.py <dist_dir> \
        [--velocity-cap N] [--skip-velocity] [--src-dir PATH]

Exit code 1 if any FAIL is reported, else 0.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import json
from datetime import datetime, timezone, timedelta
from html.parser import HTMLParser
from typing import Dict, List, Optional, Set, Tuple
from xml.etree import ElementTree as ET

SITE_ORIGIN = "https://realworldjapanese.com"

# URL path shape for an article page, e.g. /en/guides/keigo-guide/ . The final
# segment is the article slug; a purely-numeric segment under /posts/ is a
# pagination index page (/en/posts/2/), not an article, so it's excluded below.
ARTICLE_PATH_RE = re.compile(r"^/(en|ja|vi|id|pt|th|zh-TW)/(guides|posts|products)/([^/]+)/?$")

# Languages considered when validating hreflang self-reference. Kept in sync
# with src/config/languages.ts active + inactive; only the *active* set is
# emitted, but we accept any known code as valid in an href.
KNOWN_LANGS = {"en", "ja", "vi", "id", "pt", "th", "zh-TW"}


# --------------------------------------------------------------------------- #
# Reporting
# --------------------------------------------------------------------------- #


class Report:
    """Accumulates PASS / WARN / FAIL lines and prints a grouped summary."""

    def __init__(self) -> None:
        self.passes: List[str] = []
        self.warns: List[str] = []
        self.fails: List[str] = []

    def ok(self, msg: str) -> None:
        self.passes.append(msg)

    def warn(self, msg: str) -> None:
        self.warns.append(msg)

    def fail(self, msg: str) -> None:
        self.fails.append(msg)

    def render(self) -> str:
        lines: List[str] = []
        lines.append("=" * 68)
        lines.append("SEO VALIDATION REPORT")
        lines.append("=" * 68)
        if self.fails:
            lines.append("")
            lines.append("FAIL ({}):".format(len(self.fails)))
            for m in self.fails:
                lines.append("  ✗ " + m)
        if self.warns:
            lines.append("")
            lines.append("WARN ({}):".format(len(self.warns)))
            for m in self.warns:
                lines.append("  ! " + m)
        lines.append("")
        lines.append("PASS ({}):".format(len(self.passes)))
        for m in self.passes:
            lines.append("  ✓ " + m)
        lines.append("")
        lines.append("-" * 68)
        verdict = "FAIL" if self.fails else ("PASS (with warnings)" if self.warns else "PASS")
        lines.append("RESULT: {}  ({} fail / {} warn / {} pass)".format(
            verdict, len(self.fails), len(self.warns), len(self.passes)))
        lines.append("-" * 68)
        return "\n".join(lines)


# --------------------------------------------------------------------------- #
# HTML parsing helpers
# --------------------------------------------------------------------------- #


class LinkExtractor(HTMLParser):
    """Collects hreflang alternates, canonical, JSON-LD blobs, meta-robots,
    and <a href> links — noting which links sit inside nav/header/footer so
    in-content link analysis can exclude chrome."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.alternates: List[Tuple[str, str]] = []  # (hreflang, href)
        self.canonical: Optional[str] = None
        self.jsonld_blobs: List[str] = []
        self.meta_robots: List[str] = []
        self.content_links: List[str] = []  # <a href> outside chrome regions
        self.chrome_links: List[str] = []   # <a href> inside nav/header/footer
        self._chrome_depth = 0
        self._in_jsonld = False
        self._jsonld_buf: List[str] = []

    def handle_starttag(self, tag: str, attrs_list) -> None:
        attrs = dict(attrs_list)
        if tag in ("nav", "header", "footer"):
            self._chrome_depth += 1
        elif tag == "link":
            rel = (attrs.get("rel") or "").lower()
            if rel == "alternate" and attrs.get("hreflang"):
                self.alternates.append((attrs["hreflang"], attrs.get("href", "")))
            elif rel == "canonical":
                self.canonical = attrs.get("href")
        elif tag == "meta":
            name = (attrs.get("name") or "").lower()
            if name == "robots" and attrs.get("content"):
                self.meta_robots.append(attrs["content"].lower())
        elif tag == "script":
            if (attrs.get("type") or "").lower() == "application/ld+json":
                self._in_jsonld = True
                self._jsonld_buf = []
        elif tag == "a":
            href = attrs.get("href")
            if href:
                if self._chrome_depth > 0:
                    self.chrome_links.append(href)
                else:
                    self.content_links.append(href)

    def handle_endtag(self, tag: str) -> None:
        if tag in ("nav", "header", "footer") and self._chrome_depth > 0:
            self._chrome_depth -= 1
        elif tag == "script" and self._in_jsonld:
            self.jsonld_blobs.append("".join(self._jsonld_buf))
            self._in_jsonld = False

    def handle_data(self, data: str) -> None:
        if self._in_jsonld:
            self._jsonld_buf.append(data)


def parse_html(path: str) -> LinkExtractor:
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        parser = LinkExtractor()
        parser.feed(fh.read())
    return parser


# --------------------------------------------------------------------------- #
# URL / path helpers
# --------------------------------------------------------------------------- #


def url_to_path(url: str) -> Optional[str]:
    """Normalize a same-site URL (absolute or root-relative) to a path with a
    single leading slash and a trailing slash preserved. Returns None for
    off-site or non-http links (mailto:, #anchor, external)."""
    if not url:
        return None
    if url.startswith("#") or url.startswith("mailto:") or url.startswith("tel:"):
        return None
    if url.startswith("http://") or url.startswith("https://"):
        if not url.startswith(SITE_ORIGIN):
            return None
        path = url[len(SITE_ORIGIN):]
    elif url.startswith("/"):
        path = url
    else:
        # Relative link; skip (site emits absolute/root-relative).
        return None
    # Strip query/fragment.
    path = path.split("#", 1)[0].split("?", 1)[0]
    if not path:
        path = "/"
    return path


def path_to_dist_file(dist_dir: str, path: str) -> str:
    """Map a URL path (directory format) to its dist HTML file."""
    rel = path.strip("/")
    if rel == "":
        return os.path.join(dist_dir, "index.html")
    return os.path.join(dist_dir, rel.replace("/", os.sep), "index.html")


def is_article_path(path: str) -> bool:
    m = ARTICLE_PATH_RE.match(path)
    if not m:
        return False
    collection, slug = m.group(2), m.group(3)
    # /posts/<n>/ is a paginated blog index, not an article.
    if collection == "posts" and slug.isdigit():
        return False
    return True


def html_path_from_file(dist_dir: str, file_path: str) -> str:
    """Reverse of path_to_dist_file: dist file → URL path (with slashes)."""
    rel = os.path.relpath(file_path, dist_dir)
    rel_dir = os.path.dirname(rel)
    if rel_dir in ("", "."):
        return "/"
    return "/" + rel_dir.replace(os.sep, "/") + "/"


# --------------------------------------------------------------------------- #
# Collection of dist pages
# --------------------------------------------------------------------------- #


def collect_html_files(dist_dir: str) -> List[str]:
    out: List[str] = []
    for root, _dirs, files in os.walk(dist_dir):
        for name in files:
            if name == "index.html" or name.endswith(".html"):
                out.append(os.path.join(root, name))
    return out


# --------------------------------------------------------------------------- #
# JSON-LD helpers
# --------------------------------------------------------------------------- #


def extract_blogposting(blobs: List[str]) -> Optional[dict]:
    for blob in blobs:
        try:
            data = json.loads(blob)
        except (ValueError, TypeError):
            continue
        candidates = data if isinstance(data, list) else [data]
        for obj in candidates:
            if isinstance(obj, dict) and obj.get("@type") == "BlogPosting":
                return obj
    return None


def normalize_iso(value: Optional[str]) -> Optional[str]:
    """Parse an ISO 8601 timestamp to a timezone-aware UTC datetime's ISO
    string (second precision) for stable comparison. Returns None on failure."""
    if not value:
        return None
    v = value.strip()
    # Python 3.9's fromisoformat doesn't accept a trailing 'Z'.
    if v.endswith("Z"):
        v = v[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(v)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc).replace(microsecond=0).isoformat()


def parse_iso_dt(value: Optional[str]) -> Optional[datetime]:
    if not value:
        return None
    v = value.strip()
    if v.endswith("Z"):
        v = v[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(v)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


# --------------------------------------------------------------------------- #
# Sitemap parsing
# --------------------------------------------------------------------------- #

SM_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"


def parse_sitemaps(dist_dir: str) -> Dict[str, Optional[str]]:
    """Return {url_path: lastmod_or_None} from all dist/sitemap-*.xml files
    (excluding the index)."""
    result: Dict[str, Optional[str]] = {}
    for name in sorted(os.listdir(dist_dir)):
        if not (name.startswith("sitemap-") and name.endswith(".xml")):
            continue
        if name == "sitemap-index.xml":
            continue
        full = os.path.join(dist_dir, name)
        try:
            tree = ET.parse(full)
        except ET.ParseError:
            continue
        root = tree.getroot()
        for url_el in root.findall(SM_NS + "url"):
            loc_el = url_el.find(SM_NS + "loc")
            if loc_el is None or not loc_el.text:
                continue
            path = url_to_path(loc_el.text.strip())
            if path is None:
                continue
            lm_el = url_el.find(SM_NS + "lastmod")
            lastmod = lm_el.text.strip() if (lm_el is not None and lm_el.text) else None
            result[path] = lastmod
    return result


# --------------------------------------------------------------------------- #
# Check (a): hreflang
# --------------------------------------------------------------------------- #


def check_hreflang(
    report: Report,
    dist_dir: str,
    pages: Dict[str, LinkExtractor],
) -> None:
    # Build a global map of what each article page lists, for reciprocity.
    # page_path -> set of alternate paths (excluding x-default).
    listed: Dict[str, Set[str]] = {}
    fails = 0

    article_pages = {p: ex for p, ex in pages.items() if is_article_path(p)}

    for path, ex in article_pages.items():
        alt_paths: Set[str] = set()
        has_self = False
        x_default_paths: List[str] = []
        for hreflang, href in ex.alternates:
            if not (href.startswith("http://") or href.startswith("https://")):
                report.fail("hreflang: non-absolute href on {} → {!r}".format(path, href))
                fails += 1
                continue
            target = url_to_path(href)
            if hreflang.lower() == "x-default":
                if target:
                    x_default_paths.append(target)
                continue
            if hreflang not in KNOWN_LANGS:
                report.warn("hreflang: unknown lang '{}' on {}".format(hreflang, path))
            if target:
                alt_paths.add(target)
                if target == path:
                    has_self = True
                # Existence check: target file must exist in dist.
                if not os.path.isfile(path_to_dist_file(dist_dir, target)):
                    report.fail("hreflang: {} points to missing page {}".format(path, target))
                    fails += 1
        listed[path] = alt_paths

        if not has_self:
            report.fail("hreflang: {} has no self-referencing alternate".format(path))
            fails += 1

        # x-default rules: if present, must resolve to an existing en page that
        # is also among this page's alternates.
        for xd in x_default_paths:
            if not os.path.isfile(path_to_dist_file(dist_dir, xd)):
                report.fail("hreflang: x-default on {} points to missing {}".format(path, xd))
                fails += 1
            elif not xd.startswith("/en/"):
                report.warn("hreflang: x-default on {} is not an /en/ URL ({})".format(path, xd))

    # Reciprocity: if A lists B (B != A), B must list A.
    for a_path, targets in listed.items():
        for b_path in targets:
            if b_path == a_path:
                continue
            if b_path not in listed:
                # b isn't an article page we parsed; only flag if it exists in dist.
                if os.path.isfile(path_to_dist_file(dist_dir, b_path)):
                    report.fail("hreflang reciprocity: {} lists {} but that page has no alternates".format(a_path, b_path))
                    fails += 1
                continue
            if a_path not in listed[b_path]:
                report.fail("hreflang reciprocity: {} lists {} but not vice versa".format(a_path, b_path))
                fails += 1

    if fails == 0:
        report.ok("hreflang: {} article pages — all absolute, self-referencing, reciprocal, no 404 alternates".format(len(article_pages)))


# --------------------------------------------------------------------------- #
# Check (b): orphans
# --------------------------------------------------------------------------- #


def check_orphans(
    report: Report,
    pages: Dict[str, LinkExtractor],
) -> None:
    article_pages = [p for p in pages if is_article_path(p)]

    # Inbound counts from in-content links of OTHER pages.
    inbound_content: Dict[str, int] = {p: 0 for p in article_pages}
    inbound_any: Dict[str, int] = {p: 0 for p in article_pages}

    for src_path, ex in pages.items():
        content_targets = set()
        for href in ex.content_links:
            t = url_to_path(href)
            if t and t != src_path:
                content_targets.add(t)
        any_targets = set(content_targets)
        for href in ex.chrome_links:
            t = url_to_path(href)
            if t and t != src_path:
                any_targets.add(t)
        for t in content_targets:
            if t in inbound_content:
                inbound_content[t] += 1
        for t in any_targets:
            if t in inbound_any:
                inbound_any[t] += 1

    orphans = [p for p in article_pages if inbound_content[p] == 0]
    near = [p for p in article_pages if inbound_content[p] == 1]

    # If chrome-filtering looks broken (every page has zero in-content inbound
    # but plenty of any-inbound), report both numbers instead of crying wolf.
    total_content_inbound = sum(inbound_content.values())
    total_any_inbound = sum(inbound_any.values())
    chrome_filter_suspect = total_content_inbound == 0 and total_any_inbound > 0

    if chrome_filter_suspect:
        report.warn(
            "orphans: in-content link filtering produced 0 inbound links for all {} article pages; "
            "chrome (nav/header/footer) detection may be unreliable. Reporting raw inbound instead.".format(
                len(article_pages)))
        orphans_any = [p for p in article_pages if inbound_any[p] == 0]
        if orphans_any:
            for p in sorted(orphans_any):
                report.fail("orphan (raw, no inbound links at all): {}".format(p))
        else:
            report.ok("orphans: every article page has ≥1 inbound link (raw count; chrome filter unreliable)")
        return

    if orphans:
        for p in sorted(orphans):
            report.fail("orphan: {} has 0 in-content inbound internal links".format(p))
    if near:
        for p in sorted(near):
            report.warn("thinly-linked: {} has only 1 in-content inbound internal link".format(p))
    if not orphans:
        report.ok("orphans: all {} article pages have ≥1 in-content inbound internal link ({} with exactly 1)".format(
            len(article_pages), len(near)))


# --------------------------------------------------------------------------- #
# Check (c): date integrity
# --------------------------------------------------------------------------- #


def check_dates(
    report: Report,
    pages: Dict[str, LinkExtractor],
    sitemap: Dict[str, Optional[str]],
) -> None:
    article_pages = {p: ex for p, ex in pages.items() if is_article_path(p)}
    fails = 0
    lastmods: List[str] = []
    checked = 0

    for path, ex in article_pages.items():
        bp = extract_blogposting(ex.jsonld_blobs)
        if bp is None:
            report.warn("dates: {} has no BlogPosting JSON-LD".format(path))
            continue
        # lastmod formula in the sitemap hook: modDatetime ?? pubDatetime.
        jsonld_effective = bp.get("dateModified") or bp.get("datePublished")
        jl_norm = normalize_iso(jsonld_effective)

        sm_lastmod = sitemap.get(path)
        if sm_lastmod is None:
            report.warn("dates: {} present in dist but has no sitemap lastmod".format(path))
            continue
        checked += 1
        lastmods.append(normalize_iso(sm_lastmod) or sm_lastmod)

        sm_norm = normalize_iso(sm_lastmod)
        if jl_norm is None:
            report.warn("dates: {} JSON-LD has no parseable date".format(path))
            continue
        if jl_norm != sm_norm:
            report.fail("dates: {} JSON-LD effective date {} != sitemap lastmod {}".format(
                path, jl_norm, sm_norm))
            fails += 1

    # Single-value lastmod signature: >90% identical → likely new Date().
    if lastmods:
        from collections import Counter
        most_common_val, most_common_n = Counter(lastmods).most_common(1)[0]
        ratio = most_common_n / len(lastmods)
        if len(lastmods) >= 5 and ratio > 0.90:
            report.fail(
                "dates: {:.0f}% of {} article lastmods share one value ({}) — "
                "looks like build-time stamping (new Date()), which forfeits lastmod trust".format(
                    ratio * 100, len(lastmods), most_common_val))
            fails += 1

    if fails == 0 and checked > 0:
        report.ok("dates: {} article pages — JSON-LD date matches sitemap lastmod, no build-time-stamp signature".format(checked))
    elif checked == 0:
        report.warn("dates: no article pages had both JSON-LD and sitemap lastmod to compare")


# --------------------------------------------------------------------------- #
# Check (d): velocity
# --------------------------------------------------------------------------- #


def check_velocity(
    report: Report,
    pages: Dict[str, LinkExtractor],
    cap: int,
    skip: bool,
) -> None:
    now = datetime.now(timezone.utc)
    window_start = now - timedelta(days=7)
    per_lang: Dict[str, int] = {}

    for path, ex in pages.items():
        if not is_article_path(path):
            continue
        bp = extract_blogposting(ex.jsonld_blobs)
        if bp is None:
            continue
        pub = parse_iso_dt(bp.get("datePublished"))
        if pub is None:
            continue
        if pub >= window_start and pub <= now:
            lang = path.split("/", 2)[1]
            per_lang[lang] = per_lang.get(lang, 0) + 1

    breaches = {lang: n for lang, n in per_lang.items() if n > cap}

    override = os.environ.get("SEO_VELOCITY_OVERRIDE") == "1"
    downgrade = skip or override

    if not breaches:
        report.ok("velocity: no language exceeds {} articles published in the trailing 7 days".format(cap))
        return

    for lang, n in sorted(breaches.items()):
        msg = ("velocity: {} articles published in [{}] in the last 7 days (cap {}); "
               "high publish velocity can trigger Google's scaled-content-abuse heuristics".format(
                   n, lang, cap))
        if downgrade:
            report.warn(msg + " [downgraded to WARN]")
        else:
            report.fail(msg)


# --------------------------------------------------------------------------- #
# Check (e): robots hygiene
# --------------------------------------------------------------------------- #


def check_robots(
    report: Report,
    dist_dir: str,
    pages: Dict[str, LinkExtractor],
) -> None:
    snippet_flagged: List[str] = []
    for path, ex in pages.items():
        for content in ex.meta_robots:
            if "nosnippet" in content or "max-snippet" in content:
                snippet_flagged.append("{} → '{}'".format(path, content))
                break
    if snippet_flagged:
        report.warn("robots: {} page(s) carry nosnippet/max-snippet (reported, not failed):".format(len(snippet_flagged)))
        for line in snippet_flagged[:20]:
            report.warn("  " + line)
    else:
        report.ok("robots: no nosnippet/max-snippet directives found in article/page HTML")

    robots_path = os.path.join(dist_dir, "robots.txt")
    if not os.path.isfile(robots_path):
        report.warn("robots: no robots.txt in dist (crawlers default to full access — OK, just noting)")
        return

    with open(robots_path, "r", encoding="utf-8", errors="replace") as fh:
        robots_txt = fh.read()

    crawlers = ["Googlebot", "OAI-SearchBot", "PerplexityBot", "Google-Extended"]
    blocked = detect_blocked_crawlers(robots_txt, crawlers)
    if blocked:
        for bot in blocked:
            report.fail("robots.txt appears to block '{}' from crawling ('Disallow: /' in its group or the catch-all)".format(bot))
    else:
        report.ok("robots.txt: no accidental full blocks for {}".format(", ".join(crawlers)))


def detect_blocked_crawlers(robots_txt: str, crawlers: List[str]) -> List[str]:
    """Very small robots.txt group parser. Returns crawler names whose effective
    group contains a `Disallow: /` (full block). A bot is governed by its own
    named group if present, else by the `*` group."""
    groups: Dict[str, List[str]] = {}
    current_agents: List[str] = []
    started_rules = False
    for raw_line in robots_txt.splitlines():
        line = raw_line.split("#", 1)[0].strip()
        if not line:
            continue
        if ":" not in line:
            continue
        field, value = line.split(":", 1)
        field = field.strip().lower()
        value = value.strip()
        if field == "user-agent":
            if started_rules:
                current_agents = []
                started_rules = False
            current_agents.append(value)
            groups.setdefault(value, [])
        elif field in ("allow", "disallow"):
            started_rules = True
            for agent in current_agents:
                groups.setdefault(agent, []).append("{}:{}".format(field, value))

    def group_blocks(agent_key: str) -> bool:
        rules = groups.get(agent_key)
        if rules is None:
            return False
        # A bare "Disallow: /" with no overriding Allow blocks everything.
        disallow_root = any(r == "disallow:/" for r in rules)
        allow_present = any(r.startswith("allow:") and r != "allow:" for r in rules)
        return disallow_root and not allow_present

    blocked: List[str] = []
    for bot in crawlers:
        # Case-insensitive match on the group key.
        key = None
        for k in groups:
            if k.lower() == bot.lower():
                key = k
                break
        if key is not None:
            if group_blocks(key):
                blocked.append(bot)
        else:
            # Governed by the wildcard group.
            if group_blocks("*"):
                blocked.append(bot)
    return blocked


# --------------------------------------------------------------------------- #
# Check (f): translation QA gate (source-side)
# --------------------------------------------------------------------------- #

# Matches a top-level `humanReviewed: <bool>` / `draft: <bool>` line in
# frontmatter. Anchored to start-of-line with no leading whitespace so a nested
# key (e.g. under a `faqs:` list item, which is indented) is never misread.
_HUMAN_REVIEWED_RE = re.compile(r"(?m)^humanReviewed:\s*(true|false)\b")
_DRAFT_RE = re.compile(r"(?m)^draft:\s*(true|false)\b")


def _read_frontmatter(text: str) -> Optional[str]:
    """Return the raw frontmatter block (between the leading `---` fences), or
    None when the file has no frontmatter."""
    m = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.DOTALL)
    return m.group(1) if m else None


def check_translation_gate(report: Report, src_data_dir: str) -> None:
    """Source-side QA gate: a non-draft article still marked
    `humanReviewed: false` is a localized article that hasn't cleared native
    review yet. Articles with no `humanReviewed` key at all are legacy /
    base-language and are fine."""
    if not os.path.isdir(src_data_dir):
        report.warn("translation: source data dir not found ({}); skipping human-review gate".format(src_data_dir))
        return

    awaiting: List[str] = []
    scanned = 0
    for root, _dirs, files in os.walk(src_data_dir):
        for name in files:
            if not name.endswith(".mdx"):
                continue
            full = os.path.join(root, name)
            try:
                with open(full, "r", encoding="utf-8", errors="replace") as fh:
                    text = fh.read()
            except OSError:
                continue
            block = _read_frontmatter(text)
            if block is None:
                continue
            scanned += 1
            hr = _HUMAN_REVIEWED_RE.search(block)
            if hr is None:
                # No humanReviewed key → legacy/base article, fine.
                continue
            if hr.group(1) != "false":
                continue
            dr = _DRAFT_RE.search(block)
            is_draft = dr is not None and dr.group(1) == "true"
            if is_draft:
                continue
            awaiting.append(os.path.relpath(full, src_data_dir))

    if awaiting:
        for rel in sorted(awaiting):
            report.fail(
                "translation: {} — localized article awaiting human review; flip "
                "humanReviewed: true after native review (seo-article-localize QA gate)".format(rel))
    else:
        report.ok("translation: no non-draft articles are stuck at humanReviewed: false ({} .mdx scanned)".format(scanned))


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description="Post-build SEO validation for dist/.")
    parser.add_argument("dist_dir", help="Path to the built dist/ directory")
    parser.add_argument("--velocity-cap", type=int, default=3,
                        help="Max articles published per language in trailing 7 days before velocity fails (default 3)")
    parser.add_argument("--skip-velocity", action="store_true",
                        help="Downgrade the velocity check from FAIL to WARN")
    parser.add_argument("--src-dir", default=None,
                        help="Path to src/data for the translation QA gate "
                             "(defaults to <repo>/src/data relative to this script)")
    args = parser.parse_args(argv)

    dist_dir = args.dist_dir
    if not os.path.isdir(dist_dir):
        sys.stderr.write("error: dist dir not found: {}\n".format(dist_dir))
        return 2

    # Source-side check (f) reads frontmatter, not dist. Resolve src/data from
    # the script location so cwd doesn't matter.
    if args.src_dir:
        src_data_dir = args.src_dir
    else:
        repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        src_data_dir = os.path.join(repo_root, "src", "data")

    report = Report()

    html_files = collect_html_files(dist_dir)
    if not html_files:
        sys.stderr.write("error: no HTML files found under {}\n".format(dist_dir))
        return 2

    # Parse each page once; key by URL path.
    pages: Dict[str, LinkExtractor] = {}
    for f in html_files:
        path = html_path_from_file(dist_dir, f)
        pages[path] = parse_html(f)

    sitemap = parse_sitemaps(dist_dir)

    check_hreflang(report, dist_dir, pages)
    check_orphans(report, pages)
    check_dates(report, pages, sitemap)
    check_velocity(report, pages, args.velocity_cap, args.skip_velocity)
    check_robots(report, dist_dir, pages)
    check_translation_gate(report, src_data_dir)

    print(report.render())
    return 1 if report.fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
