from python:3.6
COPY ./thumbnail /app/thumbnail
COPY Pipfile Pipfile.lock /app/
WORKDIR /app
RUN pip install pipenv
RUN pipenv install --system --deploy
