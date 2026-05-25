---
# === IDENTIFICATION ===
slug: "business-japanese"
collection: "guides"
cluster: "foundations"                     # Site-wide hub above the 6 sub-clusters. Registered in src/config/clusters.ts (added 2026-05-25). Slug stays "business-japanese" (exact head-term match); cluster is the umbrella nav label.
pillar: null                               # This IS the master pillar — every cluster pillar rolls up to it.

# === SEO ===
target_keyword: "business japanese"
serp_language: "en"
target_intent: "informational"
search_volume_estimate: "2k–5k/mo (head term; broad informational intent, splits into etiquette / phrases / test-prep / learning-path sub-intents)"
difficulty_estimate: "high"
secondary_keywords:
  - "business japanese guide"
  - "business japanese phrases"
  - "japanese for work"
  - "how to learn business japanese"
  - "business japanese etiquette"

# === FUNNEL ===
funnel_stage: "TOFU"
product_cta: "essential-30"
lead_magnet: null

# === LANGUAGES ===
languages:
  en:
    status: "published"
    url_slug: "business-japanese"
    diff_spec: null
  ja:
    status: "published"
    url_slug: "business-japanese"
    diff_spec: "specs/articles/business-japanese.ja.spec.md"   # seo-article-localize 2026-05-25: diff_needed=TRUE, Option B audience pivot (HR/trainer).

# === LIFECYCLE ===
status: "published"
created: "2026-05-25"
last_serp_audit: "2026-05-25"
---

# articleSpec: Business Japanese (site-wide hub pillar)

> **How to use this file**
> - The `seo-article-outline` skill generates the initial version.
> - Humans review and refine the "Our Differentiation" and "primary_info_seeds" sections.
> - When SERP changes significantly, re-run the skill to refresh sections 2–4.
> - Do NOT delete the spec after publication — it's the source of truth for updates.
>
> **Role:** This is the **master hub pillar** for the entire site. It does not try to teach every topic in depth; it gives a 300–500-word orientation per cluster and routes the reader to the deep-dive article. All 6 clusters (keigo / business-email / meetings / workplace-culture / tech-japanese / daily-office) are downstream of this page.

---

## 1. Target & Intent

### JA

**主要な検索意図:** 「business japanese」と検索する人は、**職場で通用する日本語の全体像**を一望し、自分に今どこが足りないかを把握して、次に何を学べばいいかの地図がほしい。単発のフレーズ集ではなく「ビジネス日本語とは何で、何から手をつけるか」という入口を探している。SERP は (a) 礼儀・マナー (b) フレーズ集 (c) BJT 等の試験対策 (d) 学習法・教材 の 4 系統に割れており、どの競合も全部を 1 ページに詰め込もうとして浅くなっている。

**読者ペルソナ:** 日本で働き始めた／これから働く外国人プロフェッショナル。日常会話レベルの日本語はあるが、上司・取引先相手だと固まる。「まず何を押さえれば仕事で恥をかかないか」を 5 分で見渡したい。

**成功基準:** 読者が (1) ビジネス日本語が普通の日本語とどう違うかを 1 段落で理解し、(2) 自分の弱点クラスター（敬語／メール／会議／文化／IT）を 30 秒で特定でき、(3) そのクラスターの深掘り記事へ迷わず進め、(4) 90 日でどの順に学ぶかの道筋を持って離脱する。

### EN

**Primary search intent:** Someone searching "business japanese" wants a **map of the whole territory** — what professional Japanese is, how it differs from the textbook Japanese they already know, where their own gap is, and what to study next. They want an orientation page, not one more flat phrase dump. The SERP splits four ways (etiquette / phrase lists / test prep like BJT / learning method), and every competitor crams all four into one page and goes shallow on each.

**Audience persona:** A foreign professional who has just started, or is about to start, working in Japan — has conversational Japanese but freezes with a boss or client, and wants to survey "what do I need so I don't embarrass myself at work" in five minutes.

**Success criteria:** The reader leaves having (1) understood in one paragraph how business Japanese differs from casual Japanese, (2) identified their weakest cluster (keigo / email / meetings / culture / tech) in 30 seconds, (3) clicked through to the right deep-dive article without friction, and (4) a sequenced 90-day path for what to learn in what order.

