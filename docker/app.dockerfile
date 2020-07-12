FROM python:3-alpine

LABEL version="1.0"
LABEL description="Personal website frontend Dockerfile"
LABEL maintainer="jzlotek@gmail.com"

WORKDIR /flask/app

COPY requirements.txt ./

RUN apk update\
    && apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev\
    && pip install --no-cache-dir -r requirements.txt\
    && apk del .build-deps

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w" , "2", "-b", "0.0.0.0:5000", "app:app"]