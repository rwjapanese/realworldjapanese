---
# === IDENTIFICATION ===
slug: "<article-slug>"                    # URL slug (e.g. "keigo-guide")
collection: "guides"                      # blog | guides | products
cluster: "<cluster-id>"                   # e.g. "keigo", "business-email"
pillar: null                              # Parent pillar slug if this is a child article; null if this IS the pillar

# === SEO ===
target_keyword: "<primary keyword>"       # e.g. "keigo guide"
serp_language: "en"                       # Language of SERP used for this spec (usually "en" for MVP)
serp_source: "websearch"                  # dataforseo | websearch — how the SERP was captured (Step 2)
target_intent: "informational"            # informational | transactional | navigational | commercial
search_volume_estimate: null              # Monthly search volume if known
difficulty_estimate: null                 # low | medium | high — REQUIRED, set by Step 4 winnability gate
focus_distance: null                      # Cosine distance from site topical centroid (Step 6), or null with reason in §2

# === FUNNEL ===
funnel_stage: "TOFU"                      # TOFU | MOFU | BOFU
product_cta: null                         # Product slug to CTA at the end (e.g. "essential-30")
lead_magnet: null                         # Lead magnet slug if applicable

# === LANGUAGES ===
# Track publication status per language.
# Initialize ONLY the serp_language entry. Other languages are added by
# seo-article-localize AFTER the base article passes its performance gate —
# do not pre-fill every language (that nudges toward translate-everything).
# Status: "planned" | "drafting" | "published" | "needs_update"
languages:
  en:
    status: "planned"
    url_slug: null                        # Optional override; defaults to `slug`
    diff_spec: null                       # Path to language-diff spec if any

# === LIFECYCLE ===
status: "drafting"                        # drafting | ready | published | archived
                                          # drafting → ready requires the novelty gate:
                                          # ≥1 seed integrated + novelty_check.py pass (see skill)
refresh_class: "evergreen"                # evergreen | listicle | event — drives refresh cadence
created: "YYYY-MM-DD"
last_serp_audit: "YYYY-MM-DD"             # Last time we re-ran SERP analysis
---

# articleSpec: <Article Title>

> **How to use this file**
> - The `seo-article-outline` skill generates the initial version.
> - Humans review and refine the "Our Differentiation" and "primary_info_seeds" sections.
> - When SERP changes significantly, re-run the skill (unpublished) or `seo-article-refresh` (published) to refresh sections 2–4.
> - Do NOT delete the spec after publication — it's the source of truth for updates.
>
> **Bilingual convention (2026-04-27 onward)**
> Sections 1, 4, 5, and 7 MUST be written in both **JA and EN**. JA goes first (primary review version for the human author), EN second. Sections 2, 3, 6, 8, 9, 11 stay in EN only — they are mechanical / reference material. (§10 bilingual since 2026-05-18.)

---

## 1. Target & Intent

### JA

**主要な検索意図:** _「<keyword>」を検索したユーザーが本当に達成したいことは何か？_

**読者ペルソナ:** _このクエリを打つ人物の一文記述。_

**成功基準:** _読者が「目的を達成できた」と感じるためには、この記事はどの問いに答える必要があるか？_

**Focus justification（focus_distance > p90 の場合のみ必須）:** _なぜこのトピックがこのサイトに属するのか。_

### EN

**Primary search intent:** _What is the user actually trying to accomplish when they search "<keyword>"?_

**Audience persona:** _One-sentence description of who types this query._

**Success criteria:** _What question(s) must this article answer for the reader to feel the job is done?_

**Focus justification (required only when focus_distance > p90):** _Why this topic belongs on this site._

---

## 2. SERP Analysis (Top 10)

> Captured on: YYYY-MM-DD. Source: dataforseo | websearch. Search engine: Google. Locale: en-US (or as specified).
> If source is websearch: results are approximate — not a true ranked, locale-controlled SERP.
> Coverage denominators in this spec are always `/10` (out of top 10 competitors).
> Word Count may be approximate (`~3000`); use "short <1500 / medium 1500-3000 / long >3000" if exact count unavailable.

