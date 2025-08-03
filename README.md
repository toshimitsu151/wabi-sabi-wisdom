# Wabi-Sabi-Wisdom

AI-powered wisdom application that delivers personalized Japanese classical quotes with AI-generated characters and voice synthesis.

## 🌟 Concept

Wabi-Sabi-Wisdom provides "intellectual and serene experiences" through psychological profiling and narrative-driven content delivery. Each experience is unique and unrepeatable (一期一会 - Ichigo Ichie).

## 🚀 Features

- **Psychological Profiling**: 10-question assessment for personalized content
- **AI-Generated Characters**: Unique anime-style characters for each quote
- **Voice Synthesis**: Character-matched voice narration
- **Japanese Classical Wisdom**: Curated quotes from Aozora Bunko
- **Global Audience**: Multi-language support for international users

## 🛠️ Tech Stack

### Frontend
- **Next.js 13** (App Router) + **TypeScript**
- **Tailwind CSS** + **shadcn/ui**
- **PWA** (Progressive Web App)

### Backend
- **Supabase** (PostgreSQL + Auth + Edge Functions)
- **Python 3.12** + **LangGraph** (AI processing)
- **pgvector** (Vector search)

### AI Generation
- **Stable Diffusion XL** (Image generation)
- **ElevenLabs** (Voice synthesis)
- **Claude-3/Gemini** (LLM processing)

## 📦 Installation

### Prerequisites
- Node.js 18+
- Python 3.12+
- uv (Python package manager)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/toshimitsu151/wabi-sabi-wisdom.git
cd wabi-sabi-wisdom
```

2. **Install Python dependencies**
```bash
uv sync
```

3. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your Supabase credentials
```

4. **Test Supabase connection**
```bash
uv run python scripts/test_supabase_connection.py
```

## 🗂️ Project Structure

```
Wabi-Sabi-Wisdom/
├── .cursor/rules/          # Cursor IDE rules
├── docs/                   # Project documentation
├── scripts/
│   ├── aozora/            # Aozora Bunko data processing
│   ├── utils/             # Utility functions
│   └── test_*.py          # Test scripts
├── pyproject.toml         # Python project config
└── uv.lock               # Python dependencies lock
```

## 🚦 Development Phases

### Phase 0 (MVP) - 0-3 months
- [x] Supabase setup and integration
- [ ] Aozora Bunko data import
- [ ] Basic quote delivery system
- [ ] User authentication

### Phase 1 (Foundation) - 3-6 months
- [ ] Psychological profiling enhancement
- [ ] AI character generation
- [ ] Voice synthesis integration

### Phase 2 (Native) - 6-12 months
- [ ] iOS/Android native apps
- [ ] Advanced features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

For support and questions, please open an issue on GitHub.

---

**Wabi-Sabi-Wisdom** - Finding beauty in imperfection and wisdom in classical Japanese literature.
