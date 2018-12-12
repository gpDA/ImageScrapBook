# Running Django locally
First, add the following lines to the host file.

```
127.0.0.1 rabbit
127.0.0.1 minio
127.0.0.1 postgres
```

Next, symlink thumbnail/thumbnail to the backend:
```
../backend/imagescrapbook $ ln -s ../thumbnail/thumbnail thumbnail
```

Make sure the services are up in another terminal:
```
$ docker-compose build
$ docker-compose up celeryworker postgres
```

Enter virtual environment:
```
$ pipenv shell
```


Export required variables:
```
$ export AWS_ACCESS_KEY_ID=minio
$ export AWS_SECRET_ACCESS_KEY=minio123
$ export DATABASE_URL=postgres://pass:user@postgres:5432/imagescrapbook
```

Run server. Make migrations if required.
```
$ python manage.py makemigrations; python manage.py migrate
$ python manage.py runserver 0.0.0.0:8000
```
