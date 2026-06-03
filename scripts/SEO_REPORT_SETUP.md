# SEO レポート連携セットアップ（一回だけ）

`scripts/seo_report.py` が Google Search Console と GA4 の API を直接叩くための
一回限りの設定。これが済めば、以降は

```bash
scripts/.venv/bin/python scripts/seo_report.py
```

を実行するだけで、todo §4 のトラッカーブロックがそのまま出力される（スクショ不要）。

---

## 採用方式：OAuth（`hello.rwjapanese@gmail.com` 本人として認証）

> **なぜこの方式か（経緯）**
> - **サービスアカウント方式は不可**：GA4/GSC の「ユーザー追加」UI が SA メールを
>   「Google アカウントと一致しません」と弾く（24h 待っても・シークレットでも不可）。
>   Google 側の挙動でこちらでは直せない。
> - **gcloud ADC も不可**：gcloud 内蔵 OAuth クライアントは Cloud 系スコープしか
>   要求できず、GSC/GA4 スコープを足すと「このアプリはブロックされます」になる。
> - **→ 自前 OAuth クライアント + 本人ログインが唯一通る**。本人は両プロパティの
>   管理者なので**ユーザー追加が一切不要**、自前クライアントなら GSC/GA4 スコープを
>   正規に要求できる。

**全手順を `hello.rwjapanese@gmail.com` でログインした状態で行う**（シークレット
ウィンドウでこのアカウントだけにログインすると確実）。所要 10〜15 分。

### 前提（済）
- Cloud プロジェクト `rwj-seo` 作成済
- Search Console API + Google Analytics Data API 有効化済
- GA4 プロパティ ID = `533586633`（`.env` 記入済）
- GSC プロパティ = `sc-domain:realworldjapanese.com`（`.env` 記入済）

---

### 1. OAuth 同意画面を設定

Google Cloud Console（`hello.rwjapanese` でログイン、プロジェクト `rwj-seo`）：

- 「APIs & Services」→「OAuth consent screen」
  （新 UI では「Google Auth Platform」→「Branding」「Audience」）
- **User type / Audience = External（外部）**
- アプリ名（例 `RWJ SEO Reporter`）、ユーザーサポートメール・デベロッパー連絡先 =
  `hello.rwjapanese@gmail.com`
- **テストユーザーに `hello.rwjapanese@gmail.com` を追加**
  （新 UI では「Audience」→「Test users」→ Add users）

> これがないとログイン時に「このアプリはブロックされます」になる。テストユーザーに
> 入れておけば「Google が確認していないアプリ」警告は出るが先に進める（手順4参照）。

### 2. OAuth クライアント ID（デスクトップアプリ）を作成

- 「APIs & Services」→「Credentials（認証情報）」→「認証情報を作成」→
  「OAuth クライアント ID」
  （新 UI では「Google Auth Platform」→「Clients」→「Create client」）
- **アプリケーションの種類 = デスクトップアプリ**
- 名前（例 `rwj-seo-desktop`）→ 作成
- 作成後ダイアログの「JSON をダウンロード」、または一覧の⬇ボタンでJSONをDL

### 3. JSON を置く

ダウンロードした `client_secret_xxx.json` を **`scripts/oauth_client.json`** という
名前で置く（`.gitignore` 済）。

> Claude に「このパスにある」と伝えれば設置してもらってもOK：
> `/Users/ryoooue/Downloads/client_secret_xxx.json`

### 4. ログイン（ブラウザが1回開く）

```bash
scripts/.venv/bin/python scripts/seo_report.py --login
```

- ブラウザが開く → **`hello.rwjapanese@gmail.com` を選ぶ**
- 「Google が確認していないアプリ」警告 → **「詳細」→「(アプリ名) に移動（安全ではない）」**
  → 続行（自分のアプリなので問題なし）
- Search Console と Analytics の読み取り許可にチェック → 続行
- `✓ Logged in. Token saved to .../oauth_token.json` が出れば完了

### 5. 実行

```bash
scripts/.venv/bin/python scripts/seo_report.py            # 直近28日
scripts/.venv/bin/python scripts/seo_report.py --days 7   # 直近7日
```

---

## トークンを長持ちさせる（任意・推奨）

同意画面が「テスト中」状態だと**リフレッシュトークンが約7日で失効**し、週次実行が
止まる（その時は手順4の `--login` を再実行すれば30秒で復活）。

恒久化するには同意画面を**「本番環境に公開（PUBLISH）」**する：
- OAuth consent screen / Audience →「アプリを公開」→ 確認
- External + 機微スコープなので「未確認アプリ」警告は残るが、所有者の利用は可能で
  リフレッシュトークンが失効しなくなる（週次利用していれば維持される）。

---

## トラブルシュート

| 症状 | 対処 |
|---|---|
| `このアプリはブロックされます` | 手順1でテストユーザーに `hello.rwjapanese` を入れる／同意画面が External か確認 |
| `Not logged in yet` | 手順4の `--login` を実行 |
| `OAuth client file not found` | 手順3：`scripts/oauth_client.json` が無い／名前違い |
| 7日ごとに `--login` を求められる | 「トークンを長持ちさせる」で本番公開する |
| `403 insufficient authentication scopes` | 古いトークン。`--login` で取り直す |

---

## 参考：使わなくなった方式の設定（残骸）

- `scripts/gsc-ga4-key.json`（サービスアカウント鍵）= SA 方式用。UI 追加が通らず
  未使用。消してよいが、将来 Google 側が直れば `AUTH_MODE=sa` で再利用可能。
