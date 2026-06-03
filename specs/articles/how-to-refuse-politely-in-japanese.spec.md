---
# === IDENTIFICATION ===
slug: "how-to-refuse-politely-in-japanese"
collection: "guides"
cluster: "keigo"
pillar: "keigo-guide"                     # child of keigo-guide; the refusal-specific speech-act companion that pairs with how-to-say-sorry-in-japanese-politely (the apology sibling) and sits alongside keigo-mistakes (pitfalls), keigo-examples (worked examples), keigo-cheat-sheet (lookup), polite-japanese-phrases-for-office (first-week phrases), japanese-business-phrases-pdf (pasteable reference)

# === SEO ===
target_keyword: "how to refuse politely in Japanese"
serp_language: "en"
target_intent: "informational"            # Searcher wants a how-to for a specific speech-act (refuse/decline), not a vocabulary list — the "politely" modifier flags they want register + indirectness guidance, not 8 random "no" words.
search_volume_estimate: null
difficulty_estimate: "medium"             # SERP is full of substantive "N ways to say no" guides; ranking requires a real differentiator (scenario matrix + decode-the-soft-no), not just one more phrase list.

# === FUNNEL ===
funnel_stage: "TOFU"
product_cta: "essential-30"               # 30-phrase reference card includes refusal-tier phrases (kekkou desu / o-kotowari shimasu); natural CTA from "I need a pasteable polite refusal right now".
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
    diff_spec: "specs/articles/how-to-refuse-politely-in-japanese.ja.spec.md"

# === LIFECYCLE ===
status: "published"
created: "2026-06-03"
last_serp_audit: "2026-06-03"
---

# articleSpec: How to Refuse Politely in Japanese

> **How to use this file**
> - The `seo-article-outline` skill generates the initial version.
> - Humans review and refine the "Our Differentiation" and "primary_info_seeds" sections.
> - When SERP changes significantly, re-run the skill to refresh sections 2–4.
> - Do NOT delete the spec after publication — it's the source of truth for updates.

---

## 1. Target & Intent

### JA

**主要な検索意図:** 「how to refuse politely in Japanese」を検索するユーザーは、単語リストではなく **「いま自分が直面している依頼・誘いを、相手との関係を壊さずに断る正しい言い方」** を求めている。修飾語 *politely* が示すのは「英語感覚で直接 No と言うと角が立つのは分かっているが、日本語ではどこまで遠回しにすべきか、どの語彙を選べば失礼にならないかが分からない」という不安。検索する瞬間は (a) 上司・先輩から飲み会／残業に誘われた直後、(b) 取引先の提案・営業を断るメールを書く前、(c) 同僚や友人の頼みを断りたいが言い出せない、のいずれかが多い。

**読者ペルソナ:** 日本在住または日本企業勤務の非ネイティブ社会人（20代後半〜40代、JLPT N4〜N2 相当）。「いいえ＝iie」は知っているが、それを実際に使うと冷たすぎると気づいており、かといって *ちょっと…* で本当に伝わるのか確信が持てない。外資の日本オフィス勤務、日本人クライアントと働くエンジニア、留学生インターン、SaaS の CS 担当などが典型。

**成功基準:** 読者が記事を読み終えた直後に以下のいずれかが達成できる：
1. 自分のいまの場面を **A/B/C × 場面マトリクス** の 1 セルに当てはめて、コピペできる完成文を 1 つ確保できる。
2. 「直接断ってよい場面か、遠回しにすべき場面か」を判定する **直接度ルーブリック** を理解できる。
3. 断りの **解剖図**（クッション → 感謝 → 断り＋理由 → 代替案／含み → 締め）を頭に持ち、単発フレーズでなく一連の応答として組み立てられる。
4. 逆方向、つまり **「相手の遠回しな No を見抜く」**（検討します／難しいですね／ちょっと…＝事実上の断り）力を得て、押し続けて失礼になる事故を避けられる。

### EN

**Primary search intent:** Users searching "how to refuse politely in Japanese" are not collecting vocabulary — they want *the right way to turn down a specific request or invitation in front of them without damaging the relationship*. The modifier **politely** signals they already sense that a blunt *iie* lands cold, but they are unsure how indirect Japanese expects them to be, or which register avoids offense. The moment of search is usually one of three: (a) right after a senior invites them to *nomikai* or asks for overtime, (b) before writing an email that declines a vendor pitch or client request, (c) wanting to decline a peer's favor but unable to find the words.

**Audience persona:** Non-native professional working in or with Japan (late 20s to early 40s, JLPT N4–N2). They know *iie* but have realized that using it sounds too cold, yet they are not confident a trailing *chotto…* actually communicates the refusal. Typical roles: foreign-affiliated office employee, engineer working with Japanese clients, intern at a Japanese company, SaaS customer success rep.

**Success criteria:** After reading, the reader should be able to:
1. Locate their current situation in our **A/B/C × scenario matrix** and copy one paste-ready refusal line.
2. Apply our **directness rubric** to decide whether they may decline plainly or must soften and go indirect.
3. Hold the **anatomy of a polite refusal** in their head (cushion → appreciation → refusal + reason → alternative / door-open → close) so the phrase lands inside a complete response, not floating in isolation.
4. Run the reverse skill — **decode a soft Japanese "no"** (*kentou shimasu* / *muzukashii desu ne* / a trailing *chotto…* are de-facto refusals) — so they stop pushing past a polite decline and causing offense.

---

## 2. SERP Analysis (Top 10)

> Captured on: 2026-06-03. Search engine: Google. Locale: en-US.
> Coverage denominators in this spec are always `/10` (out of top 10 competitors).
> 8/10 outlines fetched successfully. jobsinjapan.com returned HTTP 403; position retained as anchor. howtosayguide.com listed as a thin SEO-template anchor (not fetched — pattern-known low-content).

