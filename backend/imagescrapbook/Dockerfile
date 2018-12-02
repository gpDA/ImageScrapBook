FROM python:3.6

# Layer deps first
COPY Pipfile Pipfile.lock /app/
WORKDIR /app
RUN pip install pipenv; pipenv install --system --deploy

# Copy app
COPY . /app
RUN python manage.py makemigrations

ENTRYPOINT ["python", "manage.py"]