| # | URL | Domain | Title | Format | Word Count | Notes |
|---|---|---|---|---|---|---|
| 1 | | | | guide / list / video / forum | ~ | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |
| 9 | | | | | | |
| 10 | | | | | | |

### SERP features present
- [ ] AI Overview — **cited domains:** _list observed citations; AIO presence cuts expected CTR by roughly one-third to one-half even at #1_
- [ ] Featured snippet
- [ ] People Also Ask (PAA)
- [ ] Video carousel
- [ ] Image pack
- [ ] Knowledge panel
- [ ] Related searches (list below)

### Winnability (Step 4 gate)
- **Strong domains:** _N/10 — list them_
- **Weak slots:** _Reddit/forums/UGC/thin pages observed_
- **Verdict:** `difficulty_estimate: low | medium | high` — _one-line reasoning. high (≥7 strong) requires explicit user go-ahead, logged in §11._

### Cannibalization (Step 5 gate)
- **Max overlap with existing specs:** _<slug>: N shared top-10 URLs_ (≥4 → halt; 2–3 → note divergence plan; ≤1 → clean)

### Related searches / PAA questions
- ...
- ...

---

## 3. Merged Outline (from Top 10)

> All distinct headings found across the top 10, with coverage count.
> Coverage = how many of top 10 articles have a section matching this heading.
> Competitor body text is cached under `specs/serp-cache/<slug>/` for the novelty gate and refresh diffs.

| Heading | Coverage (x/10) | Notes |
|---|---|---|
| ... | 8/10 | Table stakes; must include |
| ... | 5/10 | Common; strong signal |
| ... | 2/10 | Rare; optional |

---

## 4. Content Gaps

> What top-10 articles collectively fail to cover, but the searcher likely wants.
> Check cached body text, not just headings — competitors sometimes cover a topic without a dedicated heading.

### JA

1. ...
2. ...
3. ...

### EN

1. ...
2. ...
3. ...

---

## 5. Our Differentiation

> Our unique angle. What makes this article rank above the top 10, not just match them?

### JA

- ...
- ...

### EN

- ...
- ...

---

## 6. primary_info_seeds

> Hypotheses for primary information (original data, first-hand experience, expert quotes) to layer on top of the article over time. Fill with **3 hypotheses** per article.
> Each seed should be something that (a) no top-10 article has, (b) we could realistically collect within ~1 week, (c) measurably improves E-E-A-T.
> Prefer ≥1 corpus-derived seed (original statistics from Tatoeba/JMdict/subtitle corpora — cheap, verifiable, and original stats are the strongest-evidenced lever for AI-answer citations).
>
> **⚠️ GATE:** `status: drafting → ready` requires ≥1 seed at `integrated` (artifact literally present in the draft) AND a passing `novelty_check.py` run (`specs/articles/<slug>.novelty.json`). A spec whose seeds stay `not_started` produces a summary-of-summaries — the profile core updates demote.

1. **<Seed title>**
   - _What:_ What data/experience/quote to collect
   - _How:_ Collection method (survey, interview, internal analytics, personal experience log, expert outreach, corpus analysis)
   - _Cost:_ Estimated time to collect
   - _Status:_ `not_started` | `collecting` | `integrated`

2. **<Seed title>**
   - _What:_
   - _How:_
   - _Cost:_
   - _Status:_ `not_started`

3. **<Seed title>**
   - _What:_
   - _How:_
   - _Cost:_
   - _Status:_ `not_started`

---

## 7. Target Article Outline

> The final outline for OUR article. Derived from sections 3–5 and the fan-out map (§8).
> **Answer-capsule rule:** every H2 chosen from the fan-out map must open with a 40–60 word direct answer paragraph (generalization of the featured-snippet rule — this is what wins snippet + AI Overview citations from outside the top 10). Mark those H2s with `[capsule]`.

