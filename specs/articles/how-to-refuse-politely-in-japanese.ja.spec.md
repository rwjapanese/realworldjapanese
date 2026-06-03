---
# === IDENTIFICATION ===
base_spec: "specs/articles/how-to-refuse-politely-in-japanese.spec.md"
slug: "how-to-refuse-politely-in-japanese"
target_language: "ja"

# === DECISION ===
diff_needed: true
diff_reason: "JA SERP は『お断りメール 例文 / 角を立てない断り方』を探す日本人ビジネスパーソン向けで占有され、外国人学習者向けは 0/10。base outline の文化セットアップ・A/B/C ローマ字・soft-no 逆引き・外国人ミスは <5/10、JA 固有追加（クッション言葉集・営業お断りメール特化・NG例文・電話・フォローアップ）≥5 → ハードなペルソナ pivot、>50% 乖離 → Option B 全面書き換え。"

# === SERP ===
serp_language: "ja"
serp_locale: "ja-JP"
last_serp_audit: "2026-06-03"

# === LIFECYCLE ===
status: "published"
created: "2026-06-03"
---

# Language Diff Spec: how-to-refuse-politely-in-japanese — ja

> **How to use this file**
> - The `seo-article-localize` skill generates this when the target-language SERP diverges materially from the base spec.
> - If `diff_needed: false`, this file may not be generated at all — the translator works directly from the base spec.
> - Do NOT duplicate content from the base spec. Only record DELTAS.

---

## 1. Decision Summary

- **Base outline coverage in target SERP:** ~3/12 of base spec §7 headings appear at ≥5/10 in the JA top 10 (the five-part anatomy, the email templates, and the scenario/recipient example-table *format*). Everything else — foreigner personas, the "why Japanese rarely says no" cultural setup, the romaji A/B/C tiers, the directness rubric, the soft-no reverse-lookup, the foreigner-specific mistakes — is ≤1/10. **base_coverage_pct ≈ 0.25.**
- **Language-unique headings:** **5–6** — クッション言葉（ビジネス枕詞）集 (6/10), 営業お断りメール特化の状況別例文 (5/10), NG例文セクション (5/10), 電話での断り (3/10), 断り後のフォローアップ (3/10), 方便・ぼかし表現＝理由の伝え方 (3/10).
- **Verdict:** **diff_needed = TRUE.** Hard persona pivot. The JA query space (「断り方 ビジネス」「お断りメール 例文」「角を立てない 断り方」) is owned by **native Japanese business readers declining a sales pitch / request / invitation themselves**, served by business-manner publishers (All About, 幻冬舎ゴールドオンライン) and email-SaaS vendor blogs (Mazrica / Blastmail / Cybozu / Emberpoint / Sales Marker / Indeed Japan). 0/10 target foreigners learning Japanese. Divergence >50% → **Option B (full rewrite)**, same call as `how-to-say-sorry-in-japanese-politely` §10 prediction and the `japanese-honorifics-chart` / `business-japanese` JA pivots. **⚠ Strategic fork in §5 — this pivots the audience away from the site's foreigner-learner core; needs a human go/no-go.**

---

## 2. Target-Language SERP (Top 10)

> Captured on: 2026-06-03. Search engine: Google. Locale: ja-JP.
> Two queries merged: 「ビジネス 角を立てない 丁寧な断り方 例文」 + 「お断りメール 例文 ビジネス 書き方」. 7/10 outlines fetched substantively.

