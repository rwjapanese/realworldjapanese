# ROADMAP.md

Project-wide TODO tracker for Real-World Japanese content + SEO infrastructure.

**Use this file to resume context between AI sessions (Cursor / Claude Code).**
Open it first, read "How to resume" at the top, then act.

Last updated: 2026-04-28

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
| `business-email-template` | ✅ published | ✅ published | `specs/articles/business-email-template.spec.md` | 2026-04-27 |
| `keigo-cheat-sheet` | ✅ published | ✅ published | `specs/articles/keigo-cheat-sheet.spec.md` | 2026-04-27 |
| `japanese-self-introduction-business` | ✅ published | ✅ published | `specs/articles/japanese-self-introduction-business.spec.md` | 2026-04-27 |
| `keigo-examples` | ✅ published | ✅ published | `specs/articles/keigo-examples.spec.md` | 2026-04-28 |
| `japanese-business-phrases-pdf` | ✅ published | ✅ published | `specs/articles/japanese-business-phrases-pdf.spec.md` | 2026-04-28 |

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

- [x] **Article #5 spec (`keigo-examples`) generated 2026-04-28.** ★4 priority per `6月26日までのコミット.md`。Top 10 SERP captured、cluster trio (`keigo-guide` + `keigo-cheat-sheet` + `keigo-examples`) が確定。Spec: `specs/articles/keigo-examples.spec.md` (status: drafting)。

- [x] **Article #5 drafting (`keigo-examples`) 完了 2026-04-28.** JA v1 → 人間レビュー → JA v2（3点修正：「冒頭〜辞去」→「入室〜退室」／シーン4 の「させていただく」連発を解消／「レジスタ」→「使い分け」）→ EN v1 シップ。JA: ~12,400字 (501 lines)、EN: ~22,800字（romaji + 英訳補完で約1.8倍）。両言語とも `ja-article-style` / `en-article-style` linter idempotent pass、`pnpm build` green。注釈凡例は ［尊］/［謙］/［丁］/⚠（JA）と [son]/[ken]/[tei]/⚠（EN）に統一（spec §11 記録済）。**2026-04-28 に publish 済**（spec status: drafting → published、両言語）。次は GSC URL 検査・インデックス登録リクエスト。Ship by 5月下旬 → 4月28日達成。

- [x] **Article #6 spec (`japanese-business-phrases-pdf`) generated 2026-04-28.** ★3 priority per `6月26日までのコミット.md`。Top 10 SERP captured (Scribd / JapanesePod101 / JETRO PDF / Pacific Bridge PDF / FluentU / Coto / Venture / PLAZA HOMES / SME / Migaku)。**PDF判定: NO mandatory** — 6/10 SERP slots are HTML guides, so HTML-only Phase 1 is viable; Print-CSS satisfies "PDF" intent. Spec: `specs/articles/japanese-business-phrases-pdf.spec.md` (status: drafting)。

- [x] **Article #6 drafting + publish (`japanese-business-phrases-pdf`) 完了 2026-04-28.** JA v1 + EN v1 同セッション一気通貫（ユーザー明示要望、feedback_article_writing_workflow.md 例外条項）。JA: ~14,070字含ローマ字、342 lines / EN: ~3,950 words、350 lines / 両言語 linter idempotent pass / `pnpm build` green。base spec が en-SERP-rooted のため `seo-article-localize` スキップ。実装：読者本人視点ペルソナ → A/B/C 凡例＋内/外 → 10 シーン × A/B/C × コピペ完成形 → 頻度順 Top30 → クッション言葉 7 → メール/電話/会議チャネル別 → 5 誤用 → PDF 保存方法 (Cmd+P) → 関連リンク 4 + Essential 30 CTA → FAQ 5。EN タイトル "Japanese Business Phrases PDF: 30 Scenarios at 3 Politeness Levels" (66 chars、exact-match KW)。**2026-04-28 に publish 済**（spec status: drafting → published、両言語）。Ship by 6月上旬 → 4月28日達成（前倒し約 5 週間）。**Phase 2 PDF deferred** — トリガーは (a) 7記事全シップ + (b) ≥1記事 GSC pos 11–20 + (c) 2–3 PDF batch Sprint。

### P1 — Known issues on shipped content

- [ ] **FAQPage JSON-LD schema** (site-wide infrastructure).
  - Implement at Astro layout level: auto-inject from article frontmatter `faqs: []` array.
  - Defer until 3–5 articles shipped so the one-shot implementation covers them all.
  - Files: `src/layouts/` or `src/components/BaseHead.astro`.

