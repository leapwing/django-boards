FROM python:3.6.3
MAINTAINER Kenny Huang <leapwing@gmail.com>

# Create the group and user to be used in this container
RUN groupadd djgroup && useradd -m -g djgroup -s /bin/bash django

RUN mkdir -p /home/django/app/web
WORKDIR /home/django/app/web

COPY requirement.txt /home/django/app/web
RUN pip install --no-cache-dir -r requirement.txt

COPY . /home/django/app/web

RUN chown -R django:djgroup /home/django

USER django
