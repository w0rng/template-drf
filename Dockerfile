FROM python:3.9.7-slim-buster

WORKDIR /app
ARG DEBUG=False

RUN pip install --no-cache-dir --upgrade pip && pip install pipenv
COPY Pipfile* /
RUN pipenv install --dev --deploy --system --ignore-pipfile

COPY src /app
