FROM python:3.7-alpine

WORKDIR /ida/code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev postgresql-client

COPY requirements.txt /ida/code/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /ida/code/

CMD [ "./wait-for-postgres.sh", "db"]

CMD [ "./startup.sh" ]
