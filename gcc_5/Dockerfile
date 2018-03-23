FROM ubuntu:xenial

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

RUN dpkg --add-architecture i386 \
    && apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends \
       python-dev=2.7.* \
       sudo=1.8.* \
       build-essential=12.* \
       wget=1.17.* \
       git=1:2.7.* \
       vim=2:7.4.* \
       libc6-dev-i386=2.23-* \
       g++-multilib=4:5.3.* \
       libgmp-dev=2:6.1.* \
       libmpfr-dev=3.1.* \
       libmpc-dev=1.0.* \
       libc6-dev=2.23-* \
       nasm=2.11.* \
       dh-autoreconf=11 \
       valgrind=1:3.11.* \
       ninja-build=1.5.*  \
       libffi-dev=3.2.* \
       libssl-dev=1.0.2* \
       ca-certificates \
       && rm -rf /var/lib/apt/lists/* \
       && wget -q --no-check-certificate https://cmake.org/files/v3.10/cmake-3.10.3-Linux-x86_64.tar.gz \
       && tar -xzf cmake-3.10.3-Linux-x86_64.tar.gz \
       && cp -fR cmake-3.10.3-Linux-x86_64/* /usr \
       && rm -rf cmake-3.10.3-Linux-x86_64 \
       && rm cmake-3.10.3-Linux-x86_64.tar.gz \
       && wget -q --no-check-certificate https://bootstrap.pypa.io/get-pip.py \
       && python get-pip.py \
       && rm get-pip.py \
       && pip install -q -U pip \
       && pip install -q --no-cache-dir conan \
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
