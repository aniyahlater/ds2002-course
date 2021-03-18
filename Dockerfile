FROM ubuntu:18.04
LABEL maintainer="UVA Data Science <nem2p@virginia.edu>"
LABEL org.opencontainers.image.source=https://github.com/ds3002/course

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York

RUN apt-get update
RUN apt-get install -y software-properties-common && add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3.8 python3.8-dev python3-pip nano \
  git curl net-tools jq zip unzip dnsutils httpie tzdata wget \
  htop iputils-ping mysql-client redis gsutil apt-transport-https \
  ca-certificates gnupg gcc python3-setuptools libffi-dev \
  libmysqlclient-dev
RUN rm -R /usr/bin/python3 && \
  ln -s /usr/bin/python3.8 /usr/bin/python3 && ln -s /usr/bin/python3.8 /usr/bin/python
RUN python3 -m pip install --upgrade pip

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" \
  -o "awscliv2.zip" \
  && unzip awscliv2.zip \
  && ./aws/install \
  && rm -rf /var/lib/apt/lists/*
RUN mkdir "/home/host"

WORKDIR /root
COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt
