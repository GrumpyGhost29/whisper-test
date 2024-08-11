FROM python:3.11-bookworm
USER root

RUN mkdir -p /app

RUN pip install -U openai-whisper && \
    apt update && \
    apt install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app
