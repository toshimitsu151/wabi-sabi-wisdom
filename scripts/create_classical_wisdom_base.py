#!/usr/bin/env python3
"""
古典文学の基本データを手動で作成するスクリプト
NDL APIでは古典文学の原典が取得できないため、手動で基本データを作成
"""

import os
from datetime import datetime

from dotenv import load_dotenv
from supabase import Client, create_client

# 環境変数読み込み
load_dotenv()

def create_classical_wisdom_base():
    """古典文学の基本データを作成"""
    
    # Supabaseクライアント初期化
    supabase: Client = create_client(
        os.getenv("SUPABASE_URL"),
        os.getenv("SUPABASE_SERVICE_KEY")
    )
    
    # 古典文学の基本データ
    classical_works = [
        # 日本古典文学
        {
            'source_type': 'poetry',
            'source_title_ja': '万葉集',
            'source_title_en': 'Man\'yōshū',
            'author_ja': '大伴家持ら',
            'author_en': 'Ōtomo no Yakamochi et al.',
            'period': '奈良時代',
            'year_estimate': 759,
            'era': '天平宝字',
            'author_death_year': 785,
            'publication_year': 759,
            'copyright_status': 'public_domain',
            'original_text': 'あかねさす紫野行き標野行き野守は見ずや君が袖振る',
            'english_translation': 'In the purple fields, in the marked fields, does the field guard not see you waving your sleeves?',
            'theme_tags': ['愛', '自然', '美'],
            'emotion_tags': ['longing', 'beauty'],
            'style_tags': ['poetic', 'metaphorical'],
            'difficulty_level': 5,
            'quality_score': 1.0
        },
        {
            'source_type': 'poetry',
            'source_title_ja': '古今和歌集',
            'source_title_en': 'Kokinshū',
            'author_ja': '紀貫之ら',
            'author_en': 'Ki no Tsurayuki et al.',
            'period': '平安時代',
            'year_estimate': 905,
            'era': '延喜',
            'author_death_year': 946,
            'publication_year': 905,
            'copyright_status': 'public_domain',
            'original_text': '春すぎて夏来にけらし白妙の衣ほすてふ天の香具山',
            'english_translation': 'Spring has passed and summer seems to have come, for the white robes are being dried on Mount Kaguyama.',
            'theme_tags': ['自然', '季節', '美'],
            'emotion_tags': ['nostalgia', 'beauty'],
            'style_tags': ['elegant', 'seasonal'],
            'difficulty_level': 4,
            'quality_score': 1.0
        },
        {
            'source_type': 'japanese_classic',
            'source_title_ja': '徒然草',
            'source_title_en': 'Tsurezuregusa',
            'author_ja': '吉田兼好',
            'author_en': 'Yoshida Kenkō',
            'period': '鎌倉時代',
            'year_estimate': 1330,
            'era': '元徳',
            'author_death_year': 1350,
            'publication_year': 1330,
            'copyright_status': 'public_domain',
            'original_text': 'つれづれなるままに、日暮らし、硯にむかひて、心にうつりゆくよしなしごとを、そこはかとなく書きつくれば、あやしうこそものぐるほしけれ',
            'english_translation': 'In my idleness, sitting at my inkstone all day long, I jot down whatever comes into my mind, and it is strange indeed how maddening it becomes.',
            'theme_tags': ['時間', '美', '道'],
            'emotion_tags': ['contemplation', 'melancholy'],
            'style_tags': ['reflective', 'philosophical'],
            'difficulty_level': 5,
            'quality_score': 1.0
        },
        {
            'source_type': 'japanese_classic',
            'source_title_ja': '方丈記',
            'source_title_en': 'Hōjōki',
            'author_ja': '鴨長明',
            'author_en': 'Kamo no Chōmei',
            'period': '鎌倉時代',
            'year_estimate': 1212,
            'era': '建暦',
            'author_death_year': 1216,
            'publication_year': 1212,
            'copyright_status': 'public_domain',
            'original_text': 'ゆく河の流れは絶えずして、しかももとの水にあらず。よどみに浮ぶうたかたは、かつ消えかつ結びて、久しくとゞまりたるためしなし',
            'english_translation': 'The flowing river never stops and yet the water never stays the same. Foam that floats on stagnant pools, now vanishing, now forming, never stays long.',
            'theme_tags': ['時間', '無常', '道'],
            'emotion_tags': ['melancholy', 'acceptance'],
            'style_tags': ['philosophical', 'metaphorical'],
            'difficulty_level': 4,
            'quality_score': 1.0
        },
        {
            'source_type': 'japanese_classic',
            'source_title_ja': '枕草子',
            'source_title_en': 'Makura no Sōshi',
            'author_ja': '清少納言',
            'author_en': 'Sei Shōnagon',
            'period': '平安時代',
            'year_estimate': 1000,
            'era': '長保',
            'author_death_year': 1025,
            'publication_year': 1000,
            'copyright_status': 'public_domain',
            'original_text': '春はあけぼの。やうやうしろくなりゆく山ぎは、すこしあかりて、むらさきだちたる雲のほそくたなびきたる',
            'english_translation': 'In spring it is the dawn that is most beautiful. As the light creeps over the hills, their outlines are dyed a faint red and wisps of purplish cloud trail over them.',
            'theme_tags': ['自然', '美', '季節'],
            'emotion_tags': ['appreciation', 'beauty'],
            'style_tags': ['elegant', 'descriptive'],
            'difficulty_level': 3,
            'quality_score': 1.0
        },
        {
            'source_type': 'japanese_classic',
            'source_title_ja': '源氏物語',
            'source_title_en': 'The Tale of Genji',
            'author_ja': '紫式部',
            'author_en': 'Murasaki Shikibu',
            'period': '平安時代',
            'year_estimate': 1008,
            'era': '寛弘',
            'author_death_year': 1014,
            'publication_year': 1008,
            'copyright_status': 'public_domain',
            'original_text': 'いづれの御時にか、女御、更衣あまたさぶらひたまひけるなかに、いとやむごとなき際にはあらぬが、すぐれて時めきたまふありけり',
            'english_translation': 'In a certain reign there was a lady not of the first rank whom the emperor loved more than any of the others.',
            'theme_tags': ['愛', '美', '宮廷'],
            'emotion_tags': ['romance', 'elegance'],
            'style_tags': ['narrative', 'courtly'],
            'difficulty_level': 5,
            'quality_score': 1.0
        },
        
        # 中国古典文学
        {
            'source_type': 'confucianism',
            'source_title_ja': '論語',
            'source_title_en': 'Analects of Confucius',
            'author_ja': '孔子',
            'author_en': 'Confucius',
            'period': '春秋時代',
            'year_estimate': -500,
            'era': '春秋',
            'author_death_year': -479,
            'publication_year': -500,
            'copyright_status': 'public_domain',
            'original_text': '学而時習之、不亦説乎',
            'english_translation': 'To learn and at due times to repeat what one has learnt, is that not after all a pleasure?',
            'theme_tags': ['学習', '喜び', '道'],
            'emotion_tags': ['joy', 'satisfaction'],
            'style_tags': ['direct', 'philosophical'],
            'difficulty_level': 3,
            'quality_score': 1.0
        },
        {
            'source_type': 'taoism',
            'source_title_ja': '老子',
            'source_title_en': 'Tao Te Ching',
            'author_ja': '老子',
            'author_en': 'Laozi',
            'period': '春秋時代',
            'year_estimate': -500,
            'era': '春秋',
            'author_death_year': -500,
            'publication_year': -500,
            'copyright_status': 'public_domain',
            'original_text': '道可道、非常道。名可名、非常名',
            'english_translation': 'The way that can be spoken of is not the constant way; the name that can be named is not the constant name.',
            'theme_tags': ['道', '哲学', '無'],
            'emotion_tags': ['mystery', 'contemplation'],
            'style_tags': ['mystical', 'paradoxical'],
            'difficulty_level': 5,
            'quality_score': 1.0
        },
        {
            'source_type': 'taoism',
            'source_title_ja': '荘子',
            'source_title_en': 'Zhuangzi',
            'author_ja': '荘子',
            'author_en': 'Zhuangzi',
            'period': '戦国時代',
            'year_estimate': -300,
            'era': '戦国',
            'author_death_year': -286,
            'publication_year': -300,
            'copyright_status': 'public_domain',
            'original_text': '北冥有魚、其名為鯤。鯤之大、不知其幾千里也',
            'english_translation': 'In the northern darkness there is a fish and his name is K\'un. The K\'un is so huge I don\'t know how many thousand li he measures.',
            'theme_tags': ['自然', '自由', '道'],
            'emotion_tags': ['wonder', 'freedom'],
            'style_tags': ['imaginative', 'metaphorical'],
            'difficulty_level': 5,
            'quality_score': 1.0
        },
        {
            'source_type': 'confucianism',
            'source_title_ja': '孟子',
            'source_title_en': 'Mencius',
            'author_ja': '孟子',
            'author_en': 'Mencius',
            'period': '戦国時代',
            'year_estimate': -300,
            'era': '戦国',
            'author_death_year': -289,
            'publication_year': -300,
            'copyright_status': 'public_domain',
            'original_text': '性善説',
            'english_translation': 'Human nature is good.',
            'theme_tags': ['人性', '善', '道'],
            'emotion_tags': ['optimism', 'hope'],
            'style_tags': ['philosophical', 'ethical'],
            'difficulty_level': 4,
            'quality_score': 1.0
        },
        
        # 仏教古典
        {
            'source_type': 'buddhism',
            'source_title_ja': '法句経',
            'source_title_en': 'Dhammapada',
            'author_ja': '釈迦牟尼',
            'author_en': 'Buddha',
            'period': '古代インド',
            'year_estimate': -500,
            'era': '古代',
            'author_death_year': -483,
            'publication_year': -500,
            'copyright_status': 'public_domain',
            'original_text': '諸悪莫作、衆善奉行、自浄其意、是諸仏教',
            'english_translation': 'Refrain from all evil, cultivate what is good, purify your mind - this is the teaching of the Buddhas.',
            'theme_tags': ['善', '道', '浄化'],
            'emotion_tags': ['peace', 'clarity'],
            'style_tags': ['direct', 'spiritual'],
            'difficulty_level': 3,
            'quality_score': 1.0
        },
        {
            'source_type': 'buddhism',
            'source_title_ja': '正法眼蔵',
            'source_title_en': 'Shōbōgenzō',
            'author_ja': '道元',
            'author_en': 'Dōgen',
            'period': '鎌倉時代',
            'year_estimate': 1231,
            'era': '寛喜',
            'author_death_year': 1253,
            'publication_year': 1231,
            'copyright_status': 'public_domain',
            'original_text': '身心脱落、脱落身心',
            'english_translation': 'Body and mind dropped off, dropped off body and mind.',
            'theme_tags': ['禅', '悟り', '道'],
            'emotion_tags': ['enlightenment', 'clarity'],
            'style_tags': ['zen', 'paradoxical'],
            'difficulty_level': 5,
            'quality_score': 1.0
        },
        
        # 武士道古典
        {
            'source_type': 'bushido',
            'source_title_ja': '葉隠',
            'source_title_en': 'Hagakure',
            'author_ja': '山本常朝',
            'author_en': 'Yamamoto Tsunetomo',
            'period': '江戸時代',
            'year_estimate': 1716,
            'era': '享保',
            'author_death_year': 1719,
            'publication_year': 1716,
            'copyright_status': 'public_domain',
            'original_text': '武士道とは死ぬことと見つけたり',
            'english_translation': 'The way of the warrior is found in death.',
            'theme_tags': ['義', '死', '道'],
            'emotion_tags': ['determination', 'acceptance'],
            'style_tags': ['direct', 'martial'],
            'difficulty_level': 4,
            'quality_score': 1.0
        },
        {
            'source_type': 'bushido',
            'source_title_ja': '五輪書',
            'source_title_en': 'The Book of Five Rings',
            'author_ja': '宮本武蔵',
            'author_en': 'Miyamoto Musashi',
            'period': '江戸時代',
            'year_estimate': 1645,
            'era': '正保',
            'author_death_year': 1645,
            'publication_year': 1645,
            'copyright_status': 'public_domain',
            'original_text': '千日の稽古を鍛とし、万日の稽古を練とす',
            'english_translation': 'A thousand days of training to develop, ten thousand days of training to polish.',
            'theme_tags': ['修行', '道', '技'],
            'emotion_tags': ['discipline', 'perseverance'],
            'style_tags': ['martial', 'practical'],
            'difficulty_level': 4,
            'quality_score': 1.0
        }
    ]
    
    try:
        # 既存データをクリア（オプション）
        # supabase.table('classical_wisdom').delete().neq('id', '00000000-0000-0000-0000-000000000000').execute()
        
        # データを挿入
        for work in classical_works:
            result = supabase.table('classical_wisdom').insert(work).execute()
            print(f"Inserted: {work['source_title_ja']} by {work['author_ja']}")
        
        print(f"\n✅ {len(classical_works)}件の古典文学データを挿入しました！")
        
        # 挿入されたデータを確認
        result = supabase.table('classical_wisdom').select('*').execute()
        print(f"Total records in classical_wisdom: {len(result.data)}")
        
    except Exception as e:
        print(f"❌ Error inserting data: {e}")

if __name__ == "__main__":
    create_classical_wisdom_base() 