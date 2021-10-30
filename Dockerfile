FROM python:3.9

LABEL version="1.0"
LABEL description="Personal website frontend Dockerfile"
LABEL maintainer="jzlotek@gmail.com"

RUN pip install --no-cache-dir poetry

WORKDIR /code
COPY poetry.lock pyproject.toml /code/

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . /code/

EXPOSE 5000

CMD ["python3", "app.py"]

