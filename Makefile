# Make different targets for 

TARGETDIR = docker-idastratus-repo-master
all: getrepo build run loaddata		## the whole enchilada

help:			## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

getrepo:		## get repo, master branch
	rm -rf $(TARGETDIR)
	git clone https://github.com/ProjectIDA/docker-idastatus.git $(TARGETDIR)

build:			## build images and containers
	cd $(TARGETDIR)
	docker-compose build

run:			## start up all containers
	cd $(TARGETDIR)
	docker-compose up -d

loaddata:		## load fixtures into database
	docker-compose exec web python manage.py loaddata stations/fixtures/initial_station_data.json

clean:			## shutdown all containers, remove containers and images, remove repo
	cd $(TARGETDIR)
	docker-compose down
	cd ..
	docker system prune --all --force #use --force to skip y/n confirmation
	rm -rf $(TARGETDIR)