| # | URL | Domain | Title (original) | Title (EN gloss) | Notes |
|---|---|---|---|---|---|
| 1 | https://allabout.co.jp/gm/gc/374362/ | allabout.co.jp | ビジネスでの上手な断り方！当たり障りのない丁寧な断り方【例文付】 | Polite, inoffensive ways to decline in business (with examples) | Business-manner publisher. 断りの基本公式（残念+理由+代案）, 決まり文句6, 方便・ぼかし表現, 「もう誘われたくない」強度別, repeat-decliner techniques. Native self-help, not learner. |
| 2 | https://mazrica.com/.../sales-decline-mail/ | mazrica.com | 【例文付き】営業お断りメールの書き方｜関係を壊さない断りの作法 | How to write a sales-decline email (with examples) | SaaS (SFA/CRM) vendor. 3基本ポイント（迅速簡潔/感謝敬意/理由明確）, 状況別4例文（基本/予算/他社利用/将来可能性）, **NG例3（返信しない/曖昧で期待/感情的）**. Strongest sales-email comp. |
| 3 | https://55hitsuji-jiji.com/businessmail-otoriy-tinei-reibun | 55hitsuji-jiji.com | ビジネスメールでのお断り方法｜相手別に使える丁寧な表現＆例文テンプレート | Polite business-email refusals, templates by recipient | 感謝・理由・配慮 3要素, **相手別4類型（取引先/顧客/上司・先輩/同僚・社内）**, 定型フレーズ, NG例文, FAQ. Recipient-hierarchy template bank. |
| 4 | https://blastmail.jp/blog/mail/decline-mail | blastmail.jp | 印象が良い「お断りメール」の書き方と例文を紹介！ | How to write a good-impression decline email | Email-delivery SaaS. クッション言葉活用, 次につながる一言, **状況別7例文**（要望/イベント誘い/採用/見積/スポンサー/寄付/連携）, NG表現, BCC個人情報注意, フォローアップ(CRM). |
| 5 | https://scene-live.com/.../6971/ | scene-live.com | ビジネス電話の角が立たない断り方は？基本マナーを徹底解説 | Inoffensive ways to decline on a business call | Phone-service vendor. **電話特有**: 5技法（クッション/はっきり断る/用件把握/理由説明/代替案）, 営業電話の見分け, 電話例文（新規取引お断り）. The phone facet. |
| 6 | https://jp.indeed.com/career-advice/.../how-to-politely-decline-by-business-email | jp.indeed.com | 言葉1つで印象が変わる！ビジネスメールで上手に断るフレーズ集 | Phrases to decline well in business email | Job board career-advice. 3段構成（前置き/断り/フォロー）, **フレーズ集**（前置き5/断り3/フォロー2）+ 組合せ例3. Phrase-bank format. |
| 7 | https://emberpoint.com/blog/column/240613-006.html | emberpoint.com | ビジネスシーンで好印象なお断りメールの書き方【例文・フレーズ付き】 | Good-impression decline emails (examples + phrases) | Marketing SaaS. 3ポイント, 基本構成, 注意点, 鉄板フレーズ, 例文, NG表現, フォローアップ. (search-summary level) |
| 8 | https://gentosha-go.com/articles/-/28426 | gentosha-go.com | これぞ大人の見せ所！「角が立たない頼み方＆断り方」10選 | "Grown-up" inoffensive ways to ask & decline (10) | Publisher (幻冬舎). Vocabulary-of-deference focus (ご教授/折り入って/伏して); 断り方 mostly teased to next page. Weaker on decline. |
| 9 | https://mailwise.cybozu.co.jp/column/28.html | cybozu (mailwise) | ビジネスメールでお断りをする際の注意点【メール文例付き】 | Cautions when declining by business email (with samples) | Cybozu mail SaaS. 注意点中心 + 文例. (anchor, not fetched in depth) |
| 10 | https://sales-marker.jp/report/sales-refusal-email/ | sales-marker.jp | 営業お断りメールの例文集｜円滑なビジネス関係を維持する方法 | Sales-decline email example collection | Sales-intelligence SaaS. 営業お断り特化の例文集. (anchor, confirms sales-email is a dense sub-genre) |

### Target-language SERP features
- [ ] Featured snippet (none dominant; opportunity for a 基本公式 snippet)
- [x] People Also Ask (local-language)
- [ ] Video carousel
- [ ] Image pack
- [x] Related searches

### Target-language PAA / related searches
- 角を立てない断り方 ビジネス
- お断りメール 例文 取引先
- 営業 断り方 メール 例文
- 丁寧な断り方 ビジネス 電話
- 「お役に立てず」 断り 言い換え
- 見送らせていただきます 使い方
- 断りメール 返信 しない 失礼
- クッション言葉 一覧 ビジネス

---

## 3. Coverage of Base Spec Outline

> Each base spec §7 (EN outline) heading checked against the JA top 10.

