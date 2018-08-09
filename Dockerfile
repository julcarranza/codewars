FROM ubuntu

# Metadata
LABEL A container used to run Junos PyEZ automation scripting. \
      Author = Julivator \
      Dokerfile creation date = 7/28/2018

# Create diretories
RUN mkdir /scripts

RUN apt-get update
RUN apt-get install -y python python-dev python-setuptools python-dev build-essential
RUN apt-get install -y python-pip

RUN pip install --upgrade pip
RUN pip install Flask


RUN apt-get --assume-yes install libxslt1-dev libssl-dev libffi-dev
RUN pip install junos-eznc

# Change the working directory to /scripts
WORKDIR /scripts

# Create a volume mount point
VOLUME /scripts

