# ROADMAP.md

Project-wide TODO tracker for Real-World Japanese content + SEO infrastructure.

**Use this file to resume context between AI sessions (Cursor / Claude Code).**
Open it first, read "How to resume" at the top, then act.

Last updated: 2026-05-13

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
| `keigo-mistakes` | ✅ published | ✅ published | `specs/articles/keigo-mistakes.spec.md` | 2026-05-11 |
| `polite-japanese-phrases-for-office` | ✅ published | ✅ published | `specs/articles/polite-japanese-phrases-for-office.spec.md` | 2026-05-11 |
| `how-to-write-japanese-business-email` | 🟡 drafting (JA v1 shipped) | 🟡 drafting (EN v1 shipped) | `specs/articles/how-to-write-japanese-business-email.spec.md` | 2026-05-12 |
| `japanese-for-it-professionals` | ✅ published | ✅ published | `specs/articles/japanese-for-it-professionals.spec.md` | 2026-05-12 |
| `best-way-to-learn-keigo` | 🟡 drafting (JA v2 shipped) | 🟡 drafting (EN v1 shipped) | `specs/articles/best-way-to-learn-keigo.spec.md` | 2026-05-12 |

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

- [ ] **Article #9 drafting (`best-way-to-learn-keigo`).** **JA v2 + EN v1 shipped 2026-05-13**。JA at `src/data/guides/ja/best-way-to-learn-keigo.mdx` (450 lines、約14,300字)、EN at `src/data/guides/en/best-way-to-learn-keigo.mdx` (454 lines、4,928 words)。両言語 linter idempotent pass（EN は 5 件 weak qualifier 手動修正：actually × 4 + just × 1）、`pnpm build` green at 24 indexed pages (8,241 words indexed)。**JA v2 修正**（人間レビュー反映、4点）：タイトル「A→B→Cの90日プラン」→「段階別90日ロードマップ」（CTR 改善、A→B→C ジャーゴン回避）／冒頭リード softening 2 箇所（決めつけ口調回避）／A/B/C 表「完全自動化」→「固める」。**EN v1 採択方針**：base spec が en-SERP-rooted のため `seo-article-localize` スキップ（`business-email-template` / `japanese-business-phrases-pdf` と同じ判断）。EN タイトル "Best Way to Learn Keigo: A 90-Day, 3-Stage Roadmap" (52 chars、KW 完全一致 + benefit promise)。JA v2 の softening を EN にもバックポート（"as one path" 系の柔らかい言い回し採用）。両言語 `status: drafting`（未 publish）。次：**人間レビュー** → 必要なら v2 → publish flip。

- [ ] **Article #11 drafting (`how-to-write-japanese-business-email`).** **JA v1 + EN v1 both shipped 2026-05-13**。JA: `src/data/guides/ja/how-to-write-japanese-business-email.mdx` (12,895 chars after title/hook tweak)、`ja-article-style` linter idempotent pass。EN: `src/data/guides/en/how-to-write-japanese-business-email.mdx` (3,862 words)、`en-article-style` linter clean after 2 weak-qualifier corrections（really × 1, just × 1）。`pnpm build` green at 84 pages, 0 errors。Spec §7 JA + EN outlines を 1:1 実装：8 ステップラダー × A/B/C 各ステップ埋め込み + TO/CC/BCC 選択章 + 1行15–25字改行ルール（before/after code block）+ 送信前10項目チェックリスト + 誤送信リカバリ章（名前間違いの謝罪メール完成形入り）+ FAQ 5 件 + 関連記事7本クロスリンク。6 zero-coverage SERP ギャップ全実装確認。**ユーザー明示要望で JA review pass 1 確定後に EN を同セッションで即着手**（feedback_article_writing_workflow.md 例外条項）。`seo-article-localize` 判定はスキップ（base spec が en-SERP-rooted、姉妹記事 `business-email-template` / `japanese-business-phrases-pdf` と同パターン）。次：**人間レビュー EN v1 → EN v2 if needed → publish flip 両言語**。

