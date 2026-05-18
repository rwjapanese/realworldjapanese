---
# === IDENTIFICATION ===
base_spec: "specs/articles/sonkeigo-vs-kenjougo.spec.md"
slug: "sonkeigo-vs-kenjougo"
target_language: "ja"

# === DECISION ===
diff_needed: true
diff_reason: "JA SERP base coverage 50% (4/8 base H2 sections appear ≥5/9 in JA top 10); 3 JA-unique additions (30+ 言い換え一覧表 / シーン別早見表 / 二重敬語独立章). Keep base outline + apply 4 small deltas."

# === SERP ===
serp_language: "ja"
serp_locale: "ja-JP"
last_serp_audit: "2026-05-18"

# === LIFECYCLE ===
status: "drafting"
created: "2026-05-18"
---

# Language Diff Spec: sonkeigo-vs-kenjougo — ja

> **How to use this file**
> - The `seo-article-localize` skill generated this because the JA SERP (`尊敬語 謙譲語 違い`) diverges materially from the EN SERP captured in the base spec.
> - The JA article writer reads the base spec for the overall outline, then applies the deltas in §3, §4, §7 of this file.
> - Do NOT duplicate base-spec content here. Only DELTAS.

---

## 1. Decision Summary

- **Base outline coverage in target SERP:** 4 / 8 base H2 sections appear ≥5/9 in JA top 10 → **50%**
- **Language-unique headings:** **3** JA-unique additions appearing ≥3/9 in JA top 10 and absent from base spec
- **Verdict:** `diff_needed = true`. Rule trigger: base coverage 50% is below the 70% threshold AND unique additions count is 3 (above the 2 threshold). However the divergence is **shallow** — base outline H2 stays intact; deltas are 1 expansion (動詞表), 1 strengthening (二重敬語), 1 new section (シーン別早見表), plus title + localization tweaks. **Option A (base + deltas)** is the correct strategy. Full rewrite (Option B) is not warranted.

---

## 2. Target-Language SERP (Top 10)

> Captured on: 2026-05-18. Search engine: Google. Locale: ja-JP. Queries: `尊敬語 謙譲語 違い 例` + `尊敬語と謙譲語の違い 使い分け`. 9/10 fetch 成功（1/10 = y-aoyama 403 のため §3 マージは 9/9 で計算）。

