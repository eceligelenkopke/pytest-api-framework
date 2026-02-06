FROM python:3.11-slim

MAINTAINER alperenacar@gmail.com

run apt-get update && apt-get -y install vim
RUN mkdir /automation

COPY ./grrmapitest /automation/grrmapitest
COPY ./setup.py /automation


WORKDIR /automation

RUN python3 setup.py install
