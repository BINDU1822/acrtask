FROM python:3.9-slim-bullseye

USER root
RUN apt-get update && apt-get install -y
RUN apt-get install unixodbc-dev libgirepository1.0-dev libcairo2-dev python3-dev gir1.2-secret-1 -y

WORKDIR /usr/local/app

COPY /requirements.txt /usr/local/app/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY / /usr/local/app

CMD ["gunicorn", "--bind=0.0.0.0","--timeout","600","runserver:app"]

