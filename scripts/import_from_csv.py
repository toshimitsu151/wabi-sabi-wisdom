#!/usr/bin/env python3
"""
CSVファイルから古典文学データをデータベースにインポートするスクリプト
"""

import csv
import os
from datetime import datetime

from dotenv import load_dotenv
from supabase import Client, create_client

# 環境変数読み込み
load_dotenv()

def determine_source_type(period, theme):
    """時代とテーマからsource_typeを決定"""
    if '神話' in period or '古事記' in period:
        return 'japanese_classic'
    elif '仏教' in theme or '浄土' in theme or '禅' in theme:
        return 'buddhism'
    elif '武士道' in theme or '武' in theme or '剣' in theme:
        return 'bushido'
    elif '儒' in theme or '学問' in theme or '修養' in theme:
        return 'confucianism'
    elif '詩歌' in theme or '俳句' in theme or '歌' in theme:
        return 'poetry'
    elif '道' in theme or '哲学' in theme:
        return 'taoism'
    else:
        return 'japanese_classic'

def create_english_title(title_ja):
    """日本語タイトルから英語タイトルを生成"""
    # 主要作品の英語タイトルマッピング
    title_mapping = {
        '古事記': 'Kojiki',
        '日本書紀': 'Nihon Shoki',
        '古今和歌集': 'Kokinshū',
        '枕草子': 'Makura no Sōshi',
        '源氏物語': 'The Tale of Genji',
        '方丈記': 'Hōjōki',
        '徒然草': 'Tsurezuregusa',
        '奥の細道': 'The Narrow Road to the Deep North',
        '葉隠': 'Hagakure',
        '五輪書': 'The Book of Five Rings',
        '論語と算盤': 'The Analects and the Abacus',
        '学問のすゝめ': 'An Encouragement of Learning',
        '武士道': 'Bushido: The Soul of Japan',
        '吾輩は猫である': 'I Am a Cat',
        '春と修羅': 'Spring and Asura',
        '善の研究': 'An Inquiry into the Good',
        '河童': 'Kappa',
        '智恵子抄': 'Chieko\'s Sky',
        '一握の砂': 'A Handful of Sand',
        '君死にたまふこと勿れ': 'Thou Shalt Not Die',
    }
    
    return title_mapping.get(title_ja, title_ja)

def create_english_author(author_ja):
    """日本語著者名から英語著者名を生成"""
    # 主要著者の英語名マッピング
    author_mapping = {
        '太安万侶': 'Ō no Yasumaro',
        '舎人親王': 'Toneri Shinnō',
        '紀貫之': 'Ki no Tsurayuki',
        '清少納言': 'Sei Shōnagon',
        '紫式部': 'Murasaki Shikibu',
        '鴨長明': 'Kamo no Chōmei',
        '吉田兼好': 'Yoshida Kenkō',
        '松尾芭蕉': 'Matsuo Bashō',
        '山本常朝': 'Yamamoto Tsunetomo',
        '宮本武蔵': 'Miyamoto Musashi',
        '渋沢栄一': 'Shibusawa Eiichi',
        '福沢諭吉': 'Fukuzawa Yukichi',
        '新渡戸稲造': 'Nitobe Inazō',
        '夏目漱石': 'Natsume Sōseki',
        '宮沢賢治': 'Miyazawa Kenji',
        '西田幾多郎': 'Nishida Kitarō',
        '芥川龍之介': 'Akutagawa Ryūnosuke',
        '高村光太郎': 'Takamura Kōtarō',
        '石川啄木': 'Ishikawa Takuboku',
        '与謝野晶子': 'Yosano Akiko',
    }
    
    return author_mapping.get(author_ja, author_ja)

