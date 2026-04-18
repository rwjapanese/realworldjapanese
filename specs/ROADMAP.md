# ROADMAP.md

Project-wide TODO tracker for Real-World Japanese content + SEO infrastructure.

**Use this file to resume context between AI sessions (Cursor / Claude Code).**
Open it first, read "How to resume" at the top, then act.

Last updated: 2026-04-18

---

## How to resume (read this first)

If you're Cursor/Claude Code picking this up in a new session:

1. Read this file top-to-bottom.
2. Check §"Current state" to understand what's live.
3. Pick a task from §"Active TODOs" (prioritized P0 → P2).
4. For article-specific context, open the matching `specs/articles/<slug>.spec.md` §11 Change Log.
5. For skill usage, see `work/AEIOU/marketing/SEO.md` §6 "AI スキル運用ガイド".
6. When you finish a task, update this file:
   - Mark the TODO checkbox
   - Add a dated entry under §"Recent decisions"
   - Move any new TODOs discovered into §"Active TODOs"

The user reads this file when they open a new chat. Keep it scannable.

---

## Current state

### Site
- Domain: `realworldjapanese.com` (planned — Cloudflare Pages deploy pending; current状態: localhost のみ検証済み)
- Default language: `/en/` (primary), `/ja/` (secondary), `/vi/ /id/ /pt/ /th/ /zh-TW/` (scaffolded, not active)
- Stack: Astro + AstroPaper theme + MDX content collections
- Analytics: GSC + GA4 未設定（配線だけ済み — `PUBLIC_GOOGLE_SITE_VERIFICATION` + `PUBLIC_GA_MEASUREMENT_ID` を env に入れれば有効化）
- Deploy 手順書: `specs/deploy-checklist.md`

### Live articles
| Slug | JA | EN | Spec | Last SERP audit |
|---|---|---|---|---|
| `keigo-guide` | ✅ published | ✅ published | `specs/articles/keigo-guide.spec.md` | 2026-04-18 |

### Product
- **Essential 30 PDF** on Gumroad: https://rwjapanese.gumroad.com/l/essential-30
- Both JA / EN articles link directly to Gumroad (verified clickable 2026-04-18)

### Skills (all in `~/.claude/skills/`, symlinked to `~/.cursor/skills/`)
- `seo-article-outline` — new article base spec generation
- `seo-article-localize` — multi-language spec diff judgment
- `ja-article-style` — JA article mechanical linter
- `en-article-style` — EN article mechanical linter + SEO/CVR checklist

---

## Active TODOs

### P0 — Blocks next meaningful launch

- [ ] **Step 9: Cloudflare Pages デプロイ** (`specs/deploy-checklist.md` §9).
  - 9-1 GitHub push / 9-2 Pages 接続 / 9-3 カスタムドメイン / 9-4 www→apex 301 / 9-5 動作確認
  - AI 側の準備（build green, sitemap, robots, `PUBLIC_GA_MEASUREMENT_ID` 配線, `.env.example`）は完了
  - ここから先はユーザー手動（GitHub / Cloudflare / DNS ダッシュボード操作）

- [ ] **Step 10: GSC + サイトマップ + GA4** (`specs/deploy-checklist.md` §10).
  - 10-1 GA4 プロパティ作成 → 測定 ID 取得
  - 10-2 `PUBLIC_GA_MEASUREMENT_ID` を Cloudflare env に設定 → 再デプロイ
  - 10-3 GA4 リアルタイム動作確認
  - 10-4 GSC ドメインプロパティ検証（DNS TXT）
  - 10-5 `sitemap-index.xml` 送信
  - 10-6 5 URL のインデックス登録リクエスト

- [ ] **Next article selection.** Decide the slug for article #2 from SEO.md priority matrix (§4-5). Top candidates:
  - `japanese-business-email-template` (★2 priority, low competition, product-adjacent)
  - `keigo-cheat-sheet` (★1 priority, PDF-format SEO intent, highest CVR)
  - `japanese-self-introduction-business` (★5 priority, high-volume, new-arrival intent)
  - Run `seo-article-outline` once decided.

### P1 — Known issues on shipped content

- [ ] **FAQPage JSON-LD schema** (site-wide infrastructure).
  - Implement at Astro layout level: auto-inject from article frontmatter `faqs: []` array.
  - Defer until 3–5 articles shipped so the one-shot implementation covers them all.
  - Files: `src/layouts/` or `src/components/BaseHead.astro`.

- [ ] **Featured-snippet paragraph tuning** for `keigo-guide` (both JA and EN).
  - Verify post-intro paragraph is 40–60 words. If not, tighten.
  - JA: currently ~line 18 area. EN: currently ~line 18 area.

- [ ] **Legacy `/products/essential-30/` landing decision.**
  - Current state: local product page may still exist for both `/ja/` and `/en/`. Gumroad is the real fulfillment.
  - Decide: (A) keep as 2-sentence landing that redirects to Gumroad, (B) delete entirely, (C) full rich product LP.
  - Recommend A for MVP.

- [ ] **Internal link graph.** Once 2+ articles exist in the `keigo` cluster:
  - Add links from `keigo-guide.mdx` to sibling articles.
  - Consider building a `business-japanese-complete` pillar page to link all cluster articles back.

### P2 — Nice to have, post-launch polish

