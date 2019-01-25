# ImageScrapBook
ImageScrapBook is a cloud-native webapp for hosting and sharing images.

# VIDEO DEMO
[![ImageScrapBook video Demo](https://img.youtube.com/vi/lS2d4uhoqBg/0.jpg)](https://www.youtube.com/watch?v=lS2d4uhoqBg)

# PROJECT DESIGN IMAGE
![PROJECT DESIGN IMAGE](https://user-images.githubusercontent.com/29666846/49106991-94a6ce80-f252-11e8-8e34-c0dd67f66eec.jpeg)

# Installing the Chrome Extension
1. Ensure the `extensions/` directory is on your disk.
2. Navigate to `chrome://extensions/`.
3. If not enabled already, enable Developer Mode.
4. Click 'Load unpacked' and select the `extension` directory.
5. The extension will display an orange camera icon in the top-right corner of the browser.

# Contributing
Here is a guide on installing a local copy of Image Scrap Book.

Install Docker. Then:
# Installing backend
Run `docker-compose up --build` while in the `backend/` directory. Docker downloads all deps and builds all containers.

## Running
`pipenv shell` to switch to virtual env--shouldn't be required.  


## Troubleshooting
### `ERROR: for backend_appserver_1_606e41b6d69c  Cannot start service appserver: OCI runtime create failed: container_linux.go:348: starting container process caused "exec: \"./init.sh\": permission denied": unknown`

```
$ sudo chmod 777 ImageScrapBook/backend/imagescrapbook/init.sh`
$ docker-compose up --build
```

# Other useful commands

`docker-compose up --build` to run a Docker setup for the first time.  
`docker-compose build [containers...]; docker-compose up` to rebuild changed containers.  

# Configuring Django
Changing the "command" attribute of `appserver` in `backend/docker-compose.yml` allows you to execute commands such as makemigrations, migrate, runserver and createsuperuser.

# Notes for contributors
### Organization
| Name | description |
|-----------|------------------------------|
| appserver | Django app                   |
| postgres  | Postgres database            |
| rabbit       | RabbitMQ backing for Celery |
| minio        | Local S3 mocking for dev |
| celeryworker | Workers that process Celery jobs |
| workprovider | Puts Celery jobs for testing purposes |


# Database containers

For ease of development, even the database has been containerized. However, databases aren't good containerization targets in the real world, and if this project is ever deployed, an alternative automation scheme for setting up and maintaining a non-containerized database cluster will be required.

# Technical Difficulties
We couldn't implement authentication in the extension, so the current version instead hardcodes uploading images as user id 1. Fixing this is a top priority for the future.
