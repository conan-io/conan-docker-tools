FROM ubuntu:artful

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

RUN dpkg --add-architecture i386 \
    && apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends \
       python3-dev=3.6.3-0ubuntu3 \
       sudo=1.8.* \
       binutils=2.29.* \
       wget=1.19.* \
       git=1:2.14.* \
       vim=2:8.0.* \
       libc6-dev-i386=2.26-* \
       linux-libc-dev:i386=4.13.* \
       g++-7-multilib=7.2.* \
       libgmp-dev=2:6.1.* \
       libmpfr-dev=3.1.* \
       libmpc-dev=1.0.* \
       libc6-dev=2.26* \
       nasm=2.13.* \
       dh-autoreconf=14 \
       valgrind=1:3.13.* \
       ninja-build=1.7.* \
       libffi-dev=3.2.* \
       libssl-dev=1.0.2* \
       pkg-config=0.29.1-0ubuntu2 \
       subversion=1.9.7-2ubuntu1 \
       ca-certificates=20170717 \
    && update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-7 100 \
    && update-alternatives --install /usr/bin/c++ c++ /usr/bin/g++-7 100 \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    && rm -rf /var/lib/apt/lists/* \
    && wget --no-check-certificate --quiet https://cmake.org/files/v3.12/cmake-3.12.1-Linux-x86_64.tar.gz \
    && tar -xzf cmake-3.12.1-Linux-x86_64.tar.gz \
    && cp -fR cmake-3.12.1-Linux-x86_64/* /usr \
    && rm -rf cmake-3.12.1-Linux-x86_64 \
    && rm cmake-3.12.1-Linux-x86_64.tar.gz \
    && wget --no-check-certificate --quiet https://bootstrap.pypa.io/get-pip.py \
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
RUN mkdir -p /home/conan/.conan