---

## 2. SERP Analysis (Top 10)

> Captured on: 2026-05-25. Search engine: Google. Locale: en-US.
> Coverage denominators are always `/10`.
> Excluded from the slate: amazon.com (book product, not an article) and japanesepod101.com/lesson-library (duplicate domain with row 7 — kept the higher-ranked blog post).

| # | URL | Domain | Title | Format | Word Count | Notes |
|---|---|---|---|---|---|---|
| 1 | https://japan-dev.com/blog/doing-business-in-japan-a-crash-course-in-japanese-for-the-workplace | japan-dev.com | Business Japanese: The Ultimate Guide [2026] | guide | long >3000 | Strongest all-rounder; grounded in author's corporate experience. Covers keigo + uchi/soto + verbs + phrases + JLPT/JPT/BJT + anime + on-the-job learning. Assumes baseline competency. |
| 2 | https://japanswitch.com/ultimate-guide-to-business-japanese/ | japanswitch.com | Ultimate Guide to Business Japanese | guide | long >3000 | Heavily BJT- and job-hunting-weighted; keigo broken out by audience (boss/customer/colleague/subordinate). Thin on email/meeting phrasing. |
| 3 | https://www.daijob.com/en/guide/skill-up/business_japanese/ | daijob.com | Mastering Business Japanese for Success | guide | medium 1500–3000 | Conceptual essay (gairaigo, business-jargon evolution, multilingualism, intercultural). Almost no concrete phrase lists — abstract. |
| 4 | https://migaku.com/blog/japanese/japanese-for-business | migaku.com | Business Japanese: Essential Phrases & Etiquette Guide | guide | medium 1500–3000 | Etiquette-heavy (cards, dress, gift, dining, hierarchy) + "reality of working as a foreigner" + FAQ. Light on grammar scaffolding. |
| 5 | https://www.fluentu.com/blog/japanese/business-japanese/ | fluentu.com | Your Guide to Business Japanese, from Vocabulary to Essential Etiquette | guide | long >3000 | Unique: industry-specific vocab across 6 industries (finance/tech/hospitality/healthcare/education/real estate) + telephone + negotiations. No worked dialogues. |
| 6 | https://tcj-education.com/blog/practical-business-japanese-the-ways-and-examples/ | tcj-education.com | Practical Business Japanese – The Ways and Examples | guide | long >3000 | Abstract: "go beyond politeness," reduce elementary mistakes, sonkeigo vs kenjougo, cultural background. Few concrete fixes for ambiguity. |
| 7 | https://www.japanesepod101.com/blog/2021/02/11/japanese-business-phrases/ | japanesepod101.com | Business Japanese: Phrases You Need for Workplace Success | guide | long >3000 | Scenario phrase lists (interview / coworkers / meeting / phone / email), each with Japanese text. No audio despite podcast brand. |
| 8 | https://scalingyourcompany.com/guide-to-best-japanese-business-phrases/ | scalingyourcompany.com | Ultimate Guide to Best Japanese Business Phrases | guide | long >3000 | Phrases + etiquette (meishi, seating, o-kaeshi) with tables; heavily promotional for the sponsor's coaching. |
| 9 | https://www.italki.com/en/blog/japanese-for-work | italki.com | The Ultimate Guide to Japanese for Work | guide | long >3000 | Most comprehensive structure: why-differs + keigo + phrases + vocab-building + common mistakes + practice routine + culture + interview + FAQ. CTAs interrupt flow. |
| 10 | https://www.smejapan.com/japan-business-guides/office-rentals-and-shared-spaces/japanese-phrases-terms-office/ | smejapan.com | Important Japanese Phrases and Terms in the Office | guide | medium 1500–3000 | 4-part format (kanji / hiragana / romaji / EN) for office phrases + company-structure terms + FAQ. Narrow to office navigation. |

### SERP features present
- [x] Featured snippet (definitional: "what is business Japanese")
- [x] People Also Ask (PAA)
- [ ] Video carousel
- [ ] Image pack
- [ ] Knowledge panel
- [x] Related searches (list below)

