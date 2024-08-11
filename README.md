# Usage
1. Install [docker desktop](https://www.docker.com/products/docker-desktop/)
2. Add audio files to the `/inputs` folder
```bash
docker build -t whisper .
docker-compose run whisper
```
