# 🧩 NFT Parser & Downloader (Alchemy API)

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Requests](https://img.shields.io/badge/requests-HTTP%20client-informational.svg)](https://requests.readthedocs.io/)
[![tqdm](https://img.shields.io/badge/tqdm-progress%20bar-brightgreen.svg)](https://tqdm.github.io/)

Скрипт для выборочного скачивания NFT по популярным коллекциям: метаданные и изображения через **Alchemy API**.  
Сохраняет данные на диск: `collections/<CollectionName>/<token_id>.png` и `<token_id>_metadata.json`, плюс `collection_info.json`.

---

## ✨ Возможности
- Получение `contractMetadata` и `openSea`-поля (включая `floorPrice`) для коллекций.
- Выборка случайных токенов (`random.sample` из диапазона) и выгрузка:
  - метаданных `*_metadata.json`;
  - изображений (через `media[0].gateway`, поддержка IPFS-шлюза).
- Прогресс-бар на скачивание (`tqdm`).
- Скрипт-валидация собранных коллекций: `check_collections.py`.

---

## 🧱 Стек
- **Python 3.10+**
- **requests**, **tqdm**
- (опционально) **web3** — подключено в `requirements.txt`, но не обязательно для текущего сценария.

---

## 📂 Структура
nft_download/
├── nft_downloader.py        
├── check_collections.py      
├── requirements.txt
├── collection_previews/      
└── collections/ 

---

## ⚙️ Быстрый старт (опционально)
> Репозиторий предназначен прежде всего для портфолио. Запуск не обязателен.  
> Если потребуется, ниже — упрощённые команды.

```bash
python3 -m venv venv
source venv/bin/activate           # Windows: venv\Scripts\activate
pip install -r requirements.txt

export ALCHEMY_API_KEY="ваш_ключ"

python nft_downloader.py

python check_collections.py