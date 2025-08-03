
# 英文音声生成アルゴリズム設計書（キャラクタープロンプト連携）

## 🎯 目的

金言および生成キャラクターのイメージに合致するトーン・声質・テンポ・感情を備えた英文音声メッセージを生成し、ユーザーに情緒的な体験を提供する。

---

## 🧩 全体フロー

```
[1. 金言データ（詩的英文 + 出典）]
[2. キャラクタープロンプト（性格・雰囲気）]
      ↓
[3. ナレーションスタイル構成エンジン]
      ↓
[4. TTS API呼び出し（Edge用）]
      ↓
[5. CDNキャッシュ or 非同期返却]
```

---

## 🔤 入力要素の例

```json
{
  "quote": "Even a broken moon reflects the sun's grace.",
  "character": {
    "gender": "female",
    "tone": "gentle, poetic",
    "tempo": "slow",
    "emotion": "hopeful",
    "style": "soft whisper-like, ASMR-inspired"
  }
}
```

---

## 🧠 音声プロンプト構築テンプレート（例）

```
Read the following line in a gentle and poetic female voice.
Use a soft and breathy tone, at a slow pace.
Express subtle hope and warmth.

"Even a broken moon reflects the sun's grace."
```

---

## 🔧 実装構造（擬似コード）

```python
def build_voice_prompt(quote, character):
    return f'''
    Read the following line in a {character["tone"]} {character["gender"]} voice.
    Use a {character["style"]} style, at a {character["tempo"]} pace.
    Express {character["emotion"]} feeling.

    "{quote}"
    '''

def synthesize_audio(prompt_text):
    return call_tts_engine(prompt_text, voice_model="edge-tts" or "ElevenLabs")
```

---

## 🎙️ 声質マッピングルール（簡略版）

| キャラ属性         | 音声パラメータ例                                    |
|--------------------|-----------------------------------------------------|
| 女性・繊細          | whispery, slow, soft tone                          |
| 男性・論理的        | neutral, mid-speed, clear pronunciation            |
| 精神性高い          | ethereal, calm, reverb-light voice                 |
| 感受性高い          | breathy, emotional rise/fall intonation            |

---

## 📦 配信戦略

- 音声は有料ユーザーに限定
- サーバー側で音声非同期生成後、CDNキャッシュ配信
- ユーザーがボタン押下 → サーバーがキャッシュ確認 → 未生成ならバックグラウンド生成 → 完了通知

---

## 🧩 拡張構想

- 多言語対応（将来的に日本語 or 仏語ナレーションなど）
- 声優モデルごとのキャラクター性切り替え（商用契約後）
- メッセージスレッド読み上げ機能（物語形式）

---

## 📌 推奨TTSエンジン

- **ElevenLabs API**（高品質だが有料）
- **Edge TTS (Microsoft)**（無料、声優風モデルあり）
- **PlayHT, Coqui TTS** なども選択肢