| # | URL | Domain | Title (original) | Title (EN gloss) | Notes |
|---|---|---|---|---|---|
| 1 | https://www.y-aoyama.jp/unicari/manners/10025/ | y-aoyama.jp | 尊敬語・謙譲語・丁寧語の違いをマスター！使い方や見分け方を紹介【一覧あり】 | Master the differences | 派遣会社系コラム。HTTP 403 で fetch 失敗 — position anchor のみ保持。 |
| 2 | https://magazine.bun-ken.net/3974 | magazine.bun-ken.net | 3種類の敬語表現「尊敬語・謙譲語・丁寧語」の違いと使い分け | Three types of honorifics: differences and usage | 編集会社系。~6,500 字。**「ウチ・ソト」概念を実践的に解説**、5 シーン別クイズあり。文化庁指針ベース。 |
| 3 | https://townwork.net/magazine/knowhow/manners/baito_manners/13309/ | townwork.net | 知っておきたい！よく使う敬語変換表【尊敬語・謙譲語・丁寧語】 | Common honorific conversion table | リクルート求人系。~3,500–4,000 字。**31 項目言い換え表**が中核 + 「あるあるベスト5」誤用集。バイト現場特化。 |
| 4 | https://sho.benesse.co.jp/column/kyouiku/251009-8.html | sho.benesse.co.jp | 国語で習う敬語とは？小学生向けに尊敬語・謙譲語・丁寧語を解説 | Honorifics taught in school: explained for elementary students | 進研ゼミ。~3,500 字。「誰の動作か」軸で分類。二重敬語の独立章あり。広告色強め。 |
| 5 | https://blastmail.jp/blog/tools/honorific-language | blastmail.jp | いまさら聞けない丁寧語・尊敬語・謙譲語の違いは？頻出のフレーズとシーン別の使用例も紹介 | What is the difference between teineigo, sonkeigo, and kenjougo? | メール配信会社。~6,500 字。**シーン別（ビジネス / メール / 接客 / 電話）章 + 例文メール 3 本 + 誤用 3 章**。実務最寄り。 |
| 6 | https://www.humantrust.co.jp/helpful_guide/work_skill/detail/employee | humantrust.co.jp | 「尊敬語」と「謙譲語」の違いについて | About the difference between honorific and humble language | 派遣会社系。~2,100 字。**比較クエリ専用**のコンパクト解説（teineigo を含まない数少ない 1 本）。 |
| 7 | https://domani.shogakukan.co.jp/600476 | domani.shogakukan.co.jp | 「尊敬語」と「謙譲語」の意味や使い分けと敬語表現一覧を紹介 | Meanings and usage with reference table | 小学館 Domani 女性誌。~2,500 字。「相手を高める／自分を低くする」対比的説明。fetch で後半切れあり。 |
| 8 | https://biz.trans-suite.jp/55914 | biz.trans-suite.jp | 「尊敬語」と「謙譲語」の違いをわかりやすく解説！例文や丁寧語も | An easy-to-understand explanation with examples | TRANS.Biz。~3,500–4,000 字。**「主語が誰になるかの違いで使い分ける」を H3 で明示** + 古文・古典の節あり（独自）。 |
| 9 | https://allabout.co.jp/gm/gc/291871/ | allabout.co.jp | 尊敬語と謙譲語の使い分け方！ビジネスでは失礼のない敬語の表現を | How to distinguish: avoid being rude in business | All About。~3,200 字。**「主語を入れ替える方法」が中核** — お客様 / 私 で入れ替え判定。 |
| 10 | https://www.hatarako.net/magazine/career/work-tips/detail/49065/ | hatarako.net | 敬語の「尊敬語・謙譲語・丁寧語」を正しく使い分けよう！【よく使う敬語表現一覧付】 | Properly distinguish honorifics with reference table | 派遣求人系。~2,800 字。**間違いやすい敬語 + 二重敬語の独立章**ペア。一覧表あり。 |

### Target-language SERP features
- [x] Featured snippet (likely)
- [x] People Also Ask (local-language) — 推定：「尊敬語と謙譲語の違いは？」「使い分けは？」「間違いやすい敬語は？」
- [ ] Video carousel
- [ ] Image pack（表データの image rich result の可能性）

### Target-language PAA / related searches
- 尊敬語と謙譲語の違いは？
- 尊敬語と謙譲語の使い分けは？
- 二重敬語とは？
- 尊敬語と謙譲語の例文
- 尊敬語・謙譲語・丁寧語の一覧
- 「させていただく」は尊敬語か謙譲語か
- 身内に尊敬語を使ってもよいか
- 敬語の指針（文化庁）とは

---

## 3. Coverage of Base Spec Outline

> Check each H2 from the base spec §7 (JA outline) against JA SERP top 10.

