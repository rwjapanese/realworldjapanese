---
# === IDENTIFICATION ===
base_spec: "specs/articles/japanese-workplace-mistakes-foreigners.spec.md"
slug: "japanese-workplace-mistakes-foreigners"
target_language: "ja"

# === DECISION ===
diff_needed: true
diff_reason: "JA SERP は ~8/10 が日本人 HR・マネージャー向け『外国人材のトラブル事例と対策』で、base spec の foreigner-first-person 視点と読者が真逆（ハード persona pivot）。base coverage ≈ 0–9%。さらに二重カニバリ：foreigner 向け JA は #17.ja を、HR 向け JA は business-japanese.ja を重複 → 現時点で clean な JA standalone 価値なし。**実行判断 = JA DEFER（EN-only 継続）。**"

# === SERP ===
serp_language: "ja"
serp_locale: "ja-JP"
last_serp_audit: "2026-06-03"

# === LIFECYCLE ===
status: "drafting"
created: "2026-06-03"
---

# Language Diff Spec: japanese-workplace-mistakes-foreigners — ja

> **How to use this file**
> - Generated because the JA SERP diverges materially from the base spec.
> - **This diff records a DECISION, not a localized outline.** The verdict is **DEFER JA / keep EN-only**. No JA article is written from this spec.
> - §7 documents the *conditional future path* if JA is ever revived — it would be a separate-slug Japanese-HR article, NOT a translation of the base spec.

---

## 1. Decision Summary

- **Base outline coverage in target SERP:** ≈ **0–1 / 11** base spec §7 headings appear (and only in a mismatched frame). The base spec's owned territory — the gaijin-pass line, the 5 foreigner-lens *meta*-mistakes, the multi-year career-trajectory arc, the job-hunt stage — has **0/10** coverage in the JA SERP. Daily-office topics (time sense, *hō-ren-sō*, indirect communication) do appear (6+/10) but framed as the **employer's** problem to manage, not the foreigner's to self-correct.
- **Language-unique headings:** Many (≥6) — JA SERP wants トラブル事例, 法的リスク (著作権・備品), 失踪・音信不通対応, 契約・解雇トラブル, 多言語マニュアル, 報連相の教え方. All belong to a Japanese-HR audience.
- **base_coverage_pct ≈ 0–9%**, **unique_additions_count > 2**, **divergence > 50%**, **hard persona pivot** → decision rule fires **diff_needed = true**.
- **Verdict (actionable): DEFER JA, keep EN-only.** The diff rule says "a JA version needs a full rewrite," but the *strategic* finding is stronger: **there is no clean JA niche for this article right now.** Both candidate JA audiences are already occupied (see below). Writing JA in either direction would cannibalize an existing published article without adding standalone value.

### The three-way fork (escalated per base §10) — resolved

