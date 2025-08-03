
# 金言AI配信アルゴリズム仕様書（ベクトルマッチング方式）

## 概要

本ドキュメントは、ユーザー心理プロファイルに基づいた金言推薦を行うためのAI配信アルゴリズム仕様である。本アルゴリズムは、オンボーディング質問やユーザー行動ログから算出された心理ベクトルと、金言データベース側の意味論的特徴ベクトルとを比較し、最適な金言を選出する。

---

## 1. システム構成概要

```
[ユーザーアプリ] 
    ↓（Onboarding回答）
[心理ベクトル生成エンジン] 
    ↓
[推薦AIエンジン]
    → 金言DB（意味ベクトル付与済み）
    ↓
[推薦結果キャッシュ] 
    ↓（表示/音声/キャラ非同期）
[フロントエンド]
```

---

## 2. ユーザープロファイルベクトル設計

### 2.1 特徴ベクトル構成例

| カテゴリ | 特徴名 | 型 | 説明 |
|----------|--------|----|------|
| Emotion | calmness_level | float (0-1) | 情緒安定度 |
| Openness | abstract_reflection | float | 哲学的メッセージ適合性 |
| Style | poetic_preference | float | 詩的文体への親和性 |
| Motivation | autonomy_score | float | 自律志向 |
| Interaction | extroversion_flag | bool | 外向性フラグ |
| Curiosity | novelty_preference | float | 新奇性志向 |
| Risk | stability_bias | float | 安定志向（変化嫌い度） |

---

## 3. 金言ベクトル構成

| フィールド | 型 | 説明 |
|------------|----|------|
| source_id | str | 出典ID |
| theme_tags | List[str] | 意味カテゴリ（例: 忍耐, 信念, 時間） |
| language_style | str | 文体種別（詩的, 直線的, 隠喩的など） |
| emotion_vector | List[float] | 感情成分埋め込み |
| latent_embedding | List[float] | 意味論的埋め込み（transformer系で生成） |

※ latent_embedding は、SBERT, OpenAI Embedding, Bedrock Titan 等により生成

---

## 4. 類似度計算ロジック

```python
score = (
    cosine_similarity(user.latent_profile, quote.latent_embedding) * 0.4 +
    emotion_match(user, quote) * 0.2 +
    style_alignment(user, quote) * 0.15 +
    novelty_weight(user, quote) * 0.1 +
    theme_bias_score(user, quote) * 0.1 +
    randomization_temperature * 0.05
)
```

- `cosine_similarity`: 埋め込み間の意味類似
- `emotion_match`: calm/active/sad等の感情マッチ
- `style_alignment`: 文体の一致度
- `novelty_weight`: 新奇性重視ユーザー向け多様化係数
- `theme_bias_score`: ユーザー関心タグと金言テーマの交差数
- `randomization_temperature`: 温度設定（0.1〜0.3）で日替わり要素確保

---

## 5. 配信フロー

1. 毎朝 5:00 JST にユーザーごとに心理ベクトルをもとにスコアリング
2. 上位10件を Redis などにキャッシュ
3. そのうちの1件を 7:00 JST に Push通知（or 開封時に即時提示）
4. 音声・キャラクター生成は非同期（ボタン押下後 or 裏で先行処理）

---

## 6. 学習・改善フィードバックループ

| ログ要素 | 活用方法 |
|----------|----------|
| 開封ログ | 評価スコア最適化（開封率向上） |
| お気に入り保存 | ユーザー好みの再学習 |
| スキップ/無反応 | 類似性低下学習 |
| フィードバックボタン | 明示的ベクトル補正（任意） |

---

## 7. セキュリティ・プライバシー

- プロファイルベクトルは非公開、DB暗号化済み
- マッチングアルゴリズムはサーバーサイド限定（クライアント非公開）
- GDPRおよび日本の個人情報保護法に準拠

---

## 8. 使用モデル例

- ベクトル生成：`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
- 類似度算出：`faiss` or `Chroma` or `Bedrock Embedding Retriever`
- サービス基盤：FastAPI + Supabase + CDNエッジ推論（音声）

---