### Related searches / PAA questions
- What is business Japanese / how is it different from regular Japanese?
- What level of Japanese do you need to work in Japan? (JLPT N2/N1, BJT)
- Business Japanese phrases / greetings list
- How to learn business Japanese (best apps, courses, textbooks)
- Business Japanese etiquette (bowing, business cards, seating)
- What is keigo? sonkeigo vs kenjougo
- Hou-ren-sou (報連相) meaning

---

## 3. Merged Outline (from Top 10)

> All distinct headings found across the top 10, with strict coverage count.

| Heading | Coverage (x/10) | Notes |
|---|---|---|
| Keigo / honorific system (sonkeigo / kenjougo / teineigo) | 7/10 | Table stakes. japan-dev, japanswitch, migaku, tcj, jpod101, italki, daijob. Everyone explains the 3 levels; nobody gives a decision model. |
| How to learn / resources / courses / textbooks | 6/10 | japan-dev, japanswitch, italki, scalingyourcompany, migaku, daijob. Lists of resources, but rarely a sequenced path. |
| Greetings & everyday office phrases | 6/10 | japan-dev, migaku, jpod101, scalingyourcompany, italki, smejapan. お疲れ様 / おはようございます / お先に失礼します. |
| Business etiquette (bowing / cards / seating / gift / dining) | 6/10 | migaku, fluentu, scalingyourcompany, japanswitch, jpod101, italki. Meishi exchange most common. |
| Self-introduction / job interview / job hunting | 6/10 | japan-dev, japanswitch, jpod101, scalingyourcompany, smejapan, italki. |
| Business vocabulary / industry-specific terms | 6/10 | fluentu (6 industries), italki, jpod101, daijob (gairaigo), smejapan, scalingyourcompany. |
| How business Japanese differs from casual / "what is it" | 5/10 | japan-dev, migaku, italki, tcj, daijob. Often the intro paragraph; featured-snippet target. |
| Business email phrases | 5/10 | japan-dev, migaku, fluentu, jpod101, italki. よろしくお願いします / sign-offs. |
| Meeting phrases & meeting culture | 4/10 | migaku, fluentu, jpod101, italki. |
| Workplace culture / hierarchy / uchi-soto | 4/10 | japan-dev (uchi/soto, social distance), italki (reading between the lines), migaku, fluentu. |
| BJT / JLPT / proficiency tests | 4/10 | japan-dev, japanswitch (heavy), daijob, italki. |
| Phone call phrases | 3/10 | fluentu, jpod101, italki. |
| Common mistakes | 3/10 | italki (honorific prefix, pronoun), tcj, japan-dev. |
| Requests / asking favors / cushion phrases | 3/10 | japan-dev, italki, smejapan. |
| FAQ section | 3/10 | migaku, italki, smejapan. |
| 報連相 (Hou-ren-sou) as a named principle | 1/10 | Mentioned in passing; almost never a structured section despite being the #1 JP workplace concept. |

---

## 4. Content Gaps

> What the top 10 collectively fail to cover, but the searcher likely wants.

### JA

1. **「地図」としての記事が存在しない (0/10):** 全競合が 1 ページに礼儀・フレーズ・試験・学習法を詰め込み、結果どれも浅い。読者を弱点別に深掘りへ誘導する「ハブ＝地図」型は皆無。本サイトは 17 本の公開記事を持つため、ここが構造的優位。
2. **レジスタ選択の判断モデルがない (0/10):** どの競合も敬語 3 種を「説明」するだけで、「いつ・どのレベルを使うか」を決める枠組みがない。本サイトの A/B/C politeness framework（`keigo-guide` 由来）を 1 度だけ導入し、各クラスターへ展開できる。
3. **学習の順序（ロードマップ）がない (≈1/10):** 教材リストは多いが、「最初に何を、次に何を」という時系列の道筋がほぼ無い。italki に学習ルーティンはあるが端から端までの順序ではない。
4. **報連相を運用原則として構造化していない (1/10):** 日本の職場コミュニケーションの最重要概念なのに、独立セクションとして扱う競合がほぼ無い。
5. **自己診断による章ルーティングがない (0/10):** 読者のレベル・職種に応じて「あなたが読むべきはここ」と振り分ける仕組みが皆無。
6. **チャネル・マトリクス（メール／Slack・Teams／電話／対面／会議）がない (0–1/10):** リモート・デジタル職場のチャネル別使い分けがほぼ未カバー。