| Base spec heading (JA) | Coverage in JA SERP (x/9) | Action | Note |
|---|---|---|---|
| この記事を読むべき人 | n/a | keep | Intro メタ、SERP 不問。 |
| 1 文サマリ（featured snippet 用 40–60 字） | n/a | keep | Featured snippet ターゲット、SERP 不問。 |
| 「主語は誰？」3 秒判断フロー | 6/9 | keep | biz.trans-suite / allabout / blastmail / bun-ken / benesse / humantrust が「主語が誰か」軸で類似説明あり。**ただし 3 ステップ decision card 形式は 0/9** → 形式そのものは独自性維持。 |
| 60 秒復習 — A/B/C フレームと主語軸 | 0/9 (A/B/C 独自) ／ 9/9 (3 種類セット解説部分) | keep | A/B/C フレーム自体は JA SERP に皆無 = 我々独自。一方「尊敬語・謙譲語・丁寧語の 3 種類セット解説」は 9/9 が table stakes として展開 → 本セクションでサクッと触れるだけで両立可能。 |
| 頻出 10 動詞の 4 列対照表 | 5/9 (言い換え表として) | **keep + expand** | townwork 31 項目 / hatarako / blastmail / bun-ken / domani が変換表を持つ。JA 読者は「10 行」では物足りない可能性が高い → **§4 と §7 の delta 参照（20-30 動詞に拡張 OR `keigo-cheat-sheet` への embed プレビュー導線を強化）**。 |
| 「自社の上司を社外に話す」内/外反転ミニ対話 | 1/9 (bun-ken のみウチ・ソト概念) | keep | フル対話例は 0/9 で完全独自。SERP には「身内に尊敬語を使わない」が 3-4/9 あるが対話展開はしない → 強い差別化候補のまま維持。 |
| よくある 5 つの誤用（wrong → right） | 5/9 | **keep + strengthen 二重敬語** | townwork / blastmail / hatarako / benesse / sho.benesse が「間違いやすい敬語」「二重敬語」章を持つ。**JA SERP では二重敬語を独立章に格上げするのが標準（5/9）** → §7 delta で対応。 |
| PAA 直撃 — 謙譲語 I と II（丁重語）の違い | 0/9 | keep | JA SERP では誰も独立章で扱わない → PAA snippet 取得の独自チャンス継続。ただし JA 読者は「謙譲語 I／II」用語に馴染みが薄い場合があるため、見出しは「謙譲語の 2 種類（一般的な謙譲語と丁重語）」のように噛み砕く。 |
| 学習負荷を半分にする「読 vs 話す」の分離 | 0/9 | keep | 完全独自。ただし JA 読者ペルソナ拡張（日本人ビジネスパーソン）に対しては「受信時に意味が取れる／発信時に口から出る」言い換えで提示。 |
| よくある質問（FAQ） | 0/9 | keep | JA SERP は「まとめ」止まりで FAQ H3 形式は皆無。スキーマ JSON-LD で PAA 取りに行ける独自。 |
| 次に読むべき関連記事 | 1/9 | keep | クラスター内 6 本クロスリンク + Essential 30 CTA。SERP 競合は内部リンクが薄い → 滞在伸長で勝てる。 |
| Essential 30 PDF CTA | n/a | keep | 商用 CTA、SERP 不問。 |

---

## 4. Language-Specific Additions

> Headings appearing ≥3/9 in JA top 10 but NOT in base spec.

| New heading | Coverage (x/9) | Why JA-relevant |
|---|---|---|
| **30 項目以上の言い換え一覧表（動詞 / 尊敬語 / 謙譲語 + 丁寧語の 4 列）** | 5/9 | townwork 31 項目 / hatarako / blastmail / bun-ken / domani が「変換表」を中核資産として置く。JA 読者は「一覧つき」「【一覧あり】」を benefit promise として期待（タイトルにも明記される慣行、Top 10 中 4 本のタイトルが【一覧】系）。Base spec §6（10 動詞）は不足。**delta: 表を 20–30 動詞に拡張するか、10 動詞表 + `keigo-cheat-sheet` 内の大表 embed preview の 2 段構え**。 |
| **シーン別早見表（ビジネス / メール / 電話 / 接客）** | 4/9 | blastmail / townwork / bun-ken / hatarako がシーン別章を独立で持つ。Base spec §7（電話を取る場面の 1 対話）はあるが、4 シーン横断の表は無い。**delta: 既存 `keigo-examples` / `business-email-template` / `polite-japanese-phrases-for-office` への動線を H2 セクションとして格上げ**（コンテンツ重複を避けながら読者期待を満たす）。 |
| **二重敬語の独立章** | 5/9 | hatarako / blastmail / sho.benesse / townwork / domani が「二重敬語」を独立章として扱う。Base spec §7-8 では 5 wrong→right ペアの 1 つに含めるのみ。**delta: §7-8 内で二重敬語ペアを 1 → 2 ペアに増やす**（「ご覧になられました」「お聞きになられました」の 2 例で典型 2 パターンを押さえる）+ コールアウトで「二重敬語の作られ方」のメカニズム 2 行解説を追加。 |

---

## 5. Localization Considerations (non-SERP)

