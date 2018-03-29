FROM ubuntu:precise

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

RUN apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends \
       python-dev=2.7.* \
       sudo=1.8.* \
       build-essential=11.* \
       wget=1.13.* \
       git=1:1.7.* \
       vim=2:7.3.* \
       libc6-dev-i386=2.15-* \
       g++-multilib=4:4.6.* \
       nasm=2.09.* \
       dh-autoreconf=5ubuntu1 \
       valgrind=1:3.7.* \
       ninja-build=1.3.* \
       libffi-dev=3.0.* \
       libssl-dev=1.0.* \
       pkg-config=0.26-1ubuntu1 \
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
