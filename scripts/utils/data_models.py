"""
データモデルとバリデーション
"""
import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional


@dataclass
class AozoraWork:
    """青空文庫著作物データモデル"""
    work_id: str
    title_ja: str
    author_ja: str
    title_en: Optional[str] = None
    author_en: Optional[str] = None
    year: Optional[int] = None
    era: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[List[str]] = None
    target_flag: bool = False
    content_ja: Optional[str] = None
    content_en: Optional[str] = None
    cultural_context: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """辞書形式に変換"""
        return {
            'work_id': self.work_id,
            'title_ja': self.title_ja,
            'title_en': self.title_en,
            'author_ja': self.author_ja,
            'author_en': self.author_en,
            'year': self.year,
            'era': self.era,
            'category': self.category,
            'tags': self.tags or [],
            'target_flag': self.target_flag,
            'content_ja': self.content_ja,
            'content_en': self.content_en,
            'cultural_context': self.cultural_context
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'AozoraWork':
        """辞書からインスタンスを作成"""
        return cls(**data)

@dataclass
class Quote:
    """金言データモデル"""
    work_id: str
    original_text: str
    english_translation: str
    poetic_english: Optional[str] = None
    cultural_context: Optional[str] = None
    meaning_explanation: Optional[str] = None
    tags: Optional[List[str]] = None
    target_audience: Optional[List[str]] = None
    difficulty_level: int = 1
    
    def to_dict(self) -> Dict[str, Any]:
        """辞書形式に変換"""
        return {
            'work_id': self.work_id,
            'original_text': self.original_text,
            'english_translation': self.english_translation,
            'poetic_english': self.poetic_english,
            'cultural_context': self.cultural_context,
            'meaning_explanation': self.meaning_explanation,
            'tags': self.tags or [],
            'difficulty_level': self.difficulty_level,
            'target_audience': self.target_audience or []
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Quote':
        """辞書からインスタンスを作成"""
        return cls(**data)

@dataclass
class CulturalContext:
    """文化的背景データモデル"""
    context_key: str
    title_en: str
    description_en: str
    historical_period: Optional[str] = None
    cultural_significance: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """辞書形式に変換"""
        return {
            'context_key': self.context_key,
            'title_en': self.title_en,
            'description_en': self.description_en,
            'historical_period': self.historical_period,
            'cultural_significance': self.cultural_significance
        }

@dataclass
class SupportedLanguage:
    """サポート言語データモデル"""
    code: str
    name_en: str
    name_native: str
    is_active: bool = True
    
    def to_dict(self) -> Dict[str, Any]:
        """辞書形式に変換"""
        return {
            'code': self.code,
            'name_en': self.name_en,
            'name_native': self.name_native,
            'is_active': self.is_active
        }

class DataValidator:
    """データバリデーション用クラス"""
    
    @staticmethod
    def validate_aozora_work(work: AozoraWork) -> bool:
        """青空文庫著作物データのバリデーション"""
        if not work.work_id or not work.title_ja or not work.author_ja:
            return False
        if work.year and (work.year < 1800 or work.year > 2024):
            return False
        return True
    
    @staticmethod
    def validate_quote(quote: Quote) -> bool:
        """金言データのバリデーション"""
        if not quote.work_id or not quote.original_text or not quote.english_translation:
            return False
        if quote.difficulty_level < 1 or quote.difficulty_level > 5:
            return False
        return True
    
    @staticmethod
    def validate_cultural_context(context: CulturalContext) -> bool:
        """文化的背景データのバリデーション"""
        if not context.context_key or not context.title_en or not context.description_en:
            return False
        return True
    
    @staticmethod
    def validate_supported_language(language: SupportedLanguage) -> bool:
        """サポート言語データのバリデーション"""
        if not language.code or not language.name_en or not language.name_native:
            return False
        return True

def create_sample_data() -> Dict[str, List]:
    """サンプルデータを作成"""
    cultural_contexts = [
        CulturalContext(
            context_key="zen-philosophy",
            title_en="Zen Philosophy",
            description_en="Buddhist philosophy emphasizing meditation and mindfulness",
            historical_period="Ancient to Modern"
        ),
        CulturalContext(
            context_key="bushido",
            title_en="Bushido (Way of the Warrior)",
            description_en="Samurai code of conduct emphasizing honor and discipline",
            historical_period="Edo Period"
        ),
        CulturalContext(
            context_key="wabi-sabi",
            title_en="Wabi-Sabi",
            description_en="Japanese aesthetic finding beauty in imperfection and transience",
            historical_period="Medieval to Modern"
        )
    ]
    
    supported_languages = [
        SupportedLanguage("en", "English", "English"),
        SupportedLanguage("ja", "Japanese", "日本語"),
        SupportedLanguage("fr", "French", "Français"),
        SupportedLanguage("de", "German", "Deutsch"),
        SupportedLanguage("es", "Spanish", "Español")
    ]
    
    return {
        'cultural_contexts': [ctx.to_dict() for ctx in cultural_contexts],
        'supported_languages': [lang.to_dict() for lang in supported_languages]
    } 