### Terminology
- **「主語」→「動作主」推奨**: Base spec §10 で既に flag 済の通り、JA 読者は文法用語の「主語」が省略される文章を日常的に読むため、「主語は誰か」よりも「動作主は誰か」「動作するのは誰か」のほうがピンと来やすい。3 秒判断フローの H3 見出し（ステップ 1）は「動作主は相手か自分か」に置き換える。
- **「ウチ・ソト」表記**: bun-ken など JA SERP で「ウチ・ソト」とカタカナで定着 → 我々の article も同様に「ウチ／ソト」をカタカナで採用（romaji は不要）。Base spec EN 版は `uchi-soto` 表記、JA 版は「ウチ／ソト」または「内／外」。
- **「丁重語」用語**: JA 読者でも「謙譲語 I / II」という分類名は馴染みが薄い → 見出しでは「謙譲語の 2 種類（一般的な謙譲語と丁重語）」のように噛み砕き、本文で「文化庁『敬語の指針』(2007) では…」と一度だけ典拠を入れて authority を取る。
- **`A/B/C` 表記**: cluster 内 house-style 「A/B/C politeness framework」は維持。ただし「**段階別**」「**段階 A／B／C**」を初出時に併記して、`A→B→C` 単独表記（CTR 毀損リスク、`best-way-to-learn-keigo` v2 で確認済の house lesson）を避ける。

### Examples to rewrite
- **電話シーン**: Base spec の 8 行ミニ対話は EN 版も JA 版も「取引先からの電話を取る」場面で共通。ただし JA 版では「お電話代わりました、〇〇でございます」「申し訳ございません、本日不在にしております」など、JA SERP 競合（blastmail / townwork）でカバー率が高い実フレーズを 2 つ折り込む。
- **メール例文**: Base spec には例文メールは無いが JA SERP では blastmail が 3 通入れる → §7 の「シーン別早見表」セクションで「メールの 1 行サンプル + 詳細は `business-email-template` へ」の動線で対応（フル例文は引き継ぐが本記事内では膨らませない）。
- **ペルソナ拡張**: Base spec EN 版は「JLPT N3–N2 非ネイティブ」が単独ターゲット。JA 版は **「①日本人ビジネスパーソン 1–3 年目 + ②帰国子女・留学経験者 + ③ビジネス日本語に再入門する社会人」** の 3 層を併記（JA SERP の派遣・教育・ビジネスメディア競合はこの 3 層を想定）。

### Register / tone
- JA 版は「です・ます」基調、ただし冒頭フックは断定形（「〜のはなぜか」「〜は知っているけれど…」）も許容（cluster 内 `keigo-examples` JA v2 で confirmed pattern）。
- 「〜と言えるでしょう」「〜かもしれません」のような hedging は避け、「〜です」「〜になります」で言い切る（`best-way-to-learn-keigo` JA v2 review で softening は決めつけ口調回避のためのみ採用、過剰な hedging は CTR と読了率を毀損）。
- 「結論」「ポイント」「まとめ」のような JA ビジネス読者向け視認語を H3 直下リードや太字キーワードに散らす（visual scan 寄り）。

### Local expert references
- **文化庁「敬語の指針」(2007)**: JA SERP 競合の 3-4 本が直接または間接的に参照する公的典拠。本記事内で 1 度だけ引用 → 「文化庁の指針では『謙譲語 I（伺う・申し上げる等）』と『謙譲語 II（丁重語：参る・申す等）』に分けています」のような形で謙譲語 I/II セクションの authority backing に使う。
- 内部 authority: `keigo-guide` pillar + `keigo-mistakes` への動線を JA 版でも明示的に置く（クラスター内 internal authority も SEO シグナル）。

---

## 6. Language-Specific primary_info_seeds

> Base spec の 3 seeds（subject-detection drill / senpai-HR interview / 14-day verb log）は **JA / EN いずれにも使える**ため、本 diff spec では追加 seed は基本不要。ただし JA 版限定で 1 つだけ意味のある追加候補：

1. **日本人新卒・若手社員の「自分が一番ヒヤッとした敬語ミス」アンケート (JA-only)**
   - _What:_ 入社 1–3 年目の日本人社員 15–25 名に「自分が言って後で『あれ間違いだった』と気づいた sonkeigo / kenjougo のミス」を 1 件ずつ書いてもらう。Base spec の seed (b) は「ネイティブ senpai/HR 視点」だが、こちらは「**ネイティブ若手の当事者視点**」で角度が違う。
   - _How:_ Google Form 公開 + Twitter (X) / LinkedIn / 著者人脈経由で配布。回答者属性（業界・年次・部署）をオプションで記録。
   - _Cost:_ ~4h（form 設計 1h + 配布 1h + 集計・匿名化 2h）
   - _Status:_ `not_started`
   - _Why JA-only:_ JA 読者ペルソナ②③（日本人ビジネスパーソン）に直接刺さる「自分も同じ立場の人がこう間違えていた」共感資産になる。EN 版は外国人学習者向けのため適用度が低い。