def import_from_csv():
    """CSVファイルからデータをインポート"""
    
    # Supabaseクライアント初期化
    supabase: Client = create_client(
        os.getenv("SUPABASE_URL"),
        os.getenv("SUPABASE_SERVICE_KEY")
    )
    
    csv_filename = 'catalog_data.csv'
    
    if not os.path.exists(csv_filename):
        print(f"❌ CSVファイル '{csv_filename}' が見つかりません")
        return
    
    works_to_insert = []
    
    with open(csv_filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            # 既存データとの重複チェック
            existing = supabase.table('classical_wisdom').select('id').eq('source_title_ja', row['title']).execute()
            if existing.data:
                print(f"⏭️ スキップ: {row['title']} (既に存在)")
                continue
            
            # source_typeを決定
            source_type = determine_source_type(row['period'], row['theme'])
            
            # 英語タイトルと著者名を生成
            title_en = create_english_title(row['title'])
            author_en = create_english_author(row['author'])
            
            # テーマタグを分割
            theme_tags = [tag.strip() for tag in row['theme'].split('・')]
            
            # 感情タグを推定
            emotion_tags = []
            if '愛' in row['theme'] or '恋' in row['theme']:
                emotion_tags.append('love')
            if '美' in row['theme']:
                emotion_tags.append('beauty')
            if '無常' in row['theme']:
                emotion_tags.append('melancholy')
            if '勇気' in row['theme'] or '義' in row['theme']:
                emotion_tags.append('courage')
            if '慈悲' in row['theme'] or '慈愛' in row['theme']:
                emotion_tags.append('compassion')
            if '旅' in row['theme']:
                emotion_tags.append('wanderlust')
            if '信仰' in row['theme']:
                emotion_tags.append('faith')
            if '自由' in row['theme']:
                emotion_tags.append('freedom')
            
            # スタイルタグを推定
            style_tags = []
            if '詩歌' in row['theme'] or '俳句' in row['theme']:
                style_tags.append('poetic')
            if '哲学' in row['theme']:
                style_tags.append('philosophical')
            if '歴史' in row['theme']:
                style_tags.append('historical')
            if '風刺' in row['theme']:
                style_tags.append('satirical')
            if '随想' in row['title'] or '随筆' in row['title']:
                style_tags.append('essay')
            
            # 難易度を推定
            difficulty_level = 3  # デフォルト
            if int(row['year']) < 1000:
                difficulty_level = 5
            elif int(row['year']) < 1600:
                difficulty_level = 4
            elif int(row['year']) < 1900:
                difficulty_level = 3
            else:
                difficulty_level = 2
            
            work_data = {
                'source_type': source_type,
                'source_title_ja': row['title'],
                'source_title_en': title_en,
                'author_ja': row['author'],
                'author_en': author_en,
                'period': row['period'],
                'year_estimate': int(row['year']),
                'era': row['period'],  # 簡略化
                'publication_year': int(row['year']),
                'copyright_status': 'public_domain',
                'original_text': f"{row['title']}の冒頭部分",  # プレースホルダー
                'english_translation': f"Opening passage of {title_en}",  # プレースホルダー
                'theme_tags': theme_tags,
                'emotion_tags': emotion_tags,
                'style_tags': style_tags,
                'difficulty_level': difficulty_level,
                'quality_score': 1.0
            }
            
            works_to_insert.append(work_data)
    
    print(f"📊 インポート対象: {len(works_to_insert)}件")
    
    if works_to_insert:
        try:
            # データを挿入
            for work in works_to_insert:
                result = supabase.table('classical_wisdom').insert(work).execute()
                print(f"✅ Inserted: {work['source_title_ja']} by {work['author_ja']}")
            
            print(f"\n🎉 {len(works_to_insert)}件のデータを正常にインポートしました！")
            
            # 挿入されたデータを確認
            result = supabase.table('classical_wisdom').select('*').execute()
            print(f"📈 Total records in classical_wisdom: {len(result.data)}")
            
        except Exception as e:
            print(f"❌ Error inserting data: {e}")
    else:
        print("ℹ️ インポート対象のデータがありません")

if __name__ == "__main__":
    import_from_csv() 