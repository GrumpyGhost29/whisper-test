FROM python:3.11-bookworm
USER root

RUN pip install -U openai-whisper
RUN apt update && apt install -y ffmpeg
RUN mkdir -p /app

WORKDIR /app

COPY audio_test.m4a .
RUN whisper audio_test.m4a --model large --language de

COPY . /app
