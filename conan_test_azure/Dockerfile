FROM ubuntu:xenial

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV CMAKE_VERSION_MAJOR_MINOR=3.18 \
    CMAKE_VERSION_FULL=3.18.2

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
       python3.8-distutils \
       golang \
       pkg-config \
       && rm -rf /var/lib/apt/lists/* \
       && wget -q --no-check-certificate https://cmake.org/files/v${CMAKE_VERSION_MAJOR_MINOR}/cmake-${CMAKE_VERSION_FULL}-Linux-x86_64.tar.gz \
       && tar -xzf cmake-${CMAKE_VERSION_FULL}-Linux-x86_64.tar.gz \
       --exclude=bin/cmake-gui \
       --exclude=doc/cmake \
       --exclude=share/cmake-${CMAKE_VERSION_MAJOR_MINOR}/Help \
       --exclude=share/vim \
       && cp -fR cmake-${CMAKE_VERSION_FULL}-Linux-x86_64/* /usr \
       && rm -rf cmake-${CMAKE_VERSION_FULL}-Linux-x86_64 \
       && rm cmake-${CMAKE_VERSION_FULL}-Linux-x86_64.tar.gz \
       && wget -q --no-check-certificate https://bootstrap.pypa.io/get-pip.py \
       && sudo ln -sf /usr/bin/python3.8 /usr/bin/python \
       && sudo ln -sf /usr/bin/python3.8 /usr/bin/python3 \
       && python3.8 get-pip.py \
       && rm get-pip.py \
       && python -m pip install -q -U pip \
       && python -m pip install -q --no-cache-dir conan conan-package-tools --upgrade \
       && python -m pip install virtualenv
