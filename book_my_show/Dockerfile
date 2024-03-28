# base image for python and alpine is a lightweight version for linux, ideal for running docker containers. (alpine is bare minimum, not having any unnecessary dependencies)
FROM python:3.8.10-slim-buster
# define maintainers
LABEL maintainers="Abhishek Jha"

# setting this env. variable value to any non-zero value specifies that the output from our print statements is not buffered but directly printed to console in real time.
# By default it will be buffered somewhere, and visible when flushed.
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY . /app
WORKDIR /app

# exposing this port to access django dev server. This port will be exposed when our image will start our container.
EXPOSE 8000

# When we build this file, all the commands create an image layer stacked one over another.
# Ex. in here, all the below commands will be stacked over base image mentioned at the top.
# ex. Copy . /app image will be stacked over FROM python:3.9-alpine3.13, etc.
# This is done internally to cache images to build faster and various other reasons.

# Below we are running all the commands at once, if we run them one by one it will create new image layer for every command
# this single run command will keep our image lightweight, making the building of image efficient.
# 1. We are creating python venv first, this will avoid any conflict in dependencies present in our project and in our base image at the same time.
# 2. Upgrades pip (python package manager) inside our virtual environment.
# 3. It will install all the requirements inside our virtual environment.
# Added extra: if DEV is set as true from docker-compose, it will install the requirements.dev.txt also, (fi used is actually closing if)
# 4. Remove the tmp directory. Makes sure docker image is as lightweight as possible.
# 5. Adds a new user inside our image, It is best practise not to use the root user. Because if an attacker gets hold of this app, he will only have priviledge as a user, not as a root user.
# 6. We are disabling password for user, and telling not to create home directory, to keep image lightweight.
# 7. We are naming the user as django-user for this one.

# it will keep the DEV var to be false by default. We are overriding this in docker-copose file to true
ARG DEV=false
RUN python -m venv /py && \
/py/bin/pip install --upgrade pip && \
/py/bin/pip install -r /tmp/requirements.txt && \
if [ ${DEV}="true" ]; \
    then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
fi && \
rm -rf /tmp && \
adduser \
--disabled-password \
--no-create-home \
django-user

# PATH is automatically created inside linux, that defines all of the directories where executables are present.
# We are specifying below the path to bin of our virtual env, which is where os will search for any executable files (any_script.py).
# If not done, I will have to specify the full path, ex. python /app/run.py
# BTW this change of PATH will reflect in all of the below stacked image layers, including base image.
ENV PATH="/py/bin:$PATH"

# Container created using this image will run using the last user the image switch to
# Using the below line we switch to django-user, default is the root user, and we don't want that. It won't have the root priviledge now. Yay
USER django-user
