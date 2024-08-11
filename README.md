# Usage
1. Install [docker desktop](https://www.docker.com/products/docker-desktop/)
2. Add audio files to the `/storage/inputs` folder
```bash
run.sh
```

# Development
1. Run `publish.sh` to build the docker image, this will download the large model locally, then pass it to docker build via context which then bakes it into the image.
2. Grab a Wissbier, this will take a while.
