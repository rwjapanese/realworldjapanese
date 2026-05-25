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
import os
import pathlib
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"

# GSC data lags ~2-3 days; end the window a few days back so the last bucket
# isn't a half-empty partial day.
GSC_LAG_DAYS = 3

GSC_SCOPE = "https://www.googleapis.com/auth/webmasters.readonly"
GA4_SCOPE = "https://www.googleapis.com/auth/analytics.readonly"


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


def get_credentials(scopes):
    try:
        from google.oauth2 import service_account
    except ImportError:
        sys.exit(
            "✗ google-auth not installed.\n"
            "  python3 -m venv scripts/.venv && "
            "scripts/.venv/bin/pip install -r scripts/requirements.txt"
        )
    key_path = require("GOOGLE_APPLICATION_CREDENTIALS")
    if not pathlib.Path(key_path).expanduser().exists():
        sys.exit(f"✗ Service-account key not found at: {key_path}")
    return service_account.Credentials.from_service_account_file(
        str(pathlib.Path(key_path).expanduser()), scopes=scopes
    )


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
# main
# --------------------------------------------------------------------------- #
def main():
    parser = argparse.ArgumentParser(description="GSC + GA4 weekly SEO report")
    parser.add_argument("--days", type=int, default=28, help="lookback window (default 28)")
    parser.add_argument("--top", type=int, default=25, help="rows per table (default 25)")
    parser.add_argument("--only", choices=["gsc", "ga4"], help="run only one source")
    args = parser.parse_args()

    load_env()

    today = dt.date.today().isoformat()
    print(f"# SEO トラッカー — 取得日 {today}\n")

    if args.only != "ga4":
        print(gsc_section(args.days, args.top))
    if args.only != "gsc":
        print(ga4_section(args.days, args.top))


if __name__ == "__main__":
    main()
