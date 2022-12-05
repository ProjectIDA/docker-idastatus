#!/bin/bash

export PATH=/usr/local/bin:$PATH

cd /usr/local/ida/docker-idastatus
/bin/make build
/bin/make run

python manage.py makemigrations
python manage.py migrate 
/bin/make loadfixtures

gunicorn idastatus.wsgi --bind 0.0.0.0:80  --timeout 3000"    
