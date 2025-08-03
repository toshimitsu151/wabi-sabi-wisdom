"""
Supabaseクライアントとユーティリティ関数
"""
import os
from typing import Dict, List, Optional, Any
from dotenv import load_dotenv
from supabase import create_client, Client

# 環境変数を読み込み
load_dotenv('.env')

class SupabaseManager:
    """Supabase接続とデータ操作を管理するクラス"""
    
    def __init__(self):
        """Supabaseクライアントを初期化"""
        self.url = os.getenv('NEXT_PUBLIC_SUPABASE_URL')
        self.key = os.getenv('SUPABASE_SERVICE_ROLE_KEY')
        
        if not self.url or not self.key:
            raise ValueError("NEXT_PUBLIC_SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY must be set in .env")
        
        self.client: Client = create_client(self.url, self.key)
    
    def test_connection(self) -> bool:
        """接続テスト"""
        try:
            # 簡単なクエリで接続をテスト
            result = self.client.table('users').select('id').limit(1).execute()
            print("✅ Supabase接続成功")
            return True
        except Exception as e:
            print(f"❌ Supabase接続エラー: {e}")
            return False
    
    def insert_aozora_works(self, works: List[Dict[str, Any]]) -> bool:
        """青空文庫著作物データを挿入"""
        try:
            result = self.client.table('aozora_works').insert(works).execute()
            print(f"✅ {len(works)}件の著作物データを挿入しました")
            return True
        except Exception as e:
            print(f"❌ 著作物データ挿入エラー: {e}")
            return False
    
    def insert_quotes(self, quotes: List[Dict[str, Any]]) -> bool:
        """金言データを挿入"""
        try:
            result = self.client.table('quotes').insert(quotes).execute()
            print(f"✅ {len(quotes)}件の金言データを挿入しました")
            return True
        except Exception as e:
            print(f"❌ 金言データ挿入エラー: {e}")
            return False
    
    def get_aozora_works(self, limit: int = 100) -> List[Dict[str, Any]]:
        """青空文庫著作物データを取得"""
        try:
            result = self.client.table('aozora_works').select('*').limit(limit).execute()
            return result.data
        except Exception as e:
            print(f"❌ 著作物データ取得エラー: {e}")
            return []
    
    def update_target_flag(self, work_id: str, target_flag: bool) -> bool:
        """ターゲティングフラグを更新"""
        try:
            result = self.client.table('aozora_works').update(
                {'target_flag': target_flag}
            ).eq('work_id', work_id).execute()
            return True
        except Exception as e:
            print(f"❌ ターゲティングフラグ更新エラー: {e}")
            return False
    
    def get_target_works(self) -> List[Dict[str, Any]]:
        """ターゲティングフラグが立った著作物を取得"""
        try:
            result = self.client.table('aozora_works').select('*').eq('target_flag', True).execute()
            return result.data
        except Exception as e:
            print(f"❌ ターゲット著作物取得エラー: {e}")
            return []
    
    def insert_cultural_contexts(self, contexts: List[Dict[str, Any]]) -> bool:
        """文化的背景データを挿入"""
        try:
            result = self.client.table('cultural_contexts').insert(contexts).execute()
            print(f"✅ {len(contexts)}件の文化的背景データを挿入しました")
            return True
        except Exception as e:
            print(f"❌ 文化的背景データ挿入エラー: {e}")
            return False
    
    def insert_supported_languages(self, languages: List[Dict[str, Any]]) -> bool:
        """サポート言語データを挿入"""
        try:
            result = self.client.table('supported_languages').insert(languages).execute()
            print(f"✅ {len(languages)}件のサポート言語データを挿入しました")
            return True
        except Exception as e:
            print(f"❌ サポート言語データ挿入エラー: {e}")
            return False

def create_supabase_manager() -> SupabaseManager:
    """SupabaseManagerインスタンスを作成"""
    return SupabaseManager()

# テスト用
if __name__ == "__main__":
    manager = create_supabase_manager()
    if manager.test_connection():
        print("Supabase接続テスト成功")
    else:
        print("Supabase接続テスト失敗") 