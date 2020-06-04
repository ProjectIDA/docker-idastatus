create user postgres with encrypted password 'CHANGE_THIS_BEFORE_RUNNING';
grant all privileges on database postgres to postgres;

CREATE DATABASE idastatus;
create user idadb with encrypted password 'CHANGE_THIS_BEFORE_RUNNING';
grant all privileges on database idastatus to idadb;
