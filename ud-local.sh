#!/bin/bash

export PATH=/usr/local/bin:$PATH

cd /usr/local/ida/docker-idastatus
/bin/make run
/bin/make loadfixtures
