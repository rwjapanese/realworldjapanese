---
# === IDENTIFICATION ===
base_spec: "specs/articles/<slug>.spec.md"   # Path to the base spec this diff extends
slug: "<article-slug>"                       # Same slug as base spec
target_language: "<lang-code>"               # ISO code: vi, ko, zh, th, id, etc.

# === DECISION ===
# Output of localization analysis. Set by the skill.
diff_needed: true                            # true if a diff spec is warranted, false if base spec is sufficient
diff_reason: "<one-line justification>"      # e.g. "VI SERP dominated by grammar-heavy academic sources; 40% divergence"

# === SERP ===
serp_language: "<lang-code>"                 # Usually same as target_language
serp_locale: "<locale>"                      # e.g. "vi-VN", "ko-KR"
last_serp_audit: "YYYY-MM-DD"

# === LIFECYCLE ===
status: "drafting"                           # drafting | ready | published | archived
created: "YYYY-MM-DD"
---

# Language Diff Spec: <slug> — <target_language>

> **How to use this file**
> - The `seo-article-localize` skill generates this when the target-language SERP diverges materially from the base spec.
> - If `diff_needed: false`, this file may not be generated at all — the translator works directly from the base spec.
> - Do NOT duplicate content from the base spec. Only record DELTAS.

---

## 1. Decision Summary

- **Base outline coverage in target SERP:** _X/10 of base spec headings appear in target-language top 10_
- **Language-unique headings:** _Y new headings not in base spec that appear ≥3 times in target top 10_
- **Verdict:** _Why the skill decided diff is/isn't needed. Quantitative when possible._

---

## 2. Target-Language SERP (Top 10)

> Captured on: YYYY-MM-DD. Search engine: Google. Locale: <serp_locale>.

| # | URL | Domain | Title (original) | Title (EN gloss) | Notes |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |
| 7 | | | | | |
| 8 | | | | | |
| 9 | | | | | |
| 10 | | | | | |

### Target-language SERP features
- [ ] Featured snippet
- [ ] People Also Ask (local-language)
- [ ] Video carousel
- [ ] Image pack

### Target-language PAA / related searches
- ...

---

## 3. Coverage of Base Spec Outline

> Check each heading from the base spec's section 7 against the target-language top 10.

| Base spec heading | Coverage in target SERP (x/10) | Action |
|---|---|---|
| | | keep / demote / drop |

Legend:
- **keep**: Retain as-is in localized article
- **demote**: Keep but shorten (less relevant to local audience)
- **drop**: Omit in localized version (not relevant / misleading in local context)

---

## 4. Language-Specific Additions

> Headings that appear ≥3 times in target top 10 but are NOT in the base spec. These should be added to the localized article.

| New heading | Coverage (x/10) | Why local-relevant |
|---|---|---|
| | | |

---

## 5. Localization Considerations (non-SERP)

> Cultural / linguistic adaptations that go beyond heading structure.

### Terminology
- _e.g. "keigo" → "kính ngữ" (VI), with romaji retained on first mention_

### Examples to rewrite
- _Base-spec example scenarios that don't land in target culture; propose replacements_

### Register / tone
- _Does the target language have strong register conventions that need explicit calibration?_

### Local expert references
- _Local authorities / institutions to cite for credibility_

---

## 6. Language-Specific primary_info_seeds

> If there is local primary information worth collecting for THIS language version specifically (beyond base spec's seeds).
> Leave empty if none.

1. _e.g. "Survey of 20 Vietnamese learners on which keigo situation they find hardest"_
2.
3.

---

## 7. Final Localized Outline

> The outline actually used to write the target-language article.
> Can be a full rewrite or a pointer to base spec's section 7 with only the additions.

- Option A: Reference base spec with deltas
  - Base: see `../<slug>.spec.md` section 7
  - Additions: insert after section N — <new heading>
  - Removals: omit section M

- Option B: Full rewrite (use when divergence is large)
  1. H1: ...
  2. H2: ...
  ...

---

## 8. Change Log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial diff spec generated via `seo-article-localize` skill | |