### EN

1. **No article positioned as a map (0/10):** Every competitor crams etiquette + phrases + tests + learning into one page and goes shallow. Nobody offers a hub that routes the reader to a deep-dive by their gap. With 17 published articles, that routing is our structural advantage.
2. **No register-selection decision model (0/10):** All ten *explain* the three keigo levels; none give a framework for *which level when*. We can introduce the A/B/C politeness framework (from `keigo-guide`) once and reuse it across every cluster section.
3. **No sequenced learning roadmap (≈1/10):** Plenty of resource lists, almost no ordered "learn this first, then this" path. italki has a daily routine but not an end-to-end sequence.
4. **Hou-ren-sou (報連相) not structured as an operating principle (1/10):** The single most important Japanese workplace-communication concept, yet virtually no competitor gives it a dedicated section.
5. **No self-diagnostic that routes the reader (0/10):** Nobody sends the reader to the right section by their level or role.
6. **No channel matrix (email / Slack-Teams / phone / in-person / meeting) (0–1/10):** Modern remote-workplace channel selection is barely addressed.

---

## 5. Our Differentiation

> Our unique angle. What makes this article rank above the top 10, not just match them?

### JA

- **ハブ＆スポーク構造:** H1 直下に全体像 → 各クラスター（敬語／メール／会議・電話／職場文化／IT職／日常オフィス）を 300〜500 字で要約し、各ブロック末に「詳しくはこちら」で深掘り記事へ動線。**地図に徹し、壁のようなテキストにしない**唯一のページ。
- **A/B/C politeness framework を背骨に:** 既存 17 記事で確立済みの A/B/C を 1 度だけ導入 → `keigo-guide` へ送る。レジスタ判断モデルを持つ競合はゼロ。
- **30 秒セルフ診断:** 5 問で読者を弱点クラスターへルーティング（敬語が不安？→ keigo / メールで固まる？→ business-email …）。`how-to-say-sorry` `common-japanese-business-mistakes` の診断パターンを流用。
- **3 つの運用原則セクション:** 報連相 ＋ ウチ・ソト ＋ 上下関係 を「なぜ」レイヤーとして構造化。フラットなフレーズ集競合には作れない。
- **90 日学習ロードマップ:** 既存 17 記事を学習順に並べた道筋（`best-way-to-learn-keigo` の 90 日モデルをサイト全体へ拡張）。
- **チャネル・マトリクス:** メール／Slack・Teams／電話／対面／会議 の 5 チャネル使い分け表 — モダン職場の差別化点。
- **80/20 スターターキット:** 全クラスター横断で「最初に覚えるべき 20」を抽出し記事前半に配置 → `japanese-business-phrases-pdf` / `japanese-email-phrases` へ送客＋Essential 30 CTA。head term の初学者に最も刺さる即効セクション。
- **「話す／書く」読み分けオーバーレイ:** クラスター章に「会議・電話・自己紹介＝話す／メール＝書く」のラベルを重ね、明日の会議 vs 今日のメールなど緊急の用途から読める導線にする（6 クラスター構造は崩さず、ナビ補助として重ねる）。
- **ロードマップの時間軸を明示:** 90 日ロードマップを Day 1 / Week 1 / Month 1 / Quarter 1 の 4 段に区切り、各段で必要になるクラスターを順に提示（`common-japanese-business-mistakes` の入社後タイムラインと整合）。

### EN

