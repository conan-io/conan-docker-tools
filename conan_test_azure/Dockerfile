FROM ubuntu:xenial

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

RUN dpkg --add-architecture i386 \
    && apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa -y \
    && apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends \
       python3-dev=3.5.1-3 \
       sudo=1.8.* \
       build-essential=12.* \
       wget=1.17.* \
       git=1:2.7.* \
       libc6-dev-i386=2.23-* \
       g++-multilib=4:5.3.* \
       libgmp-dev=2:6.1.* \
       libmpfr-dev=3.1.* \
       libmpc-dev=1.0.* \
       libc6-dev=2.23-* \
       nasm=2.11.* \
       dh-autoreconf=11 \
       ninja-build=1.5.*  \
       libffi-dev=3.2.* \
       libssl-dev=1.0.2* \
       pkg-config=0.29.1-0ubuntu1 \
       subversion=1.9.3-2ubuntu1.1 \
       ca-certificates \
       python-software-properties \
       python3.4 \
       python3.5 \
       python3.6 \
       python3.7 \
       python-setuptools \
       python-dev \
       python3.4-dev \
       python3.5-dev \
       python3.6-dev \
       python3.7-dev \
       golang \
       pkg-config \
       && rm -rf /var/lib/apt/lists/* \
       && wget -q --no-check-certificate https://cmake.org/files/v3.14/cmake-3.14.3-Linux-x86_64.tar.gz \
       && tar -xzf cmake-3.14.3-Linux-x86_64.tar.gz \
       --exclude=bin/cmake-gui \
       --exclude=doc/cmake \
       --exclude=share/cmake-3.12/Help \
       && cp -fR cmake-3.14.3-Linux-x86_64/* /usr \
       && rm -rf cmake-3.14.3-Linux-x86_64 \
       && rm cmake-3.14.3-Linux-x86_64.tar.gz \
       && wget -q --no-check-certificate https://bootstrap.pypa.io/get-pip.py \
       && python3 get-pip.py \
       && rm get-pip.py \
       && pip install -q -U pip \
       && pip install -q --no-cache-dir conan conan-package-tools --upgrade \
       && pip install virtualenv
