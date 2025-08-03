"""
Supabase接続テストスクリプト
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.utils.supabase_client import create_supabase_manager
from scripts.utils.data_models import create_sample_data, DataValidator

def test_supabase_connection():
    """Supabase接続テスト"""
    print("🔗 Supabase接続テストを開始...")
    
    try:
        manager = create_supabase_manager()
        
        # 接続テスト
        if not manager.test_connection():
            print("❌ 接続テスト失敗")
            return False
        
        print("✅ 接続テスト成功")
        return True
        
    except Exception as e:
        print(f"❌ 接続エラー: {e}")
        return False

def test_sample_data_insertion():
    """サンプルデータ挿入テスト"""
    print("\n📝 サンプルデータ挿入テストを開始...")
    
    try:
        manager = create_supabase_manager()
        sample_data = create_sample_data()
        
        # 既存データをチェック
        existing_contexts = manager.client.table('cultural_contexts').select('context_key').execute()
        existing_languages = manager.client.table('supported_languages').select('code').execute()
        
        existing_context_keys = [ctx['context_key'] for ctx in existing_contexts.data]
        existing_language_codes = [lang['code'] for lang in existing_languages.data]
        
        # 文化的背景データ挿入テスト（重複チェック）
        print("文化的背景データをチェック中...")
        new_contexts = [ctx for ctx in sample_data['cultural_contexts'] 
                       if ctx['context_key'] not in existing_context_keys]
        
        if new_contexts:
            if manager.insert_cultural_contexts(new_contexts):
                print(f"✅ {len(new_contexts)}件の文化的背景データを挿入しました")
            else:
                print("❌ 文化的背景データ挿入失敗")
                return False
        else:
            print("✅ 文化的背景データは既に存在します")
        
        # サポート言語データ挿入テスト（重複チェック）
        print("サポート言語データをチェック中...")
        new_languages = [lang for lang in sample_data['supported_languages'] 
                        if lang['code'] not in existing_language_codes]
        
        if new_languages:
            if manager.insert_supported_languages(new_languages):
                print(f"✅ {len(new_languages)}件のサポート言語データを挿入しました")
            else:
                print("❌ サポート言語データ挿入失敗")
                return False
        else:
            print("✅ サポート言語データは既に存在します")
        
        return True
        
    except Exception as e:
        print(f"❌ データ挿入エラー: {e}")
        return False

def test_data_retrieval():
    """データ取得テスト"""
    print("\n📖 データ取得テストを開始...")
    
    try:
        manager = create_supabase_manager()
        
        # 文化的背景データ取得
        contexts = manager.client.table('cultural_contexts').select('*').execute()
        print(f"✅ 文化的背景データ: {len(contexts.data)}件取得")
        
        # サポート言語データ取得
        languages = manager.client.table('supported_languages').select('*').execute()
        print(f"✅ サポート言語データ: {len(languages.data)}件取得")
        
        return True
        
    except Exception as e:
        print(f"❌ データ取得エラー: {e}")
        return False

def main():
    """メイン関数"""
    print("🚀 Supabase連携テスト開始")
    print("=" * 50)
    
    # 接続テスト
    if not test_supabase_connection():
        print("\n❌ 接続テスト失敗 - 環境変数を確認してください")
        return
    
    # サンプルデータ挿入テスト
    if not test_sample_data_insertion():
        print("\n❌ データ挿入テスト失敗")
        return
    
    # データ取得テスト
    if not test_data_retrieval():
        print("\n❌ データ取得テスト失敗")
        return
    
    print("\n" + "=" * 50)
    print("🎉 すべてのテストが成功しました！")
    print("Supabase連携が正常に動作しています。")

if __name__ == "__main__":
    main() 