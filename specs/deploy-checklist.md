# Deploy checklist: Step 9 (Cloudflare) + Step 10 (GSC / GA4)

土日のコミット.md の Step 9・10 を実行するための具体的な手順書。
インフラ・技術側の準備（AI 側）はすべて完了済み。以下はユーザー手動作業のみ。

---

## 前提（AI 側で済ませたこと）

- ✅ `pnpm build` がローカルで green（dist 出力も確認済み）
- ✅ `@astrojs/sitemap` で `sitemap-index.xml` を自動生成
- ✅ `/robots.txt` が `sitemap-index.xml` を正しく参照
- ✅ `PUBLIC_GOOGLE_SITE_VERIFICATION` は Layout に配線済み
- ✅ `PUBLIC_GA_MEASUREMENT_ID` を追加し、gtag.js + config を条件付き挿入（`/src/layouts/Layout.astro`）
- ✅ `.env.example` を用意（Cloudflare と揃える用）

---

## Step 9: Cloudflare Pages デプロイ

### 9-1. GitHub に push

```bash
cd ~/dev/rwjapanese/realworldjapanese
# まだ init してなければ
git init -b main
git add .
git commit -m "feat: initial launch (JA+EN keigo-guide, GA4 hook)"

# GitHub 側で新規リポジトリ rwjapanese/realworldjapanese を作成した前提
git remote add origin git@github.com:rwjapanese/realworldjapanese.git
git push -u origin main
```

> まだ `git init` 済みかは `git status` で確認。既にあれば `git add . && git commit && git push` のみ。

### 9-2. Cloudflare Pages でプロジェクト作成

1. Cloudflare dashboard → Workers & Pages → Create application → Pages → Connect to Git
2. GitHub アカウントを連携し `rwjapanese/realworldjapanese` を選択
3. ビルド設定:

   | 項目 | 値 |
   |---|---|
   | Production branch | `main` |
   | Framework preset | `Astro` |
   | Build command | `pnpm build` |
   | Build output directory | `dist` |
   | Root directory | (空) |
   | Node version | `20` （Variables で `NODE_VERSION=20`）|

4. Environment variables（Production と Preview 両方に入れる）:

   | Key | Value | 必要？ |
   |---|---|---|
   | `NODE_VERSION` | `20` | ✅ 必須 |
   | `PUBLIC_GOOGLE_SITE_VERIFICATION` | GSC で発行した content の値 | Step 10 後に追加 |
   | `PUBLIC_GA_MEASUREMENT_ID` | `G-XXXXXXXXXX` | Step 10 後に追加 |

5. Save and Deploy → 初回ビルドが通ることを確認

### 9-3. カスタムドメイン接続

1. Cloudflare Pages → プロジェクト → Custom domains → Set up a custom domain
2. `realworldjapanese.com` を追加
3. 別途 `www.realworldjapanese.com` も追加
4. DNS を Cloudflare が管理している場合、自動で A/CNAME が入る
5. 外部 DNS の場合は Cloudflare が表示する CNAME を手動で登録

### 9-4. 301 Redirect: www → apex

Cloudflare dashboard → 該当ドメイン → Rules → Redirect Rules → Create rule

| 項目 | 値 |
|---|---|
| Rule name | `www to apex` |
| If → Custom filter expression | `(http.host eq "www.realworldjapanese.com")` |
| Then → Type | `Dynamic` |
| Expression | `concat("https://realworldjapanese.com", http.request.uri.path)` |
| Status code | `301` |
| Preserve query string | on |

### 9-5. 動作確認

```bash
# apex で 200
curl -I https://realworldjapanese.com/
curl -I https://realworldjapanese.com/ja/
curl -I https://realworldjapanese.com/en/
curl -I https://realworldjapanese.com/ja/guides/keigo-guide/
curl -I https://realworldjapanese.com/en/guides/keigo-guide/

# www で 301 → apex
curl -I https://www.realworldjapanese.com/
```