| Base spec heading | Coverage in target SERP (x/10) | Action |
|---|---|---|
| Who this guide is for (4 foreigner personas) | 0/10 | **drop** — JA audience is native business people; rewrite to a native-reader frame |
| 30-second self-diagnostic (foreigner directness routing) | 1/10 | **drop** — reframe lightly as 相手別ルーティング (see §4) |
| Why Japanese rarely says a direct "no" + *uchi-soto* layer | 0/10 | **drop** — natives don't need the cultural setup |
| Three politeness tiers A/B/C (romaji) applied to refusals | 0/10 | **drop** the romaji A/B/C framing; the *recipient-formality* idea survives as 相手別 |
| Directness rubric (4 axes, romaji tiers) | 0/10 | **drop** — replace with 相手別×場面の判断（社外/取引先/上司/社内） |
| A/B/C × scenario matrix (24 romaji cells) | 6/10 (as *format*) | **keep, reframe** — the 状況別/相手別 example-table format is the JA norm; remove all romaji, write native completed 例文 |
| Five-part anatomy (cushion → appreciation → refusal+reason → alternative → close) | 7/10 | **keep** — strongest match; JA universally teaches 感謝→理由→代替案/配慮 + クッション + 次の一言 |
| Four full refusal email templates | 8/10 | **keep & expand** — お断りメール例文 is the dominant JA intent; expand to 相手別×状況別 |
| How to spot a soft "no" (reverse lookup) | 1/10 | **drop / repurpose** — natives know 検討します=no; repurpose as an NG ("曖昧で期待を持たせる表現は避ける") |
| Five refusal mistakes (foreigner-specific) | 5/10 (as NG概念) | **keep, reframe** — drop foreigner framing; rebuild as 日本語ネイティブ向け NG例（返信しない/曖昧/感情的/嘘がバレる/代替なし） |
| FAQ | 4/10 | **keep, re-target** to native PAA |
| Related reading + CTA | n/a (internal) | **keep** — but re-point siblings (business-email cluster heavy) |

---

## 4. Language-Specific Additions

> Headings appearing ≥3 times in JA top 10 but NOT in the base spec.

| New heading | Coverage (x/10) | Why local-relevant |
|---|---|---|
| **クッション言葉（ビジネス枕詞）集** | 6/10 | JA readers harvest a standalone phrase bank (恐れ入りますが／申し訳ございませんが／せっかくですが／ありがたいお話ですが／ご期待に添えず／お役に立てず／身に余るお言葉ですが). Base treats cushion as one anatomy step; JA wants a lookup list. |
| **営業・提案お断りメール特化（状況別）** | 5/10 | A dense JA sub-genre: 基本／予算が合わない／他社を既利用／時期尚早・将来の可能性. Heavily monetized (Mazrica / Blastmail / Sales Marker). |
| **NG例文セクション（やってはいけない断り方）** | 5/10 | 返信しない（無視）／曖昧で期待を持たせる（前向きに検討）／感情的・高圧的／嘘がバレる理由. Taught as a dedicated 反面教師 section, not just inline. |
| **電話での断り方** | 3/10 | 電話特有のマナー：はっきり断る・用件を早く把握・沈黙/間の管理・新規取引お断りの定型. (Scene Live / 電話代行) |
| **断り後のフォローアップ** | 3/10 | 再連絡のタイミング／関係維持（CRM 視点）／「またの機会に」の運用. (Emberpoint / Mazrica) |
| **理由の伝え方＝方便・ぼかし表現の許容範囲** | 3/10 | JA-specific cultural nuance: 「家庭の事情で」「よんどころない事情で」など、嘘にならない範囲でぼかす作法 (All About). A delicate point a learner-frame would never raise. |

---

## 5. Localization Considerations (non-SERP)

### ⚠ Strategic fork (human go/no-go required before drafting)

This is **not a translation — it's an audience switch.** The EN article serves foreigners working in Japan; the JA SERP serves **native Japanese business people declining a sales pitch / request / invitation themselves.** Three live options:

