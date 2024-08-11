#!/bin/sh

# Build and push the image
docker buildx build --platform linux/arm64 -t grumpyghost29/images:whisper --push --progress=plain .
