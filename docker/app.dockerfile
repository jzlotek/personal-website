FROM python:3-alpine

LABEL version="1.0"
LABEL description="Personal website frontend Dockerfile"
LABEL maintainer="jzlotek@gmail.com"

RUN apk update
RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev

WORKDIR /flask/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "./app.py"]