### JA outline (target)

1. H1: _<日本語タイトル案>_
2. H2: この記事を読むべき人
3. H2: <セクション1> `[capsule]`
   - H3: <サブセクション>
4. H2: <セクション2>
5. ...
6. H2: よくある質問
7. H2: CTA / 関連記事

### EN outline (target)

1. H1: _<Working title>_
2. H2: Intro — who should read this
3. H2: <Section 1> `[capsule]`
   - H3: <Subsection>
4. H2: <Section 2>
5. ...
6. H2: FAQ
7. H2: CTA / Related articles

---

## 8. FAQ / PAA / Query fan-out map

> AI Overviews / AI Mode expand the query into fan-out sub-queries; self-contained sections win citations from SERPs the page never ranks on (~38% of AIO citations come from outside the organic top 10).
> Sub-queries live INSIDE this article as sections — never as separate spinout pages (scaled-content-abuse pattern).

| Sub-query | Source | SERP status | Covered by | Capsule? |
|---|---|---|---|---|
| _question or sub-intent_ | PAA / related / suggest / LLM | covered / weak / uncovered | H2 §N or FAQ item | yes/no |
| | | | | |

### FAQ block (maps to the article's FAQ section)

| Question | Where answered |
|---|---|
| | |
| | |

---

## 9. Internal Links

### Upstream (pillars / hubs linking to this article)
- ...

### Downstream (articles this article links to)
- ...

### Sibling cluster articles
- ...

### Inbound edits — REQUIRED (≥2 when ≥2 published articles exist)

> Execution list, not a wish list: these edits are applied to EXISTING articles when this article publishes, so it never ships as an orphan ("Discovered - currently not indexed" is fixed by internal inbound links + value).

| # | Source file | Insertion sentence (with anchor marked) | Anchor text |
|---|---|---|---|
| 1 | | | |
| 2 | | | |

---

## 10. Localization Notes

> Heads-up for language-diff specs. Flag items that are likely to behave differently in non-English SERPs.

### JA

- **用語:** _英語版でローマ字保持する語の挙動 / 直訳が崩れる語 (例: "keigo" は EN でローマ字、VI/KO では別表記の可能性)。_
- **表記変種:** _JA SERPで漢字/カタカナ/ひらがな/ローマ字のどれが主流か（検索量とインテントが表記で割れる）。_
- **文化的前提:** _EN 版が読者背景について暗黙に置いている前提。_
- **競合ランドスケープ:** _VI / KO など他言語 SERP で top-10 競合セットが全く別物になる可能性。KO は Naver が検索の約半分〜6割で Google-only 分析は部分的。_
- **言語固有のリスク:** _翻訳で意味が落ちる表現、書き直しが必要なフレーズ。_
- **ペルソナ pivot の必要性:** _EN 版と JA 版でターゲット読者が乖離するケース (例: EN は外国人学習者、JA SERP は日本人ビジネスパーソン → audience pivot 要否)。_

### EN

- **Terminology:** _Key terms that may not translate directly (e.g. "keigo" stays romanized in EN, but may vary in VI/KO)._
- **Script variants:** _Which JA script variant (kanji/katakana/hiragana/romaji) dominates the SERP — volume and intent split by script._
- **Cultural assumptions:** _Assumptions the EN version makes about the reader's background._
- **Competitor landscape:** _Is the top-10 competitor set likely to be totally different in, say, VI or KO? For KO, Naver holds roughly half to 60% of search — Google-only analysis is partial._
- **Language-specific risks:** _Expressions that don't survive translation and need re-writing._
- **Persona pivot signal:** _Cases where the EN and JA readers diverge (e.g. EN = foreign learners, JA SERP = Japanese business adults → audience pivot decision needed)._

---

## 11. Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial spec generated via `seo-article-outline` skill | |
