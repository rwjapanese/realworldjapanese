#!/usr/bin/env python3
"""
seo_report.py — Pull weekly SEO numbers from Google Search Console + GA4 and
print a ready-to-paste tracker block (matches the §4 block in
todo/6月26日までのコミット.md), so the "毎週月曜 GA4/GSC 実数確認" P0 task
no longer needs screenshots.

Usage:
    python3 scripts/seo_report.py                # last 28 days
    python3 scripts/seo_report.py --days 7       # last 7 days
    python3 scripts/seo_report.py --top 40       # show top 40 queries/pages

Config (read from scripts/.env, the repo .env, or real environment):
    GOOGLE_APPLICATION_CREDENTIALS  absolute path to the service-account JSON key
    GSC_SITE_URL                    e.g. sc-domain:realworldjapanese.com
                                    (domain property) OR
                                    https://realworldjapanese.com/ (URL-prefix)
    GA4_PROPERTY_ID                 numeric GA4 property id, e.g. 123456789

One-time setup is documented in scripts/SEO_REPORT_SETUP.md.
Install deps: python3 -m venv scripts/.venv && scripts/.venv/bin/pip install -r scripts/requirements.txt
Then run:     scripts/.venv/bin/python scripts/seo_report.py
"""
import argparse
import datetime as dt
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"
DATA_DIR = REPO_ROOT / "src" / "data"

# GSC data lags ~2-3 days; end the window a few days back so the last bucket
# isn't a half-empty partial day.
GSC_LAG_DAYS = 3

SITE_ORIGIN = "https://realworldjapanese.com"
# A page younger than this (by pubDatetime) is still "maturing" — it hasn't had
# time to rank, so a low position is expected and must NOT be read as decay.
REFRESH_MATURITY_DAYS = 180

# Collection dir name (under src/data/) → URL base path segment.
# Note: the blog collection is served under /posts/, not /blog/.
COLLECTION_URL_BASE = {"guides": "guides", "blog": "posts", "products": "products"}

# GA4 sessionSource values (regex) that indicate an AI assistant referral.
AI_SOURCE_REGEX = (
    r"chatgpt\.com|chat\.openai\.com|perplexity|gemini\.google|"
    r"copilot\.microsoft|claude\.ai"
)

# beehiiv API. The email list is the sprint's most important KPI, so its section
# runs first. These emails are the owner's own test signups — netting them out
# gives the "real" acquisition count the Go/No-Go gate is judged on.
BEEHIIV_API_BASE = "https://api.beehiiv.com/v2"
BEEHIIV_TEST_EMAILS = {
    "hello.rwjapanese@gmail.com",
    "ryaryuryoooue@gmail.com",
    "r.oue@arin-tech.co.jp",
}

GSC_SCOPE = "https://www.googleapis.com/auth/webmasters.readonly"
GA4_SCOPE = "https://www.googleapis.com/auth/analytics.readonly"
# OAuth mode requests both scopes at once; the saved token carries both.
OAUTH_SCOPES = [GSC_SCOPE, GA4_SCOPE]
OAUTH_CLIENT_FILE = SCRIPTS_DIR / "oauth_client.json"
OAUTH_TOKEN_FILE = SCRIPTS_DIR / "oauth_token.json"


# --------------------------------------------------------------------------- #
# config / env
# --------------------------------------------------------------------------- #
def load_env():
    """Load KEY=VALUE pairs from scripts/.env and repo-root .env into os.environ
    (without overwriting anything already set in the real environment)."""
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


def require(name):
    val = os.environ.get(name)
    if not val:
        sys.exit(
            f"✗ Missing config: {name}\n"
            f"  Set it in scripts/.env (see scripts/SEO_REPORT_SETUP.md)."
        )
    return val


def oauth_login():
    """One-time interactive login as hello.rwjapanese@gmail.com using our own
    OAuth client (scripts/oauth_client.json). Opens a browser, saves a refresh
    token to scripts/oauth_token.json. No GA4/GSC "user add" needed because we
    authenticate as the human admin of both properties."""
    if not OAUTH_CLIENT_FILE.exists():
        sys.exit(
            f"✗ OAuth client file not found: {OAUTH_CLIENT_FILE}\n"
            "  Create an OAuth client (Desktop app) in Google Cloud, download the\n"
            "  JSON, and save it there. See scripts/SEO_REPORT_SETUP.md."
        )
    try:
        from google_auth_oauthlib.flow import InstalledAppFlow
    except ImportError:
        sys.exit(
            "✗ google-auth-oauthlib not installed.\n"
            "  scripts/.venv/bin/pip install -r scripts/requirements.txt"
        )
    # Google may echo back openid/email alongside the requested scopes; relax so
    # the flow doesn't raise on the (harmless) scope mismatch.
    os.environ.setdefault("OAUTHLIB_RELAX_TOKEN_SCOPE", "1")
    flow = InstalledAppFlow.from_client_secrets_file(str(OAUTH_CLIENT_FILE), OAUTH_SCOPES)
    creds = flow.run_local_server(port=0, prompt="consent", access_type="offline")
    OAUTH_TOKEN_FILE.write_text(creds.to_json())
    try:
        OAUTH_TOKEN_FILE.chmod(0o600)
    except OSError:
        pass
    print(f"✓ Logged in. Token saved to {OAUTH_TOKEN_FILE}")
    if not creds.refresh_token:
        print(
            "⚠ No refresh token returned — re-run --login (revoke prior grant at\n"
            "  https://myaccount.google.com/permissions if it keeps happening)."
        )


