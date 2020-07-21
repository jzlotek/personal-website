FROM python:3-alpine

LABEL version="1.0"
LABEL description="Personal website frontend Dockerfile"
LABEL maintainer="jzlotek@gmail.com"

WORKDIR /flask/app

COPY requirements.txt ./

RUN apk update\
    && apk add --no-cache --virtual .build-deps gcc g++ python3-dev musl-dev zeromq-dev linux-headers\
    && pip install --no-cache-dir -r requirements.txt\
    && apk del .build-deps

COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]
