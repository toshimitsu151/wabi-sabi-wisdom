# Wabi-Sabi-Wisdom

AIが生成するキャラクターと音声合成により、パーソナライズされた日本の古典金言を配信するAI駆動の知恵アプリケーション。

## 🌟 コンセプト

Wabi-Sabi-Wisdomは、心理的プロファイリングとナラティブ駆動のコンテンツ配信により「知的で静寂な体験」を提供します。各体験は唯一無二で再現不可能（一期一会 - Ichigo Ichie）です。

## 🚀 機能

- **心理的プロファイリング**: パーソナライズされたコンテンツのための10問診断
- **AI生成キャラクター**: 各金言に合わせた唯一無二のアニメ風キャラクター
- **音声合成**: キャラクターに合致した音声ナレーション
- **日本の古典知恵**: 青空文庫から厳選された金言
- **グローバル対応**: 国際ユーザー向けの多言語サポート

## 🛠️ 技術スタック

### フロントエンド
- **Next.js 13**（App Router）+ **TypeScript**
- **Tailwind CSS** + **shadcn/ui**
- **PWA**（Progressive Web App）

### バックエンド
- **Supabase**（PostgreSQL + Auth + Edge Functions）
- **Python 3.12** + **LangGraph**（AI処理）
- **pgvector**（ベクトル検索）

### AI生成
- **Stable Diffusion XL**（画像生成）
- **ElevenLabs**（音声合成）
- **Claude-3/Gemini**（LLM処理）

## 📦 インストール

### 前提条件
- Node.js 18+
- Python 3.12+
- uv（Pythonパッケージマネージャー）

### セットアップ

1. **リポジトリをクローン**
```bash
git clone https://github.com/toshimitsu151/wabi-sabi-wisdom.git
cd wabi-sabi-wisdom
```

2. **Python依存関係をインストール**
```bash
uv sync
```

3. **環境変数を設定**
```bash
cp .env.example .env
# .envファイルにSupabase認証情報を編集
```

4. **Supabase接続をテスト**
```bash
uv run python scripts/test_supabase_connection.py
```

## 🗂️ プロジェクト構造

```
Wabi-Sabi-Wisdom/
├── .cursor/rules/          # Cursor IDEルール
├── docs/                   # プロジェクトドキュメント
├── scripts/
│   ├── aozora/            # 青空文庫データ処理
│   ├── utils/             # ユーティリティ関数
│   └── test_*.py          # テストスクリプト
├── pyproject.toml         # Pythonプロジェクト設定
└── uv.lock               # Python依存関係ロック
```

## 🚦 開発フェーズ

### Phase 0（MVP）- 0-3ヶ月
- [x] Supabaseセットアップと統合
- [ ] 青空文庫データインポート
- [ ] 基本的な金言配信システム
- [ ] ユーザー認証

### Phase 1（基盤強化）- 3-6ヶ月
- [ ] 心理的プロファイリング強化
- [ ] AIキャラクター生成
- [ ] 音声合成統合

### Phase 2（ネイティブ展開）- 6-12ヶ月
- [ ] iOS/Androidネイティブアプリ
- [ ] 高度な機能

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています - 詳細は[LICENSE](LICENSE)ファイルを参照してください。

## 🤝 コントリビューション

1. リポジトリをフォーク
2. 機能ブランチを作成（`git checkout -b feature/amazing-feature`）
3. 変更をコミット（`git commit -m '機能追加: 素晴らしい機能を追加'`）
4. ブランチにプッシュ（`git push origin feature/amazing-feature`）
5. プルリクエストを作成

## 📞 サポート

サポートや質問については、GitHubでissueを作成してください。

---

**Wabi-Sabi-Wisdom** - 不完全さの中に美を見出し、日本の古典文学から知恵を見つける。