---

## 7. Final Localized Outline

> **Option A: Reference base spec with deltas**
>
> - Base: see `specs/articles/sonkeigo-vs-kenjougo.spec.md` §7 JA outline.
> - Deltas を以下に列挙（追加・変更のみ）。

### Title

- Base spec JA タイトル: 「尊敬語と謙譲語の違い｜『主語は誰？』で 3 秒判断する完全ガイド」
- **JA delta（採用案）:** 「**尊敬語と謙譲語の違い｜『動作主は誰？』で 3 秒判断＋使い分け一覧つき**」
  - 変更理由: (1) 「主語」→「動作主」（§5 terminology delta）。(2) 「【一覧つき】」または「使い分け一覧つき」を入れる（JA SERP 上位 4 タイトルが【一覧】系 benefit promise を持つ）。
  - 字数: 約 38 字（JA 上限 40 字以内に収まる）。

### Section-level deltas

| Base §7 番号 | Delta タイプ | 内容 |
|---|---|---|
| H2 「主語は誰？」3 秒判断フロー | **rename** | 「**動作主は誰？**」3 秒判断フローに変更（§5 terminology）。Step 1 H3 も同様に「動作主は相手か自分か」に。 |
| H2 60 秒復習 — A/B/C フレーム | **rename + tweak** | 見出し冒頭に「**段階別**」を追加 → 「60 秒復習 — **段階別** A/B/C フレームと動作主軸の関係」。本文中の `A→B→C` 表記は初出のみとし、以降は「段階 A / B / C」に統一。 |
| H2 頻出 10 動詞の 4 列対照表 | **expand** | 動詞を **20 行** に拡張（base の `iku/kuru/iru/iu/taberu/miru/kiku/suru/shitteiru/au` の 10 動詞 + 「来る／行く」以外で JA SERP 頻出の `agetu/morau/kau/yomu/kaku/yobu/kangaeru/omou/dekiru/au` の 10 動詞）。表の冒頭に「より詳しい変換表は `keigo-cheat-sheet` へ」のリンクを 1 行明示。 |
| H2 「自社の上司を社外に話す」内/外反転ミニ対話 | **rephrase** | 「**ウチ／ソト**」表記をカタカナで導入し、対話本文内では「内（社内）／外（社外）」の併記。`uchi-soto` ローマ字は使わない。 |
| H2 5 つの誤用（wrong → right） | **strengthen + restructure** | 2 段構成にする：(A) **動作主取り違え型** 3 ペア（base 通り：`部長が参られました` / `お客様が申されました` / `私が召し上がります`）+ (B) **二重敬語型** 2 ペア（`ご覧になられました` → `ご覧になりました` / `お聞きになられました` → `お聞きになりました`）。冒頭に「**JA 読者がよく出会う 2 系統のミス**」と 2 ブロックに分けることで JA SERP の「二重敬語独立章」期待を吸収しつつ動作主混同のメッセージは保持。 |
| H2 PAA 直撃 — 謙譲語 I と II | **rephrase** | 見出しを **「謙譲語の 2 種類（一般的な謙譲語 I と『丁重語』II）」** に変更。本文内で「文化庁『敬語の指針』(2007) では…」を 1 文だけ引用。`mairu` / `mousu` の対比は維持。 |
| **NEW** H2 シーン別早見表（メール / 電話 / 接客 / 社内会議） | **add** | 新規 H2 を `§7-9（PAA snippet）` の直後 / `§7-10（読 vs 話す）` の前 に挿入。中身は **4 行ミニ早見表**（シーン × 「よく出る尊敬語 1 例」「よく出る謙譲語 1 例」「詳細は…」3 列）+ 各シーン末尾に sibling リンク 1 本（`business-email-template` / `keigo-examples`（電話）/ `polite-japanese-phrases-for-office`（接客）/ `keigo-examples`（社内会議））。本文は薄くし、深掘りは sibling に渡す（記事間カニバリ回避）。 |
| H2 学習負荷を半分にする「読 vs 話す」分離 | **rephrase** | 「**受信時に意味が取れればよい／発信時に口から出るべき**」と JA 文脈の言い回しを採用（base の英語的「read vs produce」直訳を避ける）。中身の動詞分け表は base 通り。 |
| H2 FAQ | **add 1 item** | base 5 件に加え、JA SERP の PAA 想定から **「『させていただく』は尊敬語と謙譲語のどちらか？」** を 1 件追加（謙譲語、ただし過剰使用注意 → `keigo-mistakes` 動線）。 |
| H2 次に読むべき関連記事 | **keep** | base 通り。 |

