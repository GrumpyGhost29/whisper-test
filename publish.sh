#!/bin/sh

# Define the model directory and file path
MODEL_DIR="models"
MODEL_FILE="$MODEL_DIR/large.pt"

# Create the model directory if it doesn't exist
mkdir -p $MODEL_DIR

# Check if the model file already exists
if [ -f "$MODEL_FILE" ]; then
    echo "Model already exists at $MODEL_FILE, skipping download."
else
    # Download the model if it doesn't exist
    echo "Model not found. Downloading..."
    wget https://openaipublic.azureedge.net/main/whisper/models/e4b87e7e0bf463eb8e6956e646f1e277e901512310def2c24bf0e11bd3c28e9a/large.pt -O $MODEL_FILE
fi

# Build and push the image
docker buildx build --platform linux/arm64 -t grumpyghost29/images:whisper --push --progress=plain .
