#!/bin/sh
docker build -t whisper .
docker compose -f docker-compose-dev.yaml run whisper
