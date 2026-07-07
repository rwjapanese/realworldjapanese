#!/usr/bin/env python3
"""
ai_citation_audit.py — Monthly "share of voice" audit for AI answer engines.

Ask Perplexity (Sonar) a fixed list of English-learner questions that match the
topics we cover, collect the citation URLs behind each answer, and measure how
often realworldjapanese.com is cited. This is the AI-search analogue of a GSC
rank check: it tells us whether the LLMs that increasingly mediate search are
surfacing our pages, and which competitor domains own the answers we don't.

Usage:
    python3 scripts/ai_citation_audit.py            # run the full audit
    python3 scripts/ai_citation_audit.py --dry-run  # just print the questions

Questions are read from scripts/citation_questions.txt (one per line; blank
lines and #-comments ignored).

Config (read from scripts/.env, the repo .env, or real environment):
    PERPLEXITY_API_KEY   required; get one at https://www.perplexity.ai/settings/api

Output:
    - Appends one row per run to specs/audits/citation-share.csv
      (date, n_questions, n_cited, share, top_competitor_domains).
    - Prints a readable summary (share of voice + citation domain frequency).

Exit codes: 0 ok, 2 missing PERPLEXITY_API_KEY.
"""
import argparse
import csv
import datetime as dt
import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"
QUESTIONS_FILE = SCRIPTS_DIR / "citation_questions.txt"
CSV_PATH = REPO_ROOT / "specs" / "audits" / "citation-share.csv"

OUR_DOMAIN = "realworldjapanese.com"
PERPLEXITY_URL = "https://api.perplexity.ai/chat/completions"
PERPLEXITY_MODEL = "sonar"
REQUEST_SLEEP_SEC = 1.0  # be polite between API calls
CSV_HEADER = ["date", "n_questions", "n_cited", "share", "top_competitor_domains"]


def load_env():
    """Load KEY=VALUE pairs from scripts/.env and repo-root .env into os.environ
    (without overwriting anything already set in the real environment). Mirrors
    seo_report.py's load_env so PERPLEXITY_API_KEY can live in scripts/.env
    alongside the Google keys. Replicated rather than imported to keep this
    script standalone (no Google API deps pulled in at import time)."""
    for env_path in (SCRIPTS_DIR / ".env", REPO_ROOT / ".env"):
        if not env_path.exists():
            continue
        for raw in env_path.read_text().splitlines():
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if key and key not in os.environ:
                os.environ[key] = val


def load_questions():
    """Read questions from QUESTIONS_FILE, skipping blanks and #-comments."""
    if not QUESTIONS_FILE.exists():
        sys.exit(f"✗ Questions file not found: {QUESTIONS_FILE}")
    questions = []
    for raw in QUESTIONS_FILE.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        questions.append(line)
    if not questions:
        sys.exit(f"✗ No questions found in {QUESTIONS_FILE}")
    return questions


def domain_of(url):
    """Return the registrable-ish host of a URL, lowercased, without a leading
    'www.'. Returns '' for anything unparseable."""
    if not url:
        return ""
    try:
        host = urllib.parse.urlsplit(url).netloc.lower()
    except ValueError:
        return ""
    if "@" in host:
        host = host.split("@", 1)[1]
    if ":" in host:
        host = host.split(":", 1)[0]
    if host.startswith("www."):
        host = host[4:]
    return host


