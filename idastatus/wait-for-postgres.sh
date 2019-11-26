#!/bin/sh
# wait-for-postgres.sh

set -e

host="$1"
shift
user="$1"
shift
pass="$1"
shift
cmd="$@"

until PGPASSWORD=$pass psql -h "$host" -U "$user" -d postgres -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd
