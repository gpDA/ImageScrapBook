FROM python:3.6
COPY . /app
COPY . /app/thumbnail
WORKDIR /app
RUN pip install pipenv ; pipenv install --system --deploy
