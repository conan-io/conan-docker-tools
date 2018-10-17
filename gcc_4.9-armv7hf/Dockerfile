FROM ubuntu:wily

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV CC=arm-linux-gnueabihf-gcc-4.9 \
    CXX=arm-linux-gnueabihf-g++-4.9 \
    CMAKE_C_COMPILER=arm-linux-gnueabihf-gcc-4.9 \
    CMAKE_CXX_COMPILER=arm-linux-gnueabihf-g++-4.9 \
    STRIP=arm-linux-gnueabihf-strip \
    RANLIB=arm-linux-gnueabihf-gcc-ranlib-4.9\
    AS=arm-linux-gnueabihf-as \
    AR=arm-linux-gnueabihf-gcc-ar-4.9 \
    LD=arm-linux-gnueabihf-ld \
    FC=arm-linux-gnueabihf-gfortran-4.9

RUN sed -i -re 's/([a-z]{2}\.)?archive.ubuntu.com|security.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list \
    && dpkg --add-architecture armhf \
    && apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends \
    ".*4\.9.*arm-linux-gnueabihf.*" \
    python3-dev=3.4.3-4ubuntu1 \
    sudo=1.8.* \
    build-essential=12.* \
    wget=1.16.* \
    git=1:2.5.* \
    vim=2:7.4.* \
    nasm=2.11.* \
    dh-autoreconf=10 \
    libc6:armhf \
    valgrind=1:3.11.* \
    ninja-build=1.3.* \
    libffi-dev=3.2.* \
    libssl-dev=1.0.2* \
    pkg-config=0.28-1ubuntu1 \
    subversion=1.8.13-1ubuntu3 \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && wget -q --no-check-certificate https://cmake.org/files/v3.12/cmake-3.12.1-Linux-x86_64.tar.gz \
    && tar -xzf cmake-3.12.1-Linux-x86_64.tar.gz \
    && cp -fR cmake-3.12.1-Linux-x86_64/* /usr \
    && rm -rf cmake-3.12.1-Linux-x86_64 \
    && rm cmake-3.12.1-Linux-x86_64.tar.gz \
    && wget -q --no-check-certificate https://bootstrap.pypa.io/get-pip.py \
    && python3 get-pip.py \
    && rm get-pip.py \
    && pip install -q -U pip \
    && pip install -q --no-cache-dir virtualenv --upgrade \
    && pip install -q --no-cache-dir conan --upgrade \
    && groupadd 1001 -g 1001 \
    && groupadd 1000 -g 1000 \
    && groupadd 2000 -g 2000 \
    && groupadd 999 -g 999 \
    && useradd -ms /bin/bash conan -g 1001 -G 1000,2000,999 \
    && printf "conan:conan" | chpasswd \
    && adduser conan sudo \
    && printf "conan ALL= NOPASSWD: ALL\\n" >> /etc/sudoers

USER conan
WORKDIR /home/conan

RUN mkdir -p /home/conan/.conan \
    && conan profile new default --detect \
    && conan profile update settings.arch=armv7hf default
