# Make different targets for 

TARGETDIR = idastatus

all: build run loadfixtures		## the whole enchilada

help:			## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

build:			## build images and containers
	cd $(TARGETDIR)
	docker-compose build

run:			## start up all containers
	cd $(TARGETDIR)
	docker-compose up -d

loadfixtures:		## load fixtures into database
	cd $(TARGETDIR)
	docker-compose exec web python manage.py loaddata stations/fixtures/initial_station_data.json
	docker-compose exec web python manage.py loaddata stations/fixtures/initial_network_data.json

