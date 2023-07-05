FROM postgres:15

ENV POSTGRES_PASSWORD          $POSTGRES_ADMIN_PASSWORD
ENV POSTGRES_IDA_USER          idadb
ENV POSTGRES_IDA_PASSWORD      $POSTGRES_IDA_PASSWORD
ENV POSTGRES_IDA_DB            idastatus

COPY init.sql /docker-entrypoint-initdb.d/
