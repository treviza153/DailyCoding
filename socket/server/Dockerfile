FROM ubuntu:latest

SHELL ["/bin/bash", "-c"]

RUN mkdir -p /server

WORKDIR /server

ADD . /server/

CMD cd /server

RUN apt-get update && \
    apt-get install -y libldap2-dev \
                       libsasl2-dev \
                       libssl-dev \
                       python-ldap \
                       net-tools \
                       dnsutils \
                       tcpdump

RUN pip install --upgrade pip
