# Используем официальный образ Python 3.10
FROM python:3.10

# Рабочая директория
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# Скачиваем большие файлы с гугл диска

# Открываем порт
EXPOSE 8000

# Команда запуска
CMD ["sh", "-c", "python download_files.py && uvicorn main:app --host 0.0.0.0 --port 8000"]
#CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000", "main:app"]

