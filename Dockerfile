# base image
FROM python:3.10.7-alpine3.16

RUN apk update && apk upgrade && apk add gcc libc-dev

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .
RUN pip3 install --upgrade pip && pip install cffi && \
    pip3 install -r requirements.txt

# copy project files
COPY . .

# run database migrations
RUN python manage.py migrate members && \
    python manage.py migrate

# specify the command to run on container start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
