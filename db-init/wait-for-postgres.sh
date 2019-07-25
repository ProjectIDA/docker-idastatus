#!/bin/sh

set -e

host="$1"
shift
cmd="$@"

until PGPASSWORD=$POSTGRES_PASSWORD psql --host="$host" --username="idadb" -c '\q' --dbname="idastatus"; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
