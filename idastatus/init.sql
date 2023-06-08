create user postgres with encrypted password $POSTGRES_USER_PASSWORD
grant all privileges on database postgres to postgres;

DROP DATABASE idastatus;

CREATE DATABASE idastatus;
create user idadb with encrypted password $POSTGRES_USER_PASSWORD
grant all privileges on database idastatus to idadb;
