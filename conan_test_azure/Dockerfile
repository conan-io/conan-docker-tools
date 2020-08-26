FROM ubuntu:xenial

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

RUN dpkg --add-architecture i386 \
    && apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa -y \
    && apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends \
       python3-dev=3.* \
       sudo=1.* \
       build-essential=12.* \
       wget=1.* \
       git=1:* \
       libc6-dev-i386=2.* \
       g++-multilib=4:* \
       libgmp-dev=2:* \
       libmpfr-dev=3.* \
       libmpc-dev=1.* \
       libc6-dev=2.* \
       nasm=2.* \
       dh-autoreconf=11 \
       ninja-build=1.*  \
       libffi-dev=3.* \
       libssl-dev=1.* \
       pkg-config=0.* \
       subversion=1.* \
       ca-certificates \
       python-software-properties \
       python3.4 \
       python3.5 \
       python3.6 \
       python3.7 \
       python3.8 \
       python-setuptools \
       python-dev \
       python3.4-dev \
       python3.5-dev \
       python3.6-dev \
       python3.7-dev \
       python3.8-dev \
       golang \
       pkg-config \
       && rm -rf /var/lib/apt/lists/* \
       && wget -q --no-check-certificate https://cmake.org/files/v3.18/cmake-3.18.2-Linux-x86_64.tar.gz \
       && tar -xzf cmake-3.18.2-Linux-x86_64.tar.gz \
       --exclude=bin/cmake-gui \
       --exclude=doc/cmake \
       --exclude=share/cmake-3.12/Help \
       && cp -fR cmake-3.18.2-Linux-x86_64/* /usr \
       && rm -rf cmake-3.18.2-Linux-x86_64 \
       && rm cmake-3.18.2-Linux-x86_64.tar.gz \
       && wget -q --no-check-certificate https://bootstrap.pypa.io/get-pip.py \
       && python3 get-pip.py \
       && rm get-pip.py \
       && pip install -q -U pip \
       && pip install -q --no-cache-dir conan conan-package-tools --upgrade \
       && pip install virtualenv