- [ ] **Article #11 spec (`how-to-write-japanese-business-email`) generated 2026-05-12.** Phase 2 第3弾。`business-email` クラスター内で既存 `business-email-template` (live、テンプレ集) の**プロセス重視・姉妹記事**として位置づけ。冒頭にユーザーへ位置づけ確認 (AskUserQuestion) を行い「プロセス重視の姉妹記事として新規作成」を採用。Top 10 SERP 取得（cotoacademy / cotoclub / daijob / scalingyourcompany / wasabi-jpn / migaku / nihongo-career / toranomon-ls / jportjournal / fluentu）— jportjournal は HTTP 500 で fetch 失敗、§2 に position anchor、§3 は 9/10 から merge。**6 ゼロカバレッジ SERP ギャップ**を全押し：(1) per-step judgment rules 0/10、(2) TO/CC/BCC/各位 選択ルール 1/10 → 章として独立、(3) 15–25 字改行ルール 1/10 → 本文セクション必須化、(4) uchi-soto × 上下二軸マトリクス 0/10（片軸のみ 2/10）、(5) 送信前 10 項目チェックリスト 0/10、(6) 誤送信リカバリ 0/10。差別化の核：8 ステップラダー（件名 → 宛先選択 → 宛名 → 冒頭挨拶 → 名乗り → 本文 → 結び → 署名）の各ステップに (a) 何を決めるか (b) ルール (c) A/B/C レジスタ 1 行決め (d) マイクロ例 1 行だけを置き、フル例が欲しい読者は `business-email-template` に動線。`keigo-guide` の A/B/C politeness framework を「ステップ × レジスタ」マトリクスとして再活用。3 primary_info_seeds：(a) per-step ambiguity audit（native 2-3 名、~6h）、(b) 15-25 字改行 read-time experiment（8-12 人、~8h）、(c) 新規入社 1 ヶ月の mistake log（3-5 名 interview、~10h）。Internal link 戦略：各ステップ末尾に `business-email-template` への動線を入れ、「process here / templates there」の役割分担を読者の頭の中に植える。Spec: `specs/articles/how-to-write-japanese-business-email.spec.md` (status: drafting、bilingual §1 §4 §5 §7)。**次：** §5 と §6 の人間レビュー → JA v1 ドラフト → 人間レビュー → JA v2 → `seo-article-localize` 判定 → EN v1。

