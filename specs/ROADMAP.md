# ROADMAP.md

Project-wide TODO tracker for Real-World Japanese content + SEO infrastructure.

**Use this file to resume context between AI sessions (Cursor / Claude Code).**
Open it first, read "How to resume" at the top, then act.

Last updated: 2026-04-27

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
- Domain: `realworldjapanese.com` **LIVE** (Cloudflare Pages 2026-04-18 デプロイ完了)
  - apex → `/en/` 301、`www` → apex 301（Redirect Rule、query string 保持）、SSL 自動発行
- Default language: `/en/` (primary), `/ja/` (secondary), `/vi/ /id/ /pt/ /th/ /zh-TW/` (scaffolded, not active)
- Stack: Astro + AstroPaper theme + MDX content collections
- Analytics: **GSC + GA4 設定完了**（GA4 `G-1YCT3NQ46J` ライブ計測中、GSC ドメインプロパティ検証済み・サイトマップ送信済み・5 URL インデックス登録リクエスト済み）
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

- [x] **Step 9: Cloudflare Pages デプロイ** 完了（2026-04-18）
  - 9-1〜9-5 全て green、`https://realworldjapanese.com/` 本番稼働中

- [x] **Step 10: GSC + サイトマップ + GA4** 完了（2026-04-18）
  - GA4 測定 ID `G-1YCT3NQ46J` を `PUBLIC_GA_MEASUREMENT_ID` として配信 → リアルタイム計測動作確認済み
  - GSC ドメインプロパティは Cloudflare Registrar 経由で即自動検証（TXT 不要）
  - サイトマップ送信済み・主要 5 URL のインデックス登録リクエスト完了

- [x] **Next article selection.** Decided on **`business-email-template`** (★2 priority per SEO.md §4-5). Spec generated 2026-04-27 via `seo-article-outline` → `specs/articles/business-email-template.spec.md`.

- [x] **Article #2 drafting.** JA body shipped 2026-04-27 (~3,500字、`ja-article-style` pass)。EN body shipped 2026-04-27 (~2,800 words、`en-article-style` pass)。`seo-article-localize` 判定で EN diff 不要を確認（base spec が en-SERP-rooted）。両言語とも `status: drafting`。次は Featured-snippet 段落チェック (`keigo-guide` 同様の P1 タスク) と本番デプロイ前の手動レビュー。

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
| 2026-04-18 | **Step 9 完了: `realworldjapanese.com` 本番稼働開始**. Cloudflare Registrar で domain 取得 → Pages プロジェクト作成（NODE_VERSION=20, Astro preset, dist output）→ CNAME `@` / `www` を Proxied 設定 → Redirect Rule「WWW to root」で www→apex 301 + query string 保持. 全動作検証 pass: www/apex/クエリ保持/JA+EN記事配信. | this session |
| 2026-04-18 | **Step 10 完了: アナリティクス & サーチエンジン登録全完了**. GA4 プロパティ `Real-World Japanese` 作成 → 測定 ID `G-1YCT3NQ46J` を `PUBLIC_GA_MEASUREMENT_ID` として Cloudflare env 反映 → 再デプロイで gtag 配信確認（57 秒ビルド）→ リアルタイム計測 1 ユーザー表示 OK. GSC ドメインプロパティは Cloudflare Registrar 経由で自動検証成功（TXT 不要）. サイトマップ `https://realworldjapanese.com/sitemap-index.xml` 送信 → インデックス正常処理. 主要 5 URL（apex/ja/en/ja-keigo-guide/en-keigo-guide）インデックス登録リクエスト完了. **MVP ローンチ完了。** | this session |
| 2026-04-27 | **Article #2 spec generated** (`business-email-template.spec.md`). ★2 priority per SEO.md. Top 10 SERP fetched (TCJ / Coto / Migaku / Nihongo-Career / JapaneseKeigo-Webnode / Daijob / ScalingYourCompany / Wasabi / NihongoKnow / Kizuna). Major content gaps identified: internal vs external split (1/10), 15–25 char line-break rule (1/10), Cc/Bcc/各位 (1/10), Slack/Teams adjacent etiquette (0/10), recovery moves after wrong-register email (0/10), template decision tree (0/10). Differentiation reuses A/B/C politeness framework from keigo-guide → applied to email register selection with 8–10 templates tagged by level + scenario. 3 primary_info_seeds initialized (real-email error scrub, HR tolerance interviews, template-download analytics). Status: `drafting`. | seo-article-outline + ryoooue |
| 2026-04-27 | **Bilingual spec convention adopted.** Sections 1 (Target & Intent), 4 (Content Gaps), 5 (Our Differentiation), 7 (Target Article Outline) MUST now be written in BOTH JA and EN (`### JA` / `### EN` sub-headings, JA first). Sections 2/3/6/8/9/10/11 stay EN-only (mechanical/reference). Reason: the human author reviews specs in JA before drafting; an EN-only spec hides direction errors until body-write time. Updated: `specs/articleSpec.template.md`, `~/.claude/skills/seo-article-outline/templates/articleSpec.default.md`, `~/.claude/skills/seo-article-outline/SKILL.md` (Step 6 + Step 9 instructions). Back-filled JA into `business-email-template.spec.md` §1 §4 §5 (§7 already bilingual). | ryoooue |

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
