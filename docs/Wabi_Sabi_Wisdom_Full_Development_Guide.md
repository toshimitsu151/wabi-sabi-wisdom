
# Wabi-Sabi-Wisdom 開発総合ガイドライン（2025年8月版）

## 🌟 コンセプト概要
「知的で静寂な体験」を中心に、ユーザー心理を分析して最適な日本古典金言を配信するアプリケーション。キャラクター・音声はあくまで補助的に演出される。

---

## 🛠️ 開発言語・フレームワーク選定

### フロントエンド（Web/PWA）
- **言語:** TypeScript
- **フレームワーク:** Next.js 13（App Router）+ React Server Components
- **スタイリング/UI:** Tailwind CSS + shadcn/ui
- **状態管理:** Zustand

### バックエンド（Edge/API）
- **言語:** TypeScript
- **ランタイム:** Cloudflare Workers / Bun

### AI処理・画像生成・音声生成
- **言語:** Python 3.12
- **フレームワーク:** LangGraph 0.9 + FastAPI
- **画像生成:** Stable Diffusion XL (InvokeAI)
- **音声生成:** ElevenLabs Professional API

---

## 🌐 全体アーキテクチャ設計

### フロント〜バックエンド構成図

```
Client (PWA / Next.js App Router)
            │
            ▼
Cloudflare Edge (Workers AI)
    └─ API Gateway (Auth + API)
            │
            ▼
Backend Orchestration (Python/LangGraph)
    ├─ Prompt Synthesizer
    ├─ Change Tracker
    ├─ Guardrail Engine
    └─ Vector DB (Pinecone v3)
            │
            ▼
Generation Layer (GPU Cluster: Modal)
    ├─ LLM (Claude-3 / Gemini)
    ├─ Stable Diffusion XL (InvokeAI)
    └─ TTS (ElevenLabs)
            │
            ▼
Asset Storage (Cloudflare R2 + CDN)
```

### データベース構成

| 種別 | 用途 | 技術 |
|---|---|---|
| OLTP | ユーザー管理、サブスクリプション | PostgreSQL 16 Serverless (Neon/Supabase/AlloyDB) |
| 履歴分析 | 配信履歴、行動分析 | ClickHouse Cloud |
| ベクトル検索 | 原典、ユーザー心理ベクトル | Pinecone Serverless v3 |
| メディアアセット | 画像・音声保存 | Cloudflare R2 |

---

## 🔑 技術スタックの強み

- **TypeScript/Next.js**で開発速度と保守性を最大化
- **Cloudflare Workers AI**で低レイテンシ＆低コスト
- **LangGraph (Python)**でAIフローの可視化・テスト性を担保
- **GPUスポット利用** (InvokeAI/Modal) で画像生成の高コストを最適化
- **Edgeストレージ＆CDN** (R2) でメディアコストを最小化

---

## 📱 モバイル対応戦略

| フェーズ | 技術 | 備考 |
|---|---|---|
| 初期（0→1） | Web/PWA (Next.js + Stripe決済) | 高速検証、低手数料 (3%) |
| 拡張フェーズ | ネイティブラッパー (Expo/React Native) | UIコード再利用 (~90%)、AppStore露出、15%手数料 |
| 将来的多角化 | ネイティブ限定機能 (オフライン, BGM) | 収益性向上（LTV最大化） |

---

## 💰 収益化・課金戦略

### プラン設計（仮）

| プラン | 月額 | 特典内容（上限） |
|---|---|---|
| Lite | $4.99 | 月4回配信 (画像+音声) |
| Standard | $9.99 | 月12回配信 |
| Premium | $19.99 | 毎日配信 + 商用音声ライセンス |
| Enterprise | 要相談 | API利用、商用画像利用 |

### コスト最適化

- **バッチ生成・キャッシュ活用** (画像・音声)
- **Stripe/Paddle決済** (Web版) で決済手数料を抑制
- App Storeはユーザー数拡大後、Small Business Tier（15%）に収める

---

## ⚖️ 二次利用・ライセンス管理

- **利用規約に明記:** 非商用利用のみ無料、商用は有料ライセンス必須
- **音声API商用契約（ElevenLabs Professional）**で商用許諾可能
- **画像生成モデルライセンス** (Stable Diffusion, DALL·E) を明示管理

---

## 🚀 開発ロードマップ（簡略版）

### Phase 0（〜3ヶ月）

- Next.js PWA MVPローンチ
- LangGraphでPrompt生成アルゴリズム確立
- ユーザー検証・収益化テスト (Stripe)

### Phase 1（〜6ヶ月）

- PWA成熟・ユーザー数拡大
- コスト最適化 (バッチ処理)
- ClickHouse導入・データ分析環境構築

### Phase 2（〜12ヶ月）

- ネイティブラッピング版リリース (Expo)
- 商用ライセンス拡張
- エンタープライズプラン提供開始

---

## 📌 成功要因とリスク

### 成功要因

- 明確な差別化（知的・静寂なUX、ナラティブ重視）
- 初期検証速度と低コスト (PWA/Web)
- AI生成物の二次利用収益化

### リスク

- 生成コストの管理が不適切だと収益を圧迫
- 商用ライセンス管理・著作権明記の不備による法的リスク

---

## 🎯 結論

- **開発速度・柔軟性・収益性**の観点でPWA→ネイティブ追加が最適戦略
- **TS×Pythonの組合せ**でAIフローとフロント連携が最も効率的
- **二次利用ポリシーを明確化**することでリスク回避と収益多角化が可能

これらを踏まえた上で開発を推進することが、Wabi-Sabi-Wisdomを成功に導くベストプラクティスである。
