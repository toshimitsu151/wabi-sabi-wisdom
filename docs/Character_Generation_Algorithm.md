
# キャラクター画像生成アルゴリズム設計書（金言連携型）

## 🎯 目的

金言生成アルゴリズムの出力（ナラティブ + 金言 + 出典）をもとに、  
詩的・情緒的・象徴的な要素を含んだ**アニメ風キャラクター画像**を自動生成するためのプロンプト構成ルールとフローを定義する。

---

## 🧩 全体フロー

```
[1. ナラティブ文]
[2. 金言メッセージ]
[3. 出典・年代情報]
      ↓
[4. SD生成プロンプト構築エンジン（Prompt Composer）]
      ↓
[5. Stable Diffusion / SDXL API 実行]
      ↓
[6. 画像キャッシュ保存（CDN）]
```

---

## 🔤 入力要素の例

### ● ナラティブ
```text
This user seeks quiet insight and spiritual reflection.
They are emotionally open and value poetic depth.
```

### ● 金言出力
```json
{
  "quote": "Even a broken moon reflects the sun's grace.",
  "original": "欠けた月にも陽の恩恵は差し込む。",
  "author": "西田幾多郎",
  "source": "善の研究",
  "year": "1911"
}
```

---

## 🧠 Prompt Composer 構造（擬似コード）

```python
def compose_character_prompt(narrative, quote_data):
    themes = extract_themes(narrative, quote_data["quote"])
    base_style = "anime, Japanese traditional style, soft lighting"
    symbolic_elements = map_to_symbols(themes)

    return f"A {themes['tone']} anime-style character, wearing {themes['clothing']}, " + \
           f"with {symbolic_elements['scene']}, {symbolic_elements['emotion']}, " + \
           f"representing the idea: '{quote_data['quote']}'"
```

---

## 🎨 プロンプト構成ルール

### ● 主体属性

| 要素           | 説明例                             |
|----------------|----------------------------------|
| 性別           | 感受性: 高 → 女性系, 論理性: 高 → 男性系 |
| 年代           | 明治／大正／昭和初期による衣装・背景調整 |
| 表情           | 感情傾向（Slot2）から導出           |

---

### ● 構文テンプレート（英語）

```
A poetic anime girl in kimono, gazing at a crescent moon.
Cherry blossoms float in the air. Soft watercolor tone.
Symbolizes hope within imperfection. -- Inspired by the quote:
"Even a broken moon reflects the sun's grace."
```

---

### ● シンボル・比喩対応表（一部）

| テーマ           | 表現対象例                                  |
|------------------|-------------------------------------------|
| 不完全美          | 欠けた月, 割れた器, 侘びた庭園                   |
| 精神性            | 瞑想, 線香の煙, 山寺                          |
| 孤独              | 一人の影, 静かな雪景色                        |
| 喜び・希望        | 朝日, 桜吹雪, 光る蝶                          |

---

## 🧰 背景構成要素

- 金言とナラティブにより自動的に「色」「構図」「象徴アイテム」が割り当てられる
- 例：
  - "sun's grace" → 黄金の後光
  - "broken moon" → 三日月 + 青系背景

---

## 🔒 再現性管理と多様性

- 同一金言でも複数テーマが抽出されるため揺らぎあり
- キャラクターは生成後にUUIDでキャッシュ保存（非同期トリガ）

---

## 🧩 拡張構想

- 「キャラの性格」「台詞」「サブプロフィール」の自動生成連動
- キャラの再召喚（再表示）機能
- キャラクターコレクション（図鑑化）

---

## 📌 備考

- 出力は512x512または768x768推奨
- モデルはSD 1.5 または SDXL（anime tuned）
- 生成回数制限：有料ユーザー向けのみに制限可能
