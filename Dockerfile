FROM python:3.10-slim-bullseye
LABEL maintainer="salahuddin.org"

ENV PYTHONUNBUFFERED=1
WORKDIR /django

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
