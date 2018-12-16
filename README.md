# ImageScrapBook

ImageScrapBook is a cloud-native webapp for hosting and sharing images.

## Installing
Install Docker. Then:
### Installing backend
Run `docker-compose up --build` while in the `backend/` directory. Docker downloads all deps and builds all containers.

- ERROR HELPER
    IF `ERROR: for backend_appserver_1_606e41b6d69c  Cannot start service appserver: OCI runtime create failed: container_linux.go:348: starting container process caused "exec: \"./init.sh\": permission denied": unknown` this error appears
    1) ImageScrapBook/backend/imagescrapbook `sudo chmod 777 init.sh`
    2) cd ..
    3) run `docker-compose up --build`

## Running (pipenv shell is optional)
`pipenv shell` to switch to virtual env--shouldn't be required.  
- ERROR HELPER
    FIRST, if you have not used `pipenv` before `brew install pipenv`
    currently required python_version for pipenv is python==3.6
    If pipenv is not intalled correctly,
    check  python version `python3 --version`
    I think if you use Anaconda for Python the default version for python3 is python==3.7.1 ...
    ERROR `Warning: Python 3.6.2 was not found on your system…`
    Then, you may install Python 3.6 by https://www.python.org/downloads/release/python-367/
    Then check `python3 --version` again
    `pipenv --python /usr/local/bin/python3`
    now run `pipenv shell` for virtual environment

    `pip install -r ../../requirements.txt`

--------------------------------------------  

`docker-compose up --build` to run a Docker setup for the first time.  
`docker-compose build [containers...]; docker-compose up` to rebuild changed containers.  

## Configuring Django
Changing the "command" attribute of `appserver` in `backend/docker-compose.yml` allows you to execute commands such as makemigrations, migrate, runserver and createsuperuser.

## Notes for contributors
### Organization
#### Service names
| docker-compose.yml | description |
|-----------|------------------------------|
| appserver | Django app                   |
| postgres  | Postgres database            |

| docker-compose.yml | description |
|--------------|-----------------------------|
| rabbit       | RabbitMQ backing for Celery |
| minio        | Local S3 mocking for dev |
| celeryworker | Workers that process Celery jobs |
| workprovider | Puts Celery jobs for testing purposes |



## Database containers

For ease of development, even the database has been containerized. However, databases aren't good containerization targets in the real world, and if this project is ever deployed, an alternative automation scheme for setting up and maintaining a non-containerized database cluster will be required.


PROJECT DESIGN IMAGE
![PROJECT DESIGN IMAGE](https://user-images.githubusercontent.com/29666846/49106991-94a6ce80-f252-11e8-8e34-c0dd67f66eec.jpeg)

## Installing Chrome Extension 

1. Download the project file from this git repository 
2. open chrome://extensions/
3. turn on the 'developer mode' on the top right corner
4. click 'Load unpacked' and select the 'extension' folder within the downloaded project folder
5. Our icon will then be up!