期待値:
- apex は `HTTP/2 200`
- www は `HTTP/2 301` + `location: https://realworldjapanese.com/...`

---

## Step 10: GSC + サイトマップ + GA4

### 10-1. GA4 プロパティ作成

1. https://analytics.google.com/ → 管理 → プロパティを作成
2. プロパティ名: `Real-World Japanese`、タイムゾーン `Asia/Tokyo`、通貨 JPY
3. データストリーム → ウェブ → URL `https://realworldjapanese.com/` + ストリーム名 `rwjapanese-prod`
4. 発行される「測定 ID」（`G-XXXXXXXXXX`）をコピー

### 10-2. 測定 ID を Cloudflare に反映

Cloudflare Pages → プロジェクト → Settings → Environment variables → Production:
- `PUBLIC_GA_MEASUREMENT_ID` = `G-XXXXXXXXXX`

Save → Deployments → 最新デプロイを Retry build で再ビルド（env を反映させるため）。

ビルド完了後:

```bash
curl -s https://realworldjapanese.com/ | grep -Eo 'G-[A-Z0-9]+'
```

`G-XXXXXXXXXX` が出れば OK。

### 10-3. GA4 リアルタイム確認

1. 本番サイトをブラウザで開く
2. GA4 → レポート → リアルタイム で自分のアクセスが見えることを確認

### 10-4. GSC プロパティ追加（ドメインプロパティ推奨）

1. https://search.google.com/search-console/ → プロパティを追加
2. タイプ: **ドメイン**（`realworldjapanese.com`、www 含む全サブドメイン対応）
3. 検証方法: DNS TXT レコード
   - Cloudflare DNS → 該当ドメイン → DNS → Records → Add record
   - Type `TXT` / Name `@` / Content に GSC が指定した `google-site-verification=...` の値
4. 検証 → 成功

> URL プレフィックス版（`https://realworldjapanese.com/`）を使いたい場合は、発行された meta tag の content を `PUBLIC_GOOGLE_SITE_VERIFICATION` に入れる方式もあり（既に配線済み）。ただしドメインプロパティの方が www・他サブドメインもカバーできて強い。

### 10-5. サイトマップ送信

GSC → サイトマップ → 新しいサイトマップの追加 → `sitemap-index.xml`

送信 → ステータスが「成功しました」になれば OK（反映に数時間〜24h）。

### 10-6. URL 検査 + インデックス登録リクエスト

GSC → URL 検査で以下を順に実行:

- `https://realworldjapanese.com/`
- `https://realworldjapanese.com/ja/`
- `https://realworldjapanese.com/en/`
- `https://realworldjapanese.com/ja/guides/keigo-guide/`
- `https://realworldjapanese.com/en/guides/keigo-guide/`

それぞれ「インデックス登録をリクエスト」を押す。

---

## 完了判定

- [ ] 9-1 GitHub push 完了
- [ ] 9-2 Cloudflare Pages 初回デプロイ green
- [ ] 9-3 `realworldjapanese.com` / `www.realworldjapanese.com` 両方が SSL + Cloudflare 経由
- [ ] 9-4 `www` → apex の 301 が効いている
- [ ] 9-5 5 URL すべて 200（または www から 301）
- [ ] 10-1 GA4 プロパティ + 測定 ID 取得
- [ ] 10-2 `PUBLIC_GA_MEASUREMENT_ID` を Cloudflare に設定して再デプロイ
- [ ] 10-3 GA4 リアルタイムで自分のアクセスが見える
- [ ] 10-4 GSC ドメインプロパティ検証済み
- [ ] 10-5 サイトマップ送信済み
- [ ] 10-6 5 URL の URL 検査 + インデックス登録リクエスト完了

全部チェックが付いたら MVP ローンチ完了。`土日のコミット.md` の Step 9・10 と `specs/ROADMAP.md` の該当タスクを更新する。
