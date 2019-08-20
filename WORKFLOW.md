# docker-idastatus

Workflow for the Dockerized version of the idastatus Django project

Changes to the Django Project and applications will be made in the idastatus directory.  Changes outside that directory, and to certain files within that directory (Dockerfile, etc.) will be only for changes to the Docker environment.

To edit the Django project, make changes to the files in the idastatus directory.  Changes to python files and the html and template files in that directory will automatically be detected by the Python web server which will reload those files.  If any changes are made to the docker environment, that environment will need to be rebuild and re-run with the following commands...

    docker-compose build

and

    docker-compose up

Should there be any oddities experienced in the web applications, it's advisible to rebuild the docker environment and re-run it.

A section should be added here for migrations