- **Hub-and-spoke architecture:** H1 overview, then a 300–500-word summary per cluster (keigo / email / meetings & phone / workplace culture / tech / daily office), each ending in a "go deeper" link to the deep-dive article. The only page on the SERP that behaves as a **map, not a wall of text**.
- **A/B/C politeness framework as the spine:** Introduce the framework (already established across 17 articles) once, then route to `keigo-guide`. Zero competitors have a register-decision model.
- **30-second self-diagnostic:** Five questions that route the reader to their weakest cluster (shaky on keigo? → keigo; freeze on email? → business-email …). Reuses the diagnostic pattern from `how-to-say-sorry` and `common-japanese-business-mistakes`.
- **Three operating-principles section:** Hou-ren-sou + uchi-soto + jouge (hierarchy) structured as the "why" layer that flat phrase-list competitors can't assemble.
- **90-day learning roadmap:** Sequences the existing 17 articles into an ordered path (extends the 90-day model from `best-way-to-learn-keigo` site-wide).
- **Channel matrix:** A five-channel selection table (email / Slack-Teams / phone / in-person / meeting) — a modern-workplace differentiator.
- **80/20 starter kit:** A cross-cluster "first 20 things to learn," placed early and routing to `japanese-business-phrases-pdf` / `japanese-email-phrases` + the Essential 30 CTA — the highest-payoff section for a head-term newcomer.
- **Spoken vs written reading-path overlay:** Label the cluster sections as spoken (meetings/phone/self-intro) vs written (email) so a reader with an urgent need can jump straight in — layered as navigation over the 6-cluster structure, not replacing it.
- **Explicit roadmap time axis:** Break the 90-day roadmap into Day 1 / Week 1 / Month 1 / Quarter 1, showing which cluster you need when (aligned with the post-onboarding timeline in `common-japanese-business-mistakes`).

---

## 6. primary_info_seeds

> 3 hypotheses for primary information to layer on over time. Each must be (a) absent from all top-10, (b) collectible in ~1 week, (c) E-E-A-T-improving.

1. **Site-corpus → workplace-moment routing map**
   - _What:_ A table mapping ~30 concrete workplace moments ("client is CC'd on a mistake," "you're late to a standup," "introducing your boss to a vendor") to the exact published article that solves each.
   - _How:_ Audit all 17 published articles; tag each to the moments it covers; surface gaps for future articles.
   - _Cost:_ ~6h
   - _Status:_ `not_started`

2. **First-90-days skill-gap survey (8–12 foreign professionals)**
   - _What:_ A data-backed ranking of "which business-Japanese gap cost you most in your first 90 days?" — used to order the hub's cluster sections by real pain, not guesswork.
   - _How:_ Google Form + DM outreach to foreign professionals working in Japan.
   - _Cost:_ ~10h (design + collection + synthesis)
   - _Status:_ `not_started`

3. **Author's 90-day onboarding field log**
   - _What:_ Week-by-week record of which skill mattered when during the author's own onboarding — anchors the roadmap section in a lived sequence rather than a generic curriculum.
   - _How:_ Personal experience log, retrospective + ongoing notes.
   - _Cost:_ ~8h spread over 12 weeks
   - _Status:_ `not_started`

---

## 7. Target Article Outline

> The final outline for OUR article. Derived from sections 3–5. This is a HUB — each cluster section is intentionally shallow (300–500 words) and ends in a deep-dive link.

### JA outline (target)

1. H1: _ビジネス日本語 完全ガイド｜職場で通用する日本語の全体像と学習ロードマップ_
2. H2: この記事を読むべき人（外国人ビジネスパーソン／これから日本で働く人）
3. H2: ビジネス日本語とは — 普通の日本語と何が違うか（featured-snippet ねらいの 40〜60 字結論段落）
4. H2: 30 秒セルフ診断 — あなたが今いちばん補強すべきはどこ？（5 問 → クラスター誘導）
5. H2: まず覚える 80/20 スターターキット — 領域横断「最初の 20」（→ `japanese-business-phrases-pdf` / `japanese-email-phrases` ＋ Essential 30 CTA）
6. H2: 3 つの運用原則 — 報連相・ウチソト・上下関係
7. H2: 敬語（A/B/C politeness framework の導入）
   - H3: A/B/C とは — 1 度だけの導入 → `keigo-guide` へ
8. H2: ビジネスメール【書く】
   - H3: パーツ → 書き方 → 完成形（`japanese-email-phrases` / `how-to-write-japanese-business-email` / `business-email-template` へ）
