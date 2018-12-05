from python:3.6

# Layer python first, only reinstall when deps change
COPY thumbnail/Pipfile thumbnail/Pipfile.lock /app/
WORKDIR /app
RUN pip install pipenv
RUN pipenv install --system --deploy
# Copy Django module
COPY imagescrapbook/main/ /app/image
# Application changes
COPY thumbnail/thumbnail/ /app/thumbnail
