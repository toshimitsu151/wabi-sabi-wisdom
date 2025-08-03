# Dynamic Source Selection Algorithm (DSSA)  
_Wabi‑Sabi‑Wisdom ― AI 原典セレクター設計書_

> **Version**: 1.0  **Generated**: 2025‑08‑02 10:39

---

## 1. ゴール

- **枯渇ゼロ**: 事前リスト不要。都度 AI がパブリックドメイン・コーパス全体から最適な一節を発掘  
- **高共感**: ユーザーのテーマ／気分／文体に合致  
- **法的安全**: 1926 年以前没・出版 100 年超の作品のみ自動フィルタ  
- **ブラックボックス**: 内部パラメータ・検索シードを秘匿し模倣を困難化

---

## 2. アーキテクチャ概要

```
User
 ↓ (テーマ・気分)
┌────────────┐
│ Prompt Gen │ ①自然言語→検索クエリ
└────────────┘
           ↓
┌──────────────────────┐
│  原典検索レイヤ        │
│  a. BM25 (5k)         │
│  b. SBERT rerank (200)│
│  c. CrossEnc (20)     │
└──────────────────────┘
           ↓ ②
┌──────────────┐
│ Validation    │ ハードフィルタ/類似度閾値
└──────────────┘
           ↓
┌──────────────┐
│ Persona化     │ キャラ生成＋現代訳
└──────────────┘
           ↓
Deliver to UX
```

---

## 3. プロンプトテンプレート

```text
System:
You are a Japanese literature scholar AI tasked with selecting
one public-domain Japanese source excerpt (<=200 chars)
that matches ALL conditions below.

Conditions:
1. Theme: { user_theme }
2. Emotional Tone: { mood_tag }
3. Era Limit: Before 1931 (Showa early)
4. Copyright: Author died >=70y ago OR text published >=100y ago
5. Readability: Avoid overly obscure kanji clusters
Return exactly one JSON payload:

##META##
{"title":"","author":"","year":1900,"era":"Meiji","excerpt":""}
```

---

## 4. コーパス & メタデータ

| ソース | 規模 | 更新頻度 | 主なカラム |
|--------|------|----------|------------|
| 青空文庫 | ~20k 作品 | 月次スクレイプ | `title, author, death_year, pub_year, text` |
| 国会図書館デジコレ (PD) | ~5k | 半期 | 追加同上 |
| 万葉集 / 古典全集等 | 固定 | 不定期 | 時代・章句番号 |
| **FAISS + ES Hybrid Index** | 約 40M センテンス | 月次リビルド | Dense / Sparse vector |

---

## 5. スコアリング & 探索

```
total_score = 0.6 * cosine(user_vec, text_vec)
            + 0.25 * diversity_boost
            + 0.15 * quality_decay
```

- **温度 τ** = `base * (1.3 – engagement_ratio)`  
  - 保存率が低いユーザー ⇒ τ↑ ⇒ 探索寄り  
- **Diversity Boost**: 未読テーマ率・時代バランス  
- **Quality Decay**: 流行依存抑止 & 連投防止

---

## 6. 二重ガード

1. **Hard Filter**  
   - 著作権年・NG キーワード・ユーザーブロックテーマ  
2. **Explain‑Match**  
   - GPT が「類似度=0.83, era=Edo」など内部説明を自己検証  
   - 0.7 未満なら自動リトライ

---

## 7. オンライン学習

| 周期 | 処理 | モデル |
|------|------|--------|
| 即時 | Skip / Save → Bandit reward | Thompson Sampling |
| 日次 | ユーザー埋め込み更新 | LightFM |
| 週次 | 全体蒸留 | GPT‑4o → Distilled on‑device |

---

## 8. プライバシー & ブラックボックス化

- **HMAC(uid, secret) + Date** で乱数 seed  
- 最終 Softmax サンプリングは **オンデバイス** 小型モデル  
- 公開は「レイヤー構造」まで。重み & 閾値はサーバー secretos

---

## 9. ペルソナ生成フロー

```
原典 excerpt  → GPT
  + 用户語彙プロファイル
  + キャラ色彩/性格タグ
─────────────►   AI Persona Card
                     ↳ 現代訳 / 英訳
                     ↳ TTS Prompt
```

---

### 結論

**DSSA** により  
- 枯渇ゼロ & 著作権安全  
- 毎回 “一期一会” の原典発掘  
- ユーザー共感を外さない高精度マッチング  

を同時実現。WSW の中核ブラックボックスとして機能します。