def get_credentials(scopes):
    """Return credentials per AUTH_MODE in env.

    AUTH_MODE=oauth → use our own OAuth client + saved refresh token (login as
                      hello.rwjapanese@gmail.com). No GA4/GSC "user add" needed.
    AUTH_MODE=adc   → gcloud Application Default Credentials. NOTE: gcloud's
                      built-in client cannot request GSC/GA4 scopes, so this mode
                      does NOT work for this script — kept only for reference.
    AUTH_MODE=sa    → service-account JSON at GOOGLE_APPLICATION_CREDENTIALS
                      (blocked unless the SA is added as a property user).
    (unset)         → 'oauth' if a token exists, else 'sa' if a key exists, else 'adc'.
    """
    mode = os.environ.get("AUTH_MODE", "").strip().lower()
    key_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "").strip()
    if not mode:
        if OAUTH_TOKEN_FILE.exists():
            mode = "oauth"
        elif key_path and pathlib.Path(key_path).expanduser().exists():
            mode = "sa"
        else:
            mode = "adc"

    if mode == "oauth":
        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request
        if not OAUTH_TOKEN_FILE.exists():
            sys.exit(
                "✗ Not logged in yet. Run once:\n"
                "    scripts/.venv/bin/python scripts/seo_report.py --login"
            )
        creds = Credentials.from_authorized_user_file(str(OAUTH_TOKEN_FILE), OAUTH_SCOPES)
        if not creds.valid:
            if creds.expired and creds.refresh_token:
                creds.refresh(Request())
                OAUTH_TOKEN_FILE.write_text(creds.to_json())
            else:
                sys.exit(
                    "✗ Saved token is invalid/expired and can't refresh.\n"
                    "    scripts/.venv/bin/python scripts/seo_report.py --login"
                )
        return creds

    if mode == "sa":
        try:
            from google.oauth2 import service_account
        except ImportError:
            sys.exit(
                "✗ google-auth not installed.\n"
                "  scripts/.venv/bin/pip install -r scripts/requirements.txt"
            )
        if not key_path or not pathlib.Path(key_path).expanduser().exists():
            sys.exit(f"✗ Service-account key not found at: {key_path or '(unset)'}")
        return service_account.Credentials.from_service_account_file(
            str(pathlib.Path(key_path).expanduser()), scopes=scopes
        )

    # ADC: don't let a leftover GOOGLE_APPLICATION_CREDENTIALS shadow the
    # gcloud user login — explicitly fall through to the well-known ADC file.
    os.environ.pop("GOOGLE_APPLICATION_CREDENTIALS", None)
    try:
        import google.auth
    except ImportError:
        sys.exit(
            "✗ google-auth not installed.\n"
            "  scripts/.venv/bin/pip install -r scripts/requirements.txt"
        )
    try:
        creds, _ = google.auth.default(scopes=scopes)
    except Exception as e:  # DefaultCredentialsError etc.
        sys.exit(
            "✗ No Application Default Credentials found.\n"
            "  Run once (as hello.rwjapanese@gmail.com):\n"
            "    gcloud auth application-default login \\\n"
            "      --scopes=https://www.googleapis.com/auth/webmasters.readonly,"
            "https://www.googleapis.com/auth/analytics.readonly,"
            "https://www.googleapis.com/auth/cloud-platform\n"
            f"  (detail: {e})"
        )
    # User ADC needs a billing/quota project for these APIs; set it here so the
    # one-time login is the only manual step (no set-quota-project needed).
    quota_project = os.environ.get("GOOGLE_CLOUD_QUOTA_PROJECT", "rwj-seo")
    if hasattr(creds, "with_quota_project"):
        creds = creds.with_quota_project(quota_project)
    return creds


# --------------------------------------------------------------------------- #
# Search Console
# --------------------------------------------------------------------------- #
def gsc_query(service, site_url, start, end, dimensions, row_limit=25):
    body = {
        "startDate": start.isoformat(),
        "endDate": end.isoformat(),
        "dimensions": dimensions,
        "rowLimit": row_limit,
    }
    resp = (
        service.searchanalytics()
        .query(siteUrl=site_url, body=body)
        .execute()
    )
    return resp.get("rows", [])


def fmt_row(r):
    return (
        r["clicks"],
        r["impressions"],
        r["ctr"] * 100,
        r["position"],
    )


