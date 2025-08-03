
# 金言AIアルゴリズム詳細設計書（意味解説付き・3段階出力方式）

## 🎯 目的

ユーザーの心理傾向（10問診断結果）をもとに、最適な日本の金言を選出し、詩的英文・原文・出典に加えて、  
その言葉が伝えたい「意味・背景」をナラティブに基づき生成する。  
感情・知性・学習を同時に満たす"深い体験"を提供することが本アルゴリズムの使命である。

---

## 🧩 全体処理フロー

```
[1] ユーザー心理ベクトル（10問回答）
      ↓
[2] プロファイルナラティブ生成
      ↓
[3] 金言選定アルゴリズム（原典検索）
      ↓
[4] 詩的英文生成（意訳）
      ↓
[5] 意味・背景ナラティブ生成（LLM）
      ↓
[6] 4段階出力：
     A. 詩的英文
     B. 原文（日本語）
     C. 出典情報
     D. 意味・背景ナラティブ（Context Meaning）
```

---

## 🖋️ 出力構造（4層フォーマット）

### A. Poetic English Message

```text
“You may feel fractured, but the light still finds you.”
```

- ナラティブに応じた感情的・比喩的な再構成
- LLMプロンプト例：

```text
Rewrite the following Japanese quote for a modern, poetic, emotionally receptive audience.
The tone should reflect quiet hope and graceful resilience.
Original: 欠けた月にも陽の恩恵は差し込む。
```

---

### B. 日本語原文

```text
欠けた月にも陽の恩恵は差し込む。
```

---

### C. 出典情報

| 項目 | 内容 |
|------|------|
| 著者 | 西田 幾多郎 |
| 書名 | 『善の研究』 |
| 年代 | 1911年（明治44年） |
| 種別 | 哲学書 |

---

### D. 意味・背景ナラティブ（LLM生成）

```text
Even if you feel imperfect or broken, you are still worthy of grace, beauty, and light.
This phrase encourages acceptance of flaws and recognizes the dignity within every stage of one's being.
It's a reminder that value isn't lost in imperfection—it is often revealed there.
```

---

## 💡 技術構成

- LLMエンジン：ChatGPT / Claude 等
- 意訳再構成＋意味解釈：プロンプト工学で制御
- 出典抽出：ナラティブ → タグ → 原典検索（事前orオンデマンド）
- 表示：フロントは4段階形式で順次開示可（段階的UX）

---

## 🔁 JSON構造（例）

```json
{
  "quote_poetic_en": "You may feel fractured, but the light still finds you.",
  "quote_original_ja": "欠けた月にも陽の恩恵は差し込む。",
  "meaning_en": "Even if you feel imperfect or broken, you are still worthy of grace, beauty, and light...",
  "source": {
    "author": "西田 幾多郎",
    "title": "善の研究",
    "year": "1911",
    "type": "哲学書"
  }
}
```

---

## 📌 差別化ポイント

| 要素 | 差別化 |
|------|--------|
| 金言選定 | DB事前準備不要のJust-In-Time抽出型 |
| 詩的意訳 | ユーザー心理ベースのPrompt Driven |
| 意味解釈 | 共感・自己投影を促すストーリーナラティブ付き |
| 表示形式 | 4段階出力構造（詩・原文・出典・意味）で情報深度に応じたUX |

---

