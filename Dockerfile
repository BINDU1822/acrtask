# FROM python:3.9-slim-bullseye

# USER root
# RUN apt-get update && apt-get install -y
# RUN apt-get install unixodbc-dev libgirepository1.0-dev libcairo2-dev python3-dev gir1.2-secret-1 -y

# WORKDIR /usr/local/app

# COPY /requirements.txt /usr/local/app/requirements.txt
# RUN python -m pip install --upgrade pip
# RUN pip install -r requirements.txt

# COPY / /usr/local/app

# CMD ["gunicorn", "--bind=0.0.0.0","--timeout","600","runserver:app"]

FROM ubuntu:18.04

# To make it easier for build and release pipelines to run apt-get,
# configure apt to not require confirmation (assume the -y argument by default)
ENV DEBIAN_FRONTEND=noninteractive
RUN echo "APT::Get::Assume-Yes \"true\";" > /etc/apt/apt.conf.d/90assumeyes

RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        jq \
        git \
        libicu60 \
        iputils-ping \
        libcurl4 \
        libunwind8 \
        netcat \
        libssl1.0 \
        zip \
        unzip \
        wget \
        apt-transport-https \
        software-properties-common \
        net-tools \
        dnsutils \
        nmap \
    && rm -rf /var/lib/apt/lists/*

# Add a repo to get a newer version of Python onto Ubuntu 18.04
RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.8 \
    && rm -rf /var/lib/apt/lists/*

RUN curl -LsS https://aka.ms/InstallAzureCLIDeb | bash \
    && rm -rf /var/lib/apt/lists/*

RUN wget -q https://packages.microsoft.com/config/ubuntu/18.04/packages-microsoft-prod.deb
RUN dpkg -i packages-microsoft-prod.deb
RUN apt-get update && apt-get install -y --no-install-recommends powershell
RUN ln -s /usr/bin/python3.8 /usr/bin/python

# Can be 'linux-x64', 'linux-arm64', 'linux-arm', 'rhel.6-x64'.
ENV TARGETARCH=linux-x64

WORKDIR /azp

COPY ./start.sh .
RUN chmod +x start.sh

ENTRYPOINT ["./start.sh"]