def gsc_section(days, top):
    from googleapiclient.discovery import build

    creds = get_credentials([GSC_SCOPE])
    service = build("searchconsole", "v1", credentials=creds, cache_discovery=False)
    site_url = require("GSC_SITE_URL")

    end = dt.date.today() - dt.timedelta(days=GSC_LAG_DAYS)
    start = end - dt.timedelta(days=days - 1)

    out = []
    out.append(f"## Search Console — {start} 〜 {end}（直近 {days} 日, データ遅延 {GSC_LAG_DAYS} 日考慮）")
    out.append(f"property: {site_url}")
    out.append("")

    # Totals
    totals = gsc_query(service, site_url, start, end, dimensions=[], row_limit=1)
    if totals:
        c, i, ctr, pos = fmt_row(totals[0])
        out.append("### 合計")
        out.append(f"- クリック: {c:,}")
        out.append(f"- 表示回数: {i:,}")
        out.append(f"- 平均CTR: {ctr:.2f}%")
        out.append(f"- 平均掲載順位: {pos:.1f}")
    else:
        out.append("### 合計\n- （データなし）")
    out.append("")

    # Top queries
    rows = gsc_query(service, site_url, start, end, dimensions=["query"], row_limit=top)
    out.append(f"### トップクエリ（上位 {min(top, len(rows))}）")
    out.append("| クエリ | clicks | impr | CTR | pos |")
    out.append("|---|--:|--:|--:|--:|")
    for r in rows:
        c, i, ctr, pos = fmt_row(r)
        out.append(f"| {r['keys'][0]} | {c} | {i} | {ctr:.1f}% | {pos:.1f} |")
    out.append("")

    # By page → triage
    pages = gsc_query(service, site_url, start, end, dimensions=["page"], row_limit=200)
    page2 = []      # 10 < position <= 20, has impressions — "あと一押しで1ページ目"
    low_ctr_p1 = [] # position <= 10, impressions >= 20, CTR < 2% — title/meta 即修正候補
    for r in pages:
        c, i, ctr, pos = fmt_row(r)
        url = r["keys"][0]
        if i < 5:
            continue
        if 10 < pos <= 20:
            page2.append((url, c, i, ctr, pos))
        elif pos <= 10 and i >= 20 and ctr < 2.0:
            low_ctr_p1.append((url, c, i, ctr, pos))

    out.append("### 🔧 リライト候補：2ページ目（pos 11–20、あと一押しで1ページ目）")
    if page2:
        page2.sort(key=lambda x: -x[2])  # by impressions
        out.append("| ページ | clicks | impr | CTR | pos |")
        out.append("|---|--:|--:|--:|--:|")
        for url, c, i, ctr, pos in page2[:top]:
            out.append(f"| {short_url(url)} | {c} | {i} | {ctr:.1f}% | {pos:.1f} |")
    else:
        out.append("（該当なし — まだ全記事が圏外 or すでに1ページ目）")
    out.append("")

    out.append("### ⚡ タイトル/メタ即修正候補：1ページ目だが低CTR（pos≤10, impr≥20, CTR<2%）")
    if low_ctr_p1:
        low_ctr_p1.sort(key=lambda x: -x[2])
        out.append("| ページ | clicks | impr | CTR | pos |")
        out.append("|---|--:|--:|--:|--:|")
        for url, c, i, ctr, pos in low_ctr_p1[:top]:
            out.append(f"| {short_url(url)} | {c} | {i} | {ctr:.1f}% | {pos:.1f} |")
    else:
        out.append("（該当なし）")
    out.append("")
    return "\n".join(out)


def short_url(url):
    """Trim https://realworldjapanese.com prefix for readability."""
    for prefix in ("https://realworldjapanese.com", "http://realworldjapanese.com"):
        if url.startswith(prefix):
            return url[len(prefix):] or "/"
    return url


# --------------------------------------------------------------------------- #
# Frontmatter parsing (YAML-light, no PyYAML dependency)
# --------------------------------------------------------------------------- #
def _strip_scalar(val):
    """Strip surrounding quotes/whitespace from a YAML scalar value."""
    val = val.strip()
    if len(val) >= 2 and val[0] == val[-1] and val[0] in ("'", '"'):
        return val[1:-1]
    return val


def _parse_iso_date(val):
    """Parse an ISO date/datetime frontmatter value into a date, or None.

    Handles '2026-05-25', '2026-05-25T00:00:00Z', and
    '2026-04-18T09:00:00+09:00'. We only need the calendar date for age math,
    so timezone offsets are ignored (dropped, not applied)."""
    if not val:
        return None
    val = _strip_scalar(val)
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", val)
    if not m:
        return None
    try:
        return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


def parse_frontmatter(text):
    """Extract top-level `key: value` scalars from the leading `---` block.

    Deliberately shallow: it reads only the top-level scalar keys we care about
    (pubDatetime, modDatetime, slug, draft, title, targetKeyword) and ignores
    nested/list structures like `faqs:` and `tags:`. Lines that are indented
    (part of a nested block) are skipped."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end]
    fm = {}
    for raw in block.splitlines():
        # Skip indented lines (nested list/map items) and blanks/comments.
        if not raw.strip() or raw[0] in (" ", "\t", "#"):
            continue
        if ":" not in raw:
            continue
        key, _, val = raw.partition(":")
        key = key.strip()
        val = val.strip()
        # Drop inline comments on plain scalars (not inside quotes).
        if val and val[0] not in ("'", '"') and " #" in val:
            val = val.split(" #", 1)[0].strip()
        fm[key] = val
    return fm


def build_url(collection, lang, slug):
    """Construct the canonical live URL for a page, with trailing slash:
    https://realworldjapanese.com/{lang}/{base}/{slug}/"""
    base = COLLECTION_URL_BASE.get(collection, collection)
    return f"{SITE_ORIGIN}/{lang}/{base}/{slug}/"


