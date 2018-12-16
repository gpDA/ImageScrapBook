# ImageScrapBook

ImageScrapBook is a cloud-native webapp for hosting and sharing images.

## Installing the Chrome Extension
1. Download the project file from this git repository 
2. open chrome://extensions/
3. turn on the 'developer mode' on the top right corner
4. click 'Load unpacked' and select the 'extension' folder within the downloaded project folder
5. Our icon will then be up!


## Technical Difficulties
In the extension, we couldn't implement a function to check the authenticated user and save the corresponding image for that specfic user.
So for example, in `extension/save_img.js` , where the image creation (post) happens, we hard-coded the user with user_id : 1 for the sake of deploying. In the future, we would implement the authentication process. 


## Contributing
Here is a guide on installing a local copy of Image Scrap Book.

Install Docker. Then:
### Installing backend
Run `docker-compose up --build` while in the `backend/` directory. Docker downloads all deps and builds all containers.

## Running
`pipenv shell` to switch to virtual env--shouldn't be required.  


## Troubleshooting
### `ERROR: for backend_appserver_1_606e41b6d69c  Cannot start service appserver: OCI runtime create failed: container_linux.go:348: starting container process caused "exec: \"./init.sh\": permission denied": unknown`

```
$ sudo chmod 777 ImageScrapBook/backend/imagescrapbook/init.sh`
$ docker-compose up --build
```

### Other useful commands

`docker-compose up --build` to run a Docker setup for the first time.  
`docker-compose build [containers...]; docker-compose up` to rebuild changed containers.  

## Configuring Django
Changing the "command" attribute of `appserver` in `backend/docker-compose.yml` allows you to execute commands such as makemigrations, migrate, runserver and createsuperuser.

## Notes for contributors
### Organization
| Name | description |
|-----------|------------------------------|
| appserver | Django app                   |
| postgres  | Postgres database            |
| rabbit       | RabbitMQ backing for Celery |
| minio        | Local S3 mocking for dev |
| celeryworker | Workers that process Celery jobs |
| workprovider | Puts Celery jobs for testing purposes |


## Database containers

For ease of development, even the database has been containerized. However, databases aren't good containerization targets in the real world, and if this project is ever deployed, an alternative automation scheme for setting up and maintaining a non-containerized database cluster will be required.


PROJECT DESIGN IMAGE
![PROJECT DESIGN IMAGE](https://user-images.githubusercontent.com/29666846/49106991-94a6ce80-f252-11e8-8e34-c0dd67f66eec.jpeg)



