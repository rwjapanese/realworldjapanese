---
# === IDENTIFICATION ===
slug: "sonkeigo-vs-kenjougo"
collection: "guides"
cluster: "keigo"
pillar: "keigo-guide"

# === SEO ===
target_keyword: "sonkeigo vs kenjougo"
serp_language: "en"
target_intent: "informational"
search_volume_estimate: null
difficulty_estimate: "medium"

# === FUNNEL ===
funnel_stage: "MOFU"
product_cta: "essential-30"
lead_magnet: null

# === LANGUAGES ===
languages:
  en:
    status: "published"
    url_slug: null
    diff_spec: null
  ja:
    status: "published"
    url_slug: null
    diff_spec: "specs/articles/sonkeigo-vs-kenjougo.ja.spec.md"

# === LIFECYCLE ===
status: "published"
created: "2026-05-18"
last_serp_audit: "2026-05-18"
---

# articleSpec: Sonkeigo vs Kenjougo — the "who's the subject?" decision

> **How to use this file**
> - The `seo-article-outline` skill generated the initial version.
> - Humans review and refine §5 "Our Differentiation" and §6 "primary_info_seeds".
> - When SERP changes significantly, re-run the skill to refresh §2–§4.
> - Do NOT delete the spec after publication — it's the source of truth for updates.

---

## 1. Target & Intent

### JA

**主要な検索意図:** `sonkeigo vs kenjougo` を打つユーザーは、ほぼ全員が「2 つを並べたときの違いを 1 度ですっきり整理したい」状態。`keigo-guide` 系の総合解説では「3 つあります」で並列に並べられて終わるため、**尊敬語と謙譲語の境界線そのもの**にフォーカスした解説に強い需要がある。比較クエリの典型で MOFU（中段）— 用語自体は知っているが運用判断（どっちを選ぶ？）で詰まっている読者。

**読者ペルソナ:** 仕事 / インターン / 留学先で日本語ビジネス場面に投入された JLPT N3–N2 レベルの非ネイティブ。3 種の名前は聞いたことがあり丁寧語まではこなせるが、`mairu` か `irassharu` か、自分の上司の動作を社外の人に話すとき何を使うか、で固まる。「動詞表は見たけど、いざ口に出すときどっち？」がコア痛点。

**成功基準:** 読者が以下 3 つを記事終了時に「自分の口で言える」状態：(a) 主語が誰かに応じて尊敬語か謙譲語かを 3 秒で判断する手順、(b) よく使う 10 動詞について両方の形を即答できる、(c) 自分の上司を社外に話すときの「内/外反転」処理を 1 例で説明できる。FAQ にある「両方混ぜていい？」「謙譲語 I と II の違いは？」にも具体回答済み。

### EN

**Primary search intent:** Users typing `sonkeigo vs kenjougo` are almost always in "compare them side-by-side so I stop confusing them" mode. Generic keigo-pillar articles dump "there are three types" without sharpening the **boundary line between sonkeigo and kenjougo**, which is exactly what the comparison query asks for. Classic MOFU comparison intent — the reader already knows the names but freezes on the operational pick (which one do I say?).

**Audience persona:** JLPT N3–N2 non-native learner working / interning / studying abroad in a Japanese-language business context. They've heard the three names, can produce teineigo reliably, but freeze on whether to say *mairu* or *irassharu*, or what to do when talking about their own boss to an outside client. Core pain point: "I've seen the verb table; the moment I need to speak, I lose which side I'm on."

**Success criteria:** Reader can do three things by the end: (a) decide between sonkeigo and kenjougo in 3 seconds using a who-is-the-subject rule, (b) produce both forms for the top 10 highest-frequency verbs without hesitation, (c) handle the "talking about my boss to an external client" inversion with at least one full example. FAQ also resolves "can I mix them?" and "what's kenjougo I vs II?".

---

## 2. SERP Analysis (Top 10)

> Captured on: 2026-05-18. Search engine: Google. Locale: en-US.
> Coverage denominators in this spec are always `/10` (out of top 10 competitors).