def load_content_index():
    """Walk src/data/**/*.{md,mdx} and return {url: {...meta}} keyed by the live
    page URL, so it can be joined against GSC page rows.

    Meta per entry: collection, lang, slug, file (repo-relative), pub (date|None),
    mod (date|None), title, target_keyword. Draft pages are skipped (they don't
    render). Files whose first path segment isn't a known lang (en|ja) are also
    skipped, matching the routing's lang extraction."""
    index = {}
    if not DATA_DIR.exists():
        return index
    for path in sorted(DATA_DIR.rglob("*")):
        if path.suffix not in (".md", ".mdx"):
            continue
        # Ignore underscore-prefixed files (the glob loader excludes them too).
        if path.name.startswith("_"):
            continue
        rel = path.relative_to(DATA_DIR)
        parts = rel.parts
        # Expect <collection>/<lang>/<...>/<name>.<ext>
        if len(parts) < 3:
            continue
        collection, lang = parts[0], parts[1]
        if lang not in ("en", "ja"):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        fm = parse_frontmatter(text)
        if _strip_scalar(fm.get("draft", "")).lower() == "true":
            continue
        slug_override = _strip_scalar(fm.get("slug", ""))
        # Slug without an override = id after the lang prefix (path segments
        # between <lang> and the filename, plus the filename stem).
        inner = list(parts[2:-1]) + [path.stem]
        slug = slug_override or "/".join(inner)
        url = build_url(collection, lang, slug)
        index[url] = {
            "collection": collection,
            "lang": lang,
            "slug": slug,
            "file": str(path.relative_to(REPO_ROOT)),
            "pub": _parse_iso_date(fm.get("pubDatetime", "")),
            "mod": _parse_iso_date(fm.get("modDatetime", "")),
            "title": _strip_scalar(fm.get("title", "")),
            "target_keyword": _strip_scalar(fm.get("targetKeyword", "")),
        }
    return index


# --------------------------------------------------------------------------- #
# GA4
# --------------------------------------------------------------------------- #
def ga4_section(days, top):
    try:
        from google.analytics.data_v1beta import BetaAnalyticsDataClient
        from google.analytics.data_v1beta.types import (
            DateRange,
            Dimension,
            Metric,
            RunReportRequest,
            Filter,
            FilterExpression,
        )
    except ImportError:
        sys.exit(
            "✗ google-analytics-data not installed.\n"
            "  scripts/.venv/bin/pip install -r scripts/requirements.txt"
        )

    creds = get_credentials([GA4_SCOPE])
    client = BetaAnalyticsDataClient(credentials=creds)
    prop = require("GA4_PROPERTY_ID")
    property_path = f"properties/{prop}"
    date_range = DateRange(start_date=f"{days}daysAgo", end_date="today")

    out = []
    out.append(f"## GA4 — 直近 {days} 日（property {prop}）")
    out.append("")

    # Site-wide totals
    totals = client.run_report(
        RunReportRequest(
            property=property_path,
            date_ranges=[date_range],
            metrics=[
                Metric(name="activeUsers"),
                Metric(name="newUsers"),
                Metric(name="sessions"),
                Metric(name="userEngagementDuration"),
            ],
        )
    )
    if totals.rows:
        v = totals.rows[0].metric_values
        active = int(v[0].value or 0)
        new = int(v[1].value or 0)
        sessions = int(v[2].value or 0)
        eng_sec = float(v[3].value or 0)
        avg_eng = (eng_sec / active) if active else 0
        out.append("### 合計")
        out.append(f"- アクティブユーザー: {active:,}")
        out.append(f"- 新規ユーザー: {new:,}")
        out.append(f"- セッション: {sessions:,}")
        out.append(f"- アクティブユーザーあたり平均エンゲージ時間: {avg_eng:.0f} 秒")
    else:
        out.append("### 合計\n- （データなし）")
    out.append("")

    # By channel
    by_channel = client.run_report(
        RunReportRequest(
            property=property_path,
            date_ranges=[date_range],
            dimensions=[Dimension(name="sessionDefaultChannelGroup")],
            metrics=[Metric(name="sessions"), Metric(name="activeUsers")],
        )
    )
    out.append("### チャネル別セッション（go/no-go は Organic Search で判定）")
    out.append("| チャネル | sessions | active users |")
    out.append("|---|--:|--:|")
    channel_rows = sorted(
        by_channel.rows,
        key=lambda r: -int(r.metric_values[0].value or 0),
    )
    organic_sessions = 0
    for r in channel_rows:
        ch = r.dimension_values[0].value
        s = int(r.metric_values[0].value or 0)
        u = int(r.metric_values[1].value or 0)
        if ch == "Organic Search":
            organic_sessions = s
        out.append(f"| {ch} | {s} | {u} |")
    out.append("")
    out.append(f"**→ Organic Search セッション = {organic_sessions}**（月100の go/no-go 基準）")
    out.append("")

    # Organic landing pages
    organic_filter = FilterExpression(
        filter=Filter(
            field_name="sessionDefaultChannelGroup",
            string_filter=Filter.StringFilter(value="Organic Search"),
        )
    )
    landing = client.run_report(
        RunReportRequest(
            property=property_path,
            date_ranges=[date_range],
            dimensions=[Dimension(name="landingPagePlusQueryString")],
            metrics=[Metric(name="sessions")],
            dimension_filter=organic_filter,
            limit=top,
        )
    )
    out.append(f"### オーガニック着地ページ（上位 {min(top, len(landing.rows))}）")
    if landing.rows:
        out.append("| ページ | organic sessions |")
        out.append("|---|--:|")
        rows = sorted(landing.rows, key=lambda r: -int(r.metric_values[0].value or 0))
        for r in rows[:top]:
            out.append(f"| {r.dimension_values[0].value} | {r.metric_values[0].value} |")
    else:
        out.append("（オーガニック着地まだなし）")
    out.append("")
    return "\n".join(out)


