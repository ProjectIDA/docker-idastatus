# Make different targets for 

DOCKERCOMPOSEFILE = docker-compose.prod.yml
TARGETDIR = idastatus
CONTAINERLIST = dockeridastatus_web_1 dockeridastatus_db_1 dockeridastatus_web_migrations_1 dockeridastatus_web_proxies_1
IMAGELIST = dockeridastatus_web dockeridastatus_web_migrations
SERVICELIST = web db web_migrations web_proxies

all:
buildall: build run loadfixtures	## build the whole enchilada
cleancontainers: stop rmcontainers	## clean containers
cleanall: stop rmcontainers rmimages	## clean the whole enchilada

ls:			## Show list of make targets 
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

lscontainers:		## Show list of idastatus containers
	docker container ls -f name=dockeridastatus

build:			## build images and containers
	docker-compose --file $(DOCKERCOMPOSEFILE) build $(SERVICELIST)

run:			## start up all containers
	docker-compose --file $(DOCKERCOMPOSEFILE) up -d $(SERVICELIST)

runfg:			## start up all containers in the foreground
	docker-compose --file $(DOCKERCOMPOSEFILE) up $(SERVICELIST)

stop:			## stop all containers
	docker-compose --file $(DOCKERCOMPOSEFILE) stop $(SERVICELIST)

rmcontainers:		## remove all stopped containers
	cd $(TARGETDIR)
	docker container rm $(CONTAINERLIST)

rmimages:		## remove all images
	docker image rm $(IMAGELIST)

loadfixtures:		## load fixtures into database
	cd $(TARGETDIR)
	docker-compose --file $(DOCKERCOMPOSEFILE) exec web python manage.py loaddata stations/fixtures/initial_instype_data.json
	docker-compose --file $(DOCKERCOMPOSEFILE) exec web python manage.py loaddata stations/fixtures/initial_network_data.json
	docker-compose --file $(DOCKERCOMPOSEFILE) exec web python manage.py loaddata stations/fixtures/initial_station_data.json
	docker-compose --file $(DOCKERCOMPOSEFILE) exec web python manage.py loaddata stations/fixtures/initial_chan_data.json
	docker-compose --file $(DOCKERCOMPOSEFILE) exec web python manage.py loaddata stations/fixtures/initial_stage_data.json

execpsql:		## log into postgres with psql
	docker exec -it dockeridastatus_db_1 psql idastatus idadb

execsh:			## log into web container
	docker exec -it dockeridastatus_web_1 bash