9. H2: 会議・電話【話す】（→ `japanese-meeting-phrases`）
10. H2: 職場文化とよくあるミス（→ `common-japanese-business-mistakes`）
11. H2: IT・技術職の日本語（→ `japanese-for-it-professionals`）
12. H2: 日常オフィスの定型表現・自己紹介【話す】（→ `polite-japanese-phrases-for-office` / `japanese-self-introduction-business`）
13. H2: チャネル別 使い分けマトリクス（メール／Slack・Teams／電話／対面／会議）
14. H2: 90 日学習ロードマップ — Day 1 / Week 1 / Month 1 / Quarter 1 で何から、どの順で
15. H2: 試験で証明する（JLPT / BJT の位置づけ）
16. H2: よくある質問
17. H2: CTA / 関連記事（Essential 30 + 各クラスター pillar）

### EN outline (target)

1. H1: _Business Japanese: The Complete Map to Workplace Japanese (+ a 90-Day Roadmap)_
2. H2: Who this guide is for
3. H2: What is business Japanese — how it differs from casual Japanese (40–60-word featured-snippet paragraph)
4. H2: 30-second self-diagnostic — where's your biggest gap right now? (5 questions → cluster routing)
5. H2: The 80/20 starter kit — the first 20 things to learn (cross-cluster → `japanese-business-phrases-pdf` / `japanese-email-phrases` + Essential 30 CTA)
6. H2: The three operating principles — hou-ren-sou, uchi-soto, hierarchy
7. H2: Keigo — the A/B/C politeness framework
   - H3: What A/B/C means — introduced once → link to `keigo-guide`
8. H2: Business email [written]
   - H3: Parts → process → templates (link to `japanese-email-phrases` / `how-to-write-japanese-business-email` / `business-email-template`)
9. H2: Meetings & phone calls [spoken] (→ `japanese-meeting-phrases`)
10. H2: Workplace culture & the most common mistakes (→ `common-japanese-business-mistakes`)
11. H2: Japanese for tech / IT roles (→ `japanese-for-it-professionals`)
12. H2: Everyday office phrases & self-introduction [spoken] (→ `polite-japanese-phrases-for-office` / `japanese-self-introduction-business`)
13. H2: The channel matrix — email / Slack-Teams / phone / in-person / meeting
14. H2: A 90-day learning roadmap — Day 1 / Week 1 / Month 1 / Quarter 1: what to learn, in what order
15. H2: Proving it on paper — where JLPT and BJT fit
16. H2: FAQ
17. H2: CTA / Related articles (Essential 30 + each cluster pillar)

---

## 8. FAQ / People Also Ask

| Question | Where answered |
|---|---|
| What is business Japanese, and how is it different from regular Japanese? | §3 (intro / featured-snippet paragraph) |
| What level of Japanese do I need to work in Japan? | §14 (tests) + FAQ |
| Do I need to pass the BJT or JLPT to get a job? | §14 (tests) |
| What is keigo? What's the difference between sonkeigo and kenjougo? | §6 (keigo) → `keigo-guide`, `sonkeigo-vs-kenjougo` |
| What does 報連相 (hou-ren-sou) mean? | §5 (operating principles) |
| How long does it take to learn business Japanese? | §13 (90-day roadmap) + FAQ |
| What's the single most useful business Japanese phrase? | §11 / FAQ (よろしくお願いします, お疲れ様です) |
| Can I get by at work with just English? | FAQ |

---

## 9. Internal Links

> This is the master hub. It is **upstream of the entire site**; nearly every link is downstream. At body-ship time, also add a backlink from each cluster pillar UP to this hub (reciprocal hub linking).

### Upstream (pillars / hubs linking to this article)
- None — this is the top-of-site master pillar. (Add reciprocal backlinks from cluster pillars during body-ship.)

