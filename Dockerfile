# Базовый образ с Python 3.9
FROM python:3.9-slim as builder

# Установка системных зависимостей
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Установка зависимостей
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Финальный образ
FROM python:3.9-slim

# Безопасность: создаем непривилегированного пользователя
RUN useradd -m botuser && \
    mkdir /app && \
    chown botuser:botuser /app

WORKDIR /app

# Копируем зависимости из builder
COPY --from=builder /root/.local /home/botuser/.local
COPY --chown=botuser:botuser . .

# Переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    PATH="/home/botuser/.local/bin:${PATH}"

# Права для статики
RUN mkdir -p /app/static && \
    chown botuser:botuser /app/static

# Переключаем пользователя
USER botuser

# Сборка статики
RUN python manage.py collectstatic --noinput

# Команда запуска
CMD ["gunicorn", "botari.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4", "--timeout", "120"]
