FROM python:3.7-slim-buster

WORKDIR /ida/code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2
RUN apt-get update \
    && apt-get -y install apt-utils \
    && apt-get -y install build-essential gcc python3-dev musl-dev \
    && apt-get -y install postgresql-client \
    && apt-get -y install bash \
    && apt-get -y install vim \
    && pip install psycopg2-binary

COPY requirements.txt /ida/code/

RUN pip install --upgrade pip

RUN pip install --trusted-host pypy.org --trusted-host files.pythonhosted.org -r requirements.txt

COPY . /ida/code/

COPY init.sql /docker-entrypoint-initdb.d/