# --------------------------------------------------------------------------- #
# Module 1: Refresh queue
# --------------------------------------------------------------------------- #
def refresh_section(days, top):
    """Rank published pages by how much a content refresh would pay off.

    Young pages (< REFRESH_MATURITY_DAYS old) are set aside as "maturing" and
    never scored — a young page ranking poorly is expected, not decayed. The
    refresh score is impressions weighted 1.5× when the page sits in the
    striking-distance band (avg position 4–15), where a refresh most reliably
    moves rankings."""
    out = ["## リフレッシュ待ち行列（decay / striking-distance で優先度付け）", ""]

    index = load_content_index()
    if not index:
        out.append(f"（スキップ: {DATA_DIR} に記事が見つからない）")
        return "\n".join(out)

    try:
        from googleapiclient.discovery import build

        creds = get_credentials([GSC_SCOPE])
        service = build("searchconsole", "v1", credentials=creds, cache_discovery=False)
        site_url = require("GSC_SITE_URL")
        end = dt.date.today() - dt.timedelta(days=GSC_LAG_DAYS)
        start = end - dt.timedelta(days=days - 1)
        pages = gsc_query(service, site_url, start, end, dimensions=["page"], row_limit=1000)
    except SystemExit:
        raise
    except Exception as e:
        out.append(f"（スキップ: GSC 取得に失敗 — {e}）")
        return "\n".join(out)

    today = dt.date.today()
    maturing = []       # young pages, excluded from scoring
    candidates = []     # (url, age_days, clicks, impr, pos, score)
    for r in pages:
        url = r["keys"][0]
        meta = index.get(url) or index.get(url.rstrip("/") + "/")
        if not meta:
            continue  # non-article URL (home, tag pages, etc.)
        c, i, ctr, pos = fmt_row(r)
        pub = meta.get("pub")
        age = (today - pub).days if pub else None
        if age is not None and age < REFRESH_MATURITY_DAYS:
            maturing.append(url)
            continue
        score = i * (1.5 if 4 <= pos <= 15 else 1.0)
        candidates.append((url, age, int(c), int(i), pos, score))

    out.append(
        f"- 対象ウィンドウ: {start} 〜 {end}（直近 {days} 日）"
    )
    out.append(
        f"- 育成中（pub < {REFRESH_MATURITY_DAYS} 日, リフレッシュ対象から除外）: "
        f"{len(maturing)} 本"
    )
    out.append("")

    if not candidates:
        out.append("（該当なし — 成熟済みでインプレッションのある記事がまだない）")
        out.append("")
        return "\n".join(out)

    candidates.sort(key=lambda x: -x[5])
    out.append("### リフレッシュ優先度（score = impr × 1.5[pos 4–15 のとき]）")
    out.append("| ページ | age日 | impr | clicks | pos | score | 推奨アクション |")
    out.append("|---|--:|--:|--:|--:|--:|---|")
    for url, age, c, i, pos, score in candidates[:top]:
        age_s = str(age) if age is not None else "?"
        out.append(
            f"| {short_url(url)} | {age_s} | {i} | {c} | {pos:.1f} | {score:.0f} | "
            f"re-run spec SERP analysis via seo-article-refresh |"
        )
    out.append("")
    return "\n".join(out)


# --------------------------------------------------------------------------- #
# Module 2: Cannibalization
# --------------------------------------------------------------------------- #
CANNIBAL_WINDOW_DAYS = 90
BRAND_TERMS = ("real world japanese", "realworldjapanese")


def cannibal_section(top):
    """Find queries where two or more of our pages split the impressions —
    a sign they compete for the same intent. Uses a fixed 90-day window
    (independent of --days) so low-volume queries accumulate enough signal."""
    out = ["## カニバリゼーション点検（同一クエリを複数ページで奪い合い / 直近90日）", ""]

    try:
        from googleapiclient.discovery import build

        creds = get_credentials([GSC_SCOPE])
        service = build("searchconsole", "v1", credentials=creds, cache_discovery=False)
        site_url = require("GSC_SITE_URL")
        end = dt.date.today() - dt.timedelta(days=GSC_LAG_DAYS)
        start = end - dt.timedelta(days=CANNIBAL_WINDOW_DAYS - 1)
        rows = gsc_query(
            service, site_url, start, end,
            dimensions=["query", "page"], row_limit=25000,
        )
    except SystemExit:
        raise
    except Exception as e:
        out.append(f"（スキップ: GSC 取得に失敗 — {e}）")
        return "\n".join(out)

    # Aggregate impressions per (query -> page).
    by_query = {}  # query -> {page: impressions}
    for r in rows:
        q, page = r["keys"][0], r["keys"][1]
        ql = q.lower()
        if any(b in ql for b in BRAND_TERMS):
            continue
        by_query.setdefault(q, {})
        by_query[q][page] = by_query[q].get(page, 0) + r["impressions"]

    flagged = []  # (query, total, [(page, share)])
    for q, pagemap in by_query.items():
        total = sum(pagemap.values())
        if total < 30:
            continue
        big = [(p, imp / total) for p, imp in pagemap.items() if imp / total > 0.20]
        if len(big) >= 2:
            big.sort(key=lambda x: -x[1])
            flagged.append((q, total, big))

    out.append(f"- 対象ウィンドウ: {start} 〜 {end}（固定90日）")
    out.append(
        "- 条件: ブランドクエリ除外・総impr≥30・2ページ以上がそれぞれimprの20%超"
    )
    out.append("")

    if not flagged:
        out.append("（該当なし — 目立ったカニバリはない）")
        out.append("")
        return "\n".join(out)

    flagged.sort(key=lambda x: -x[1])
    out.append("| クエリ | ページ | 分割% | 総impr | メモ |")
    out.append("|---|---|---|--:|---|")
    for q, total, big in flagged[:top]:
        pages_s = "<br>".join(short_url(p) for p, _ in big)
        share_s = "<br>".join(f"{share * 100:.0f}%" for _, share in big)
        out.append(
            f"| {q} | {pages_s} | {share_s} | {int(total)} | "
            f"same intent — consider consolidating or differentiating |"
        )
    out.append("")
    return "\n".join(out)


