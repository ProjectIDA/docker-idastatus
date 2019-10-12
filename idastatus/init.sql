create user postgres with encrypted password 'password';
grant all privileges on database postgres to postgres;

CREATE DATABASE idastatus;
create user idadb with encrypted password 'password';
grant all privileges on database idastatus to idadb;