| # | URL | Domain | Title | Format | Word Count | Notes |
|---|---|---|---|---|---|---|
| 1 | https://cotoacademy.com/saying-no-japanese-polite-way-decline-refuse-offers/ | cotoacademy.com | No in Japanese: Politely Declining or Refusing Offers in Japanese | numbered list | medium 1500–3000 | 10 phrases iie→tabun with formality notes; cultural framing; weak on which phrases combine in a real sequence |
| 2 | https://jobsinjapan.com/living-in-japan-guide/how-to-politely-say-no-in-japanese/ | jobsinjapan.com | How to Politely Say No in Japanese | (403) | — | WebFetch blocked; position anchor only |
| 3 | https://migaku.com/blog/japanese/no-in-japanese | migaku.com | Japanese Refusal Guide: The Art of Saying No Politely | guide + vocab tables | medium 1500–3000 | Direct vs. indirect split; pivots into promo for paid academy; pedagogically thin at the tail |
| 4 | https://www.likejapan.com/en/life/say-no/ | likejapan.com | Japanese never say "No"? 5 ways to reject someone politely in Japanese | list | short <1500 | 5 ambiguous expressions (chotto / uun / kekkou / daijoubu / ii desu) with conversation pairs; no hierarchy guidance |
| 5 | https://www.valiantjapanese.jp/blog/how-to-say-no-or-to-refuse-in-japanese/ | valiantjapanese.jp | How to say NO or to Refuse in Japanese | grammar reference | short <1500 | 9 phrases across formality levels with context notes; no cultural nuance, no scenarios |
| 6 | https://www.daijob.com/en/guide/skill-up/saying-no-in-japan-how-to-decline-soemthing-respectfully/ | daijob.com | Saying No in Japan: how to decline something respectfully | guide + scenarios | medium 1500–3000 | **Strongest business comp.** 6 indirect strategies, 3 worked scenarios, AND a "how to understand you are being declined" section (rare reverse-direction angle) |
| 7 | https://lingopie.com/blog/no-in-japanese/ | lingopie.com | No In Japanese: 5 Easy To Politely Refuse In Japanese | practical guide | medium 1500–3000 | 5 phrases + regional differences (Kansai/Tohoku/Kyushu) + cultural context; heavy promo integration |
| 8 | https://blog.gaijinpot.com/how-to-say-no-in-japan/ | gaijinpot.com | How To Say No In Japan | first-person guide | medium 1500–3000 | Personal-experience voice; explains the cultural reasoning well; leans on "white lies" rather than authentic alternatives |
| 9 | https://www.tomo-japanese.com/single-post/how-to-decline-an-invitation-from-your-boss-or-senpai | tomo-japanese.com | How to decline an invitation from your Boss or Senpai? | guide + cultural commentary | short <1500 | Narrow but on-target: declining a senior's invitation; stresses gratitude-when-declining; no broader scenarios or written examples |
| 10 | https://howtosayguide.com/how-to-say-i-decline-in-japanese/ | howtosayguide.com | How to Say "I Decline" in Japanese | thin SEO template | short <1500 | Position anchor; templated low-content "how to say X" page, not a substantive guide |

### SERP features present
- [ ] Featured snippet (none observed; opportunity)
- [x] People Also Ask (PAA)
- [ ] Video carousel
- [ ] Image pack
- [ ] Knowledge panel
- [x] Related searches

### Related searches / PAA questions
- How do you say "no" politely in Japanese?
- Why don't Japanese people say no directly?
- What does *chotto* mean as a refusal?
- How do you decline an invitation in Japanese?
- How to say "no thank you" in Japanese (*kekkou desu* vs *daijoubu desu*)?
- How do you refuse a request from your boss in Japanese?
- What does *kentou shimasu* (検討します) really mean?
- How to politely decline in a Japanese business email?

---

## 3. Merged Outline (from Top 10)

> All distinct headings found across the top 10, with coverage count.
> Coverage = how many of top 10 articles have a section matching this heading (jobsinjapan 403 + howtosayguide thin → conservatively excluded from tallies; true denominator ≈ 8/10).

| Heading | Coverage (x/10) | Notes |
|---|---|---|
| Cultural context — why Japanese avoid a direct "no" (*wa*, harmony, indirectness) | 8/10 | Table stakes; almost every competitor front-loads this |
| Soft-deflection — *chotto…* (trailing, intentionally incomplete) | 8/10 | Table stakes; the single most-taught refusal device |
| "No thank you" offers — *kekkou desu* / *daijoubu desu* / *ii desu* | 7/10 | Table stakes; must disambiguate (these confuse learners constantly) |
| Direct "no" words — *iie* / *ie* / *iya* / *uun* + when each is OK | 7/10 | Table stakes; must include with register warnings |
| Expressing difficulty/impossibility — *muzukashii desu* / *kibishii desu* | 5/10 | Common; should include in the indirect ladder |
| Indirect strategies catalog (vagueness, blame external, offer alternative, change subject) | 4/10 | Common; daijob is the fullest; we systematize it |
| Business / formal refusals — *o-kotowari shimasu* / *miokurasete kudasai* | 4/10 | Strong signal; under-served at the formal C tier |
| Declining an invitation from a senior (boss / senpai) | 3/10 | Valuable; only tomo-japanese centers it |
| Gratitude-first framing (thank before you decline) | 3/10 | Strong signal; we make it a structural step, not a tip |
| Regional variation (Kansai/Tohoku etc.) | 1/10 | Rare (lingopie only); low priority, brief mention at most |
| "How to tell you are being refused" — decode the soft no | 2/10 | **Big opportunity**; only daijob (+ partial gaijinpot) covers the reverse direction |
| *Kentou shimasu* / *kangaete okimasu* as de-facto "no" | 2/10 | Under-explained; high search interest; we make it explicit |
| A/B/C politeness × scenario matrix (paste-ready table) | 0/10 | **Zero-coverage** |
| Directness rubric — when you may be plain vs. must go indirect | 0/10 | **Zero-coverage** |
| Anatomy of a refusal (cushion → appreciation → refusal+reason → alternative → close) | 0/10 | **Zero-coverage** |
| Full refusal email/chat templates (decline meeting / vendor offer / extra scope / invitation) | 0/10 | **Zero-coverage** (1/10 has a stray formal email phrase, no template) |
| Self-diagnostic / decision tree to pick directness + tier | 0/10 | **Zero-coverage** |
| Refusal-specific mistakes non-natives make (blunt iie, over-chotto, ghosting, fake-yes) | 0/10 | **Zero-coverage** (general keigo mistakes exist, not refusal-specific) |
| *Uchi-soto* + seniority dual axis applied to refusal choice | 0/10 | **Zero-coverage** |

