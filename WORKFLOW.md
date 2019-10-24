# docker-idastatus

Workflow for the Dockerized version of the idastatus Django project

Changes to the Django Project and applications will be made in the idastatus directory.  Changes outside that directory, and to certain files within that directory (Dockerfile, etc.) will be only for changes to the Docker environment.

To edit the Django project, make changes to the files in the idastatus directory.  Changes to python files and the html and template files in that directory will automatically be detected by the Python web server which will reload those files.  If any changes are made to the docker environment, that environment will need to be rebuild and re-run with the following commands...

    docker-compose build

and

    docker-compose up

Should there be any oddities experienced in the web applications, it's advisible to rebuild the docker environment and re-run it.

After changing the models file, you must make a migrations file for it

    docker-compose exec web python manage.py makemigrations --noinput --name <text_to_describe_migration>

The text you give at the end of that command will form the base of the migration filename.  After successfully making the migration file, you can run the following to perform the migrations

    docker-compose exec web python manage.py migrate

After the migrations are successfully applied, you can load data from into the new database format with a fixture.  A fixture is a JSON file that contains data elements intended for the database.  See any of the files in the fixtures directory for the structure.  The specific fixture files are applied with

    docker-compose exec web python manage.py loaddata stations/fixtures/<JSON filename>
