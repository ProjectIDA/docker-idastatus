#!/bin/bash

export PATH=/usr/local/bin:$PATH

cd /usr/local/ida/docker-idastatus
/bin/make run
aws s3 sync s3://projectida.dcc/fixtures/ ./idastatus/stations/fixtures/
/bin/make loadfixtures