**Core (≥5/10):** 5 headings — politeness must surface them all.
**Rare but valuable (1–4/10):** 7 headings — adopt selectively (decode-the-soft-no and senior-invite are the highest-value).
**Zero-coverage gaps:** 7 headings — these are our differentiation surface.

---

## 4. Content Gaps

### JA

1. **A/B/C × 場面マトリクス（0/10）** — どの場面でどの語彙レベルで断るかを、コピペ可能な完成文と共に 1 表に並べた競合はゼロ。競合は「フォーマル順に N 種類」のフラットリストで、読者は「飲み会の誘いと取引先の提案を、自分はどう断ればいいのか」を場面起点で引けない。
2. **直接度ルーブリック（0/10）** — 「日本語では直接 No と言わない」とは全員書くが、**いつなら直接断ってよく、いつ遠回しが必須か** の判定基準を渡す競合がいない。相手（社内/社外・上下）、依頼の性質（業務/私的）、繰り返しか否か、で直接度を自己判定できる軸が必要。
3. **断りの解剖図（0/10）** — 丁寧な断りは単一フレーズではなく **クッション → 感謝 → 断り＋理由 → 代替案／含み → 締め** の連続応答。特に「感謝を先に置く」「最後に含み（またの機会に）を残す」の 2 ステップを構造として明示した競合はない。
4. **断りメール完成形（0/10）** — 会議辞退・営業/提案辞退・追加スコープの辞退・誘いの辞退など、頻出パターンごとの **コピペ可能な雛形**（件名→本文→署名）を備えた競合はゼロ。
5. **遠回しの No を見抜く（2/10 部分実装）** — daijob が一部触れるのみ。*検討します／難しいですね／ちょっと…＋沈黙* が事実上の断りであることを **逆引き** で教えるパートは、押し続けて失礼になる非ネイティブ事故を直接防ぐ。
6. **断り特化のミスカタログ（0/10）** — 「いきなり iie で冷たく聞こえる」「*ちょっと* を多用しすぎて伝わらない」「断りづらくて既読スルー（ゴースト）して関係を悪化」「*検討します* を社交辞令で言って相手に期待させる」など、断り**固有**の失敗を集めた競合はない。`keigo-mistakes` は keigo 全般、本記事は断りに絞れる。

### EN

1. **A/B/C × scenario matrix (0/10)** — No competitor offers a single paste-ready table where the reader locates their situation (drink invite / extra-work request / vendor pitch / favor / meeting request, etc.) on one axis and the politeness tier on the other. Competitors give flat "N ways ranked by formality" lists; readers cannot look up by *situation*.
2. **Directness rubric (0/10)** — Everyone writes "Japanese don't say no directly," but nobody hands the reader a rule for *when a plain decline is fine vs. when indirectness is mandatory*. We can score it on recipient (internal/external, senior/peer), nature of the ask (work/personal), and repeat-vs-first-time.
3. **Anatomy of a polite refusal (0/10)** — A polite refusal is not one phrase but a sequence: cushion → appreciation → refusal + reason → alternative / door-open → close. In particular, "thank *before* you decline" and "leave a door open at the end" are structural steps no competitor names as structure.
4. **Refusal email/chat templates (0/10)** — No competitor ships paste-ready templates (subject → body → sign-off) for the highest-frequency written refusals: declining a meeting, declining a vendor/sales offer, declining extra scope, declining an invitation in writing.
5. **Decode the soft "no" (2/10 partial)** — Only daijob partially covers the reverse direction. Teaching that *kentou shimasu* / *muzukashii desu ne* / a trailing *chotto…* are de-facto refusals — as a lookup — directly prevents the non-native failure of pushing past a polite decline.
6. **Refusal-specific mistake catalog (0/10)** — "Blunt *iie* sounds cold," "over-using *chotto* so the message never lands," "ghosting because declining felt hard, which worsens the relationship," "saying *kentou shimasu* as a social nicety and leaving the other side hoping." `keigo-mistakes` covers keigo broadly; this article drills into refusal-specific traps.

---

## 5. Our Differentiation

### JA

