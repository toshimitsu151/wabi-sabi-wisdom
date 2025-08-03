
# ナラティブ生成エンジン詳細設計書（Vector-Driven Prompt Synthesizer）

## 🎯 目的
10問のユーザー心理質問（2択×3問 + 5段階×7問）によって得られるスコアベクトルから、
意味的な人格記述（ナラティブ）を生成し、金言選定LLMプロンプトへ自然言語として組み込む中間層の設計。

---

## 🧩 全体フロー

```
[ユーザー回答]
   ↓
[スコアベクトル（長さ10）]
   ↓
[心理因子抽出（3〜4軸）]
   ↓
[カテゴリスコアマッピング]
   ↓
[意味単位スロット抽出]
   ↓
[ナラティブ構文テンプレートへ差し込み]
   ↓
[自然言語プロンプト出力（英語）]
```

---

## 🔢 スコアベクトル定義

- Q1〜Q3：Binary（0/1）
- Q4〜Q10：Likert（1〜5）

例：
```json
[1, 0, 1, 4, 2, 3, 5, 1, 3, 2]
```

---

## 🧠 心理因子マッピングロジック（例）

| 因子名     | 対応質問       | スコア範囲 | 解釈             |
|------------|----------------|-------------|------------------|
| 内向性     | Q1, Q2, Q4     | 0〜7        | 6以上：強い内向 |
| 精神性     | Q3, Q5, Q10    | 0〜11       | 9以上：高精神性 |
| 感受性     | Q6, Q7, Q8     | 3〜15       | 12以上：高感受性|
| 認知柔軟性 | Q9             | 1〜5        | 1-2：低い        |

※ 各因子はカテゴリスコアとして正規化（Min-Max）

---

## 🧰 スロットベーステンプレート

### ● テンプレート構文例
```
This user [Slot1:知的態度], 
and tends to [Slot2:感情傾向]. 
They are [Slot3:精神特性] and [Slot4:行動様式].
```

### ● スロット例

- Slot1（知的態度）:
  - "seeks solitude and reflection"
  - "values outward expression and action"

- Slot2（感情傾向）:
  - "process emotion inwardly and deeply"
  - "move past feeling with reason"

- Slot3（精神特性）:
  - "spiritually curious"
  - "focused on logic and clarity"

- Slot4（行動様式）:
  - "methodical and reserved"
  - "energetic and expressive"

---

## 🧪 アルゴリズム概要（擬似コード）

```python
def generate_narrative(vector):
    profile = analyze_vector(vector)  # 心理軸への正規化とカテゴリ分類
    slot1 = slot_lookup("intellect", profile["introversion"])
    slot2 = slot_lookup("emotion", profile["sensitivity"])
    slot3 = slot_lookup("spirituality", profile["spirituality"])
    slot4 = slot_lookup("action", profile["flexibility"])

    return f"This user {slot1}, and tends to {slot2}. They are {slot3} and {slot4}."
```

---

## 🔐 ユニーク性
- 同一ベクトルでも、スロット選択は複数パターン存在（= 揺らぎ）
- ナラティブ文は文体を変えてランダム生成（LLM補正可）

---

## 🧩 応用拡張
- 時間帯/天気などの外部文脈情報も追加スロット化可能
- キャラクター生成や金言テーマ選定にも同スロット連携可
