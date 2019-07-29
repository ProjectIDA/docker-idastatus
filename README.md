# docker-idastatus
Dockerized version of the idastatus Django project

One can run the Django app, idastatus, on its own, not utilizing Docker.  If that is your desired development environment, you can work within the idastatus directory and ignore the Docker files.  All changes made can be commit and tested from outside docker.

Building and running this app in Docker is fairly straightforward.  Requirements to develop in this containerized environment include:

*    Have the Docker Desktop application installed and running.  It takes a few minutes to fire up, so make sure you start that up first.

That's all the software you need to have installed prior to running the Docker environment.  All necessary software will be installed into the Docker containers.

To create the containers and run the Django applications...

*    Clone this repo to your Macintosh and go to the root directory of the repo.
*    First we need to build the containers with <code>docker-compose build</code>
*    Then bring the containers up with <code>docker-compose up</code>

The containers are now running, both the web service and the database service.  You can start your browser and go to the web page:

*    <code>http://127.0.0.1:8000/</code>

At this point you will get an error from the SQL query <code>SELECT * from stations.station;</code>.  This is because we haven't yet created a database in the db container.  I'll be looking into doing this automatically, but for now we will do this from the command line.

Execute the following commands from the bash prompt at the root of the idastatus project...

*    <code>docker exec docker-idastatus_db_1 psql -U postgres -w -p 5432 --command="CREATE DATABASE idastatus"</code>
*    <code>docker exec docker-idastatus_db_1 psql -U postgres -w -p 5432 --command="create user idadb with encrypted password 'password';"</code>
*    <code>docker exec docker-idastatus_db_1 psql -U postgres -w -p 5432 --command="grant all privileges on database idastatus to idadb;"</code>

This will create the <code>idastatus</code> database and the idadb user with sufficient privileges for development.  <strong>NOTE!!! These privileges should not be used for production databases</strong>

At this point we need to apply database migrations to the database, as well as add data to the database using the fixtures files.  Execute the following commands...

*    <code>docker-compose exec web python manage.py migrate --noinput</code>
*    <code>docker-compose exec web python manage.py loaddata stations/fixtures/initial_data.json</code>

At this point you should be able to reload the home web page from the following URL and see the home page of the idastatus project...

*    <code>http://127.0.0.1:8000/</code>