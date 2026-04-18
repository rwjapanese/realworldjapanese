---
# === IDENTIFICATION ===
slug: "<article-slug>"                    # URL slug (e.g. "keigo-guide")
collection: "guides"                      # blog | guides | products
cluster: "<cluster-id>"                   # e.g. "keigo", "business-email"
pillar: null                              # Parent pillar slug if this is a child article; null if this IS the pillar

# === SEO ===
target_keyword: "<primary keyword>"       # e.g. "keigo guide"
serp_language: "en"                       # Language of SERP used for this spec (usually "en" for MVP)
target_intent: "informational"            # informational | transactional | navigational | commercial
search_volume_estimate: null              # Monthly search volume if known
difficulty_estimate: null                 # low | medium | high

# === FUNNEL ===
funnel_stage: "TOFU"                      # TOFU | MOFU | BOFU
product_cta: null                         # Product slug to CTA at the end (e.g. "essential-30")
lead_magnet: null                         # Lead magnet slug if applicable

# === LANGUAGES ===
# Track publication status per language.
# Status: "planned" | "drafting" | "published" | "needs_update"
languages:
  en:
    status: "planned"
    url_slug: null                        # Optional override; defaults to `slug`
    diff_spec: null                       # Path to language-diff spec if any
  ja:
    status: "planned"
    url_slug: null
    diff_spec: null

# === LIFECYCLE ===
status: "drafting"                        # drafting | ready | published | archived
created: "YYYY-MM-DD"
last_serp_audit: "YYYY-MM-DD"             # Last time we re-ran SERP analysis
---

# articleSpec: <Article Title>

> **How to use this file**
> - The `seo-article-outline` skill generates the initial version.
> - Humans review and refine the "Our Differentiation" and "primary_info_seeds" sections.
> - When SERP changes significantly, re-run the skill to refresh sections 2–4.
> - Do NOT delete the spec after publication — it's the source of truth for updates.

---

## 1. Target & Intent

**Primary search intent:** _What is the user actually trying to accomplish when they search "<keyword>"?_

**Audience persona:** _One-sentence description of who types this query._

**Success criteria:** _What question(s) must this article answer for the reader to feel the job is done?_

---

## 2. SERP Analysis (Top 10)

> Captured on: YYYY-MM-DD. Search engine: Google. Locale: en-US (or as specified).
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
- [ ] Featured snippet
- [ ] People Also Ask (PAA)
- [ ] Video carousel
- [ ] Image pack
- [ ] Knowledge panel
- [ ] Related searches (list below)

### Related searches / PAA questions
- ...
- ...

---

## 3. Merged Outline (from Top 10)

> All distinct headings found across the top 10, with coverage count.
> Coverage = how many of top 10 articles have a section matching this heading.

| Heading | Coverage (x/10) | Notes |
|---|---|---|
| ... | 8/10 | Table stakes; must include |
| ... | 5/10 | Common; strong signal |
| ... | 2/10 | Rare; optional |

---

## 4. Content Gaps

> What top-10 articles collectively fail to cover, but the searcher likely wants.

1. ...
2. ...
3. ...

---

## 5. Our Differentiation

> Our unique angle. What makes this article rank above the top 10, not just match them?

- ...
- ...

---

## 6. primary_info_seeds

> Hypotheses for primary information (original data, first-hand experience, expert quotes) to layer on top of the article over time. Fill with **3 hypotheses** per article.
> Each seed should be something that (a) no top-10 article has, (b) we could realistically collect within ~1 week, (c) measurably improves E-E-A-T.

1. **<Seed title>**
   - _What:_ What data/experience/quote to collect
   - _How:_ Collection method (survey, interview, internal analytics, personal experience log, expert outreach)
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

> The final outline for OUR article. Derived from sections 3–5.

1. H1: _<Working title>_
2. H2: Intro — who should read this
3. H2: <Section 1>
   - H3: <Subsection>
4. H2: <Section 2>
5. ...
6. H2: FAQ
7. H2: CTA / Related articles

---

## 8. FAQ / People Also Ask

> Questions to answer in the article. Map each to a section or a dedicated FAQ block.

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

---

## 10. Localization Notes

> Heads-up for language-diff specs. Flag items that are likely to behave differently in non-English SERPs.

- **Terminology:** _Key terms that may not translate directly (e.g. "keigo" stays romanized in EN, but may vary in VI/KO)._
- **Cultural assumptions:** _Assumptions the EN version makes about the reader's background._
- **Competitor landscape:** _Is the top-10 competitor set likely to be totally different in, say, VI or KO?_
- **Language-specific risks:** _Expressions that don't survive translation and need re-writing._

---

## 11. Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial spec generated via `seo-article-outline` skill | |
