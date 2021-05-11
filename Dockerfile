FROM python:3.9-slim

LABEL maintainer="jmutuku95@gmail.com" Name=CurrencyExchangeApp Version=0.0.1

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

RUN apt-get update -y && apt-get upgrade -y && apt-get install build-essential -y

COPY . /app/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt


EXPOSE 8000

RUN rm /bin/sh && ln -s /bin/bash /bin/sh


ENTRYPOINT [ "/bin/bash", "./docker-entrypoint.sh"]
