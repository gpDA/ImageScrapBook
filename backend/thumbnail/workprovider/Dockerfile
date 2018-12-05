from python:3.6

# Layer python first, only reinstall when deps change
COPY thumbnail/Pipfile thumbnail/Pipfile.lock /app/
WORKDIR /app
RUN pip install pipenv
RUN pipenv install --system --deploy
# img files change more frequently than deps, less than app
COPY thumbnail/imgsrc /app/imgsrc/
# app files may change rapidly and take little time to copy
COPY thumbnail/thumbnail /app/thumbnail
COPY thumbnail/workprovider /app/
