FROM python:3.11-slim as requirements-stage

WORKDIR /tmp

RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

RUN python3 -m virtualenv /tmp/venv

RUN /tmp/venv/bin/pip install -r requirements.txt

FROM python:3.11-slim

WORKDIR /code
COPY --from=requirements-stage /tmp/venv /venv

COPY . /code

CMD ["/venv/bin/python3", "app.py"]
