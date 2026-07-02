FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1
ENV OLLAMA_HOST=127.0.0.1:11434
ENV OLLAMA_MODEL=qwen2.5:0.5b

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl \
    tesseract-ocr \
    libgl1 \
    libglib2.0-0 \
    sqlite3 \
    zstd \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://ollama.com/install.sh | sh

COPY . /app

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN chmod +x /app/start.sh

EXPOSE 7860

CMD ["/app/start.sh"]