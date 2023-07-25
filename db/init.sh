#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username postgres --dbname postgres <<-EOSQL
        CREATE USER idadb;
        CREATE DATABASE idastatus;
        GRANT ALL PRIVILEGES ON DATABASE idastatus TO idadb;
EOSQL