# --------------------------------------------------------------------------- #
# Module 3: Alerts (WoW traffic step-change + Google update overlap)
# --------------------------------------------------------------------------- #
def _gsc_totals(service, site_url, start, end):
    rows = gsc_query(service, site_url, start, end, dimensions=[], row_limit=1)
    if not rows:
        return 0, 0
    return int(rows[0]["clicks"]), int(rows[0]["impressions"])


def _google_search_incidents(window_start, window_end):
    """Fetch the Google Search Status dashboard incidents JSON and return those
    that overlap [window_start, window_end] as (begin_date, title) tuples.
    Returns None on any network/parse error so callers can skip gracefully."""
    url = "https://status.search.google.com/incidents.json"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "rwj-seo-report/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, json.JSONDecodeError, OSError, ValueError):
        return None

    def _to_date(s):
        if not s:
            return None
        m = re.match(r"(\d{4})-(\d{2})-(\d{2})", s)
        if not m:
            return None
        try:
            return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            return None

    incidents = []
    for inc in data if isinstance(data, list) else []:
        begin = _to_date(inc.get("begin"))
        # An open incident has no `end`; treat it as ongoing (overlaps).
        end = _to_date(inc.get("end")) or window_end
        if begin is None:
            continue
        if begin <= window_end and end >= window_start:
            incidents.append((begin, inc.get("external_desc") or inc.get("uri") or "(no title)"))
    incidents.sort(key=lambda x: x[0])
    return incidents


def alerts_section():
    """Week-over-week site-wide traffic delta plus any Google Search ranking
    incidents overlapping the last 28 days, so a traffic step-change can be
    lined up against a known Google update."""
    out = ["## アラート（WoW トラフィック急変 + Google アップデート重なり）", ""]

    try:
        from googleapiclient.discovery import build

        creds = get_credentials([GSC_SCOPE])
        service = build("searchconsole", "v1", credentials=creds, cache_discovery=False)
        site_url = require("GSC_SITE_URL")
    except SystemExit:
        raise
    except Exception as e:
        out.append(f"（スキップ: GSC 認証/接続に失敗 — {e}）")
        return "\n".join(out)

    # Last 7 full days (respecting lag) vs the prior 7.
    last_end = dt.date.today() - dt.timedelta(days=GSC_LAG_DAYS)
    last_start = last_end - dt.timedelta(days=6)
    prev_end = last_start - dt.timedelta(days=1)
    prev_start = prev_end - dt.timedelta(days=6)

    try:
        cur_c, cur_i = _gsc_totals(service, site_url, last_start, last_end)
        prev_c, prev_i = _gsc_totals(service, site_url, prev_start, prev_end)
    except Exception as e:
        out.append(f"（スキップ: GSC 取得に失敗 — {e}）")
        return "\n".join(out)

    def _delta(cur, prev):
        if prev == 0:
            return None
        return (cur - prev) / prev * 100.0

    di = _delta(cur_i, prev_i)
    dc = _delta(cur_c, prev_c)
    out.append(f"- 直近7日: {last_start} 〜 {last_end} / 前7日: {prev_start} 〜 {prev_end}")
    out.append(
        f"- 表示回数: {prev_i:,} → {cur_i:,}"
        + (f"（{di:+.0f}%）" if di is not None else "（前週0のため%算出不可）")
    )
    out.append(
        f"- クリック: {prev_c:,} → {cur_c:,}"
        + (f"（{dc:+.0f}%）" if dc is not None else "（前週0のため%算出不可）")
    )
    if di is not None and di <= -30:
        out.append("")
        out.append(f"⚠️ 表示回数が前週比 {di:.0f}% — 急落。下のアップデート一覧と突き合わせを。")
    out.append("")

    # Google Search Status incidents overlapping the last 28 days.
    inc_start = dt.date.today() - dt.timedelta(days=28)
    inc_end = dt.date.today()
    incidents = _google_search_incidents(inc_start, inc_end)
    out.append("### Google 検索ステータス（直近28日に重なるインシデント）")
    if incidents is None:
        out.append("（スキップ: status.search.google.com への接続に失敗）")
    elif not incidents:
        out.append("（直近28日に重なる公表インシデントなし）")
    else:
        out.append("| 開始日 | タイトル |")
        out.append("|---|---|")
        for begin, title in incidents:
            out.append(f"| {begin} | {title} |")
    out.append("")
    return "\n".join(out)