- [x] **Article #10 (`japanese-for-it-professionals`) JA v1 + EN v1 一気通貫 ship 2026-05-13.** Phase 2 第2弾、新クラスター `tech-japanese` のピラー記事。EN（外国人エンジニア向け）と JA（**Option B 採択：日本人 PM / テックリード / EM 向け「外国人エンジニアと働くための日本語」**）が対の物語を構成。EN: A/B/C × 6 儀式マトリクス 24+ コピペ文 + Week-1 deck 20 phrase + JLPT × engineering task ladder + 片仮名ピッチアクセント 12 語 + Top 5 engineer-specific keigo mistakes + 100-word read-vs-write split。JA: 6 つの詰まり場面 + 3 原則（短く・主語明示・選択肢提示）+ 6 儀式言い換え + 7 つの書き方ルール + 日本人側 5 落とし穴 + Slack / Notion / 議事録テンプレ運用。両言語 linter idempotent pass（EN は 11 件 weak qualifier 手動修正 + 2 個の URL anchor 修復、JA は CJK-ASCII 空白自動除去）。`astro check`: 0/0/0、`pnpm build`: green、22 pages indexed。両言語 `status: drafting`（spec lifecycle、未 publish）。**次：** 人間レビュー → 必要なら v2 → publish flip。**Option B 決定の根拠** spec §10 に記録：(1) サイトブランド整合、(2) `tech-japanese` クラスター整合、(3) primary_info_seeds 80% 共有可、(4) EN/JA の対物語性。

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
| 2026-05-11 | **Article #7 (`keigo-mistakes`) published — Phase 1 完了**. ★6 priority の最終記事。JA at `src/data/guides/ja/keigo-mistakes.mdx` (281 lines)、EN at `src/data/guides/en/keigo-mistakes.mdx` (286 lines)。Tier 1/2/3 重大度モデルを記事の骨組みに、A/B/C politeness framework と独立した第二軸として導入。冒頭 self-diagnostic（5問 yes/no）で読者がすぐ自分の最優先ミスを特定できる構成。spec lifecycle: `drafting` → `published`、両言語 published に flip。Phase 1 終了：**全 7 記事 live**（`keigo-guide` / `business-email-template` / `keigo-cheat-sheet` / `japanese-self-introduction-business` / `keigo-examples` / `japanese-business-phrases-pdf` / `keigo-mistakes`）。6月26日コミット計画より約1.5ヶ月先行で達成。次の手は GSC URL 検査 + インデックス登録リクエスト。| ryoooue (publish trigger) + Claude Opus 4.7 |
| 2026-05-12 | **Article #9 spec (`best-way-to-learn-keigo`) generated** — Phase 2 第1弾。Top 10 SERP 取得（Risu Press / JLPTLord / Nihon GO! World / Coto / Ishikawa JET / Japan Living Life / Kokoro Media / Kanadojo / FluentU / WaniKani forum）。SERP intent-mismatch を発見：純粋な HOW-TO learning-strategy は 3/10、ハイブリッド 3/10、純粋な WHAT-IS explainer が 4/10 → "best way to learn" 直球の HOW-TO 記事は事実上不在。**5 ゼロカバレッジ・ギャップ**：(1) 時間軸ロードマップ 0/10、(2) ステージ別マイルストーン 0/10、(3) 学習法比較マトリクス 0/10、(4) セルフ診断 0/10、(5) 期間感の実数 0/10。差別化の核：A/B/C politeness framework（`keigo-guide` 由来）を **90 日学習プランの骨格**に転用してクラスター内整合性を維持 + 6 手法 × 6 軸の method matrix + シャドーイング 5 ステップ + ロープレ台本 3 本（面接 / 報告 / 謝罪）+ つまずきカルテ（敬語パラリシス／「させていただく」過剰／sonkeigo-kenjougo 混同 を *学習者が通る段階の症状* として再フレーム）。3 primary_info_seeds：(a) 著者本人による 90 日学習ログ、(b) 非ネイティブ 10–15 名サーベイ、(c) shadowing vs SRS vs tutor vs manga の A/B 自己実験。Internal link: pillar = `keigo-guide`、sibling として既存 8 記事すべて参照（学習ロードマップ・ノードとして cluster をまとめる位置づけ）。Spec: `specs/articles/best-way-to-learn-keigo.spec.md` (status: drafting、bilingual §1 §4 §5 §7)。次は §5・§6 の人間レビュー → JA v1 ドラフト。| seo-article-outline (Claude Opus 4.7) + ryoooue |
| 2026-05-13 | **Article #11 (`how-to-write-japanese-business-email`) EN v1 shipped**. Body at `src/data/guides/en/how-to-write-japanese-business-email.mdx` (3,862 words)。JA v1 を同セッションで author 確定（タイトル「一から」削除 + 冒頭 hook を house-style 疑問形に変更で広いターゲット層に拡大）→ ユーザー明示で EN 即着手（feedback_article_writing_workflow.md 例外条項「JA も EN もまとめて作って」の同セッション完了パターン）。`seo-article-localize` 判定はスキップ（base spec が en-SERP-rooted、`business-email-template` / `japanese-business-phrases-pdf` と同パターン）。Spec §7 EN outline を 1:1 実装：title "How to Write a Japanese Business Email: 8 Steps from Subject to Signature" (74 chars、exact-match KW を冒頭 38 chars 内に配置、JA タイトルと整合的に「8 steps」を強調)、4 persona bullets、Three ways Japanese business email differs from English (Featured-snippet-friendly preamble、A/B/C テーブル + 15–25-char ルール紹介)、Step 0 with *uchi-soto* (内外) framing + TO/CC/BCC chapter、Steps 1–8 各々が「What to decide / Rule / A/B/C table / Common mistakes」の 4 パート固定構造 + ステップ末尾の `business-email-template` 動線、Body section に before/after コードブロック（15–25 字改行）+ 「conclusion → reason → ask」原則、10-item pre-send checklist (0/10 SERP gap)、Recovery section + 30-second correction email full template (0/10 SERP gap)、FAQ 5 H3 (PAA-aligned)、7 sibling cross-links + Essential 30 CTA。en-article-style ルール A1–D7 全準拠：em-dash spacing / en-dash for ranges (N3–N2) / Oxford comma / sentence-case H2/H3 / italic *romaji* + (kanji) on first use with Hepburn macrons (ō/ū) / 40–60-word featured-snippet paragraph / 4-sentence paragraph cap / bold key phrase / descriptive anchors。Linter: 0 auto-fixes、2 weak-qualifier flag を手動修正（"really" "just"）。`pnpm build` green at 84 pages, 0 errors。両言語とも `status: drafting`（spec lifecycle、未 publish）。**次：人間レビュー EN v1 → EN v2 if needed → publish flip 両言語**。| Claude Opus 4.7 + ryoooue |
| 2026-05-13 | **Article #11 (`how-to-write-japanese-business-email`) JA v1 shipped**. Body at `src/data/guides/ja/how-to-write-japanese-business-email.mdx` (12,847 chars含む frontmatter + FAQ)。Spec §7 JA outline を 1:1 実装：8 ステップ全部に「何を決めるか／ルール／A/B/C選び方表／ありがちなミス」の4パートを固定で配置 + ステップ0 を「書き始める前に決める3つのこと」として TO/CC/BCC を独立章にし SERP 1/10 ギャップを正面突破 + 1行15–25字改行ルールを本文セクションに before/after コードブロックで明示し SERP 1/10 ギャップ実装 + 送信前10項目チェックリスト（0/10 ギャップ）+ 誤送信リカバリ章（0/10 ギャップ、名前間違いの謝罪メール完成形 1 本収録）+ FAQ 5 件 PAA 起点 + 関連記事7本クロスリンク。タイトル「日本語ビジネスメールの書き方｜件名から署名まで8ステップで一から組み立てる」（39 字、KW 完全一致 + benefit promise）。`ja-article-style` linter: 1 回目で 8 個の `**...**`→`<strong>` 変換（CommonMark flanking rules 起因）+ 1 個の `TO / CC / BCC`→`TO/CC/BCC` collapse、2 回目で idempotent pass。手動修正: `NGです`→「不適切」 (Rule 3) と `OK（短縮版）`→「可（短縮版）」 (Rule 3 同) の 2 箇所。`pnpm build` green at 70 pages (前回 67 → +3 ja/en/index.html 経路で記事1 本 + faq/sitemap 派生)。**次：人間レビュー待ち** → JA v2 → `seo-article-localize` 判定 → EN v1。EN は JA レビュー前に着手しない方針（feedback_article_writing_workflow.md 例外条項「JA も EN もまとめて作って」が今回はないため、姉妹記事 `business-email-template` と同じ JA-first 順序で進める）。| Claude Opus 4.7 + ryoooue |
| 2026-05-12 | **Article #11 spec (`how-to-write-japanese-business-email`) generated** — Phase 2 第3弾、`business-email` クラスター内の **プロセス重視・姉妹記事**。冒頭に AskUserQuestion で位置づけ確認（既存 `business-email-template` と secondary keyword "how to write Japanese business email" が重複していたため）→ 「プロセス重視の姉妹記事として新規作成」を採用。Top 10 SERP 取得：9/10 fetch 成功（cotoacademy / cotoclub / daijob / scalingyourcompany / wasabi-jpn / migaku / nihongo-career / toranomon-ls / fluentu）、1/10 失敗（jportjournal HTTP 500、§2 に position anchor として記録、§3 は 9/10 から merge）。**6 つの zero-coverage SERP ギャップ**全押し：(1) per-step judgment rules 0/10、(2) TO/CC/BCC/各位 選択ルール 1/10、(3) 15–25 字改行ルール 1/10、(4) uchi-soto × 上下二軸マトリクス 0/10（片軸のみ 2/10）、(5) 送信前 10 項目チェックリスト 0/10、(6) 誤送信リカバリ 0/10。差別化の核：**8 ステップラダー**（件名 → 宛先選択 → 宛名 → 冒頭挨拶 → 名乗り → 本文 → 結び → 署名）× **A/B/C レジスタ各ステップ埋め込み**（`keigo-guide` 由来）。各ステップは (a) 何を決めるか (b) 判断ルール (c) A/B/C レジスタ 1 行決め (d) マイクロ例 1 行だけで完結 → フル例が必要な読者は `business-email-template` に動線。**Internal link 戦略**：各ステップ末尾に `business-email-template` への動線を埋めて「process here / templates there」を読者の頭に植える。`business-email` クラスターは今や 2 記事（`business-email-template` + この記事）でペア構成、pillar なし。3 primary_info_seeds：(a) per-step ambiguity audit by 2-3 native business-JP reviewers（~6h）、(b) 15-25 字改行 read-time experiment（8-12 人、~8h）、(c) 新規非ネイティブ入社 1 ヶ月の mistake log via 3-5 名 interview（~10h）。Spec: `specs/articles/how-to-write-japanese-business-email.spec.md` (status: drafting、bilingual §1 §4 §5 §7)。次は §5 / §6 の人間レビュー → JA v1 ドラフト着手。| seo-article-outline (Claude Opus 4.7) + ryoooue |
| 2026-05-12 | **Article #10 spec (`japanese-for-it-professionals`) generated** — Phase 2 第2弾、**新クラスター `tech-japanese` のピラー記事**（`src/config/clusters.ts` に既存定義）。Top 10 SERP 取得：7/10 fetch 成功（Coto / Japan Dev / Daijob / LinkedIn pulse / Travel With Languages / Le Wagon Medium / Build+）、3/10 失敗（TokyoDev 403、SelfTaughtJapanese 403、Quora 429 — position anchors retained）。SERP intent dual：①vocab-token list（Coto 200語 / Japan Dev / Daijob / Travel）②career decision（LinkedIn / Build+ / Le Wagon）。**7 ゼロカバレッジ・ギャップ**：(1) 完成文 × 儀式マッピング 0/10、(2) A/B/C register × 儀式マトリクス 0/10、(3) read-vs-write 受発信分離 0/10、(4) 週1生存デッキ優先順位 0/10、(5) JLPT × 業務ラダー 0/10、(6) 片仮名ピッチアクセント注意 0/10、(7) エンジニア特有 keigo ミス 0/10。差別化の核：既存 `keigo` cluster の **A/B/C politeness framework を 6 エンジニア儀式**（Daily Standup / PR Review / Sprint Planning / Demo / Retrospective / Client Call）に転用、18 セル × 2-3 文 = **30+ コピペ完成文**でトークンリスト記事群から差別化。100語 read-vs-write 2列表（受信 60 語 / 発信 40 語）で学習負荷削減フレーム提示。3 primary_info_seeds：(a) PR コメント頻度分析（公開 OSS 50 PR + 匿名化社内 20 PR、~6h）、(b) N3-N2 エンジニア 3 名インタビュー「1週目に欲しかったフレーズ」（~5h）、(c) 著者2週間ピッチアクセント field log（~5h）。Internal link：upstream なし（本記事 = `tech-japanese` cluster pillar）、downstream `keigo-guide` / `keigo-mistakes` / `japanese-business-phrases-pdf` / `japanese-self-introduction-business`、planned children `japanese-pr-review-phrases` / `japanese-standup-phrases` / `katakana-tech-pitch-accent` / `engineer-keigo-mistakes`。**Localization 重要フラグ**：KW「japanese for it professionals」は外国人エンジニア向けのため、JA 版は前提崩壊（日本人読者はターゲットでない）。JA 着手前に方向性再決定が必須（候補 A：日本人エンジニア向け英語テック語、B：日本人 PM / 同僚向け「外国人エンジニアが詰まる日本語ポイント」、C：JA 公開せず EN 単体）。Spec: `specs/articles/japanese-for-it-professionals.spec.md` (status: drafting、bilingual §1 §4 §5 §7)。次は §5 / §6 / §10 の人間レビュー → JA 方向性決定 → ドラフト着手。| seo-article-outline (Claude Opus 4.7) + ryoooue |
| 2026-05-11 | **Article #8 (`polite-japanese-phrases-for-office`) published — Phase 1 ボーナス記事**. オリジナル7記事計画外で追加した keigo cluster 第8記事。target keyword `polite japanese phrases for office`、cluster: keigo / pillar: keigo-guide、sibling として `keigo-cheat-sheet` / `keigo-examples` / `japanese-business-phrases-pdf` の隣に位置づけ。差別化の核：(1) chronological office-day arc（朝→仕事→ランチ→退社→事故時、SERP 9件中ゼロ）、(2) who-says-this-to-whom 4列マトリクス（上司/同僚/後輩/社外客 × 10フレーズ、SERP 9件中ゼロ）、(3) 全フレーズ行に「common mistake」コールアウト（iiicareer のみが部分実装）。ミス章は `keigo-mistakes` への明示的バトンに縮約しクラスター内重複を回避。JA at `src/data/guides/ja/polite-japanese-phrases-for-office.mdx` (257 lines)、EN at `src/data/guides/en/polite-japanese-phrases-for-office.mdx` (260 lines)。両言語 linter idempotent pass、astro check 0/0/0。spec lifecycle: `drafting` → `published`、両言語 flip。**Phase 1 = 8/7 (114%)** — 元計画+1で完了。バンドル commit (`keigo-mistakes` と並列で同セッション内2 separate commits)。次の手は GSC URL 検査 + インデックス登録リクエスト 2記事分。| ryoooue (publish trigger) + Claude Opus 4.7 |
| 2026-05-13 | **Article #10 両言語 publish flip — Phase 2 初の publish 記事**. ユーザー approve（JA v1.1 review pass + EN v1 そのまま OK）→ spec `status: drafting → published`、両言語 `published` に flip、ROADMAP Live articles 表 ✅ published。`tech-japanese` クラスター pillar 第1号として live。**Phase 2 進捗**: #9 `best-way-to-learn-keigo` / #10 `japanese-for-it-professionals` / #11 `how-to-write-japanese-business-email` の 3 記事中、**#10 が最初の publish**（#9 #11 は未 publish）。両 mdx ファイルは `draft: false` 設定済のため、git push で Cloudflare Pages auto-build → 反映予定。次：git commit (`feat: ship japanese-for-it-professionals article (JA + EN)`) → push → GSC URL 検査 + インデックス登録リクエスト 2 URL（ja/en）。| ryoooue (publish trigger) + Claude Opus 4.7 |
| 2026-05-13 | **Article #10 JA v1.1 ユーザーレビュー反映**。3 点修正：(1) JA タイトル「PR・朝会で『伝わる』書き方」→「あなたの指示が伝わる書き方」（4 候補から AskUserQuestion で選定、「自分ごと化しづらい」の指摘に対応）、(2)「レジスタ」→「言葉遣い／調子／レベル」7 箇所置換（過去の `keigo-examples` JA v2 で確立した house-style「レジスタ→使い分け」を tech 文脈に拡張）、(3) H2「日本語で詰まる 6 つの場面」→「日本語でぶつかる 6 つの壁」+ 直下リード「詰まりどころ」→「ぶつかる壁」（読者の感情語に寄せる）。EN は変更なし。`ja-article-style` idempotent pass、`pnpm build` green at 23 pages indexed。spec lifecycle: 両言語 `drafting` のまま。次：EN レビュー → publish flip。| Claude Opus 4.7 + ryoooue |
| 2026-05-13 | **Article #10 (`japanese-for-it-professionals`) JA v1 + EN v1 一気通貫 ship**. ユーザー明示指示で同セッション両言語同時着手（feedback_article_writing_workflow.md 例外条項：「JA も EN もまとめて」相当）。**Option B 採択**：JA は外国人エンジニア向けではなく **日本人 PM / テックリード / EM 向け「外国人エンジニアと働くための日本語」** に reframe。EN は外国人エンジニア向けで spec §7 EN outline を 1:1 実装。**EN ファイル**（`src/data/guides/en/japanese-for-it-professionals.mdx`、約 4,200 words）：A/B/C × 6 儀式（Standup / PR Review / Sprint Planning / Demo / Retro / Client Call）= 24+ コピペ完成文 + Week-1 deck 20 phrase + JLPT N5→N1 × engineering task ladder + 片仮名ピッチアクセント 12 語 watchlist + Top 5 engineer-specific keigo mistakes（`keigo-mistakes` への動線）+ 100-word read-vs-write split + Slack/Notion observation log の習慣スタック + FAQ 5。EN タイトル "Japanese for IT Professionals: A Working Engineer's Guide" (52 chars、KW 完全一致 + benefit promise)。**JA ファイル**（`src/data/guides/ja/japanese-for-it-professionals.mdx`、約 4,800 字）：6 つの詰まり場面 + 「短く・主語明示・選択肢提示」3 原則 + 6 儀式 A/B/C 言い換え集（各儀式に「外国人エンジニア向けの注意」コールアウト）+ 7 つの書き方ルール + JLPT 別調整目安 + 日本人側 5 落とし穴（`keigo-mistakes` の鏡像）+ 片仮名アクセント 10 語 + Slack/Notion/議事録 3 場所のテンプレ運用ガイド + FAQ 5。JA タイトル「外国人エンジニアと働くための日本語ガイド｜PR・朝会で『伝わる』書き方」(39 字、secondary KW 含む)。**両言語 linter idempotent pass**：EN 1 回目で `weak qualifier` 警告 11 件 → 手動修正（actually/just/very/really を別表現置換）+ linter が壊した 2 個の URL anchor を修復（`#read-vs-write-vocabulary--the-100-word-split` と `/keigo-mistakes/#mistake-5-baito-keigo-...` が em-dash 変換で破損 → リンクを簡略化して回避）、JA は CJK-ASCII 空白除去 + bold→strong 変換が自動適用。`astro check`: 0/0/0、`pnpm build`: green、**22 pages indexed**（前回 20 → +2 = JA + EN）。**両言語 spec lifecycle: `languages.{en,ja}.status: planned → drafting`**（spec `status` も `drafting`）。**Option B 決定の根拠** spec §10 + §7 JA に記録：(1) サイトブランド「Real-World Japanese」整合、(2) `tech-japanese` クラスター内整合、(3) primary_info_seeds（PR コメント観察 / 1週目インタビュー / 片仮名アクセント field log）80% 流用可、(4) EN「外国人視点」/ JA「日本人マネージャー視点」で対の物語性を構成しクロスリンクで滞在伸長期待。Option A（日本人向け英語テック語）と Option C（JA 非公開）は spec §10 で却下記録済。**次：** JA + EN 人間レビュー → 必要なら v2 → publish flip（両言語まとめてフリップが推奨、対の物語性が崩れないように同タイミング公開）。| Claude Opus 4.7 + ryoooue |
| 2026-05-13 | **Article #9 (`best-way-to-learn-keigo`) EN v1 shipped** — JA v2 と同セッション内で両言語完走。EN at `src/data/guides/en/best-way-to-learn-keigo.mdx` (454 lines、4,928 words)、`en-article-style` linter idempotent pass after 5 weak-qualifier 手動修正（*actually*×4 + *just*×1：FAQ frontmatter "actually use in client emails" / quoted persona "I just don't know... how long it'll actually take" / "what you actually want" / "It's actually reserved for" / "the pace you can actually sustain" を全て削減形に置換）、`pnpm build` green at **24 indexed pages**（前回 22 → +2 ja/en 経路）、サイトマップ登録予定。**`seo-article-localize` 判定: スキップ** — base spec が en-SERP-rooted (`serp_language: en`) のため EN diff spec 不要（`business-email-template` / `japanese-business-phrases-pdf` と同じ判断、`feedback_article_writing_workflow.md` の EN 単独判定パス）。EN タイトル "Best Way to Learn Keigo: A 90-Day, 3-Stage Roadmap" (52 chars、KW exact-match + benefit promise)。en-article-style ルール A1–D7 全準拠：em-dash + spaces / en-dash for ranges (N3–N2, Day 1–30) / Oxford comma / sentence-case H2/H3 / italic *romaji* + (kanji) on first use / Hepburn macrons (ō / ū) / 40–60-word featured-snippet 段落（intro 直後の "The fastest way to learn keigo is to lock in *teineigo* first..."）/ persona hooks 4 bullets / contractions 多用 / FAQ 5 H3 / descriptive anchors。**JA v2 softening を EN にもバックポート**：A→B→C ジャーゴンは title から外し、intro と framework section 以降で本格紹介。Stage 1/2/3 のテーブル説明では "Start with the pace you can sustain" など 1 つの選択肢としての提示を維持。両言語 `status: drafting`（未 publish）。spec `languages.en.status: planned → drafting` に更新。次：**人間レビュー** → 必要なら EN v2 → publish flip。| Claude Opus 4.7 + ryoooue |
| 2026-05-13 | **Article #9 (`best-way-to-learn-keigo`) JA v1 → JA v2 shipped** — JA v1 を人間レビュー後、4 点修正で JA v2 化：(1) タイトル「敬語を最短で身につける学習法｜A→B→Cの90日プラン」→「敬語を最短で身につける学習法｜段階別90日ロードマップ」（A→B→C は初見ユーザーに伝わらず CTR を毀損するため "段階別" + "ロードマップ" に置換、34 → 28 字）。(2) 冒頭リード「丁寧語の自動化からスタートして90日で職場運用ラインに到達するステージ別ロードマップを、A→B→Cの3段階で示します」→「丁寧語の習得を最初の足場として、90日で職場運用ラインに近づくための段階別ロードマップを1つの選択肢として示します」（決めつけ口調を回避、選択肢として提示）。(3) 「その章だけ拾い読みする使い方を推奨します」→「必要な章だけ拾い読みする読み方もできます」（推奨ではなく許可ニュアンスに）。(4) A/B/C 表 B 行「ステージ1（Day 1〜30）で完全自動化」→「ステージ1（Day 1〜30）で固める」（「完全自動化」が機械的）。`ja-article-style` linter は修正後も idempotent pass。CTR 寄与の "最短" + "90日" + "ロードマップ" の主要 hook は維持。**この softening を EN v1 にもバックポート**して同セッション内で EN 完走へ。| Claude Opus 4.7 + ryoooue |
| 2026-05-13 | **Article #9 (`best-way-to-learn-keigo`) JA v1 shipped**. Body at `src/data/guides/ja/best-way-to-learn-keigo.mdx` (450 lines、約14,300字含ローマ字)、`ja-article-style` linter idempotent pass、`pnpm build` green at 20 indexed pages (Pagefind index 完了)、サイトマップ登録予定。タイトル「敬語を最短で身につける学習法｜A→B→Cの90日プラン」(34 字、`｜` 区切り + benefit promise)。Spec §7 JA outline を 1:1 実装：4 ペルソナ → 5 問セルフ診断（Yes 数で章ルーティング：0–1 → ステージ1、2 → ステージ2、3–4 → ステージ3、5 → keigo-mistakes へ）→ A/B/C フレームの 60 秒復習 + 「読む7割×話す3割」インプット比率ルール + 「3 種類同時学習はなぜ遠回りか」3 理由 → 90 日ロードマップ全体表（6 列：到達目標 / 教材 / 1 日 15 分タスク / 週末 30 分ドリル / 自己テスト）→ ステージ1（Day 1–30、丁寧語の自動化）：7 日スターターメニュー + Day 30 の 10 問口頭テスト → ステージ2（Day 31–60、核 8 動詞ペア + 現場フレーズ）：8 動詞ペア 3 列表 + SRS カードレイアウト + メール/電話/会議 各 5 本 + Day 60 5 シーン即答テスト → ステージ3（Day 61–90、アウトプット中心）：シャドーイング 5 ステップ + ロープレ台本 3 本（面接 / 上司報告 / 取引先謝罪）+ Day 90 未見 3 シーンテスト → 学習法マトリクス（6 手法 × 7 列：1 日コスト / 週コスト / 主な役割 / 適したステージ / 教材例 / 弱点）+ 各手法の使い方メモ → つまずきカルテ 3 症状（敬語パラリシス / 「させていただく」過剰 / sonkeigo-kenjougo 混同）+ 各症状に「次の一手」3 つずつ → 期間感のリアル表（5 段階累計時間：40-60h / +20h / +40h / 累計120-150h / 累計250-400h）+ 週ペース別 3 シナリオ（週 2h / 週 4.5h / 週 7h）→ FAQ 5 件 → 関連リンク 6 sibling + Essential 30 CTA。**用語ハウスルール再適用**：linter 自動修正後、過去の `keigo-examples` JA v2 で確定済みの「レジスタ→レベル」ルール を replace_all で 11 箇所適用（C/B レジスタ → C/B レベル）。Yes/No は構造的なクイズ形式として維持。Spec の `languages.ja.status: planned → drafting` に更新。**次：人間レビュー待ち** → JA v2（あれば）→ `seo-article-localize` 判定 → EN v1（EN は JA v2 確定まで着手しない、feedback_article_writing_workflow.md ルール）。| Claude Opus 4.7 + ryoooue |

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
