# docker-idastatus

Dockerized version of the idastatus Django project

## Description

One can run the Django app, idastatus, on its own, not utilizing Docker.  If that is your desired development environment, you can work within the idastatus directory and ignore the Docker files.  All changes made can be commit and tested from outside docker

## Build and run instructions

Building and running this app in Docker is fairly straightforward.  Requirements to develop in this containerized environment include:

* Have the Docker Desktop application installed and running.  It takes a few minutes to fire up, so make sure you start that up first.

That's all the software you need to have installed prior to running the Docker environment.  All necessary software will be installed into the Docker containers.

To create the containers and run the Django applications...

* Clone this repo to your Macintosh and go to the root directory of the repo.
* First we need to build the containers with docker-compose build
* Then bring the containers up with docker-compose up

The containers are now running, both the web service and the database service.  You can start your browser and go to the web page:

    http://127.0.0.1:8000/

At this point you will see that you have no stations.  This is because we haven't applied an initial data load from a fixture file.  

Execute the following commands from the bash prompt at the root of the idastatus project

    docker-idastatus/idastatus
    docker-compose exec web python manage.py loaddata stations/fixtures/initial_station_data.json

At this point you should be able to reload the home web page from the following URL and see the home page of the idastatus project...

    http://127.0.0.1:8000/

To connect to the container, you can do the following:

    docker ps -a

From the results of that command, you can get the Container ID (the first column in the results) of container to which you want to connect.  Then:

    docker exec -it container_id bash

This will run a bash shell on that container and log you into it as root.  Then, execute any commands you wish or use the following to connect to a database with the psql client.

    psql --username=db_username database_name

## Deploying to a remote server

NOTE: a more robust Continuous Integration / Continuous Deployment (CI/CD) system will be implemeted at a later date.

A makefile is provided in the root of this repository.  That makefile contains the targets and command for deploying the collection of containers.  The targets of the Makefile are:

* help

    This make target will print all the targets in this makefile

* getrepo

    This target will clone the git repo to the local directory.  It will get the master branch from the docker-idstatus repo in the ProjectIDA workspace.

* build

    This target will build the images and containers needed

* run

    This target runs the needed containers

* loaddata

    This target runs the needed fixtures to perform the initial data load for the database

* clean

    This target shuts down all containers, removes the containers and images, and then deletes the git repository

* all
    This target will run the getrepo, build, run, and loaddata targets

The procedure to deploy this continer collection is as follow:

* Check out the docker-idastatus repo on the install server

        git clone <https://github.com/ProjectIDA/docker-idastatus.git>

* Move into the repo directory

        cd docker-idastatus

* Build and run the containers

        make all

* Test the API service from another machine

        <http://idastatus-dev.ucsd.edu:8000/api/stations/>