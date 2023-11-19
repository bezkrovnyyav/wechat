# base image
FROM python:3.7-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .
RUN pip3 install --upgrade pip3 && \
    pip3 install -r requirements.txt

# copy project files
COPY . .

# run database migrations
RUN python manage.py migrate members && \
    python manage.py migrate

# specify the command to run on container start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
