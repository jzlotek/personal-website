# personal-website

This is the repo for my personal site. It is deployed on a personal VPS with Docker.

![Deploy to docker hub](https://github.com/jzlotek/personal-website/workflows/Deploy%20to%20docker%20hub/badge.svg)

## Setting Up

- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`

## Developing

- `python app.py --debug  # for auto reloading`

## Deploying Locally

### Docker

This snippet is how to deploy this site directly without downloading it.
It is build using GitHub actions to push to Docker Hub.
Watchtower is used to automatically detect and relaunch the docker image on a VPS.
More about watchtower here https://github.com/containrrr/watchtower.

Save this as `docker-compose.yml` and run: `docker-compose up --detach` to deploy.

```yaml
version: '3'
services:
  website-frontend:
    image: "jzlotek/personal-website"
    restart: unless-stopped
    container_name: "website-frontend"
    ports:
      - 5000:5000
  watchtower:
    image: "containrrr/watchtower"
    restart: unless-stopped
    container_name: "watchtower"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
```

### Without Docker

- `source venv/bin/activate`
- `python app.py --port {PORT}`