### Downstream (articles this article links to)
- `keigo-guide` — keigo cluster pillar (A/B/C framework source)
- `best-way-to-learn-keigo` — 90-day roadmap section
- `japanese-email-phrases` / `how-to-write-japanese-business-email` / `business-email-template` — business-email cluster (parts / process / templates)
- `japanese-meeting-phrases` — meetings cluster pillar
- `japanese-self-introduction-business` — meetings cluster (self-intro)
- `common-japanese-business-mistakes` — workplace-culture cluster pillar
- `japanese-for-it-professionals` — tech-japanese cluster pillar
- `polite-japanese-phrases-for-office` — daily-office phrases
- `japanese-business-phrases-pdf` — printable phrase reference (+ Essential 30 CTA)
- Secondary: `sonkeigo-vs-kenjougo`, `keigo-cheat-sheet`, `keigo-examples`, `keigo-mistakes`, `japanese-honorifics-chart`, `how-to-say-sorry-in-japanese-politely`

### Sibling cluster articles
- N/A — the hub has no siblings; it parents all 6 clusters.

---

## 10. Localization Notes

> Heads-up for language-diff specs. Flag items likely to behave differently in non-English SERPs.

### JA

- **用語:** keigo / sonkeigo / kenjougo / uchi-soto / hou-ren-sou は EN ではローマ字＋漢字グロス。JA 版では当然すべて日本語表記（報連相、ウチ・ソト、上下関係）で、ローマ字は不要。
- **文化的前提:** EN 版は「読者＝日本の職場文化に不慣れな外国人」を前提に礼儀の「なぜ」を厚く説明する。JA 版はこの前提が成立しない可能性が高い（後述ペルソナ pivot 参照）。
- **競合ランドスケープ:** JA SERP「ビジネス日本語」は (a) 日本語学校・日本語教師向け教材、(b) 外国人材向け研修サービス、(c) BJT 対策 が中心になる見込みで、EN SERP（外国人学習者向け語学ブログ）と競合セットが大きく異なる。**この乖離が `seo-article-localize` を回すべき最大の根拠。**
- **言語固有のリスク:** 「business Japanese」という括り自体が日本語ネイティブには自明すぎて検索されにくい。JA 版のターゲットKW・タイトルは「ビジネス日本語」より具体的なロングテール（例「外国人 ビジネス日本語 勉強法」）へ寄せる必要があるかもしれない。
- **ペルソナ pivot の必要性:** **高い。** EN＝日本で働く外国人プロフェッショナル。JA 版は (i) 日本語で学ぶ外国人、(ii) 外国人部下を持つ日本人マネージャー／日本語教師 のどちらに寄せるかで記事が別物になる。`japanese-honorifics-chart` / `common-japanese-business-mistakes` と同じ判断構造 → **JA 着手前に `seo-article-localize` 必須**。Option B（audience pivot）になる公算が大きい。

### EN

- **Terminology:** keigo / sonkeigo / kenjougo / uchi-soto / hou-ren-sou stay romanized with a kanji gloss on first use (house style). These are the EN article's anchor terms.
- **Cultural assumptions:** The EN version assumes the reader is a foreigner unfamiliar with Japanese workplace norms, so it spends words on the "why" behind etiquette. That assumption does not hold for a native-Japanese audience.
- **Competitor landscape:** The JA SERP for "ビジネス日本語" is expected to be dominated by (a) Japanese-language-school / teacher materials, (b) corporate training services for foreign hires, and (c) BJT prep — a materially different competitor set from the EN SERP (foreign-learner language blogs). This divergence is the primary reason to run `seo-article-localize`.
- **Language-specific risks:** "Business Japanese" as a bucket may be too self-evident for native speakers to search; the JA target keyword/title may need to shift to a more specific long-tail than a direct translation of "ビジネス日本語."
- **Persona pivot signal:** **High.** EN = foreign professional working in Japan. JA could pivot to (i) foreigners studying in Japanese, or (ii) Japanese managers / teachers who work with foreign hires — and the article would be fundamentally different in each case. Same decision structure as `japanese-honorifics-chart` and `common-japanese-business-mistakes` → **run `seo-article-localize` before JA v1**; Option B (audience pivot) is the likely outcome.

---

## 11. Change Log

