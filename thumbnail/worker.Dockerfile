from python:3.6

# Layer python first, only reinstall when deps change
COPY Pipfile Pipfile.lock /app/
WORKDIR /app
RUN pip install pipenv
RUN pipenv install --system --deploy
# Application changes
COPY ./thumbnail /app/thumbnail
