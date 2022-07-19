FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y netcat-openbsd gcc && \
    apt-get clean && \
    pip install -r requirements.txt  && \
    apt purge -y gcc && \
    apt autoremove -y && \
    rm -rf /var/lib/apt/lists/*

COPY . .