| # | URL | Domain | Title | Format | Word Count | Notes |
|---|---|---|---|---|---|---|
| 1 | https://migaku.com/blog/japanese/sonkeigo-vs-kenjougo | migaku.com | Sonkeigo vs Kenjougo: Use Japanese Teineigo, Sonkeigo and Kenjougo Correctly | guide | ~2,200 | Exact-match KW. "Knight kneeling before king" metaphor for the elevate/lower split. Heavy product promo. |
| 2 | https://medium.com/@keithkat/the-japanese-keigo-trio-teineigo-sonkeigo-and-kenjougo-85f28bc8d113 | medium.com | The Japanese Keigo Trio — Teineigo, Sonkeigo, and Kenjougo | video-blog | ~1,100 | No H2/H3 — flat blog post. Beginner-author personal-discovery tone; anime-credits angle. Weak authority. |
| 3 | https://blog.boxofmanga.com/keigo-sonkeigo-kenjougo-teineigo/ | boxofmanga.com | The 3 Kinds of Keigo: Sonkeigo, Kenjougo and Teineigo | guide | ~1,200 | Context-based when/where breakdown; relies on prose, light on sentence-level examples. |
| 4 | https://www.japaneseammo.com/japanese-business-speech-敬語-keigo-sonkeigo-and-kenjougo/ | japaneseammo.com | Japanese Business Speech 敬語 (Keigo)┃Sonkeigo and Kenjougo | guide | ~3,200 | Fast-food vs restaurant dual-scenario walkthroughs. Dense terminology; no priority guidance. |
| 5 | https://talkpal.ai/culture/what-is-the-difference-between-sonkeigo-and-kenjougo/ | talkpal.ai | What is the difference between sonkeigo and kenjougo? | guide | ~1,350 | AI-generated style. Side-by-side verb table + practical dialogue. No audio / no interactivity. |
| 6 | https://risupress.com/japanese/basic-keigo-need-know-japan/ | risupress.com | Basic Keigo You Need to Know in Japan | guide | ~1,800 | Same knight-king metaphor as #1. Free chart referenced but not embedded — UX friction. |
| 7 | https://my-senpai.com/grammar/grammar-guides/japanese-keigo-guide.html | my-senpai.com | Japanese Keigo Guide: Sonkeigo, Kenjougo, Teineigo & Baito Keigo Explained | guide | ~5,800 | Strongest competitor: uchi-soto unifying logic + baito-keigo dedicated section + decision guide + FAQ. Heavy on tables. |
| 8 | https://en.wikipedia.org/wiki/Honorific_speech_in_Japanese | wikipedia.org | Honorific speech in Japanese | grammar-reference | ~6,500 | Sociolinguistic depth + theoretical frames (Brown-Levinson etc.). Outdated citations; reference-y, not operational. |
| 9 | https://www.japanistry.com/honorifics | japanistry.com | Honorifics in Japanese: A Complete Introduction to Keigo, Sonkeigo, and Kenjogo | grammar-reference | ~3,200 | Adds bikago (美化語) section. Example-heavy but no exercises / no decision rule. |
| 10 | https://jtalkonline.com/business-japanese-keigo-ii-kenjougo/ | jtalkonline.com | Business Japanese – Keigo II – Kenjougo | guide | ~2,200 | Kenjougo-only article (sister to a sonkeigo piece). Phone-call + apology scenarios. Verb-table heavy. |

### SERP features present
- [x] Featured snippet (likely — comparison query)
- [x] People Also Ask (PAA)
- [ ] Video carousel
- [ ] Image pack
- [ ] Knowledge panel
- [x] Related searches

### Related searches / PAA questions
- What is the difference between sonkeigo and kenjougo?
- When do you use kenjougo?
- Is sonkeigo or kenjougo more polite?
- Can you mix sonkeigo and kenjougo in the same sentence?
- What are examples of kenjougo verbs?
- How do you know when to use sonkeigo?
- What is kenjougo I vs kenjougo II (謙譲語I/謙譲語II / teichougo 丁重語)?
- Do Japanese people actually use kenjougo every day?

---

## 3. Merged Outline (from Top 10)

> All distinct headings found across the top 10, with coverage count.
> Coverage = how many of top 10 articles have a section matching this heading.

