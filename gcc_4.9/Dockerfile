FROM ubuntu:xenial

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

RUN dpkg --add-architecture i386 \
    && apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends \
       python-dev=2.7.11-1 \
       sudo=1.8.16-0ubuntu1 \
       g++-4.9=4.9.3-13ubuntu2 \
       g++-4.9-multilib=4.9.3-13ubuntu2 \
       gcc-multilib=4:5.3.1-1ubuntu1 \
       libc6-dev-i386=2.23-0ubuntu9 \
       wget=1.17.1-1ubuntu1 \
       git=1:2.7.4-0ubuntu1 \
       vim=2:7.4.1689-3ubuntu1.2 \
       nasm=2.11.08-1 \
       dh-autoreconf=11 \
       valgrind=1:3.11.0-1ubuntu4 \
       ninja-build=1.5.1-0.1ubuntu1 \
       libffi-dev=3.2.1-4 \
       libssl-dev=1.0.2g-1ubuntu4.9 \
    && rm -rf /var/lib/apt/lists/* \
    && update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.9 100 \
    && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 100 \
    && update-alternatives --install /usr/bin/cc cc /usr/bin/gcc-4.9 100 \
    && update-alternatives --install /usr/bin/c++ c++ /usr/bin/g++-4.9 100 \
    && wget -q --no-check-certificate https://cmake.org/files/v3.9/cmake-3.9.0-Linux-x86_64.tar.gz \
    && tar -xzf cmake-3.9.0-Linux-x86_64.tar.gz \
    && cp -fR cmake-3.9.0-Linux-x86_64/* /usr \
    && rm -rf cmake-3.9.0-Linux-x86_64 \
    && rm cmake-3.9.0-Linux-x86_64.tar.gz \
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
