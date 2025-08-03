
# 📄 Wabi-Sabi-Wisdom MVP 開発ドキュメント

---

## 1️⃣ Requirements（要件定義）

### 概要
- 日本の古典的金言を現代的ナラティブとして配信
- ユーザー心理プロファイルに基づきメッセージ選定
- 軽量な画像・音声演出を提供

### 機能要件
| カテゴリ | 機能 | 備考 |
|---|---|---|
| ユーザー認証 | メール認証（Magic Link） | OAuth等は将来追加 |
| オンボーディング | 10問による初期心理診断 | 心理特性ベクトル化 |
| メッセージ配信 | 週1回の配信 | MVPは最低限頻度 |
| メディア生成 | AI画像＋音声（英語） | 生成API経由 |
| 課金 | Stripe月額サブスクリプション | 初期1プランのみ |
| 履歴 | ユーザーへの配信履歴表示 | 最大1ヶ月保持 |
| プラットフォーム | Web/PWA (Next.js) | モバイルは後日追加 |

### 非機能要件
- レスポンス速度: 画像・音声生成後キャッシュで <3秒
- セキュリティ: 認証・決済・データ暗号化
- 拡張性: ver1.0への発展を考慮したアーキテクチャ

---

## 2️⃣ Design（設計）

### 全体アーキテクチャ
```
Client (Next.js PWA)
        │
        ▼
Edge API (Cloudflare Workers)
        │
        ▼
Backend (LangGraph + FastAPI)
        │
        ▼
Media Generation (Modal GPU Cluster)
        │
        ▼
Asset Storage (Cloudflare R2 + CDN)
```

### データベース設計（PostgreSQL）
```sql
CREATE TABLE users (
  id BIGSERIAL PRIMARY KEY,
  email CITEXT UNIQUE,
  onboarding_vec SMALLINT[10],
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE messages_sent (
  id BIGSERIAL PRIMARY KEY,
  user_id BIGINT REFERENCES users(id),
  quote_text TEXT,
  image_url TEXT,
  audio_url TEXT,
  sent_at TIMESTAMPTZ DEFAULT NOW()
);
```

---

## 3️⃣ Task list（タスク整理）

### 📋 フロントエンド（Next.js）
- [ ] UIワイヤフレーム（Figma）
- [ ] Next.jsプロジェクトセットアップ
- [ ] オンボーディング画面実装
- [ ] メッセージ表示画面実装
- [ ] 課金ページ実装（Stripe連携）
- [ ] 配信履歴画面実装

### 📋 API/Edge（Cloudflare Workers）
- [ ] Workersプロジェクト作成
- [ ] 認証機能 (Magic Link / Supabase Auth)
- [ ] メッセージ生成API実装
- [ ] 履歴取得API実装

### 📋 バックエンドAI（LangGraph＋FastAPI）
- [ ] LangGraphプロジェクト構成
- [ ] 心理ベクトル解析ノード実装
- [ ] ナラティブ生成ノード実装
- [ ] 金言LLMノード実装
- [ ] メディア生成API実装（画像・音声生成）
- [ ] FastAPIによるLangGraph API公開

### 📋 DB設計・構築（PostgreSQL）
- [ ] PostgreSQL Serverlessインスタンス作成
- [ ] DBスキーマセットアップ（users, messages_sent）

### 📋 インフラ（Cloudflare R2/CDN）
- [ ] R2バケット作成
- [ ] CDN設定

### 📋 CI/CD（GitHub Actions）
- [ ] フロントエンドデプロイ設定
- [ ] バックエンドデプロイ設定

### 📋 課金処理（Stripe）
- [ ] Stripeアカウント設定
- [ ] Checkoutセッション実装

---

## 🚦 開発順序（推奨）
1. UIワイヤフレーム → フロント最小実装
2. 認証 → Edge API基盤セットアップ
3. LangGraph MVP (Prompt生成最小版)
4. メディア生成 (画像＋音声API)
5. Stripe決済
6. 履歴機能

---

## ✅ MVP成功基準
- MAU 1,000ユーザー獲得
- 有料コンバージョン率5%以上
- 配信完了速度3秒以内（キャッシュ）

以上を達成することで、柔軟で将来性のある堅牢なMVPを構築可能。