| Heading | Coverage (x/10) | Notes |
|---|---|---|
| What is keigo / 3 types overview | 9/10 | Table stakes — every competitor opens here. |
| Sonkeigo definition + elevate-others framing | 9/10 | Table stakes. |
| Kenjougo definition + humble-self framing | 9/10 | Table stakes. |
| Teineigo as foundation / "desu-masu" baseline | 8/10 | Most still bundle teineigo as context-setter. |
| Sonkeigo verb conjugation table (special verbs + ~reru/rareru + o-...-ni-naru) | 7/10 | Strong signal. Quality varies widely. |
| Kenjougo verb conjugation table (special verbs + o-...-suru) | 7/10 | Strong signal. |
| When to use each (workplace / external-client scenarios) | 8/10 | Almost universal; quality varies. |
| Side-by-side same-verb comparison (sonkeigo + kenjougo together for one verb) | 3/10 | Talkpal partial; Japaneseammo / My-Senpai scatter through prose. Weak. |
| Uchi-soto / in-group out-group | 4/10 | My-Senpai + Wikipedia dedicated; Migaku + Risupress mention. Most miss the inversion case. |
| Common mistakes (using kenjougo for boss's action, etc.) | 3/10 | Migaku + My-Senpai + scattered. Rarely a full wrong→right table. |
| Bikago (美化語) / word beautification | 2/10 | Wikipedia + Japanistry only. Optional. |
| Baito keigo (バイト敬語) | 2/10 | My-Senpai dedicated; Migaku mentions. Niche. |
| Cushion words (クッション言葉) | 1/10 | My-Senpai only. |
| Decision flow / "which one when?" framework | 1/10 | My-Senpai's "Decision Guide" closest. SERP gap. |
| FAQ section | 1/10 | My-Senpai only. SERP gap. |
| Honorific titles (-san, -sama, etc.) | 1/10 | Wikipedia only. Out of scope for the comparison query. |
| Kenjougo I vs II (謙譲語 I / II / 丁重語) distinction | 0/10 | Total SERP gap. PAA question, unanswered. |
| Subject-detection 3-question rule | 0/10 | SERP gap — the actual operational test. |
| Talking-about-my-boss-to-external-client uchi-soto inversion full dialogue | 0/10 | SERP gap. Mentioned in prose by 2 sites; never a dedicated mini-scene. |
| Top 10 highest-frequency keigo verbs to memorize first | 0/10 | SERP gap. Every competitor lists 20–40 verbs without priority. |
| Read-vs-write split (recognize vs produce) | 0/10 | SERP gap. |
| 5 wrong→right swap mistake pairs with one-line "why" | 0/10 | SERP gap. |

---

## 4. Content Gaps

> What top-10 articles collectively fail to cover, but the searcher likely wants.

### JA

1. **「主語は誰か？」3 秒判断ルール (0/10)** — どの記事も尊敬語と謙譲語を「並べて説明」はするが、「いざ口に出すときの 1 番目の問い」を明確化していない。`(a) 主語は相手か自分か (b) 相手は内 / 外のどちら側か (c) 動詞そのものは何か`の順で判断する 3 ステップを最初に置けば、SERP の比較クエリ意図に最短で答えられる。
2. **同じ動詞を尊敬語 / 謙譲語の両形で 1 行に並べた頻出 10 動詞表 (0/10 — 部分的に 3/10)** — Talkpal が比較表を出すが弱い。`iku` / `kuru` / `iru` / `iu` / `taberu` / `miru` / `kiku` / `suru` / `shitteiru` / `au` の 10 動詞を「動詞 / 丁寧語 / 尊敬語 / 謙譲語」4 列で並べた一枚岩の表が SERP に存在しない。
3. **「上司の動作を社外に話す」内/外反転ミニ対話 (0/10)** — uchi-soto は 4/10 で説明はあるが、「外部の取引先に対して自分の上司について話すときに敬語が反転する」というキラー場面のフル対話例は誰も載せていない。実務で最も混乱する局面で、ここで差別化が立つ。
4. **5 つの wrong→right 入れ替え例 + 1 行「なぜダメか」(0/10)** — `部長が参られました` / `お客様が申されました` 系の典型誤用を「✗ → ◯ → 理由 1 行」の 3 列で並べた表が SERP に皆無。`keigo-mistakes` への動線確保と本記事の差別化を同時に成立させる。
5. **謙譲語 I と II（丁重語）の違い (0/10)** — PAA に出る質問だが SERP 10/10 で扱われていない。`mairu`（謙譲語 I：行為の向き先がいる場合）と `mousu`（謙譲語 II/丁重語：聞き手だけ立てる場合）の差を 1 段落で線引きするだけで、PAA snippet を取りに行ける。
6. **頻度順 Top 10 動詞（最初に覚えるべき優先順位）(0/10)** — どの記事も 20–40 動詞をフラットに並べる。実務で最初に 10 個覚えれば 8 割の場面に対応できる、というランキング提示は誰もしていない。学習負荷削減の差別化ポイント。

### EN

1. **3-second "who's the subject?" decision rule (0/10)** — Every competitor explains sonkeigo and kenjougo *in parallel* but no one frames the operational first question: `(a) Is the subject the other person or me? (b) Is that person uchi or soto? (c) What's the verb?` Putting this 3-step test up front directly answers the comparison-query intent.
2. **Top 10 highest-frequency verbs side-by-side in one table (0/10; partial 3/10)** — Talkpal has a comparison table but it's weak. A single 4-column table — `verb / teineigo / sonkeigo / kenjougo` — for `iku` / `kuru` / `iru` / `iu` / `taberu` / `miru` / `kiku` / `suru` / `shitteiru` / `au` does not exist anywhere in the SERP.
3. **"Talking about your boss to an external client" inversion dialogue (0/10)** — Uchi-soto is named by 4/10 but no one writes the full mini-dialogue where keigo flips when the audience is external. This is the single hardest moment in practice and the cleanest differentiation hook.
4. **5 wrong→right swap pairs with one-line "why" (0/10)** — `Buchou ga mairaremashita` / `Okyakusama ga moushimashita` errors are mentioned in prose but no SERP article gives a clean `✗ → ◯ → reason` 3-column table. Anchors a hand-off link to `keigo-mistakes`.
5. **Kenjougo I vs II (humble vs teichougo / 丁重語) (0/10)** — A standing PAA question; 0/10 SERP coverage. A one-paragraph cut — `mairu` (humble I, directed at an in-scene recipient) vs `mousu` (humble II / 丁重語, neutral lowering for the listener only) — is enough to attempt the PAA snippet.
6. **Frequency-ranked Top 10 verbs (which to memorize first) (0/10)** — Every competitor dumps 20–40 verbs flat. None rank them so the learner knows the first 10 will cover ~80% of office situations. Cuts learning load and differentiates.

---

## 5. Our Differentiation

> Our unique angle. What makes this article rank above the top 10, not just match them?

### JA

- **A/B/C politeness framework × 主語軸の二軸再構成。** `keigo-guide` / `keigo-cheat-sheet` / `keigo-examples` で確立済みの A/B/C を、本記事では「主語が誰か」という第二軸とクロスさせて、A/B 行は teineigo 領域・C 行を「主語=他者→sonkeigo 列 / 主語=自分→kenjougo 列」に縦割りする。クラスター内の framework 一貫性を維持しつつ、比較クエリに最短で答える。
- **「主語は誰か？」3 秒判断フロー (0/10 gap)。** 記事の冒頭直後に "Who's the subject?" 3 ステップ判断（主語＝相手か自分か → 内/外 → 動詞）を decision card として配置。featured snippet を狙える 40–60 ワード段落として書く。
- **頻出 10 動詞の 4 列同時表（0/10 gap）。** 動詞 / 丁寧語 / 尊敬語 / 謙譲語の 1 行 = 1 動詞、10 行で完結する table を 1 つ置く。`keigo-cheat-sheet` には類似表があるが「両形を並べる」という見せ方は本記事の専用。
- **内/外反転ミニ対話（0/10 gap）。** 「自社内で『部長は今出ています』と取引先に電話で言う」場面をフル対話 8 行で展開し、内/外がどこで切り替わるかを step-by-step 注釈で示す。`keigo-examples` のフル対話と相互参照（あちらは 5 場面、こちらは 1 場面集中の深掘り）。
- **5 wrong→right ペア + 1 行理由（0/10 gap）。** `部長が参られました` / `お客様が申されました` など 5 件を `✗ → ◯ → 理由` で並べ、深掘り解説は `keigo-mistakes` に動線。
- **謙譲語 I vs II（丁重語）の 1 段落整理（0/10 gap）。** `mairu` と `mousu` の使い分けを 1 段落で線引きする PAA snippet 候補。
- **読 vs 書/話の分離（0/10 gap）。** 「聞いて分かれば良い」(認識) と「自分で言えるべき」(産出) を 2 列で分け、学習負荷を約半分に圧縮するフレーム提示。

### EN

- **A/B/C politeness framework × subject axis as a second dimension.** Reuse the A/B/C framework already established across `keigo-guide` / `keigo-cheat-sheet` / `keigo-examples`. In this article, the C row splits vertically into "subject = other → sonkeigo column" and "subject = self → kenjougo column." Keeps cluster-wide framework consistency while answering the comparison query head-on.
- **"Who's the subject?" 3-second decision flow (0/10 gap).** Place a 3-step decision card right after the intro (subject = other or self → uchi/soto → verb). Write it as a 40–60-word featured-snippet target paragraph.
- **Top 10 verbs in one 4-column table (0/10 gap).** Verb / teineigo / sonkeigo / kenjougo, one row per verb, 10 rows total. `keigo-cheat-sheet` has a similar table but never side-by-sides both forms — that's this article's signature.
- **Uchi-soto inversion mini-dialogue (0/10 gap).** Build the "answering the phone for your boss to an external client — '部長は今出ています'" scene as a full 8-line dialogue with step-by-step annotation of where keigo flips. Cross-reference with `keigo-examples` (their five scenes, our one-scene deep dive).
- **5 wrong→right pairs + one-line reason (0/10 gap).** `Buchou ga mairaremashita` / `Okyakusama ga moushimashita`-class errors in a `✗ → ◯ → reason` table; full diagnoses live in `keigo-mistakes`.
- **Kenjougo I vs II (teichougo) in one paragraph (0/10 gap).** A single clean paragraph parsing `mairu` vs `mousu` — the standing PAA question no one has answered.
- **Read-vs-produce split (0/10 gap).** A two-column table separating "recognize when heard" from "produce when speaking," cutting effective vocab load roughly in half.

---

## 6. primary_info_seeds

> Hypotheses for primary information (original data, first-hand experience, expert quotes) to layer on top of the article over time. 3 hypotheses, all `not_started`.

1. **Subject-detection drill error log**
   - _What:_ Have 15–20 non-native learners complete a 15-item fill-in drill where each item is a short scene + a verb in plain form; they must pick (a) "who's the subject?" and (b) "sonkeigo or kenjougo." Tabulate which step fails most — verb retrieval, subject mis-identification, or uchi-soto handling.
   - _How:_ Google Form distributed via Discord JLPT communities + Reddit r/LearnJapanese + LinkedIn networking. Optional follow-up 5-min Zoom on 3 respondents who scored lowest.
   - _Cost:_ ~6h (instrument design 2h + recruit 1h + analysis 3h)
   - _Status:_ `not_started`

2. **Manager-side cringe interview**
   - _What:_ Ask 5 Japanese senpai / hiring managers (mix of HR + line managers): "Of all the sonkeigo-vs-kenjougo mistakes you've heard from non-native juniors, which one is hardest to mentally un-hear when evaluating that person?" One-quote-per-respondent for `<aside>` placement in the wrong→right section.
   - _How:_ 30-min interviews via author's existing network. Anonymize to "(HR manager, 8 yrs)" style attribution.
   - _Cost:_ ~5h (5 × 30-min interview + 2h transcription/anonymization)
   - _Status:_ `not_started`

3. **Top 10 verb usage frequency self-log**
   - _What:_ Over 14 days log every observed in-office use of the 10 candidate verbs (`iku` / `kuru` / `iru` / `iu` / `taberu` / `miru` / `kiku` / `suru` / `shitteiru` / `au`) — both own production and others' speech, tagged sonkeigo / kenjougo / teineigo. Use raw counts to rank "memorize-first" priority and validate or revise the Top-10 list before locking the article table.
   - _How:_ Notion / Apple Notes tally with timestamp + verb + form + channel (Slack / call / face-to-face).
   - _Cost:_ ~6h (1 setup + 14 × 15-min daily logging + 2h tally/analysis)
   - _Status:_ `not_started`

---

## 7. Target Article Outline

> The final outline for OUR article. Derived from §3–§5.

### JA outline (target)

1. H1: _尊敬語と謙譲語の違い｜「主語は誰？」で 3 秒判断する完全ガイド_
2. H2: この記事を読むべき人
3. H2: 1 文サマリ（featured snippet 用 40–60 字）
4. H2: 「主語は誰？」3 秒判断フロー（decision card）
   - H3: ステップ 1 — 主語は相手か自分か
   - H3: ステップ 2 — 相手は内 / 外のどちらか
   - H3: ステップ 3 — 動詞を選ぶ
5. H2: 60 秒復習 — A/B/C フレームと主語軸の関係
   - H3: A/B 行 = 主語に関わらず teineigo
   - H3: C 行 = 主語＝他者 → sonkeigo / 主語＝自分 → kenjougo
6. H2: 頻出 10 動詞の 4 列対照表
   - H3: 表の見方（teineigo / sonkeigo / kenjougo 列）
   - H3: 10 動詞表（行 = `iku` `kuru` `iru` `iu` `taberu` `miru` `kiku` `suru` `shitteiru` `au`）
   - H3: 表に出ない動詞は `o-...-ni-naru` / `o-...-suru` で作る
7. H2: 「自社の上司を社外に話す」内/外反転ミニ対話
   - H3: 対話 8 行（取引先からの電話を取る場面）
   - H3: どこで内/外が反転するか（行ごと注釈）
   - H3: 同じ内容を社内会議で話したらどう変わるか
8. H2: よくある 5 つの誤用（wrong → right）
   - H3: ✗ 部長が参られました → ◯ 部長がいらっしゃいました
   - H3: ✗ お客様が申されました → ◯ お客様がおっしゃいました
   - H3: ✗ 私が召し上がります → ◯ 私がいただきます
   - H3: ✗ 部長がご覧になられました → ◯ 部長がご覧になりました（二重敬語）
   - H3: ✗ お客様にお伺いします → ◯ お客様にお尋ねします（謙譲先の不一致）
9. H2: PAA 直撃 — 謙譲語 I と II（丁重語）の違い
10. H2: 学習負荷を半分にする「読 vs 話す」の分離
    - H3: 認識さえできれば良い動詞（受け身モード）
    - H3: 自分の口でも言うべき動詞（産出モード）
11. H2: よくある質問（FAQ）
    - H3: 尊敬語と謙譲語は同じ文に混ぜていい？
    - H3: 尊敬語と謙譲語、覚えるならどちらが先？
    - H3: 友だち相手にも使う？
    - H3: 「お / ご」はどちらに付く？
    - H3: いつまで覚え続ければ業務で困らなくなる？
12. H2: 次に読むべき関連記事
    - keigo-guide（pillar）
    - keigo-cheat-sheet（一覧表）
    - keigo-examples（フル対話）
    - keigo-mistakes（誤用の深掘り）
    - best-way-to-learn-keigo（学習ロードマップ）
13. H2: 業務でそのまま使えるフレーズ集 → Essential 30 PDF CTA

### EN outline (target)

1. H1: _Sonkeigo vs Kenjougo: The "Who's the Subject?" Test That Settles It in 3 Seconds_
2. H2: Who this guide is for
3. H2: One-sentence answer (featured-snippet target, 40–60 words)
4. H2: The "who's the subject?" 3-second decision flow
   - H3: Step 1 — Is the subject the other person or you?
   - H3: Step 2 — Is that person *uchi* (in-group) or *soto* (out-group)?
   - H3: Step 3 — Pick the verb
5. H2: 60-second refresher — the A/B/C frame and the subject axis
   - H3: A and B rows = teineigo regardless of subject
   - H3: C row splits — subject = other → sonkeigo / subject = self → kenjougo
6. H2: Top 10 verbs side by side (4-column reference table)
   - H3: How to read the table (teineigo / sonkeigo / kenjougo columns)
   - H3: The 10 verbs (`iku` `kuru` `iru` `iu` `taberu` `miru` `kiku` `suru` `shitteiru` `au`)
   - H3: Verbs that don't have special forms — build with *o-...-ni-naru* / *o-...-suru*
7. H2: The uchi-soto inversion in action — talking about your boss to an external client
   - H3: 8-line dialogue (answering the phone from a client)
   - H3: Where keigo flips, line by line
   - H3: Same content inside a team meeting — what changes?
8. H2: 5 common wrong → right swaps
   - H3: ✗ *Buchou ga mairaremashita* → ◯ *Buchou ga irasshaimashita*
   - H3: ✗ *Okyakusama ga moushimashita* → ◯ *Okyakusama ga osshaimashita*
   - H3: ✗ *Watashi ga meshiagarimasu* → ◯ *Watashi ga itadakimasu*
   - H3: ✗ *Buchou ga goran ni nararemashita* → ◯ *Buchou ga goran ni narimashita* (double honorific)
   - H3: ✗ *Okyakusama ni o-ukagai shimasu* → ◯ *Okyakusama ni o-tazune shimasu* (humbled-target mismatch)
9. H2: PAA quick hit — kenjougo I vs II (teichougo / 丁重語)
10. H2: Halve your study load — recognize vs produce
    - H3: Verbs you only need to recognize (receptive)
    - H3: Verbs you actually need to produce (active)
11. H2: Frequently asked questions
    - H3: Can I mix sonkeigo and kenjougo in the same sentence?
    - H3: If I have to memorize one first, which?
    - H3: Do I use either with friends?
    - H3: Does *o-* / *go-* attach to sonkeigo or kenjougo?
    - H3: How long until I stop second-guessing at work?
12. H2: Related deep-dives in the keigo cluster
    - keigo-guide (pillar)
    - keigo-cheat-sheet (lookup tables)
    - keigo-examples (full dialogues)
    - keigo-mistakes (error catalogue)
    - best-way-to-learn-keigo (study roadmap)
13. H2: Office-ready phrases you can paste tomorrow → Essential 30 PDF CTA

---

## 8. FAQ / People Also Ask

> Questions to answer in the article. Map each to a section or a dedicated FAQ block.

| Question | Where answered |
|---|---|
| What is the difference between sonkeigo and kenjougo? | §3 (one-sentence answer) + §4 (decision flow) |
| When do you use kenjougo? | §4 Step 1 (subject = self) + §6 (table kenjougo column) |
| Is sonkeigo more polite than kenjougo? | §10 FAQ "If I have to memorize one first, which?" |
| Can you mix sonkeigo and kenjougo in the same sentence? | §10 FAQ "Can I mix..." |
| What are examples of kenjougo verbs? | §6 (10-verb table kenjougo column) + §7 dialogue |
| How do you know when to use sonkeigo? | §4 (decision flow) |
| What is kenjougo I vs kenjougo II / teichougo? | §9 (dedicated PAA snippet) |
| Do Japanese people actually use kenjougo every day? | §10 FAQ "How long until..." (implicit answer: yes, in business) |
| Does *o-* / *go-* attach to sonkeigo or kenjougo? | §10 FAQ "Does *o-* / *go-*..." |

---

## 9. Internal Links

### Upstream (pillars / hubs linking to this article)
- `keigo-guide` (pillar) — add a "Going deeper on sonkeigo vs kenjougo? Read [this]" inline link from the existing "The 3 types of keigo" section.

### Downstream (articles this article links to)
- `keigo-cheat-sheet` — for the full verb-conjugation lookup tables beyond the Top 10.
- `keigo-examples` — for full multi-scene dialogues (this article does one deep-dive scene; that one does five).
- `keigo-mistakes` — for the full diagnosis of each wrong→right pair.
- `best-way-to-learn-keigo` — for the 90-day study roadmap once readers know what they need to learn.

### Sibling cluster articles
- `polite-japanese-phrases-for-office` — chronological-day phrasebook; complementary not overlapping.
- `business-email-template`, `how-to-write-japanese-business-email` — where sonkeigo/kenjougo choice has direct business email impact.
- `japanese-business-phrases-pdf` — scenario × A/B/C matrix for paste-ready phrases.

---

## 10. Localization Notes

> Heads-up for language-diff specs. Flag items that are likely to behave differently in non-English SERPs.

- **Terminology:** *sonkeigo* / *kenjougo* / *teineigo* / *teichougo* / *bikago* all stay romanized with kanji in parentheses on first mention; subsequent mentions italicized romaji only. JA version uses 尊敬語 / 謙譲語 / 丁寧語 / 丁重語 / 美化語 directly without romaji.
- **Cultural assumptions:** EN persona assumes a JLPT N3–N2 non-native in a Japanese-language workplace. JA persona assumes either a Japanese native who wants to nail the boundary for client-facing work, or a returning non-native who has internalized teineigo but blanks on the C row. The "talking-about-my-boss-to-client" inversion case applies to both audiences with identical mechanics.
- **Competitor landscape:** The JA SERP for `尊敬語 謙譲語 違い` is likely dominated by goo-/biglobe-style dictionary sites + benesse / nikkei / mynavi business-Japanese explainers (different from the EN SERP studied here). When localizing JA, **`seo-article-localize` should be run** before drafting JA — this article is one of the rarer cases where JA + EN SERPs are likely to diverge meaningfully (unlike `business-email-template` / `japanese-business-phrases-pdf` which used a single EN-rooted spec).
- **Language-specific risks:** The 3-second decision flow names "subject" — in JA the subject is grammatically often omitted, so the JA version should reframe Step 1 as 「動作主は誰か」(who performs the action) rather than 「主語は誰か」 to avoid the missing-subject confusion that natives experience differently from non-natives. The "Verbs that don't have special forms — use *o-...-ni-naru* / *o-...-suru*" section is mechanically identical across languages.
- **Phase 2 languages (vi / id / pt / th / zh-TW):** Defer per ROADMAP P2. When triggered, expect significant SERP divergence — keigo as a concept has minimal direct competitor coverage in vi / id / th, and `seo-article-localize` will likely return "spec rewrite required."

---

## 11. Change Log

| Date | Change | Author |
|---|---|---|
| 2026-05-18 | Initial spec generated via `seo-article-outline` skill. 10/10 SERP fetched cleanly. Locked the differentiation around (a) the "who's the subject?" 3-step decision flow, (b) the 10-verb 4-column comparison table, (c) the uchi-soto inversion mini-dialogue, (d) the 5 wrong→right swap pairs, (e) the kenjougo I vs II PAA snippet, (f) the read-vs-produce split — six zero-coverage SERP gaps, all addressable. Reused the A/B/C politeness framework from `keigo-guide` as the cluster-consistency thread. Flagged in §10: this is one of the rarer articles where running `seo-article-localize` before JA drafting is recommended (JA SERP likely diverges from EN, unlike `business-email-template`). | seo-article-outline (Claude Opus 4.7) |
| 2026-05-18 | **両言語 publish flip — `status: drafting → published`**. ユーザー approve（JA v1 + EN v1 ともに「修正なし」）→ base spec `status: drafting → published`、`languages.en.status: drafting → published`、`languages.ja.status: drafting → published` を一括 flip。ROADMAP Live articles 表に ✅ published として登録予定。mdx 両ファイルは `draft: false` 設定済のため、git push で Cloudflare Pages auto-build → 反映予定。**Phase 2 keigo cluster の比較クエリ深掘り記事として live**：pillar `keigo-guide` の下、`keigo-cheat-sheet` / `keigo-examples` / `keigo-mistakes` / `best-way-to-learn-keigo` / `polite-japanese-phrases-for-office` と並ぶ 6 番目の keigo sibling（`japanese-honorifics-chart` #15 が未 publish のため、本記事が #13 として keigo cluster の 7 記事目 live）。次：git commit (`feat: ship sonkeigo-vs-kenjougo article (JA + EN)`) → push → GSC URL 検査 + インデックス登録リクエスト 2 URL（ja/en）。 | ryoooue (publish trigger) + Claude Opus 4.7 |
| 2026-05-18 | **EN v1 shipped**. Body at `src/data/guides/en/sonkeigo-vs-kenjougo.mdx` (~4,400 words)。Base spec §7 EN outline を 1:1 実装：title "Sonkeigo vs Kenjougo: The 3-Second 'Who's the Subject?' Test" (60 chars、KW 完全一致 + benefit promise + `feedback_en_title_article.md` の "The + singular methodology noun" ルール準拠 = "The Test")。en-article-style ルール A1–D7 全準拠：em-dash + spaces / en-dash for ranges (N3–N2 / Day 1–30) / Oxford comma / sentence-case H2/H3 / italic *romaji* + (kanji) on first use / Hepburn macrons (ō/ū) / 40–60-word featured-snippet target 段落（intro "The fastest way to settle..."）/ 3 persona bullets / 4-sentence paragraph cap / FAQ 5 H3 PAA-aligned / descriptive anchors。Linter: 0 auto-fixes、2 件 weak-qualifier 手動修正（"actually" in H2「The 10 verbs you'll actually use」→「you'll use most」/ "just" in PAA section「If you're just being formal」→「If you're being formal ... with no specific recipient being elevated」）。2 回目 idempotent pass。`pnpm build` green at **31 pages indexed** (前回 28 → +3 EN ja-mirror routes), **9,468 words indexed**。`languages.en.status: planned → drafting` flip。**EN は 10 動詞テーブル維持**（JA 版は 20 行に拡張する delta 適用、EN 版は base spec の 10 動詞で en-SERP-rooted のままが正解 — Talkpal が 3/10 で部分実装した形式に対し、本記事は完全実装で勝負）。**EN ペルソナ 3 件**（JA は 4 ペルソナに拡張する delta 適用、EN は base spec の N3-N2 非ネイティブ単独ターゲットを維持）。FAQ 5 件（JA は 6 件で「させていただく」delta 追加、EN は base spec の 5 件を維持 — *o-/go-* 質問が EN ペルソナにとってより核心的なため）。両言語とも `status: drafting`（未 publish）。**次：人間レビュー** → 必要なら EN v2 → publish flip 両言語。 | Claude Opus 4.7 + ryoooue |
| 2026-05-18 | **JA v1 shipped**. Body at `src/data/guides/ja/sonkeigo-vs-kenjougo.mdx` (約14,300字含frontmatter+FAQ)。Base spec §7 JA outline + diff spec §7 7 deltas を 1:1 実装：title「動作主は誰？」+「使い分け一覧つき」採用 (39字)、4 ペルソナ (外国人ビジネスパーソン + 日本人若手 + 帰国子女 + keigo-guide 既読者)、結論 1 文（featured snippet target）、3 ステップ判断フロー（動作主→ウチ／ソト→動詞）、60 秒復習で段階別 A/B/C × 動作主軸の交差解説（A/B = 丁寧語領域、C = sonkeigo/kenjougo 縦割り）、20 動詞 4 列対照表（10→20 拡張 delta 実装、keigo-cheat-sheet への明示動線）、ウチ／ソト反転 8 行コードブロック対話（取引先電話）+ 行ごと注釈 + 社内会議対比、5 誤用を「動作主取り違え 3 + 二重敬語 2」の 2 ブロック化（delta 実装）、謙譲語 I/II 章で文化庁『敬語の指針』(2007) を 1 文引用 (delta 実装)、新規 H2「シーン別早見表」追加（メール/電話/接客/社内会議 × sibling 動線、delta 実装）、受信時／発信時分離（読 vs 話す）、FAQ 6 件（5 件 + 「させていただく」delta 実装）、関連記事 6 sibling + Essential 30 CTA。`ja-article-style` linter: 1 回目で auto-fix 適用（`**...**`→`<strong>` の CommonMark flanking rules 修正、`A/B/C` 表記の半角空白除去）、2 回目で idempotent pass。`pnpm build` green at **28 pages indexed**（前回 24 → +4 ja/en/index/sitemap）、**8,926 words indexed**。`languages.ja.status: planned → drafting` に flip。**次：人間レビュー** → JA v2 if needed → EN v1（EN は base spec のみで進行、`seo-article-localize` 不要）。 | Claude Opus 4.7 + ryoooue |
| 2026-05-18 | Ran `seo-article-localize` for `ja`: **diff NEEDED** (base coverage 50% [4/8 H2 ≥5/9], 3 JA-unique additions). Strategy = Option A (base + deltas). 7 specific deltas captured in diff spec: title rewrite (動作主 + 一覧つき), 動詞表 expand 10→20, 「ウチ／ソト」表記化, 5 誤用を「動作主取り違え 3 + 二重敬語 2」の 2 ブロック化, 謙譲語 I/II 章で文化庁指針引用, 新規 H2「シーン別早見表」追加, FAQ +「させていただく」1 件。Diff spec: `specs/articles/sonkeigo-vs-kenjougo.ja.spec.md`. Base spec `languages.ja.diff_spec` を更新。`languages.ja.status` は `planned` のまま（JA v1 ドラフト着手で `drafting` に flip 予定）。EN は base spec のみで進行可（en SERP = base spec の SERP captured と同一）。 | seo-article-localize (Claude Opus 4.7) |
