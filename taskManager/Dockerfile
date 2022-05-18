FROM python:3.8-slim-buster

WORKDIR /app/task

ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app/task

EXPOSE 8000
