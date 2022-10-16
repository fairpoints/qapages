# syntax = docker/dockerfile:1.4
FROM python:3.10-slim-bullseye

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y --no-install-recommends tini && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements/main.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

RUN mkdir -p /src
COPY src/ /src/
RUN pip install --no-cache-dir --editable /src
COPY tests/ /tests/

WORKDIR /src

