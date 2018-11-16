FROM python:3.6
COPY imgsrc /app/imgsrc
COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv ; pipenv install --system --deploy
COPY thumbnail /app/thumbnail
COPY provide_work.py /app/
WORKDIR /app