| Option | Verdict | Why |
|---|---|---|
| **(a) JA-not-published / EN-only** | ✅ **RECOMMENDED** | The base spec's unique value (gaijin-pass frame, foreigner-lens *meta*-mistakes, self-managed career arc) is EN-native. The "gaijin pass" frame relies on the EN reader's self-irony and turns patronizing when told to a Japanese-HR reader. EN already shipped and stands alone vs #17. |
| **(b) Merge career-arc + gaijin-pass INTO `common-japanese-business-mistakes.ja` (#17.ja)** | ❌ **REJECTED** | #17.ja is foreigner-first-person and tightly scoped to the first 90 days ("入社90日で避けたい優先順位ガイド"). Bolting on a multi-year career arc + a gaijin-pass section would blur its onboarding focus, and the gaijin-pass frame doesn't survive into JA. (A *light* future touch — 1 FAQ line on 「外国人だから許される範囲」 — is fine, but that's not a merge of this article.) |
| **(c) Pivot to a Japanese-HR slug (e.g. `gaikokujin-shain-mistakes-shidou`)** | ⏸ **DEFERRED (conditional)** | This is what the JA SERP actually wants, and it's a real, high-CV audience. BUT it overlaps `business-japanese.ja` (the published 外国人社員 育成ハブ: 受け入れ・指導・つまずきマップ・90日ロードマップ). If revived, it must be a **fresh `seo-article-outline` run** against the HR-trouble SERP and positioned as a **child of `business-japanese.ja`** — not a translation of this spec. Hold until the JA hub strategy matures (same posture as deferred `japanese-business-phrases.ja` #19). |

---

## 2. Target-Language SERP (Top 10)

> Captured on: 2026-06-03. Search engine: Google. Locale: ja-JP. Queries: 「外国人 日本 職場 やりがちな ミス 失敗 仕事」 + 「外国人 社員 日本企業 ありがちな失敗 文化の違い 注意点」.

| # | URL | Domain | Title (original) | Title (EN gloss) | Notes |
|---|---|---|---|---|---|
| 1 | https://global-saponet.mgl.mynavi.jp/know-how/1830 | マイナビグローバル | 【事例6選】外国人労働者が起こしやすいトラブルとは？企業が事前に知っておきたい対策方法も解説 | 6 trouble cases foreign workers cause + employer countermeasures | **HR/employer.** 著作権違反・備品・失踪・従業員間・契約・解雇。Pure management-risk frame. |
| 2 | https://izanau.com/ | izanau | 外国人採用後にトラブルや問題に発展してしまう会社の7つの… | 7 traits of companies that hit trouble after hiring foreigners | **HR/employer.** Recruiting-platform content. |
| 3 | https://global-saponet.mgl.mynavi.jp/know-how/5263 | マイナビグローバル | 【外国人材相談事例#2】お願いした仕事の「仕上がりがおかしい」問題の処方箋 | Case: the deliverable came back wrong — a prescription | **HR/manager.** Manager's how-to. |
| 4 | https://www.mhlw.go.jp/content/11650000/001213435.pdf | 厚生労働省 (MHLW) | （就業規則・安全規程が理解してもらえない 等） | Gov PDF: rules not understood, communication breakdown | **Gov/employer.** Employment-rules guidance for companies. |
| 5 | https://service.alue.co.jp/blog/examples-of-cross-cultural-communication-failures | アルー株式会社 | 海外駐在社員によくある異文化コミュニケーションの失敗例と解決策 | Cross-cultural comm failures of overseas-posted staff | **Corporate training.** Adjacent (駐在 = JP staff abroad), employer-training frame. |
| 6 | https://www.chocobio.click/外国人と働けない日本人… | chocobio | 外国人と働けない日本人＆日本を勘違いしている外国人 | Japanese who can't work with foreigners & foreigners who misread Japan | Opinion blog; mixed audience. |
| 7 | https://www.global.staff-manzoku.co.jp/blog/foreign-worker-troubles | スタッフ満足 | 外国人労働者に多いトラブルとは？件数と原因・解決法を解説 | Common foreign-worker troubles: counts, causes, fixes | **HR/employer.** |
| 8 | https://michi.sociarise.co.jp/recruiting-tips/low-performance-check/ | MICHI | 外国人社員のパフォーマンスが低いと感じたら確認すべきこと | What to check when a foreign employee underperforms | **HR/manager.** |
| 9 | https://www.gtalent.jp/blog/japanwork/work-abroad/Japan-office-differences | GTalent | 日本のオフィス環境・職場文化の独特な違いとは？IT・機電エンジニア向け完全ガイド | Japan office/culture differences — for IT/mechanical engineers | **Foreigner (engineer).** The lone foreigner-facing ranker — and its niche is already owned by `japanese-for-it-professionals`. |
| 10 | https://www.myanmarunity.jp/problem/18212/ | ミャンマー・ユニティ | 採用担当が知っておくべき外国人雇用の"落とし穴" 文化のギャップで起こる5大トラブルと回避策 | 5 culture-gap troubles recruiters should know | **HR/recruiter** (fetch timed out; title is decisive). Also: ヨロワーク / RISE / willof / gaikokusaiyo all rank on query 2, all HR/manager. |

### Target-language SERP features
- [x] People Also Ask (local-language) — clusters on 文化の違い / トラブル対策 / マネジメント, all employer-side
- [ ] Featured snippet
- [ ] Video carousel
- [ ] Image pack

### Target-language PAA / related searches
- 外国人労働者 トラブル 事例
- 外国人 マネジメント コツ / 失敗例
- 外国人社員 報連相 教え方
- 外国人 雇用 注意点 採用担当
- 文化の違い 職場 対策

---

## 3. Coverage of Base Spec Outline

> Each base §7 (JA outline) heading vs the JA top 10. Frame mismatch noted where a topic appears but for the wrong audience.

| Base spec heading | Coverage in target SERP (x/10) | Action |
|---|---|---|
| 外国人のミスは「個別マナー」より「姿勢」で起きる（地図） | 0/10 | drop |
| gaijin pass の真実（許される/許されない/trust window） | 0/10 | drop |
| 外国人特有の5つの *meta*-mistake（言語力≠能力 / 差別か文化か / 過剰同化 / 完璧主義 / 言い訳） | 0/10 | drop |
| 日常オフィスのミス（空気・時間・報連相・服装） | 6/10 **but wrong frame** (employer-manages, not foreigner-self-corrects) | drop (covered by #17.ja for foreigners; HR frame ≠ base content) |
| キャリア軌道の落とし穴（昇進志向 / 実績記録 / 契約・権利 / 滞留） | 0/10 (契約 appears as employer's duty, not foreigner self-advocacy) | drop |
| 就活・入社前段階のミス | 0/10 | drop |
| やってしまった時のリカバリーの考え方 | 0/10 | drop |
| FAQ（gaijin pass / 完璧な日本語 / 差別か文化か / 日本人らしく / 一度の失敗） | 0/10 | drop |

**Result:** essentially every base heading is `drop` for the JA SERP. There is no Option-A (base + deltas) path — the JA SERP wants a different article for a different reader.

---

## 4. Language-Specific Additions

> What a JA article on this keyword *would* need (Japanese-HR audience). Listed to show the gap, NOT to author now — these belong to option (c)'s future fresh outline and overlap `business-japanese.ja`.

| New heading | Coverage (x/10) | Why local-relevant |
|---|---|---|
| 外国人材のトラブル事例（著作権・備品・失踪・契約・解雇） | ~5/10 | JA SERP's dominant format; legal/HR risk |
| 文化ギャップ別の対策（時間・報連相・締切・家庭優先） | ~6/10 | Employer-side mitigation framing |
| 報連相・社内ルールの「教え方」 | ~4/10 | Manager onboarding duty |
| 多言語マニュアル / 日本語レベルに合わせた指示 | ~3/10 | Practical HR tooling |
| 定着・パフォーマンス改善 | ~3/10 | Retention/management |

**Every one of these overlaps `business-japanese.ja` (外国人社員 育成ハブ).** This is precisely why option (c) is deferred, not actioned.

---

## 5. Localization Considerations (non-SERP)

### Terminology
- "gaijin pass" — **does not localize.** No JA equivalent frame; telling a Japanese-HR reader "外国人は大目に見てもらえる" inverts the tone into something patronizing/odd. This single term failing to carry is a microcosm of why the whole article is EN-native.
- *hō-ren-sō* (報・連・相), 空気を読む, ウチ／ソト — already standard JA; would need no gloss (the reverse of EN), which itself signals the audience is native-JA, i.e. not this article's reader.

### Examples to rewrite
- All recovery/self-advocacy examples ("voice your ambition in 1-on-1s," "check your contract rights") are written *to the foreigner*. For the JA SERP's HR reader they'd flip to "how to draw out a foreign report's ambitions" / "how to explain the contract" — a different article.

### Register / tone
- EN = empathetic peer-to-peer ("you, the foreigner"). JA SERP = professional HR/managerial. Incompatible registers; not a tone tweak but an audience change.

### Local expert references
- A future JA-HR article (option c) would cite MHLW (厚労省) employment guidance, 出入国在留管理庁, and recruiting-industry sources (マイナビグローバル etc.) — none of which fit the EN foreigner-lens piece.

---

## 6. Language-Specific primary_info_seeds

_None to action now (JA deferred)._ If option (c) is ever revived, the relevant seed would be a **Japanese-manager interview on "the foreign-hire mistakes that actually cause trouble, and how they coached the recovery"** — but that overlaps base seed #1 (the two-sided gaijin-pass survey) and `business-japanese.ja`'s manager interviews. Do not collect separately until (c) is greenlit.

---

## 7. Final Localized Outline

**No localized outline produced — JA is deferred (see §1 verdict).**

- Option A (base + deltas): **not viable** — §3 shows ~all base headings `drop`.
- Option B (full rewrite): **not authored now** — would require pivoting to a Japanese-HR audience (option c), which overlaps `business-japanese.ja` and needs its own `seo-article-outline` run against the HR-trouble SERP, under a separate slug. Hold until JA hub strategy matures.

**If revived later, start fresh — do not translate this spec.**

---

## 8. Change Log

| Date | Change | Author |
|---|---|---|
| 2026-06-03 | Initial diff spec generated via `seo-article-localize` skill. JA SERP captured (2 queries): ~8/10 Japanese-HR/manager "foreign-worker trouble cases & countermeasures" (マイナビグローバル ×2 / izanau / MHLW / アルー / スタッフ満足 / MICHI / ミャンマーユニティ / ヨロワーク / RISE / willof / gaikokusaiyo); lone foreigner-facing ranker (GTalent) is engineer-specific and already owned by `japanese-for-it-professionals`. base_coverage_pct ≈ 0–9%, hard persona pivot, divergence >50% → diff_needed=true. **Three-way fork resolved: (a) DEFER JA / EN-only = RECOMMENDED; (b) merge into #17.ja = REJECTED (audience + scope mismatch, gaijin-pass frame doesn't carry); (c) Japanese-HR separate slug = DEFERRED (overlaps `business-japanese.ja`; needs fresh outline if revived).** No JA article authored. Base spec `languages.ja.diff_spec` linked; `languages.ja.status` stays `planned` (deferred). | seo-article-localize (Claude Opus 4.8) + ryoooue |