- [ ] **EN article weak-word pass** on `keigo-guide.mdx`.
  - `en-article-style --check` reports 6 `just`/`actually` occurrences. Review and trim where not intentional. 15 min.

- [ ] **JA FAQ expansion** if analytics show the 5 entries aren't capturing enough PAA.
  - Candidate additions: "敬語はビジネス以外でも使うか？", "外国人に敬語は必要？"

- [ ] **Multi-language rollout (VI / ID / PT / TH / ZH-TW)**.
  - Deferred until EN + JA prove traction (≥500 organic PV/mo per SEO.md projection).
  - When ready: run `seo-article-localize` per target language.

- [ ] **Style skills for non-EN/JA languages** (`vi-article-style`, etc.).
  - Only when that language's first article is drafted.

- [ ] **Interactive keigo quiz** (from `keigo-guide.spec.md` §6 primary_info_seeds #2).
  - Lead-magnet candidate. Engineering ~8h. Defer to Phase 2.

- [ ] **Primary-info research** from `keigo-guide.spec.md` §6:
  1. Non-native mistake frequency survey (3h design + 2wk data collection)
  2. Register-switching reaction-time experiment (8h engineering)
  3. HR manager interviews on keigo tolerance (13h total)
  - Any of these ships → update `keigo-guide` with quote + data to differentiate further.

### P3 — Infrastructure / dev-experience

- [ ] **Content CI hook.** Run `ja-article-style --check` and `en-article-style --check` in pre-commit or GitHub Actions. Block merge on failure.

- [ ] **Sitemap audit.** Verify `@astrojs/sitemap` is generating entries for `/ja/` and `/en/` versions with hreflang.

- [x] **Analytics wiring (GA4 コード側).** 2026-04-18 完了. `PUBLIC_GA_MEASUREMENT_ID` を `Layout.astro` に条件付き挿入 + `.env.example` 準備. 残りは env に測定 ID を入れて再デプロイするだけ（Step 10-2）.

- [ ] **CHANGELOG.md strategy.** Currently upstream AstroPaper auto-gen. Decide if fork-specific changes belong there or in a separate `CHANGELOG-content.md`. Revisit at article count = 5.

---

## Recent decisions

| Date | Decision / Action | Source |
|---|---|---|
| 2026-04-18 | Launched `keigo-guide` in JA and EN. Essential 30 Gumroad CTA integrated in both. FAQ H2 added to both languages. SERP spec refreshed with production data. | this session |
| 2026-04-18 | Created 4 skills (`seo-article-outline`, `seo-article-localize`, `ja-article-style`, `en-article-style`) under `~/.claude/skills/` with Cursor symlinks. | this session |
| 2026-04-18 | Adopted "base spec + lazy language-diff spec" strategy: single `<slug>.spec.md` rooted in EN SERP; language diffs only when SERPs materially diverge. | session before |
| 2026-04-18 | JA article style rules formalized: no CJK-ASCII space (except after `→` / `=`), `A/B/C` compact notation, `<strong>` for broken `**` patterns, translate ambiguous acronyms (HR → 人事). | session before |
| 2026-04-18 | EN article style rules formalized: em-dash + Oxford comma + sentence-case H2, italic romaji + kanji gloss on first use, FAQ H2 with PAA-aligned H3s, descriptive anchors. | this session |
| 2026-04-18 | Created `specs/ROADMAP.md` (this file) to persist cross-session context. | this session |
| 2026-04-18 | Added `AGENTS.md` (repo root) + `.cursor/rules/roadmap-workflow.mdc` + `CLAUDE.md` symlink so every Cursor / Claude Code session auto-reads ROADMAP.md and auto-updates it on task completion. No manual handoff needed. | this session |
| 2026-04-18 | Deploy 準備: `pnpm build` green / `sitemap-index.xml` + `robots.txt` 検証 / `Layout.astro` に GA4 (`PUBLIC_GA_MEASUREMENT_ID`) 条件付き挿入 / `astro.config.ts` env schema 追加 / `.env.example` 作成 / `specs/deploy-checklist.md` にユーザー手動作業（Cloudflare / GSC / GA4）の具体手順を作成. | this session |

---

## Quick reference

- **Article specs**: `specs/articles/<slug>.spec.md`
- **Skill invocation guide**: `work/AEIOU/marketing/SEO.md` §6
- **Keyword priority matrix**: `work/AEIOU/marketing/SEO.md` §4-5
- **Weekend launch plan** (historical): `work/AEIOU/marketing/土日のコミット.md`
- **Site structure decisions**: `work/AEIOU/marketing/サイト構造.md`
- **Skill source**: `~/.claude/skills/{seo-article-outline, seo-article-localize, ja-article-style, en-article-style}/`

---

## Session auto-loading (no manual handoff needed)

This repo ships `AGENTS.md` + `.cursor/rules/roadmap-workflow.mdc` at the root,
which Cursor and Claude Code auto-read every session. Those files instruct the
agent to:

1. Read this ROADMAP.md before responding.
2. Update it when tasks complete (tick checkboxes, log decisions, queue new
   TODOs).

So the user does **not** need to paste any handoff phrase. Just open the repo
and start working.

If you ever need to override that behavior in a specific chat, paste:

> Read `specs/ROADMAP.md` and pick up from the P0 section. After any task,
> tick the TODO and log under "Recent decisions".
