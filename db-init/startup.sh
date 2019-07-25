#!/bin/bash


>&2 echo "Postgres is up - executing startup.sh"

python3 manage.py migrate --no-input

python3 manage.py loaddata stations/fixtures/initial_data.json