- **Option B — native pivot (this spec's §7 default).** Write 「角を立てない丁寧な断り方・お断りメール例文集」 for native business readers. **Pros:** matches a high-volume, commercially-rich JA keyword (お断りメール例文 is fought over by email-SaaS vendors → real, monetizable demand, unlike the thin foreigner-learner JA queries behind `working-in-japan`); strong standalone growth slot. **Cons:** pivots away from the site's foreigner-learner brand; the JA article would read to a different reader than every other JA article on the site.
- **Option B′ — hybrid (per [[feedback-localize-business-growth-frame]]).** Keep a **foreigner-in-Japan reader** but **align KW + title to the JA "お断りメール 例文 / 断り方" reality**: a JA article that hands a non-native the native completed 例文 + クッション言葉集 + 相手別テンプレ, framed as "現場でそのまま使える断り方". Captures part of the example-bank demand while staying on-brand and internally consistent with the foreigner-focused JA corpus. **Recommended** as the on-brand growth play.
- **Option C — defer / EN-only.** JA stays `planned`, EN runs solo (like `working-in-japan-as-foreigner`). Choose if we don't want a native-audience JA piece and B′ doesn't clear the bar. Lower effort, leaves the JA keyword on the table.

**Recommendation:** **B′ hybrid** — the JA 断り demand is genuine and worth capturing (business-growth frame, not just SEO volume), but a full native pivot (B) fractures the site's audience model. B′ keeps the foreigner reader, adopts the native example-bank + クッション言葉 + 相手別テンプレ structure, and titles to the JA query. Surface to the user before drafting.

### Cannibalization check

- No existing JA article is a **decline-specialized** piece. `business-email-template` (ja) covers 8 email scenarios for foreigners (apology-heavy, no dedicated お断り genre); `japanese-email-phrases` (ja) is a parts-level phrase dictionary; `keigo-*` are register guides. A JA 断り article (B′) fills a fresh slot.
- **Risk to watch:** the クッション言葉集 overlaps `keigo-cheat-sheet` (ja) and `japanese-email-phrases` (ja). Keep this article's cushion list **refusal-scoped** (断り枕詞のみ) and cross-link out rather than reproducing a general 敬語 phrase table.
- Adjacency: this is nominally `keigo` cluster (parent `keigo-guide`, sibling of the apology article), but the JA pivot leans **business-email**. Keep cluster `keigo` for series coherence; cross-link heavily into the business-email trio.

### Terminology
- Drop ALL romaji glosses (*chotto* / *kekkou desu* / *miokuru*) — write native (ちょっと…／結構です／見送らせていただきます). Romaji is base-spec scaffolding for EN readers only.
- Drop the in-house **A/B/C** label from prose and title ([[feedback-title-no-internal-jargon]]); express recipient formality as 相手別（社外・取引先／上司・先輩／社内・同僚）.

### Examples to rewrite
- All 24 base matrix cells: re-author as native completed 例文 (no romaji), reorganized **相手別 × 場面**（取引先の提案／上司の誘い・残業依頼／社内の頼み事／営業電話・営業メール／イベントの誘い）.
- Replace the EN "client discount request" worked example with a JA-native 「営業提案を断る」 / 「見積もり後に見送る」 flow.

### Register / tone
- Native business register throughout (敬語前提、ローマ字・初心者注釈なし). The five-part anatomy maps tightly to native names: クッション言葉 → お礼（感謝）→ お断り＋理由 → 代替案・次の一言 → 結び.
- The 方便・ぼかし表現 section needs careful tone: present 「嘘にならない範囲でぼかす」 as etiquette, not deception (All About leans into 方便; we frame it as 配慮).

### Local expert references
- Optional: 文化庁『敬語の指針』(2007) for the お断り敬語 note (precedent: `sonkeigo-vs-kenjougo.ja` cites it). Business-manner framing can reference the universal 感謝・理由・配慮 3要素 without a single source.

---

## 6. Language-Specific primary_info_seeds

> Beyond the base spec's 3 seeds (field log / soft-no decode test / native grading), which are EN-foreigner-oriented.

1. **日本人ビジネスパーソン「断りメールのヒヤッと」survey（10–15 名）** — 営業お断り／依頼辞退で「後で気まずくなった／関係が悪化した」実例と、その時の文面を収集。NG例セクションと「次につながる一言」の実証背骨に。Google Form、~4h。(JA-only; reuse the `sonkeigo-vs-kenjougo.ja` survey channel.)
2. **営業お断りメール 30 通のネイティブ採点** — 基本／予算／他社利用／時期尚早の各テンプレに register/配慮エラーを混ぜ、営業・購買経験者 2–3 名が natural/awkward/wrong + 「関係は保てたか」で採点。~8h。（base seed #3 の JA 営業版）

---

## 7. Final Localized Outline

> **Option B (full rewrite).** Default below is written for the **native pivot**; if the user picks **B′ hybrid** (recommended), keep this structure but restore a 1-paragraph foreigner-reader hook + title to "現場でそのまま使える" framing and keep light romaji only in a first-use parenthetical. JA divergence from base >50% → Option B per skill rule.

1. H1: _角を立てない丁寧な断り方｜ビジネスでそのまま使えるお断りメール例文集_（候補。B′ なら "外国人も現場でそのまま使える 丁寧な断り方とお断りメール例文" 系）
2. H2: この記事でできること（断りの基本公式 → 相手別例文 → クッション言葉 → NG回避 まで）
3. H2: 丁寧な断りの基本公式（感謝 → 理由 → 代替案・次の一言）← 40〜60字スニペット狙い段落
   - H3: なぜ「断り＝関係を壊す」ではないのか（角を立てない＝断りを断る、ではなく断り方を整える）
   - H3: 5部構成（クッション → お礼 → お断り＋理由 → 代替案／含み → 結び）
4. H2: クッション言葉（ビジネス枕詞）集 — 断り専用
   - H3: 目上・社外向け（恐れ入りますが／せっかくですが／ありがたいお話ですが／身に余るお言葉ですが）
   - H3: 「お役に立てず」「ご期待に添えず」系の言い換え
   - H3: ＞ keigo-cheat-sheet / japanese-email-phrases への動線（一般敬語はそちら）
5. H2: 相手別・場面別 お断り例文集（コピペ可）
   - H3: 取引先の提案・依頼を断る
   - H3: 上司・先輩の誘い／残業依頼を断る
   - H3: 社内・同僚の頼み事を断る
   - H3: 食事・贈り物の勧めを断る（結構です／お気持ちだけ）
   - H3: イベント・会の誘いを断る（またの機会に）
6. H2: 営業・提案を断るメール（状況別テンプレート）
   - H3: 基本テンプレート（感謝＋見送り＋含み）
   - H3: 予算・条件が合わない
   - H3: 他社サービスを既に利用している
   - H3: 時期尚早・将来の可能性を残す
7. H2: 理由の伝え方 — どこまで・どうぼかすか
   - H3: 嘘にならない範囲のぼかし表現（家庭の事情で／よんどころない事情で）
   - H3: 理由は1文・盛りすぎない（言い訳・嘘くささを避ける）
8. H2: 電話で断るときの作法
   - H3: クッション → はっきり断る → 代替案（曖昧にして長引かせない）
   - H3: 営業電話の定型（新規のお取引は控えております）
9. H2: やってはいけない断り方（NG例）
   - H3: 返信しない・無視する
   - H3: 曖昧で期待を持たせる（「前向きに検討します」の害）
   - H3: 感情的・高圧的な表現
   - H3: 嘘がバレる理由／代替案ゼロの突き放し
10. H2: 断った後のフォロー
    - H3: 「またの機会に」を運用する（再連絡のタイミング）
    - H3: 関係を継続する一言
11. H2: よくある質問（PAA起点）
    - H3: 「お役に立てず」の丁寧な言い換えは？
    - H3: 「見送らせていただきます」はいつ使う？
    - H3: 断りメールに返信しないのは失礼？
    - H3: 取引先への断りは電話とメールどちらが良い？
    - H3: 「前向きに検討します」と書いてもよい？
12. H2: 関連記事 + Essential 30 PDF
    - H3: pillar: `keigo-guide`
    - H3: 姉妹: `how-to-say-sorry-in-japanese-politely`（謝罪）/ business-email トリオ（`how-to-write-japanese-business-email` / `business-email-template` / `japanese-email-phrases`）/ `keigo-cheat-sheet` / `polite-japanese-phrases-for-office`

---

## 8. Change Log

| Date | Change | Author |
|---|---|---|
| 2026-06-03 | **JA v1 review pass + publish flip.** ユーザー approve（タイトル整合性確認：主 KW「丁寧な断り方」front＋副「角を立てない／お断りメール例文」包含）。base `languages.ja.status → published`、本 diff spec `status → published`、Live articles 表 JA 列 ✅。最終 `pnpm build` exit 0（lock 直列化、47 pages、EN+JA 生成確認）。次：git commit/push → GSC 登録 2 URL。 | ryoooue + Claude Opus 4.8 |
| 2026-06-03 | **JA v1 shipped（B′ ハイブリッド）.** `src/data/guides/ja/how-to-refuse-politely-in-japanese.mdx`（~8,350字）。§7 の B′ 構造を 1:1 実装：外国人読者フック＋4 ペルソナ → featured-snippet（基本公式 感謝→理由→代替案、55語級）→ 5 部構成（クッション→お礼→お断り＋理由→代替案/含み→結び、悪い例→良い例）→ **断り専用クッション言葉集**（目上・社外向け 6＋「お役に立てず/ご期待に添えず」言い換え 5、一般敬語は keigo-cheat-sheet/japanese-email-phrases へ動線）→ **相手別・場面別お断り例文集**（取引先/上司・先輩/社内・同僚/食事・贈り物/イベント、各コピペ例文＋⚠ミス列）→ **営業お断りメール 状況別 4 テンプレ**（基本/予算/他社利用/時期尚早、件名→本文→署名）→ 理由の伝え方（ぼかし表現＋一文ルール、悪い例→良い例）→ 電話で断る作法（クッション→はっきり→代替案＋営業電話定型）→ **NG 4**（返信しない/曖昧で期待/感情的/嘘バレ・突き放し）→ 断り後フォロー → FAQ 5（PAA 起点）→ 関連 7 sibling（business-email トリオ＋謝罪姉妹を厚めに）＋Essential 30 CTA。Title「日本語の丁寧な断り方｜「いいえ」を使わず角を立てないフレーズとお断りメール例文」（39字、KW「丁寧な断り方」front＋お断りメール例文、A/B/C ジャーゴン除外）。相手別フレーミング採用（A/B/C は keigo-guide へ cross-link で吸収）。`ja-article-style` linter no-changes（クリーン初回）、`pnpm astro check` 0/0/0。base spec `languages.ja.status: planned → drafting`、ja diff spec `status: drafting`。**次：人間レビュー JA v1 → 必要なら v2 → publish flip。** | Claude Opus 4.8 + ryoooue |
| 2026-06-03 | **戦略フォーク決定（AskUserQuestion）→ B′ ハイブリッド採択.** ユーザーが (B′) を選択：外国人読者を維持しつつ、ネイティブ例文バンク＋断り専用クッション言葉集＋相手別テンプレ構造を採用し、KW/title を JA SERP の「お断りメール例文／丁寧な断り方」に寄せる。on-brand な business-growth play。§7 は 相手別フレーミング（A/B/C ローマ字ジャーゴンは prose/title から除外、keigo-guide へ cross-link で吸収）。JA v1 これで着手。 | Claude Opus 4.8 + ryoooue |
| 2026-06-03 | Initial diff spec generated via `seo-article-localize` skill. JA SERP captured (2 queries merged, 7/10 fetched substantively). **diff_needed = TRUE** (base_coverage ≈25%, 5–6 unique additions, hard persona pivot). JA top 10 = native-business-reader content (All About / 幻冬舎 + email-SaaS vendors Mazrica/Blastmail/Cybozu/Emberpoint/Sales Marker + Indeed JP + 電話代行), 0/10 foreigner-learner. Coverage: keep = 5-part anatomy (7/10) + email templates (8/10) + scenario-table format (6/10, romaji stripped); drop = foreigner personas / cultural setup / A/B/C romaji / directness rubric / soft-no reverse-lookup; reframe = mistakes → JA NG例. Additions: クッション言葉集 / 営業お断りメール特化 / NG例文 / 電話 / フォローアップ / 方便・ぼかし表現. Option B full rewrite (>50% divergence). **§5 surfaces a strategic fork (B native pivot / B′ hybrid-recommended / C defer) — needs human go/no-go before drafting; default §7 written for native pivot, B′ keeps foreigner reader + native example-bank structure.** 2 JA-specific primary_info_seeds added. Base spec `languages.ja.diff_spec` updated. | seo-article-localize (Claude Opus 4.8) + ryoooue |
