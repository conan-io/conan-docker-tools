FROM ubuntu:bionic

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

RUN dpkg --add-architecture i386 \
    && apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends \
       python-dev=2.7.* \
       sudo=1.* \
       binutils=2.* \
       wget=1.19.* \
       git=1:2.* \
       vim=2:8.* \
       libc6-dev=2.27* \
       linux-libc-dev=4.* \
       g++-6-multilib=6.4.* \
       libgmp-dev=2:6.1.2+dfsg-2 \
       libmpfr-dev=4.0.1-1 \
       libmpc-dev=1.1.0-1 \
       libc6-dev=2.27-3ubuntu1 \
       nasm=2.13.02-0.1 \
       dh-autoreconf=17 \
       valgrind=1:3.13.0-2ubuntu2 \
       ninja-build=1.8.2-1 \
       libffi-dev=3.2.1-8 \
       libssl-dev=1.* \
       pkg-config=0.29.1-0ubuntu2 \
       subversion=1.9.7-4ubuntu1 \
       ca-certificates=20180409 \
    && update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-6 100 \
    && update-alternatives --install /usr/bin/c++ c++ /usr/bin/g++-6 100 \
    && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6 100 \
    && update-alternatives --install /usr/bin/cc cc /usr/bin/gcc-6 100 \
    && rm -rf /var/lib/apt/lists/* \
    && wget --no-check-certificate --quiet https://cmake.org/files/v3.12/cmake-3.12.0-Linux-x86_64.tar.gz \
    && tar -xzf cmake-3.12.0-Linux-x86_64.tar.gz \
    && cp -fR cmake-3.12.0-Linux-x86_64/* /usr \
    && rm -rf cmake-3.12.0-Linux-x86_64 \
    && rm cmake-3.12.0-Linux-x86_64.tar.gz \
    && wget --no-check-certificate --quiet https://bootstrap.pypa.io/get-pip.py \
    && python get-pip.py \
    && rm get-pip.py \
    && pip install -q -U pip \
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