### 採用しない（Option A の範囲外）
- **古文・古典での尊敬語/謙譲語**: biz.trans-suite が独自に持つが、本記事ペルソナ（ビジネス読者）と乖離するため drop。
- **小学生向け視点**: sho.benesse が持つが、ペルソナ不一致で drop。
- **接客敬語 / バイト敬語**: townwork / blastmail が部分章にする。シーン別早見表（new H2）の接客 1 行で消化し、独立章は持たない（`polite-japanese-phrases-for-office` への動線で十分）。

---

## 8. Change Log

| Date | Change | Author |
|---|---|---|
| 2026-05-18 | Initial diff spec generated via `seo-article-localize` skill. JA SERP fetched 9/10 cleanly (y-aoyama 403 = position anchor only). Verdict: `diff_needed = true` — base coverage 50% (4/8 H2 ≥5/9) AND 3 JA-unique additions (30+ 言い換え表 / シーン別早見表 / 二重敬語独立章). Strategy: **Option A (base + deltas)** — divergence is shallow, base outline H2 stays intact. Recorded 7 specific deltas: title rewrite (動作主 + 一覧つき), 動詞表を 10 → 20 行に拡張, 内/外反転対話の「ウチ／ソト」表記化, 5 誤用を 動作主取り違え 3 + 二重敬語 2 の 2 ブロック化, 謙譲語 I/II 章で文化庁指針引用, **新規 H2「シーン別早見表」追加** (sibling 動線格上げ), FAQ に「させていただく」1 件追加。Localization §5 で 「主語→動作主」用語置換 + ペルソナを 3 層に拡張 (日本人若手社員 + 帰国子女 + ビジネス再入門社会人) を確定。JA 限定 primary_info_seed 1 件追加（日本人新卒・若手社員ヒヤッと敬語ミス Google Form survey, ~4h）。 | seo-article-localize (Claude Opus 4.7) |
| 2026-05-18 | **JA published — base spec と同タイミングで `published` flip**. base spec `status` および両言語 `languages.{en,ja}.status: drafting → published` flip。本 diff spec の役割（JA 着手前の SERP 乖離判定 + delta 提示）は JA v1 で全 7 deltas を実装したことで完了。今後 SERP の大きな変動があった場合に re-run の参照点として保持。 | ryoooue (publish trigger) + Claude Opus 4.7 |
| 2026-05-18 | **JA v1 shipped — 7 deltas 全実装確認**. Body: `src/data/guides/ja/sonkeigo-vs-kenjougo.mdx` (約14,300字)。本 diff spec §7 deltas を 1:1 実装：(1) title「動作主は誰？」+「使い分け一覧つき」 ✓、(2) 動詞表 10→20 行 + `keigo-cheat-sheet` 動線 ✓、(3) ウチ／ソト カタカナ表記統一 ✓、(4) 5 誤用 2 ブロック化（動作主取り違え 3 + 二重敬語 2）✓、(5) 謙譲語 I/II 章で文化庁『敬語の指針』(2007) 1 文引用 ✓、(6) 新規 H2「シーン別早見表」追加（メール/電話/接客/社内会議 × sibling 動線 4 本）✓、(7) FAQ に「させていただく」1 件追加（合計 6 件）✓。Localization §5 用語置換も実装：「主語→動作主」全面採用、A→B→C は初出のみで以降「段階A/B/C」、文化庁引用は 1 度のみ。`ja-article-style` linter idempotent pass、`pnpm build` green at 28 pages / 8,926 words indexed。`languages.ja.status: planned → drafting` に flip 済（base spec frontmatter）。次：人間レビュー → JA v2 if needed → EN v1。 | Claude Opus 4.7 + ryoooue |
