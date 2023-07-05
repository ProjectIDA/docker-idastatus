CREATE DATABASE $POSTGRES_IDA_DB;
create user $POSTGRES_IDA_USER with encrypted password $POSTGRES_IDA_PASSWORD
grant all privileges on database $POSTGRES_IDA_DB to $POSTGRES_IDA_USER;
