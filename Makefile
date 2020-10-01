# Make different targets for 

TARGETDIR = idastatus
CONTAINERLIST = dockeridastatus_web_1 dockeridastatus_db_1 dockeridastatus_web_migrations_1
IMAGELIST = dockeridastatus_web dockeridastatus_web_migrations
SERVICELIST = web db web_migrations

all:
buildall: build run loadfixtures	## build the whole enchilada
cleancontainers: stop rmcontainers	## clean containers
cleanall: stop rmcontainers rmimages	## clean the whole enchilada

ls:			## Show list of make targets 
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

build:			## build images and containers
	docker-compose build

run:			## start up all containers
	docker-compose up -d

runfg:			## start up all containers in the foreground
	docker-compose up

stop:			## stop all containers
	docker-compose stop $(SERVICELIST)

rmcontainers:		## remove all stopped containers
	cd $(TARGETDIR)
	docker container rm $(CONTAINERLIST)

rmimages:		## remove all images
	docker image rm $(IMAGELIST)

loadfixtures:		## load fixtures into database
	cd $(TARGETDIR)
	docker-compose exec web python manage.py loaddata stations/fixtures/initial_instype_data.json
	docker-compose exec web python manage.py loaddata stations/fixtures/initial_network_data.json
	docker-compose exec web python manage.py loaddata stations/fixtures/initial_station_data.json
	docker-compose exec web python manage.py loaddata stations/fixtures/initial_chan_data.json
	docker-compose exec web python manage.py loaddata stations/fixtures/initial_stage_data.json

execpsql:		## log into postgres with psql
	docker exec -it dockeridastatus_db_1 psql idastatus idadb

execsh:			## log into web container
	docker exec -it dockeridastatus_web_1 bash

sanitycheck:		## perform a basic curl to test API
	curl http://localhost:8000/api/stations/?format=json