| Date | Change | Author |
|---|---|---|
| 2026-05-25 | Initial spec generated via `seo-article-outline` skill. Positioned as site-wide master hub pillar (user-confirmed via AskUserQuestion: hub role + slug `business-japanese`). Top-10 SERP captured, all 10 WebFetch succeeded. | Claude Opus 4.7 + ryoooue |
| 2026-05-25 | **EN v1 shipped.** `src/data/guides/en/business-japanese.mdx` (~3,400 words) implements the §7 EN outline 1:1 as the learner hub: who-it's-for, what-is + 6-area map table, 30-sec self-check, 80/20 starter kit (20 phrases), 3 operating principles, 6 area sections (each routing to the cluster deep-dive), channel matrix, Day1/Week1/Month1/Quarter1 roadmap, JLPT/BJT, FAQ (5, also in frontmatter for JSON-LD), and a Where-to-go-next link hub to all 17 articles + Essential 30 CTA. `en-article-style` linter idempotent pass (6 weak-qualifier + 1 title-case heading fixes, then auto-normalize). Page built OK (dist HTML generated); full `pnpm build` errored only on a concurrent parallel-session `rm -rf dist` (OG-image chunk ENOENT), not on this article. `languages.en.status: planned → drafting`. | Claude Opus 4.7 + ryoooue |
| 2026-05-25 | **JA v1 shipped (Option B audience pivot).** `src/data/guides/ja/business-japanese.mdx` (~10,500 chars) implements `business-japanese.ja.spec.md` §7 1:1 as the **HR/育成-facing hub** ("外国人社員のビジネス日本語 育成ガイド"): who-it's-for (人事・現場リーダー), what-is + 6-area stumbling map, teaching method ("見せて・言わせて・直す" + 直接法), A/B/C as a tool for diagnosing a report's register, "first 20 to teach" starter kit, etiquette teaching, email coaching, corporate support (現状把握→学習支援→研修), material selection, BJT, 90-day onboarding/development roadmap, FAQ (5, also frontmatter), related-articles hub + Essential 30 CTA. NOT a translation of EN — pivoted reader per §10. `ja-article-style` linter idempotent pass (0 changes). Full `pnpm build` green: astro check 0 errors, both `/en/` and `/ja/guides/business-japanese/` built, OG images generated, Pagefind 42 pages / 12,103 words. `languages.ja.status: planned → drafting`. | Claude Opus 4.7 + ryoooue |
| 2026-05-25 | Title space fix: 「ビジネス日本語 育成ガイド」→「ビジネス日本語育成ガイド」 (stray CJK-CJK space, missed by linter); same fix on the 90-day roadmap heading (「入社90日 受け入れ…」→「入社90日の受け入れ…」). | Claude Opus 4.7 + ryoooue |
| 2026-05-25 | **Publish flip (both languages).** User approved EN v1 and JA v1. `status: drafting → published`; `languages.{en,ja}.status: drafting → published`. Added to ROADMAP Live articles table. Both mdx already `draft: false`; goes live on next git push → Cloudflare Pages auto-build. | Claude Opus 4.7 + ryoooue |
| 2026-05-25 | Ran `seo-article-localize` for `ja`: **diff_needed = TRUE** (base coverage ≈10%, 5 language-unique additions, >50% divergence). JA SERP for 「ビジネス日本語」 is dominated by employer/HR/trainer content (teaching methods, corporate training, material selection, BJT). Diff spec `specs/articles/business-japanese.ja.spec.md` generated with **Option B audience pivot** (JA = Japanese HR/team-lead "外国人社員のビジネス日本語 育成ハブ"). EN-only flagged as a live alternative for this master-hub pillar — pending user call. | Claude Opus 4.7 + ryoooue |
| 2026-05-25 | **Consolidated duplicate mega-pillar.** A parallel session produced `business-japanese-complete.spec.md` targeting the same head term "business japanese" (cluster `foundations`). Per user decision (avoid keyword cannibalization on a single head term), kept THIS `business-japanese` slug as the canonical hub (exact head-term match) and retired the duplicate. Folded the duplicate's unique angles into §5/§7: cross-cluster 80/20 starter kit, Day 1 / Week 1 / Month 1 / Quarter 1 roadmap labels, and a spoken/written reading-path overlay. Cluster changed `business-japanese` → `foundations` (registered in `src/config/clusters.ts`, added 2026-05-25). | Claude Opus 4.7 + ryoooue |