- **A/B/C politeness フレームを断りに適用** — 既存の `keigo-guide` (A: 友達・部活、B: 同僚・初対面、C: 上司・取引先) を 8 場面（飲み会/誘いの辞退・残業/追加依頼の辞退・取引先の提案/営業の辞退・会議招集の辞退・同僚の頼み事の辞退・食事/飲み物の勧めの辞退・締切前倒し依頼の辞退・慣習/参加の辞退）にマッピング → **24 セル × コピペ完成文**。`how-to-say-sorry-in-japanese-politely`（謝罪の姉妹記事）と同じマトリクス構造を採り、speech-act シリーズとして読者の頭に一貫したメンタルモデルを刻む。
- **直接度ルーブリック** — 4 軸（相手は社内/社外 / 相手は目上か / 依頼は業務か私的か / 初回か繰り返しか）で「直接 OK／要クッション／要全力遠回し」の 3 段階を判定。「日本語＝とにかく遠回し」という過剰一般化を解き、直接でよい場面（社内・対等・私的な軽い誘い等）も正しく示す。
- **断りの解剖図（5 部構成）** — 1. クッション（せっかくですが／あいにく／申し訳ないのですが）/ 2. 感謝（お誘いありがとうございます／ありがたいお話ですが）/ 3. 断り＋理由（語彙レベル A/B/C、理由は 1 文・言い訳にしない）/ 4. 代替案 or 含み（またの機会に／次回はぜひ）/ 5. 締め（よろしくお願いします）。各部に **悪い例 → 良い例** ペアを付け、特に「感謝を断りの前に置く」「含みで終える」の 2 ステップが誠意を生むことを前後比較で見せる。
- **断りメール完成形 4 雛形** — (a) 会議辞退（最頻出・社内/社外両用）/ (b) 取引先の提案・営業辞退（最重要、`business-email-template` と相互リンク）/ (c) 追加スコープ/依頼の辞退（プロジェクト境界）/ (d) 誘いの書面辞退（飲み会/イベント）。各雛形に件名・本文・署名まで full、`how-to-write-japanese-business-email` の 8 ステップに沿わせる。
- **遠回しの No 逆引き（decode the soft no）** — *検討します／難しいですね／ちょっと…＋沈黙／前向きに考えます／また連絡します* を「実際は断り」と読み解く逆引きセクション。daijob の弱い実装を超え、**「相手の No を見抜けず押し続けて失礼になる」非ネイティブ事故** を正面から防ぐ。この記事を speech-act シリーズで唯一の「双方向（言う側＋受け取る側）」記事にする。
- **3 問セルフ診断** — (1) 相手は社内か社外か (2) 相手は目上か (3) 業務上の依頼か私的な誘いか → 結果で直接度と A/B/C 行をルーティング。`keigo-mistakes` で実証済みの「Yes 数で章ルーティング」パターンを断り特化で再利用。
- **断り固有のミス 5 つ** — (1) いきなり iie で冷たい / (2) *ちょっと* を多用しすぎて伝わらない / (3) 断りづらくて既読スルー（ゴースト）し関係悪化 / (4) *検討します* を社交辞令で使い相手に期待させる / (5) 理由を盛りすぎて言い訳・嘘くさくなる。各ミスに「次に言うべき正しい一文」をセット。`keigo-mistakes` 本記事との重複を避け、本記事は **断り場面に絞った専門カタログ** として住み分け。

### EN