# --------------------------------------------------------------------------- #
# Module 4: AI surfaces (LLM referral traffic)
# --------------------------------------------------------------------------- #
def ai_section(top):
    """Report traffic arriving from AI assistants, two ways: by the GA4
    'AI Assistant' default channel group (available since May 2026), and by a
    source-regex fallback that also breaks out landing pages. Organic Search is
    shown alongside as the baseline for comparison."""
    out = ["## AI 流入面（LLM アシスタント経由の流入）", ""]

    try:
        from google.analytics.data_v1beta import BetaAnalyticsDataClient
        from google.analytics.data_v1beta.types import (
            DateRange,
            Dimension,
            Metric,
            RunReportRequest,
            Filter,
            FilterExpression,
        )
    except ImportError:
        out.append("（スキップ: google-analytics-data 未インストール）")
        return "\n".join(out)

    try:
        creds = get_credentials([GA4_SCOPE])
        client = BetaAnalyticsDataClient(credentials=creds)
        prop = require("GA4_PROPERTY_ID")
    except SystemExit:
        raise
    except Exception as e:
        out.append(f"（スキップ: GA4 認証に失敗 — {e}）")
        return "\n".join(out)

    property_path = f"properties/{prop}"
    date_range = DateRange(start_date="28daysAgo", end_date="today")
    out.append("- ウィンドウ: 直近28日")
    out.append("")

    # (a) By default channel group — look for the "AI Assistant" group.
    try:
        by_channel = client.run_report(
            RunReportRequest(
                property=property_path,
                date_ranges=[date_range],
                dimensions=[Dimension(name="sessionDefaultChannelGroup")],
                metrics=[Metric(name="sessions"), Metric(name="engagedSessions")],
            )
        )
        channel_map = {
            r.dimension_values[0].value: (
                int(r.metric_values[0].value or 0),
                int(r.metric_values[1].value or 0),
            )
            for r in by_channel.rows
        }
        out.append("### チャネルグループ別（AI Assistant / Organic Search）")
        out.append("| チャネル | sessions | engaged sessions |")
        out.append("|---|--:|--:|")
        if "AI Assistant" in channel_map:
            s, e = channel_map["AI Assistant"]
            out.append(f"| AI Assistant | {s} | {e} |")
        else:
            out.append("| AI Assistant | — | （このチャネル値はまだ出現していない） |")
        if "Organic Search" in channel_map:
            s, e = channel_map["Organic Search"]
            out.append(f"| Organic Search | {s} | {e} |")
        out.append("")
    except Exception as e:
        out.append(f"（チャネルグループ取得をスキップ — {e}）")
        out.append("")

    # (b) Source-regex fallback + landing-page breakdown, AI vs Organic.
    def _source_report(dimensions, dim_filter):
        return client.run_report(
            RunReportRequest(
                property=property_path,
                date_ranges=[date_range],
                dimensions=dimensions,
                metrics=[Metric(name="sessions"), Metric(name="engagedSessions")],
                dimension_filter=dim_filter,
                limit=top,
            )
        )

    ai_filter = FilterExpression(
        filter=Filter(
            field_name="sessionSource",
            string_filter=Filter.StringFilter(
                match_type=Filter.StringFilter.MatchType.FULL_REGEXP,
                value=AI_SOURCE_REGEX,
                case_sensitive=False,
            ),
        )
    )
    organic_filter = FilterExpression(
        filter=Filter(
            field_name="sessionDefaultChannelGroup",
            string_filter=Filter.StringFilter(value="Organic Search"),
        )
    )

    try:
        ai_tot = _source_report([Dimension(name="sessionSource")], ai_filter)
        ai_sessions = sum(int(r.metric_values[0].value or 0) for r in ai_tot.rows)
        ai_engaged = sum(int(r.metric_values[1].value or 0) for r in ai_tot.rows)
        org_tot = _source_report([Dimension(name="sessionDefaultChannelGroup")], organic_filter)
        org_sessions = sum(int(r.metric_values[0].value or 0) for r in org_tot.rows)
        org_engaged = sum(int(r.metric_values[1].value or 0) for r in org_tot.rows)

        out.append("### ソース正規表現による AI 流入 vs Organic Search")
        out.append("| 区分 | sessions | engaged sessions |")
        out.append("|---|--:|--:|")
        out.append(f"| AI アシスタント（{AI_SOURCE_REGEX}） | {ai_sessions} | {ai_engaged} |")
        out.append(f"| Organic Search | {org_sessions} | {org_engaged} |")
        out.append("")

        if ai_tot.rows:
            out.append("#### AI 流入のソース内訳")
            out.append("| source | sessions | engaged |")
            out.append("|---|--:|--:|")
            for r in sorted(ai_tot.rows, key=lambda r: -int(r.metric_values[0].value or 0)):
                out.append(
                    f"| {r.dimension_values[0].value} | "
                    f"{r.metric_values[0].value} | {r.metric_values[1].value} |"
                )
            out.append("")

        ai_land = _source_report(
            [Dimension(name="landingPagePlusQueryString")], ai_filter
        )
        if ai_land.rows:
            out.append(f"#### AI 流入の着地ページ（上位 {min(top, len(ai_land.rows))}）")
            out.append("| ページ | sessions | engaged |")
            out.append("|---|--:|--:|")
            for r in sorted(ai_land.rows, key=lambda r: -int(r.metric_values[0].value or 0))[:top]:
                out.append(
                    f"| {r.dimension_values[0].value} | "
                    f"{r.metric_values[0].value} | {r.metric_values[1].value} |"
                )
            out.append("")
        else:
            out.append("（AI 流入の着地ページはまだなし）")
            out.append("")
    except Exception as e:
        out.append(f"（ソース内訳をスキップ — {e}）")
        out.append("")

    return "\n".join(out)


