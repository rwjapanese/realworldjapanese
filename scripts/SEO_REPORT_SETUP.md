# SEO レポート連携セットアップ（一回だけ）

`scripts/seo_report.py` が Google Search Console と GA4 の API を直接叩くための
一回限りの設定。これが済めば、以降は

```bash
scripts/.venv/bin/python scripts/seo_report.py
```

を実行するだけで、todo §4 のトラッカーブロックがそのまま出力される（スクショ不要）。

所要 15〜25 分。**コンソールのクリック作業は ryoooue さん側**、迷ったら各ステップを
Claude に貼って聞けば OK。

---

## 0. 前提

- **GSC / GA4 の管理者アカウント = `hello.rwjapanese@gmail.com`**（ooue_ryo@hear.co.jp ではない）
- このアカウントが realworldjapanese.com の GSC プロパティと GA4 プロパティの**管理者**であること（確認済）

> **重要：手順1〜3 はすべて `hello.rwjapanese@gmail.com` でログインした状態で行う。**
> 理由：手順3 でサービスアカウントを GSC/GA4 に「ユーザー追加」できるのは各プロパティの
> 管理者だけ。hear.co.jp の Workspace アカウントは組織ポリシーでサービスアカウント鍵の
> ダウンロードがブロックされていることがあるので、その意味でも gmail 側で完結させるのが安全。
> （ブラウザで複数 Google アカウントにログインしているなら、Cloud Console / GSC / GA4 を
> 開く前に右上のアイコンから `hello.rwjapanese@gmail.com` に切り替える）

---

## 1. Google Cloud プロジェクトと API 有効化

### コンソールでやる場合
1. https://console.cloud.google.com/ を開く
2. 上部のプロジェクト選択 →「新しいプロジェクト」→ 名前 `rwj-seo`（何でも可）→ 作成
3. 作ったプロジェクトを選択した状態で、以下2つの API を有効化：
   - 「Search Console API」 https://console.cloud.google.com/apis/library/searchconsole.googleapis.com → **有効にする**
   - 「Google Analytics Data API」 https://console.cloud.google.com/apis/library/analyticsdata.googleapis.com → **有効にする**

### gcloud でやる場合（このセッションで `! ` を付けて実行できる）
```bash
# 初回のみブラウザ認証（インタラクティブなので ! を付けて自分で実行）
# → ブラウザでは必ず hello.rwjapanese@gmail.com を選ぶ
! gcloud auth login
! gcloud projects create rwj-seo --name="RWJ SEO"        # 既存プロジェクトを使うなら省略
! gcloud config set project rwj-seo
! gcloud services enable searchconsole.googleapis.com analyticsdata.googleapis.com
```

---

## 2. サービスアカウント作成 + JSON 鍵ダウンロード

サービスアカウント = 「Claude が代理でデータを読むためのロボット用 Google アカウント」。
人間のログインを毎回しなくて済む。

### コンソール
1. https://console.cloud.google.com/iam-admin/serviceaccounts → 「サービスアカウントを作成」
2. 名前 `seo-reporter` → 作成して続行 → ロールは付けずに「完了」
   （プロジェクトの IAM ロールは不要。GSC/GA4 側で個別に権限を渡す）
3. 作ったサービスアカウントをクリック →「キー」タブ →「鍵を追加」→「新しい鍵を作成」→ **JSON** → 作成
4. ダウンロードされた JSON を **`scripts/gsc-ga4-key.json`** に置く
   （`.gitignore` 済なのでコミットされない）
5. **このサービスアカウントのメールアドレス**を控える
   （`seo-reporter@rwj-seo.iam.gserviceaccount.com` のような形）。次の手順で使う。

### gcloud
```bash
! gcloud iam service-accounts create seo-reporter --display-name="SEO reporter"
# メールを確認
! gcloud iam service-accounts list
# 鍵をDL（<EMAIL> を上で確認したものに置換）
! gcloud iam service-accounts keys create scripts/gsc-ga4-key.json --iam-account=<EMAIL>
```

---

## 3. GSC と GA4 にサービスアカウントを「ユーザー追加」

API 有効化だけではデータは読めない。**各プロパティでこのロボットに閲覧権を渡す**。

### Search Console
1. https://search.google.com/search-console → realworldjapanese.com プロパティを選択
2. 左下「設定」→「ユーザーと権限」→「ユーザーを追加」
3. メール = 手順2で控えたサービスアカウントのアドレス
4. 権限 = **「制限付き」で OK**（読み取り専用で十分）→ 追加

### GA4
1. https://analytics.google.com/ → 左下「管理」（歯車）
2. 「プロパティ」列の「プロパティのアクセス管理」→ 右上「＋」→「ユーザーを追加」
3. メール = 同じサービスアカウントのアドレス
4. ロール = **「閲覧者」** → 追加
5. ついでに「プロパティの設定」を開き、**プロパティ ID（数字 9 桁前後）** を控える

---

## 4. `scripts/.env` を作る

```bash
cp scripts/.env.example scripts/.env
```

`scripts/.env` を開いて 3 つ埋める：

```
GOOGLE_APPLICATION_CREDENTIALS=/Users/ryoooue/dev/rwjapanese/realworldjapanese/scripts/gsc-ga4-key.json
GSC_SITE_URL=sc-domain:realworldjapanese.com
GA4_PROPERTY_ID=（手順3-5で控えた数字）
```

> `GSC_SITE_URL` の形に注意：
> - GSC でプロパティが「ドメイン」型 → `sc-domain:realworldjapanese.com`
> - 「URL プレフィックス」型 → `https://realworldjapanese.com/`
> - どっちか分からなければ両方試す。間違うと「権限なし/404」エラーになる。

---

## 5. 依存インストール（済んでいなければ）

```bash
python3 -m venv scripts/.venv
scripts/.venv/bin/pip install -r scripts/requirements.txt
```

> Python は 3.10+ 推奨（3.9 でも動くが Google が EOL 警告を出す。警告は stderr なので
> レポート出力自体は汚れない）。

---

## 6. 実行

```bash
scripts/.venv/bin/python scripts/seo_report.py            # 直近28日
scripts/.venv/bin/python scripts/seo_report.py --days 7   # 直近7日
```

出力に含まれるもの：
- **GSC**: 合計（clicks / impr / CTR / 順位）、トップクエリ、トップページ、
  🔧 2ページ目（pos 11–20）= リライト候補、⚡ 1ページ目だが低CTR = タイトル/メタ即修正候補
- **GA4**: 合計（active / new / sessions / 平均エンゲージ秒）、チャネル別、
  Organic Search セッション（go/no-go 判定値）、オーガニック着地ページ

毎週月曜はこれを実行 → 出力を todo §4 に貼るだけ。

---

## トラブルシュート

| 症状 | 原因 / 対処 |
|---|---|
| `403 ... does not have sufficient permission` (GSC) | 手順3-GSC のユーザー追加漏れ、または `GSC_SITE_URL` の形違い |
| `403 ... User does not have access` (GA4) | 手順3-GA4 の閲覧者追加漏れ、または property ID 違い |
| `API has not been used / disabled` | 手順1の API 有効化漏れ。有効化直後は反映に数分かかることあり |
| `Service-account key not found` | `GOOGLE_APPLICATION_CREDENTIALS` のパスが実ファイルと不一致 |