- **A/B/C politeness × scenario matrix** — Reuse the established A/B/C framework from `keigo-guide` (A: friend, B: peer/first-meet, C: senior/client) mapped to 8 scenarios (drink/nomikai invite · overtime or extra-task request · vendor/sales pitch · meeting request · peer's favor · offered food/drink · "can you pull the deadline in?" · declining to attend/participate) → **24 paste-ready cells**. It uses the same matrix structure as `how-to-say-sorry-in-japanese-politely` (the apology sibling), building one consistent mental model across the speech-act series.
- **Directness rubric** — Four axes (internal vs. external · senior vs. peer · work ask vs. personal · first-time vs. repeat) → a 3-level verdict (decline plainly OK / cushion required / go fully indirect). This dissolves the over-generalization that "Japanese is always indirect" and correctly shows the cases where a plain decline is fine (internal, equal, light personal invite).
- **Five-part anatomy of a polite refusal** — 1. Cushion (*sekkaku desu ga* / *ainiku* / *mōshiwake nai no desu ga*) → 2. Appreciation (*o-sasoi arigatou gozaimasu* / *arigatai ohanashi desu ga*) → 3. Refusal + reason (A/B/C level; one-line reason, not an excuse) → 4. Alternative or door-open (*mata no kikai ni* / *jikai wa zehi*) → 5. Close (*yoroshiku onegai shimasu*). Each part shown as **bad → good pair**, spotlighting that "thank *before* you decline" and "leave a door open" are what make it read as sincere.
- **Four full refusal email templates** — (a) declining a meeting (highest frequency, internal + external), (b) declining a vendor/sales pitch (most important; cross-linked with `business-email-template`), (c) declining extra scope/request (project boundaries), (d) declining an invitation in writing (nomikai/event). Each with subject + body + signature, anchored to the 8-step structure of `how-to-write-japanese-business-email`.
- **Decode the soft "no" (reverse lookup)** — A lookup section that reads *kentou shimasu* / *muzukashii desu ne* / a trailing *chotto…* + silence / *maemuki ni kangaemasu* / *mata renraku shimasu* as **de-facto refusals**. It surpasses daijob's thin treatment and squarely prevents the non-native failure of *missing the no and pushing on*. This makes the article the only **two-directional** (speaker + listener) piece in the speech-act series.
- **3-question self-diagnostic** — (1) Internal or external recipient? (2) Is the other person senior? (3) Work request or personal invite? → Routes the reader to a directness level + A/B/C row. Mirrors the proven `keigo-mistakes` self-diagnostic pattern, retargeted to refusals.
- **Five refusal-specific mistakes** — (1) blunt *iie* sounds cold, (2) over-using *chotto* so the refusal never lands, (3) ghosting because declining felt hard (worsens the relationship), (4) saying *kentou shimasu* as a social nicety and leaving the other side hoping, (5) piling on reasons until it reads as an excuse or a lie. Each paired with a "what to say instead" line. Scoped to refusals so it does not overlap `keigo-mistakes` broadly.

---

## 6. primary_info_seeds

> Hypotheses for primary information (original data, first-hand experience, expert quotes) to layer on top of the article over time. Fill with **3 hypotheses** per article.

1. **Field log: 4-week catalog of real-world Japanese refusal scenes**
   - _What:_ First-person observation log of 30–50 refusals witnessed in workplace, retail, transit, and email/chat — capturing (scenario, phrase used, speaker register, listener register, whether a door was left open, outcome). Differentiates "what learners are taught" vs. "what natives actually do" in 2026, including how often *chotto…* alone is used to close a refusal.
   - _How:_ Personal observation log + transcription notebook, supplemented with anonymized screenshots of own received refusal emails/Slack messages (with sender permission).
   - _Cost:_ ~6h spread over 4 weeks (10–15 min/day capture + 90 min synthesis)
   - _Status:_ `not_started`

2. **Soft-no decode test — can learners spot a refusal? (10–15 learners, N3+)**
   - _What:_ Show N3+ non-native learners 10 short Japanese replies (mix of real soft-no's like *kentou shimasu* / *muzukashii desu ne* / trailing *chotto…* with genuine maybes/yeses) and ask: refusal, genuine maybe, or yes? Quantifies how often non-natives miss a polite "no" — the core failure this article targets. Predicted: *kentou shimasu* and *maemuki ni kangaemasu* are most often misread as positive.
   - _How:_ Google Form distributed via 1–2 N3+ learner Discord/Slack communities + own network; ~10 min response time.
   - _Cost:_ ~8h (form design 2h, recruit 2h, synthesize 4h)
   - _Status:_ `not_started`

3. **Native-speaker grading of 24 drafted refusals + 4 email templates**
   - _What:_ Submit the 24 matrix cells and 4 email templates (with a few deliberate register/directness errors mixed in) to 2–3 native Japanese business reviewers. Collect per-item grades: *natural / awkward / wrong* + 1-line reason, plus "did this leave the relationship intact?" Produces a defensible register-and-directness reference no SERP competitor has.
   - _How:_ Recruit reviewers via existing client/colleague network; pay ¥3k–5k each; Google Form intake.
   - _Cost:_ ~10h (3h draft prep, 4h coordinate, 3h synthesize)
   - _Status:_ `not_started`

---

## 7. Target Article Outline

### JA outline (target)

1. H1: _日本語で丁寧に断る方法｜「すみません、ちょっと…」では伝わらない8場面の使い分け_
2. H2: この記事を読むべき人（4 ペルソナ箇条書き：日本企業勤務・外資日本オフィス・エンジニア×日本人クライアント・留学生インターン）
3. H2: 3 つの質問で「直接断ってよいか／遠回しが必要か」を 30 秒で診断（セルフ診断 3 問 + ルーティング表）
4. H2: なぜ日本語では直接「いいえ」と言わないのか（40〜60 字のスニペット狙い段落）
   - H3: *iie* が冷たく聞こえる理由
   - H3: 内/外（*uchi-soto*）× 上下のレイヤー
5. H2: 直接度ルーブリック（4 軸 → 直接 OK／要クッション／要全力遠回し）
   - H3: 相手は社内か社外か / 目上か / 業務か私的か / 初回か繰り返しか
   - H3: 判定 → 推奨スタイル + 例文
6. H2: A/B/C × 場面マトリクス（24 セル、コピペ完成文）
   - H3: 凡例（A 軽 / B 標準 / C 重 + 内外）
   - H3: 飲み会・誘いの辞退
   - H3: 残業・追加依頼の辞退
   - H3: 取引先の提案・営業の辞退
   - H3: 会議招集の辞退
   - H3: 同僚の頼み事の辞退
   - H3: 食事・飲み物の勧めの辞退（*kekkou desu* vs *daijoubu desu*）
   - H3: 締切前倒し依頼の辞退
   - H3: 参加・慣習の辞退
7. H2: 丁寧な断りの解剖図（5 部構成）
   - H3: 1. クッション（せっかくですが／あいにく／申し訳ないのですが）
   - H3: 2. 感謝（断りの前に置く）
   - H3: 3. 断り＋理由（語彙レベル A/B/C、理由は 1 文）
   - H3: 4. 代替案 or 含み（またの機会に／次回はぜひ）
   - H3: 5. 締め（よろしくお願いします のレベル選び）
8. H2: 断りメール 4 雛形（コピペ可能、件名 → 本文 → 署名）
   - H3: 会議辞退（社内/社外）
   - H3: 取引先の提案・営業辞退
   - H3: 追加スコープ・依頼の辞退
   - H3: 誘いの書面辞退（飲み会/イベント）
9. H2: 相手の「遠回しな No」を見抜く（逆引き）
   - H3: 検討します／前向きに考えます
   - H3: 難しいですね／厳しいです
   - H3: ちょっと…＋沈黙
   - H3: また連絡します／また今度
10. H2: 非ネイティブが踏みやすい断り 5 つの落とし穴
    - H3: いきなり iie で冷たい
    - H3: *ちょっと* を多用しすぎて伝わらない
    - H3: 断りづらくて既読スルー（ゴースト）
    - H3: *検討します* を社交辞令で使い期待させる
    - H3: 理由を盛りすぎて言い訳・嘘くさい
11. H2: よくある質問（5 件 PAA 起点）
    - H3: *kekkou desu* と *daijoubu desu* の違いは？
    - H3: 上司の飲み会の誘いは断ってもいい？
    - H3: *検討します* は本当に断り？
    - H3: ビジネスメールで一番無難な断り方は？
    - H3: 「いいえ」と直接言ってよい場面はある？
12. H2: 関連記事 + Essential 30 PDF
    - H3: pillar: `keigo-guide`
    - H3: 姉妹: `how-to-say-sorry-in-japanese-politely` / `keigo-mistakes` / `keigo-examples` / `keigo-cheat-sheet` / `polite-japanese-phrases-for-office` / `japanese-business-phrases-pdf` / `how-to-write-japanese-business-email` / `business-email-template`

### EN outline (target)

1. H1: _How to Refuse Politely in Japanese: An A/B/C × Scenario Matrix (and How to Spot a Soft "No")_
2. H2: Who this guide is for (4-bullet persona block)
3. H2: 30-second self-diagnostic — may you decline plainly, or must you soften?
   - H3: Question 1: Is the recipient internal or external?
   - H3: Question 2: Is the other person senior?
   - H3: Question 3: Work request or personal invite?
   - H3: Routing table (answers → directness level + matrix row)
4. H2: Why Japanese rarely says a direct "no" (40–60 word featured-snippet paragraph immediately under H2)
   - H3: Why *iie* lands cold
   - H3: The *uchi-soto* + seniority layer
5. H2: The directness rubric — when plain is fine vs. when to go indirect
   - H3: Four axes (internal/external · senior/peer · work/personal · first/repeat)
   - H3: Verdict → recommended style (plain OK / cushion required / fully indirect) with example
6. H2: A/B/C × scenario matrix — 24 paste-ready lines
   - H3: How to read the matrix
   - H3: Drink / *nomikai* invitation
   - H3: Overtime or extra-task request
   - H3: Vendor / sales pitch
   - H3: Meeting request
   - H3: A peer's favor
   - H3: Offered food or drink (*kekkou desu* vs *daijoubu desu*)
   - H3: "Can you pull the deadline in?"
   - H3: Declining to attend / participate
7. H2: The five-part anatomy of a polite refusal
   - H3: 1. Cushion (*sekkaku desu ga* / *ainiku* / *mōshiwake nai no desu ga*)
   - H3: 2. Appreciation — thank *before* you decline (with bad/good pair)
   - H3: 3. Refusal + reason — the one-line rule that avoids sounding like an excuse
   - H3: 4. Alternative or door-open (*mata no kikai ni* / *jikai wa zehi*)
   - H3: 5. Close (which *yoroshiku onegai shimasu* to use)
8. H2: Four full refusal email templates (subject → body → signature)
   - H3: Declining a meeting (internal + external)
   - H3: Declining a vendor / sales pitch
   - H3: Declining extra scope or a request
   - H3: Declining an invitation in writing
9. H2: How to spot a soft "no" (reverse lookup)
   - H3: *Kentou shimasu* / *maemuki ni kangaemasu*
   - H3: *Muzukashii desu ne* / *kibishii desu*
   - H3: A trailing *chotto…* + silence
   - H3: *Mata renraku shimasu* / *mata kondo*
10. H2: Five refusal mistakes non-natives make
    - H3: Blunt *iie* sounds cold
    - H3: Over-using *chotto* so the refusal never lands
    - H3: Ghosting because declining felt hard
    - H3: *Kentou shimasu* as a social nicety leaves them hoping
    - H3: Piling on reasons until it reads as an excuse
11. H2: FAQ (5, PAA-aligned)
    - H3: What's the difference between *kekkou desu* and *daijoubu desu*?
    - H3: Can I decline my boss's invitation to drinks?
    - H3: Does *kentou shimasu* (検討します) really mean no?
    - H3: What's the safest way to decline in a business email?
    - H3: Is there ever a time to say a plain "*iie*"?
12. H2: Related reading + Essential 30 PDF
    - H3: Pillar: `keigo-guide`
    - H3: Siblings: `how-to-say-sorry-in-japanese-politely` / `keigo-mistakes` / `keigo-examples` / `keigo-cheat-sheet` / `polite-japanese-phrases-for-office` / `japanese-business-phrases-pdf` / `how-to-write-japanese-business-email` / `business-email-template`

---

## 8. FAQ / People Also Ask

> Questions to answer in the article. Map each to a section or a dedicated FAQ block.

| Question | Where answered |
|---|---|
| How do you say "no" politely in Japanese? | §6 matrix (B/C columns) + §4 cultural framing |
| Why don't Japanese people say no directly? | §4 (why *iie* lands cold) |
| What does *chotto* mean as a refusal? | §6 (deflection rows) + §10 mistake #2 (over-use) |
| What's the difference between *kekkou desu* and *daijoubu desu*? | §6 "offered food/drink" row + §11 FAQ |
| How do you decline an invitation in Japanese? | §6 nomikai row + §8 written-invite template + §11 FAQ (boss invite) |
| How do you refuse a request from your boss in Japanese? | §5 directness rubric (senior axis) + §6 overtime row |
| What does *kentou shimasu* (検討します) really mean? | §9 decode-the-soft-no + §11 FAQ |
| How to politely decline in a Japanese business email? | §8 templates (all 4) + cross-link to `how-to-write-japanese-business-email` |
| Is it ever OK to say a plain *iie*? | §5 rubric (plain-OK verdict) + §11 FAQ |
| How can I tell if someone is politely refusing me? | §9 decode-the-soft-no (whole section) |

---

## 9. Internal Links

### Upstream (pillars / hubs linking to this article)
- `keigo-guide` (pillar) — add a "How to refuse politely →" link from the politeness-level / speech-acts section, paired with the existing "Apologies in detail →" link.

### Downstream (articles this article links to)
- `how-to-write-japanese-business-email` — from §8 (email templates) point to the full 8-step process.
- `business-email-template` — from §8 (vendor/sales refusal) point to the full template library.
- `keigo-mistakes` — from §10 (refusal mistakes) point to the broader keigo-mistakes taxonomy.

### Sibling cluster articles
- `how-to-say-sorry-in-japanese-politely` — the apology speech-act sibling; cross-link both ways (refusals often pair with a cushion apology). Same matrix structure → reinforce the series.
- `keigo-cheat-sheet` — from §6 matrix link to the broader phrase lookup table.
- `keigo-examples` — from §7 (anatomy) link to fully worked dialogues showing the 5-part structure.
- `polite-japanese-phrases-for-office` — from §6 (overtime, peer-favor rows) link to the chronological office-day arc.
- `japanese-business-phrases-pdf` — from §8 link as a downloadable/scannable phrase reference; also from CTA.
- `best-way-to-learn-keigo` — from intro as a "if you're still building your foundation, start here" sidebar link.

---

## 10. Localization Notes

> Heads-up for language-diff specs. Flag items that are likely to behave differently in non-English SERPs.

### JA

- **用語:** *chotto* / *kekkou desu* / *daijoubu desu* / *o-kotowari shimasu* / *kentou shimasu* は EN SERP で強い認知（初出はイタリック romaji + 漢字）。JA ではローマ字不要、native 表記が主。VI/KO/ZH-TW では romaji か現地音写かでランクが変わる可能性、*chotto* の「言い切らない」ニュアンスは音写で伝わりにくい。
- **文化的前提:** EN 版は「日本語では直接 No と言わない／なぜ *iie* が冷たいか」の文化セットアップを前提に置く。JA 版は native 読者には不要 → 「断りを構造で組み立てる（クッション＋感謝＋含み）」に再フレームし、マトリクスと雛形・**逆引き（相手の No を見抜く）** に重心を移す。`japanese-for-it-professionals` の Option B 再フレーム前例が有効。
- **競合ランドスケープ:** EN SERP は欧米の語学学習サイト（cotoacademy / migaku / lingopie 等）＋ daijob/tomo の在日就労系。JA SERP「角を立てずに断る ビジネス」「お断りメール 例文」は全く別セット（Mynavi / All About / ビジネスマナー出版社 / 例文テンプレ集）になる見込み → `seo-article-localize` 判定で JA-diff spec が必要になる可能性大。drafting 時に判断。
- **言語固有のリスク:** 5 部構成は JA に各部の名前（*kushion kotoba* / *o-rei* / *okotowari* / *daitaian* / *musubi*）があり EN より自然に収まる。逆引き（soft-no decode）は JA native には自明な部分があるので、JA 版では「非ネイティブ視点」を外し「メールで断られているのに気づかず追撃しない」等の実務 tips に転用する。
- **ペルソナ pivot の必要性:** EN は在日/日系で働く外国人。JA SERP は日本人ビジネスパーソンが「自分が角を立てず断る言い回し／お断りメール例文」を探す層が主 → audience pivot 要否は SERP 取得時に判定（謝罪姉妹記事と同じ判断ポイント）。

### EN

- **Terminology:** Romanized forms (*chotto*, *kekkou desu*, *daijoubu desu*, *o-kotowari shimasu*, *kentou shimasu*) carry strong recognition in EN SERP (italic romaji + kanji on first use). In JA, romanization is unnecessary; native spelling dominates. In VI/KO/ZH-TW, watch whether romaji or local-script transliteration ranks better — the "intentionally unfinished" nuance of *chotto* is hard to convey in transliteration.
- **Cultural assumptions:** The EN version assumes a non-native operating in/with Japan who needs the "why Japanese avoids a direct no / why *iie* sounds cold" setup. The JA version targets readers who do not need it — JA reframes to "build a refusal by structure (cushion + appreciation + door-open)" and shifts weight to the matrix, templates, and the **reverse-lookup decode** section. The Option B reframing from `japanese-for-it-professionals` is a useful precedent.
- **Competitor landscape:** EN SERP = Western language-learning sites (cotoacademy / migaku / lingopie) + the daijob/tomo in-Japan-work axis. JA SERP for "角を立てずに断る ビジネス" or "お断りメール 例文" will be a completely different set (Mynavi / All About / business-etiquette publishers / template banks) — `seo-article-localize` will likely require a JA-diff spec. Decision deferred to drafting time.
- **Language-specific risks:** The five-part anatomy maps cleanly to JA (each part has a native name), a tighter fit than EN. The soft-no decode section is partly self-evident to JA natives, so the JA version should repurpose it from "non-native comprehension" to practical tips ("don't chase a written refusal you didn't notice").
- **Persona pivot signal:** EN = foreigners working in/with Japan; JA SERP is likely Japanese business adults searching for their own polite-refusal wording and decline-email examples → audience pivot decision needed at SERP-capture time (same decision point as the apology sibling).

---

## 11. Change Log

| Date | Change | Author |
|---|---|---|
| 2026-06-03 | **JA v1 review pass + JA publish flip.** ユーザー approve（JA v1「レビューOK」、タイトル整合性も確認＝主 KW「丁寧な断り方」front＋副「角を立てない／お断りメール例文」をタイトルに包含）。`languages.ja.status: drafting → published`、ja diff spec `status: published`、Live articles 表の JA 列を ✅ published (B′ pivot) に更新。mdx は `draft: false`。**最終確認 `pnpm build` exit 0**（lock 直列化で ENOENT なし、47 pages indexed、EN+JA 両ページ生成確認）。両言語 published に揃った。**次（ユーザートリガー）：** git commit & push → Cloudflare Pages auto-build → GSC URL 検査 + インデックス登録 2 URL（en/ja）。 | ryoooue (review/publish) + Claude Opus 4.8 |
| 2026-06-03 | **JA 戦略フォーク確定（B′ ハイブリッド）+ JA v1 shipped.** AskUserQuestion で **B′ ハイブリッド**採択（外国人読者維持＋ネイティブ例文バンク／断り専用クッション言葉集／相手別テンプレ構造、KW/title を JA SERP「お断りメール例文／丁寧な断り方」に寄せる）。JA v1: `src/data/guides/ja/how-to-refuse-politely-in-japanese.mdx`（~8,350字、`.ja.spec.md` §7 1:1）。詳細は ja diff spec §8。`ja-article-style` no-changes、`pnpm astro check` 0/0/0。`languages.ja.status: planned → drafting`。**次：人間レビュー JA v1 → publish flip。** | Claude Opus 4.8 + ryoooue |
| 2026-06-03 | **`seo-article-localize` JA 判定完了 → diff NEEDED（Option B 全面書き換え）.** JA SERP（「お断りメール 例文」「角を立てない 断り方」、2 クエリ merge・7/10 fetch）は **日本人ビジネスパーソンが自分の断り方/お断りメールを探す層** に占有され（All About / 幻冬舎 + email-SaaS：Mazrica/Blastmail/Cybozu/Emberpoint/Sales Marker + Indeed JP + 電話代行）、**外国人学習者向け 0/10**。base_coverage ≈25%（keep=5部解剖図 7/10・メール例文 8/10・状況別例文 format 6/10／drop=外国人ペルソナ・文化セットアップ・A/B/C ローマ字・soft-no 逆引き・外国人ミス／reframe=ミス→NG例）、JA 固有追加 5–6（クッション言葉集・営業お断りメール特化・NG例文・電話・フォローアップ・方便ぼかし表現）。Diff spec 生成：`specs/articles/how-to-refuse-politely-in-japanese.ja.spec.md`（Option B）。**§5 で戦略フォークを上申**：(B) ネイティブ pivot／(B′) ハイブリッド＝外国人読者維持＋ネイティブ例文バンク構造に KW/title を寄せる（**推奨**、[[feedback-localize-business-growth-frame]] 準拠）／(C) defer。**JA 断り需要は本物で commercial（お断りメール例文は SaaS が競合）→ business-growth として B′ を推奨**するが、full native pivot はサイトの外国人読者モデルを分断するため **drafting 前に人間 go/no-go 必須**。base spec `languages.ja.diff_spec` 更新。 | seo-article-localize (Claude Opus 4.8) + ryoooue |
| 2026-06-03 | **EN review pass + EN publish flip.** ユーザー approve（EN v1「問題ない」、v2 不要）→ base spec `status: drafting → published`、`languages.en.status: drafting → published`。JA は `planned` 据え置き（§10 のとおり着手前に `seo-article-localize` 判定必須）。ROADMAP Live articles 表に行追加（JA=🔜 planned, localize 判断待ち）、#23 TODO `[ ] → [x]`。mdx は `draft: false`、`pnpm astro check` 0 errors / 0 warnings / 0 hints。**ビルド運用ルール更新を採用**（ROADMAP §"Parallel-work rules"）：記事検証は `pnpm astro check`（並列OK）、full build は `pnpm build` のみ（lock で直列化、`npm` 禁止）、astro build は最終1回。**次（ユーザートリガー）：** git commit & push → Cloudflare Pages auto-build → GSC URL 検査 + インデックス登録 1 URL（`/en/guides/how-to-refuse-politely-in-japanese/`）。 | Claude Opus 4.8 + ryoooue |
| 2026-06-03 | **EN v1 shipped.** Body at `src/data/guides/en/how-to-refuse-politely-in-japanese.mdx` (~4,085 words). `seo-article-localize` 判定スキップ（base spec が en-SERP-rooted、姉妹 `how-to-say-sorry-in-japanese-politely` と同パターン）。§7 EN outline を 1:1 実装：4 ペルソナ + 40–60 語 featured-snippet 段落（intro 直下）+ 3 問セルフ診断（plain/cushion/indirect ルーティング）+ 「なぜ直接 No と言わないか」+ *uchi-soto* × seniority レイヤー + 3-tier A/B/C 表 + 4 軸直接度ルーブリック + worked example（client 値引き要求 → 7 点 fully indirect）+ 24 セル 8 場面マトリクス（nomikai / 残業 / vendor / meeting / favor / food-drink kekkou-vs-daijoubu / deadline pull-in / 参加辞退、各 common-mistake 列付き）+ 5 部構成解剖図（cushion → appreciation → refusal+reason → alternative/door → close、各 bad→good ペア、「感謝を先に」「含みで終える」を強調）+ 4 断りメール完成形（meeting / vendor / scope / invitation、件名→本文→署名）+ **soft-no decode 逆引き 6 行表**（kentou shimasu / maemuki / muzukashii / chotto+silence / mata renraku / zensho、+ 押し返さない対応 4 点）+ 断り固有 5 ミス（blunt iie / over-chotto / ghosting / 社交辞令 kentou / 理由盛りすぎ、各 better ペア）+ FAQ 5（kekkou vs daijoubu / 上司 nomikai / kentou=no / メール安全形 / plain iie いつ）+ 関連 9 sibling + Essential 30 CTA（中盤なし・記事末 1、productCTA frontmatter で自動描画 + 末尾手置き CTA セクション）。Title "How to Refuse Politely in Japanese: 8 Scenarios and How to Spot a Soft No"（73 chars、KW 完全一致を冒頭 34 字以内、A/B/C ジャーゴン除外 `feedback-title-no-internal-jargon`、number-led + verb-phrase subtitle なので冠詞なし D8、`feedback-title-structure-count` の structure-count 8 採用）。description 159 chars。`en-article-style` linter idempotent pass（auto-fix 0、weak-qualifier フラグは全て正当例外：FAQ 自然クエリ "really mean no" / temporal "just invited" / "merely" の just / 対比の actually）。`pnpm build` green at **46 pages / 13,072 words indexed**（先行ビルドの vite ENOENT は並行セッション `japanese-workplace-mistakes-foreigners` の stale `.astro` content-layer キャッシュ由来 → `rm -rf .astro dist node_modules/.vite` で解消、exit 0）。`languages.en.status: planned → drafting`、spec lifecycle `drafting` のまま。**次：人間レビュー EN v1 → EN v2 if needed → publish flip（EN のみ先行 or JA と同期）。JA は §10 のとおり着手前に `seo-article-localize` 判定必須。** | Claude Opus 4.8 + ryoooue |
| 2026-06-03 | Initial spec generated via `seo-article-outline` skill. Top 10 SERP captured (8/10 fetched; jobsinjapan.com 403 → position anchor, howtosayguide.com thin-template anchor). 7 zero-coverage gaps identified (A/B/C × scenario matrix / directness rubric / 5-part refusal anatomy / refusal email templates / self-diagnostic / refusal-specific mistakes / uchi-soto × seniority dual axis). Highest-value rare signal = "decode the soft no" (2/10, daijob only) → made a flagship reverse-lookup section, positioning this as the only two-directional (speaker + listener) article in the speech-act series. Differentiation locked around: 24-cell A/B/C × 8-scenario matrix, 4-axis directness rubric, 5-part anatomy (cushion → appreciation → refusal+reason → alternative/door-open → close) with bad/good pairs, 4 paste-ready refusal email templates, decode-the-soft-no lookup, 3-question self-diagnostic, 5 refusal-specific mistakes. 3 primary_info_seeds initialized (field-log / soft-no decode test / native-grading). Cluster: keigo, pillar: keigo-guide. Mirrors the structure of sibling `how-to-say-sorry-in-japanese-politely`. Status: `drafting`. Bilingual §1 §4 §5 §7 §10 per convention. | seo-article-outline (Claude Opus 4.8) + ryoooue |
