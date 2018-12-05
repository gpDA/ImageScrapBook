FROM python:3.6

# Layer deps first
COPY imagescrapbook/Pipfile imagescrapbook/Pipfile.lock /app/
WORKDIR /app
RUN pip install pipenv; pipenv install --system --deploy
COPY thumbnail/thumbnail/ /app/thumbnail/

# Copy app
COPY imagescrapbook/ /app
RUN python manage.py makemigrations

ENTRYPOINT ["python", "manage.py"]
