# Installing
Install `pipenv`.
In `backend/`, run `pipenv install.`

# Running
`pipenv shell` to switch to virtual env.
`python manage.py runserver` to start server.

# Notes for contributors
## In the thumbnail directory

`docker-compose up` for initial docker creation.

`docker-compose up -d --force-recreate -build [containers...]` to kill, rebuild and restart containers.

## Organization

For ease of development, even the database has been containerized. However, databases aren't good containerization targets in the real world, and if this project is ever deployed, an alternative automation scheme for setting up and maintaining a non-containerized database cluster will be required.
