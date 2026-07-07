# SEO Skill Audit — 2026-07-07

`seo-article-outline` / `seo-article-localize`（`~/.claude/skills/`）を、2026年7月時点のSEOベストプラクティス調査と突き合わせた監査の正本。

## 調査方法

- 8軸の並列リサーチ（ランキング要因 / AI検索 / 情報利得 / トピカルオーソリティ / オンページ技術 / 鮮度・decay / 自動化事例 / 多言語・日本語SERP）
- 重要主張32件を独立の懐疑エージェントが裏取り（confirmed / partially-true / refuted 判定）
- スキル実物4本 + テンプレート + `/seo` 計測ループと突き合わせ（strengths 12件 / gaps 15件）
- 計42エージェント、2026-07-07 実行

## ファイル

| ファイル | 内容 |
|---|---|
| [research.md](research.md) | 8軸の調査全文（64主張、検証ステータス・自動化案つき） |
| [critique.md](critique.md) | 監査全文（強み12 + ギャップ15、根拠と自動化実装案つき） |

注: 調査時の参照URL一覧はワークフローの中間出力で失われたため、本文中の研究名（Ahrefs / Surfer / Pew / Princeton GEO / Seer Interactive / Zyppy 等）を手がかりにすること。

## headline findings（数値は裏取り済み or 方向性確認済み）

- AI Overviews は informational クエリの CTR を約47〜61%削る（Pew / Ahrefs 30万kw / Seer 2,500万imp収束値、方向性確認）
- AIO被引用URLのうち従来top10内は約38%のみ（Ahrefs）— 低DAでも引用は取れる
- 更新ページは30日以内にtop10入りする確率が約2倍（Surfer 30万ページ、方向性確認)
- AIエンジンはorganic top10より約26%新しいURLを引用（Ahrefs 1,700万引用）
- scaled content abuse の手動対応は2025年6月頃から執行（confirmed）。HCU系のサイト全体demoteからの本格回復第一波は約21か月後
- FAQ リッチリザルトは2026年5月に完全終了（schemaでなくFAQコンテンツ本体が正解）
- 韓国はNaverが検索の約44〜63%（Google-only分析は構造的に盲目）
- Google公式: 署名・肩書はランキング要因ではない（author schema過剰投資は無駄）

## 改善バックログ（15項目）— 全項目 2026-07-07 実装完了

### Critical
- [x] ① novelty gate — outline Step 7 で競合本文を `specs/serp-cache/<slug>/` にキャッシュ、`status: ready` 遷移に「seed≥1 integrated + `novelty_check.py` pass」を必須化（「Draft → ready gate」節）
- [x] ② キーワード勝算ゲート — outline Step 4（strong/weak分類 → `difficulty_estimate` 必須記入、strong≥7でSTOP+GSC長尾代替案）
- [x] ③ 翻訳QAゲート — localize「Post-draft: translation QA gate」節 + `humanReviewed` frontmatter（content.config.ts）+ validate_seo.py が false のまま公開をFAIL + 週3本/言語の velocity rule

### High
- [x] ④ リフレッシュループ — `seo-article-refresh` スキル新設（熟成ガード<180日、SERP diff、work order生成、modDatetime実質変更ルール）+ `seo_report.py --only refresh`（maturing バケット付き待ち行列）
- [x] ⑤ fan-out マップ + AIO記録 — outline Step 10 + テンプレ§8刷新 + §2にAIO行 + per-H2 `[capsule]` ルール（en-article-style C2拡張・ja-article-style Rule 8新設）
- [x] ⑥ カニバリゲート — outline Step 5（既存spec §2と共有URL≥4で halt）+ `seo_report.py --only cannibal`（query×page 90日、>20%×2ページ検出）
- [x] ⑦ 変種展開 + ko市場ゲート — localize Step 3（Naver到達シェア見積り+確認必須）・Step 4（表記変種→`keyword_variants.py` Suggest比較→`target_keyword_local`）
- [x] ⑧ ローカライズ昇格制 — localize Step 2（90日GSC実績ゲート、閾値50clicks or 500impr&pos≤20、override理由ログ）+ outlineは serp_language のみ初期化に変更
### Medium
- [x] ⑨ hreflang — Layout.astro を「翻訳が実在する言語のみ alternate」に修正（translationMap.ts、slug override対応）+ validate_seo.py で相互参照/自己参照/絶対URL/実在をCI検証
- [x] ⑩ 内部リンク強制 — outline Step 12 で被リンク編集≥2（ソースファイル+挿入文+アンカー）をspec必須化 + validate_seo.py orphan検出
- [x] ⑪ lastmod整合 — sitemapLastmod.ts（modDatetime??pubDatetime、ビルド時刻スタンプ禁止）+ JSON-LD⇔sitemap一致をCI検証
- [x] ⑫ velocity cap + 異常検知 — validate_seo.py（週3本/言語）+ `seo_report.py --only alerts`（WoW -30%アラート + Search Status注記）
- [x] ⑬ SERP APIレイヤー — `serp_fetch.py`（DataForSEO、~¥90/1,000 SERP、JSON保存）+ WebSearchフォールバック、`serp_source` frontmatter記録
- [x] ⑭ AI流入計測 — `seo_report.py --only ai`（AI Assistantチャネル+参照元regex）+ `ai_citation_audit.py`（月次Perplexity SoV → citation-share.csv）
- [x] ⑮ focus ガード — outline Step 6 + `focus_distance.py`（short-proxy参照分布+最近傍で covered/expansion/outlier 3段階判定）

検証: 実ビルド（48記事ページ）に対し `validate_seo.py` 7チェック全PASS、novelty/focus/variants スクリプトは実コーパスで機能検証済み（2026-07-07）。

## スキルの実所在（重要・2026-07-07訂正）

本監査の対象は **ユーザーレベルの `~/.claude/skills/`** のセット。どのプロジェクトから呼んでも同一で、リポジトリ固有の配管（⑨⑪⑫⑭等）だけが本リポジトリに実装される。

**訂正**: 監査当初「1セットのみ」と記したが、その後 **HeaR専用セット**が seishun `work/HeaR/.claude/skills/`（`hear-seo-article-outline` / `hear-seo-article-refresh` / `hear-article-style`、2026-06-11作成）に実在すると判明。2026-07-07中に、本監査の移植可能項目（勝算②・カニバリ⑥・novelty①ゲート、AIO記録⑤、回答カプセル⑤、熟成ガード④、FAQリッチリザルト終了注記、serp_fetch⑬共有）をHeaR側スキルにも適用済み。
