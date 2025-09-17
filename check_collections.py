import os
import json

def check_collection(collection_path):
    print(f"Проверка коллекции: {os.path.basename(collection_path)}")
    
    collection_info_path = os.path.join(collection_path, 'collection_info.json')
    if not os.path.exists(collection_info_path):
        print(f"❌ Отсутствует collection_info.json в {collection_path}")
        return False
    
    preview_path = os.path.join(collection_path, 'preview.png')
    if not os.path.exists(preview_path):
        print(f"❌ Отсутствует preview.png в {collection_path}")
        return False
    
    nft_count = len([f for f in os.listdir(collection_path) if f.endswith('.png') and not f.startswith('preview')])
    metadata_count = len([f for f in os.listdir(collection_path) if f.endswith('_metadata.json')])
    
    print(f"✅ Найдено NFT: {nft_count}")
    print(f"✅ Найдено метаданных: {metadata_count}")
    
    if nft_count != metadata_count:
        print(f"⚠️ Количество NFT и метаданных не совпадает!")
    
    return True

def main():
    collections_path = 'nft_download/collections'
    all_collections = [os.path.join(collections_path, d) for d in os.listdir(collections_path) 
                       if os.path.isdir(os.path.join(collections_path, d))]
    
    successful_collections = []
    failed_collections = []
    
    for collection in all_collections:
        result = check_collection(collection)
        if result:
            successful_collections.append(os.path.basename(collection))
        else:
            failed_collections.append(os.path.basename(collection))
    
    print("\n📊 Итоги проверки:")
    print(f"Успешные коллекции ({len(successful_collections)}): {', '.join(successful_collections)}")
    print(f"Проблемные коллекции ({len(failed_collections)}): {', '.join(failed_collections)}")

if __name__ == '__main__':
    main() 