FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app