- [ ] **Print-CSS site-wide** (multiplier for "PDF" keyword family).
  - Add `@media print { ... }` rules that hide nav, sidebar, ads, footer, and CTA blocks so Cmd+P (Mac) / Ctrl+P (Win) → clean printable PDF for every article.
  - Surfaced from `japanese-business-phrases-pdf.spec.md` §10 as the actual deliverable that satisfies "PDF" search intent without producing PDF files. Benefits all current + future articles.
  - One-shot site-level work (~1–2 hr). Files: new `src/styles/print.css` + import in `src/layouts/Layout.astro`.
  - Pair with body work for Article #6 (`japanese-business-phrases-pdf`); the article can reference "Cmd+P → save as PDF" as a feature rather than a hack.

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
| 2026-04-28 | **Article #5 spec generated** (`keigo-examples.spec.md`). ★4 priority per `6月26日までのコミット.md`. Top 10 SERP fetched (cotoacademy / wikipedia / risupress / fluentu / tcj-education / rosettastone / gogonihon / learnoutlive / medium / privatejapaneselesson). Cluster positioning decided: trio = `keigo-guide` (explainer pillar) + `keigo-cheat-sheet` (lookup tables) + `keigo-examples` (annotated worked examples). Major content gaps: full-dialogue examples (0/10), A/B/C three-level side-by-side per scene (1/10), line-level annotation (0/10), full email body shown end-to-end (1/10), Slack / chat-register section (0/10), interview/phone-call/meeting full dialogues (0/10), wrong→right inline pairs (2/10). Differentiation locked around 30+ examples × 8–10 scenes + 5 fully-rendered worked dialogues + dedicated Slack section + 🅢/🅚/🅣/⚠ inline annotation legend. 3 primary_info_seeds initialized (real-error catalogue, native-speaker dialogue review, anonymized Slack screenshots). Status: `drafting`. Bilingual §1 §4 §5 §7 per 2026-04-27 convention. | seo-article-outline + ryoooue |
| 2026-04-28 | **Article #5 (`keigo-examples`) JA v1 shipped**. Body at `src/data/guides/ja/keigo-examples.mdx` (~12,400字, 501 lines). Spec §7 outline 全項目を実装。場面別表は10シーン × A/B/C ＋誤用ペア、フル対話は面接 / 謝罪メール / 電話応対 / 会議冒頭 / Slack の5本、Slack 単独例セクション + 「お／ご」表 + 5誤用ペア表 + FAQ 5件。`ja-article-style` linter idempotent pass。注釈凡例は spec §5 §7 の 🅢🅚🅣 から ［尊］／［謙］／［丁］／⚠ のbracket記法に変更（font 依存リスク回避、意味は同一、spec §11 change log に記録）。**人間レビュー待ち**。EN は JA v2 確定後に `seo-article-localize` → EN v1 の順で展開予定（feedback_article_writing_workflow.md ルール）。 | Claude Opus 4.7 + ryoooue |
| 2026-04-28 | **Article #6 spec generated** (`japanese-business-phrases-pdf.spec.md`). ★3 priority per `6月26日までのコミット.md`. Top 10 SERP fetched (Scribd PDF / JapanesePod101 / JETRO PDF / Pacific Bridge PDF / FluentU / Coto / Venture / PLAZA HOMES / SME / Migaku); JETRO PDF binary fetch failed (recorded in §2 as position-anchor). **PDF判定: HTML-only Phase 1 viable** — 6/10 SERP slots are HTML guides, so the "PDF" KW is satisfiable via Print-CSS clean Cmd+P output without producing a new PDF artifact. Major zero-coverage gaps: scenario × A/B/C matrix (0/10), frequency-ranked top 30 (0/10), mistake-pair on phrase row (0/10), Print-CSS-clean layout (0/10), ungated mobile-vertical PDF (0/10). Differentiation reuses A/B/C framework (`keigo-guide` + `keigo-cheat-sheet`) → applied to scenario-driven full-sentence phrases (Slack / email pasteable). 3 primary_info_seeds initialized (week-1 frequency observation log, native-speaker grading, first-person mistake survey). New P1 ROADMAP TODO added: **site-wide Print-CSS** as the actual deliverable for the "PDF" query family — multiplier across all articles, not just this one. **Phase 2 PDF (1080×1920 mobile-vertical) deferred** with explicit triggers: (a) all 7 Phase-1 articles shipped, (b) ≥1 article at GSC pos 11–20, (c) batch design Sprint covering 2–3 PDFs. Status: `drafting`. Bilingual §1 §4 §5 §7. | seo-article-outline (Claude Opus 4.7) + ryoooue |
| 2026-04-28 | **Article #6 JA v1 shipped** (`/ja/guides/japanese-business-phrases-pdf/`). ~14,070 chars (含ローマ字)、342 lines、`ja-article-style` linter idempotent pass、`pnpm build` green、サイトマップ登録済。実装：読者本人視点ペルソナ4項目 → A/B/C 凡例 + uchi-soto + 誤用列の見方 → 10シーン × A/B/C × コピペ完成形 + 誤用注意 → 頻度順 Top30 (6列) → クッション言葉 7 種 → メール8 / 電話6 / 会議6 → 5誤用 → PDF保存方法 (Cmd+P, Phase 2 mobile-vertical 予告) → 関連リンク 4 sibling + Essential 30 CTA → FAQ 5件。タイトル「ビジネス日本語フレーズ集｜シーン別30選・PDFで保存できる早見表」(日常語ルール、"PDF" KW 含む)。差別化の4ゼロカバレッジ・ギャップ全て実装：scenario × A/B/C matrix (0/10 → 10シーン) / frequency-ranked top 30 (0/10 → 6列ランキング) / mistake-pair on row (0/10 → 各シーン誤用注意 + Top30 誤用列) / clean PDF-save UX (0/10 → Cmd+P 案内 + Phase 2 公式 PDF 予告)。**次：人間レビュー待ち** → JA v2 → `seo-article-localize` → EN v1。EN は JA レビュー前に着手しない。並列でPhase 1の他記事と進めて問題ないが、ROADMAP統合は片側にまとめるのが安全（本日 keigo-examples spec と並列実行で File modified エラー1回発生）。| Claude Opus 4.7 + ryoooue |
| 2026-04-28 | **Article #6 EN v1 shipped** (`/en/guides/japanese-business-phrases-pdf/`). ~3,950 words、350 lines、`en-article-style` linter idempotent pass after 8 weak-qualifier corrections（*just*×4 / *very*×1 / *actually*×2 を別表現に置換）、`pnpm build` green at 14 indexed pages、サイトマップ登録済。**ユーザー明示要望で JA v1 と同セッション一気通貫実行**（feedback_article_writing_workflow.md 例外条項：「JA も EN もまとめて作って」と明示時のみ）。base spec が en-SERP-rooted のため `seo-article-localize` 判定スキップ（`business-email-template` と同じ判断）。タイトル "Japanese Business Phrases PDF: 30 Scenarios at 3 Politeness Levels" (66 chars、exact-match KW + benefit promise)。en-article-style ルール A1–D7 全準拠：em-dash + spaces / en-dash for ranges (N3–N2) / Oxford comma / sentence-case H2/H3 / italic *romaji* + (kanji) on first use / Hepburn macrons (ō/ū) / 40–60-word featured-snippet 段落 / persona hooks 4 bullets / 4-sentence paragraph cap / bold key phrase / FAQ 5 H3 / descriptive anchors。Hook lead で boss-greeting freeze + ryōkai correction story を使い、CVR を意識した冒頭。**次：JA v1 の人間レビュー待ち**。JA v2 で修正が入る場合、対応箇所を EN v1 にもバックポートする手順が必要（このサイクルが Article #5 keigo-examples と同じパターン）。| Claude Opus 4.7 + ryoooue |
| 2026-04-28 | **Articles #5 + #6 published 一括リリース**. `keigo-examples` (JA + EN) と `japanese-business-phrases-pdf` (JA + EN) の両 spec で `status: drafting` → `published`、`languages.{en,ja}.status` も `published` に更新。ROADMAP Live articles 表で両記事を ✅ published に。両記事は frontmatter `draft: false` 設定済のため git push で Cloudflare Pages auto-build → 反映予定。**Phase 1 進捗 6/7（86%）**：live = 6記事 (`keigo-guide` / `business-email-template` / `keigo-cheat-sheet` / `japanese-self-introduction-business` / `keigo-examples` / `japanese-business-phrases-pdf`)。残るは `keigo-mistakes` ★6 (6月中旬予定)。コミット構成：(a) `chore` deploy-checklist の MVP closeout（Step 9・10 チェックボックス反映）、(b) `feat` ship keigo-examples、(c) `feat` ship japanese-business-phrases-pdf、計 3 コミットを `main` に push。次の手は両記事の GSC URL 検査 + インデックス登録リクエスト。| ryoooue (publish trigger) + Claude Opus 4.7 |

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
