import os
import gdown

def download_with_gdown(file_id, output_path):
    if os.path.exists(output_path):
        print(f"✅ {output_path} уже существует. Пропускаю загрузку.")
        return True

    try:
        url = f"https://drive.google.com/uc?id={file_id}"
        print(f"📥 Начинаю загрузку: {output_path}")
        gdown.download(url, output_path, quiet=False, fuzzy=True)
        print(f"✅ Загрузка завершена: {output_path}")
        return True
    except Exception as e:
        print(f"❌ Ошибка при загрузке файла {output_path}: {e}")
        return False

def main():
    os.makedirs("data", exist_ok=True)

    # ID файлов из Google Drive
    csv_downloaded = download_with_gdown("18DaxAerTDvQlyq24_UfndYr6G6kBdAii", "data/recommendations.csv")
    parquet_downloaded = download_with_gdown("1MS2YEQYaBj99cxBWWeI97S1Rg_eBQsJx", "data/ratings.parquet")

    if csv_downloaded and parquet_downloaded:
        print("🎉 Все файлы готовы — можно запускать FastAPI!")
    else:
        print("⚠️ Один или несколько файлов не загружены — сервер может работать некорректно.")

main()