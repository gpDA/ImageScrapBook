# Installing
Install Docker, then run `docker-compose up --build` while in either the `backend/` or `thumbnail` directory. This should download, build and run all images.

# Running
`pipenv shell` to switch to virtual env--shouldn't be required.  
`docker-compose up --build` to run a Docker setup for the first time.  
`docker-compose build [containers...]; docker-compose up` to rebuild changed containers.  

# Notes for contributors
## Organization

For ease of development, even the database has been containerized. However, databases aren't good containerization targets in the real world, and if this project is ever deployed, an alternative automation scheme for setting up and maintaining a non-containerized database cluster will be required.
