FROM python:3.6
COPY Pipfile Pipfile.lock /app/
WORKDIR /app
RUN pip install pipenv ; pipenv install --system --deploy
COPY imgsrc /app/imgsrc/
COPY thumbnail /app/thumbnail
COPY workprovider /app/
