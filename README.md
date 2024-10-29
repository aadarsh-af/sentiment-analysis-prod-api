# Sentiment Analysis

This project utilizes Python FastAPI and transformers to return sentiment to the input sentence provided by a user. I have used docker to deploy this API. The docker container uses python-3.11-slim version of Python. The API will deploy `distilbert/distilbert-base-uncased-finetuned-sst-2-english` model from HuggingFace. This model is used to reduce latency in the application with great accuracy of results. This API is secured with

## Ubuntu Installation Steps

### Clone this repository

```bash
git clone https://github.com/aadarsh-af/sentiment-analysis-prod-api && cd sentiment-analysis-prod-api
```

### Install docker and docker-compose

```bash
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo curl -L "https://github.com/docker/compose/releases/download/$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep 'tag_name' | cut -d'"' -f4)/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/bin/docker-compose
clear
docker-compose --version
```

### Configure AUTH_TOKEN in `example.env`

A client can access the API only if they provide correct `AUTH_TOKEN`

```ini
AUTH_TOKEN=your_auth_token
```

Then, change the filename to `.env` using command: `mv example.env .env`

### Build the Sentiment Analysis API

Takes around 350 seconds to build.

```bash
sudo docker-compose --build
```

### Start the API with Docker Container (in background with detached mode)

```bash
sudo docker-compose up -d
```

### Access the API

```bash
curl http://0.0.0.0:8000/
```

### Access Docker Container

```bash
sudo docker ps --filter name=sentiment-analysis-api
```

### Stop the API Docker Container

```bash
sudo docker stop $(sudo docker ps -aq --filter name=sentiment-analysis-api)
```
