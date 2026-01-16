FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Устанавливаем зависимости
COPY pyproject.toml ./
RUN pip install --upgrade pip && \
    pip install -e .

# Dev зависимости (опционально)
ARG DEV=false
RUN if [ "$DEV" = "true" ] ; then pip install -e .[dev] ; fi

# Копируем код
COPY ./app ./app

# На случай отсутствия ML модели
RUN mkdir -p ./ml/model && touch ./ml/model/model.pkl

# PYTHONPATH для пакета
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Порт
EXPOSE 8080

# Запуск
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