def extract_citation_urls(payload):
    """Pull citation URLs out of a Perplexity chat-completions response.

    The API has shipped citations in a few shapes over time: a top-level
    `citations` list of URL strings, and a richer `search_results` list of
    objects with a `url` field. Read both and dedupe."""
    urls = []
    for c in payload.get("citations") or []:
        if isinstance(c, str):
            urls.append(c)
        elif isinstance(c, dict) and c.get("url"):
            urls.append(c["url"])
    for r in payload.get("search_results") or []:
        if isinstance(r, dict) and r.get("url"):
            urls.append(r["url"])
    # Dedupe, preserve order.
    seen, out = set(), []
    for u in urls:
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def ask_perplexity(question, api_key):
    """POST one question to Perplexity and return its citation URL list.

    Returns [] on any HTTP/parse error (a failed question just contributes no
    citations rather than aborting the whole run)."""
    body = json.dumps(
        {
            "model": PERPLEXITY_MODEL,
            "messages": [{"role": "user", "content": question}],
            "stream": False,
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        PERPLEXITY_URL,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = ""
        try:
            detail = e.read().decode("utf-8")[:200]
        except OSError:
            pass
        print(f"  ⚠ HTTP {e.code} for question — skipping. {detail}", file=sys.stderr)
        return []
    except (urllib.error.URLError, json.JSONDecodeError, OSError, ValueError) as e:
        print(f"  ⚠ request failed — skipping. ({e})", file=sys.stderr)
        return []
    return extract_citation_urls(payload)


def append_csv_row(row):
    """Append one row to CSV_PATH, writing the header first if the file is new."""
    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    new_file = not CSV_PATH.exists()
    with CSV_PATH.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new_file:
            w.writerow(CSV_HEADER)
        w.writerow(row)


def main():
    parser = argparse.ArgumentParser(
        description="Monthly AI citation share-of-voice audit (Perplexity Sonar)."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the questions and exit (no API calls)",
    )
    args = parser.parse_args()

    questions = load_questions()

    if args.dry_run:
        print(f"# {len(questions)} citation questions ({QUESTIONS_FILE.name})\n")
        for i, q in enumerate(questions, 1):
            print(f"{i:2d}. {q}")
        return

    load_env()
    api_key = os.environ.get("PERPLEXITY_API_KEY", "").strip()
    if not api_key:
        print(
            "✗ Missing PERPLEXITY_API_KEY.\n"
            "  Get a key at https://www.perplexity.ai/settings/api and run:\n"
            "    export PERPLEXITY_API_KEY=pplx-...\n"
            "    python3 scripts/ai_citation_audit.py",
            file=sys.stderr,
        )
        sys.exit(2)

    n_cited = 0                 # questions where our domain appears in citations
    domain_freq = {}           # domain -> count across all questions' citations
    print(f"# AI citation audit — {dt.date.today().isoformat()} "
          f"({len(questions)} questions)\n")

    for i, q in enumerate(questions, 1):
        urls = ask_perplexity(q, api_key)
        domains = {domain_of(u) for u in urls}
        domains.discard("")
        cited = OUR_DOMAIN in domains
        if cited:
            n_cited += 1
        for d in domains:
            domain_freq[d] = domain_freq.get(d, 0) + 1
        mark = "✓" if cited else "·"
        print(f"{i:2d}. [{mark}] {q}  ({len(domains)} domains cited)")
        if i < len(questions):
            time.sleep(REQUEST_SLEEP_SEC)

    n = len(questions)
    share = n_cited / n if n else 0.0

    # Competitor domains = everyone cited except us, ranked by frequency.
    competitors = sorted(
        ((d, c) for d, c in domain_freq.items() if d != OUR_DOMAIN),
        key=lambda x: (-x[1], x[0]),
    )
    top_competitors = [d for d, _ in competitors[:5]]

    print("\n## Summary")
    print(f"- Questions asked: {n}")
    print(f"- Questions citing {OUR_DOMAIN}: {n_cited}")
    print(f"- Share of voice: {share * 100:.1f}%")
    print("\n### Citation domain frequency (top 15)")
    for d, c in sorted(domain_freq.items(), key=lambda x: (-x[1], x[0]))[:15]:
        tag = "  ← us" if d == OUR_DOMAIN else ""
        print(f"- {d}: {c}{tag}")

    append_csv_row(
        [
            dt.date.today().isoformat(),
            n,
            n_cited,
            f"{share:.4f}",
            ";".join(top_competitors),
        ]
    )
    print(f"\n✓ Appended run to {CSV_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