# --------------------------------------------------------------------------- #
# beehiiv (email list — the sprint's most important KPI)
# --------------------------------------------------------------------------- #
def _beehiiv_get(path, api_key, params=None):
    """GET {BEEHIIV_API_BASE}{path} with Bearer auth, return parsed JSON."""
    url = f"{BEEHIIV_API_BASE}{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {api_key}"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _beehiiv_all_subscriptions(pub_id, api_key):
    """Page through every subscription (cursor pagination — the endpoint returns
    no total count) and return the raw list."""
    rows = []
    cursor = None
    while True:
        params = {"limit": 100}
        if cursor:
            params["cursor"] = cursor
        data = _beehiiv_get(f"/publications/{pub_id}/subscriptions", api_key, params)
        rows.extend(data.get("data", []))
        if not data.get("has_more"):
            break
        cursor = data.get("next_cursor")
        if not cursor:
            break
    return rows


def beehiiv_section(days):
    """Email-list KPI: total active subscribers, new signups in the window, and
    a channel breakdown (utm_source/medium) so the sprint can see WHICH channel
    is acquiring — the Go/No-Go 'channel 成立' gate. Owner test emails are netted
    out to give the real acquisition count."""
    out = ["## 📧 メール登録（最重要KPI — beehiiv）", ""]

    api_key = os.environ.get("BEEHIIV_API_KEY")
    pub_id = os.environ.get("BEEHIIV_PUBLICATION_ID")
    if not api_key or not pub_id:
        out.append(
            "（スキップ: BEEHIIV_API_KEY / BEEHIIV_PUBLICATION_ID が未設定。"
            "scripts/.env に設定すると登録数が自動取得されます）"
        )
        out.append("")
        return "\n".join(out)

    try:
        subs = _beehiiv_all_subscriptions(pub_id, api_key)
    except urllib.error.HTTPError as e:
        out.append(f"（スキップ: beehiiv API {e.code} — キー失効/権限を確認）")
        out.append("")
        return "\n".join(out)
    except Exception as e:
        out.append(f"（スキップ: beehiiv 取得に失敗 — {e}）")
        out.append("")
        return "\n".join(out)

    active = [s for s in subs if s.get("status") == "active"]
    real = [s for s in active if (s.get("email") or "").lower() not in BEEHIIV_TEST_EMAILS]
    tests = len(active) - len(real)

    cutoff = dt.datetime.now(dt.timezone.utc).timestamp() - days * 86400
    new_real = [s for s in real if (s.get("created") or 0) >= cutoff]

    out.append(f"- ウィンドウ: 直近 {days} 日")
    out.append(
        f"- **実登録（テスト除く）: {len(real)} 件**"
        f"（うち直近{days}日で新規 {len(new_real)} 件）"
        f" ／ 全 active {len(active)} 件（テスト {tests} 件を含む）"
    )
    # Go/No-Go context (実行プラン §2): Go ≥60 / 条件付き 25-59 / No-Go <25.
    n = len(real)
    if n >= 60:
        gate = "🟢 **Go 圏（≥60）**"
    elif n >= 25:
        gate = "🟡 条件付き継続圏（25-59）"
    else:
        gate = "🔴 No-Go 圏（<25）— 配布を実行した上で 8/28 判定"
    out.append(f"- Go/No-Go 進捗（8/28 判定・実登録ベース）: {gate}")
    out.append("")

    # Channel attribution — which source is actually acquiring (the '成立' gate).
    if real:
        from collections import Counter

        def _lab(s):
            src = (s.get("utm_source") or "direct").strip() or "direct"
            med = (s.get("utm_medium") or "").strip()
            return f"{src} / {med}" if med else src

        by_ch = Counter(_lab(s) for s in real)
        out.append("### 獲得チャネル内訳（実登録 utm_source / medium）")
        out.append("| チャネル | 実登録 | 直近窓の新規 |")
        out.append("|---|--:|--:|")
        new_by_ch = Counter(_lab(s) for s in new_real)
        for ch, c in by_ch.most_common():
            out.append(f"| {ch} | {c} | {new_by_ch.get(ch, 0)} |")
        out.append("")
    else:
        out.append("（実登録はまだゼロ。配布導線を稼働中）")
        out.append("")

    return "\n".join(out)


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #
def main():
    parser = argparse.ArgumentParser(description="GSC + GA4 weekly SEO report")
    parser.add_argument("--days", type=int, default=28, help="lookback window (default 28)")
    parser.add_argument("--top", type=int, default=25, help="rows per table (default 25)")
    parser.add_argument(
        "--only",
        choices=["email", "gsc", "ga4", "refresh", "cannibal", "alerts", "ai"],
        help="run only one section",
    )
    parser.add_argument(
        "--login",
        action="store_true",
        help="one-time OAuth login (opens browser as hello.rwjapanese@gmail.com)",
    )
    args = parser.parse_args()

    load_env()

    if args.login:
        oauth_login()
        return

    today = dt.date.today().isoformat()
    print(f"# SEO トラッカー — 取得日 {today}\n")

    # Full report (no --only) runs every section in order; --only <name> runs
    # just that one. Each section degrades gracefully on data-source failure.
    only = args.only
    if only in (None, "email"):
        print(beehiiv_section(args.days))
    if only in (None, "gsc"):
        print(gsc_section(args.days, args.top))
    if only in (None, "ga4"):
        print(ga4_section(args.days, args.top))
    if only in (None, "refresh"):
        print(refresh_section(args.days, args.top))
    if only in (None, "cannibal"):
        print(cannibal_section(args.top))
    if only in (None, "alerts"):
        print(alerts_section())
    if only in (None, "ai"):
        print(ai_section(args.top))


if __name__ == "__main__":
    main()
