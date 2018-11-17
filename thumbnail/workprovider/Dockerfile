FROM python:3.6
# layer deps
COPY Pipfile Pipfile.lock /app/
WORKDIR /app
RUN pip install pipenv ; pipenv install --system --deploy
# img files change more frequently than deps, less than app
COPY imgsrc /app/imgsrc/
# app files may change rapidly and take little time to copy
COPY thumbnail /app/thumbnail
COPY workprovider /app/
