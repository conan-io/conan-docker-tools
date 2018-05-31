FROM ubuntu:xenial

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

RUN dpkg --add-architecture i386 \
    && apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends \
       python-dev=2.7.12-1~16.04 \
       sudo=1.8.16-0ubuntu1.5 \
       build-essential=12.1ubuntu2 \
       wget=1.17.1-1ubuntu1.4 \
       git=1:2.7.4-0ubuntu1.3 \
       vim=2:7.4.1689-3ubuntu1.2 \
       libc6-dev-i386=2.23-0ubuntu10 \
       g++-4.9-multilib=4.9.3-13ubuntu2 \
       gcc-4.9=4.9.3-13ubuntu2 \
       g++-4.9=4.9.3-13ubuntu2 \
       libgmp-dev=2:6.1.0+dfsg-2 \
       libmpfr-dev=3.1.4-1 \
       libmpc-dev=1.0.3-1 \
       libc6-dev=2.23-0ubuntu10 \
       nasm=2.11.08-1 \
       dh-autoreconf=11 \
       valgrind=1:3.11.0-1ubuntu4.2 \
       ninja-build=1.5.1-0.1ubuntu1  \
       libffi-dev=3.2.1-4 \
       libssl-dev=1.0.2g-1ubuntu4.12 \
       pkg-config=0.29.1-0ubuntu1 \
       ca-certificates=20170717~16.04.1 \
       && update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.9 100 \
       && update-alternatives --install /usr/bin/c++ c++ /usr/bin/g++-4.9 100 \
       && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 100 \
       && update-alternatives --install /usr/bin/cc cc /usr/bin/gcc-4.9 100 \
       && ln -s /usr/include/asm-generic/ /usr/include/asm \
       && rm -rf /var/lib/apt/lists/* \
       && wget -q --no-check-certificate https://cmake.org/files/v3.11/cmake-3.11.2-Linux-x86_64.tar.gz \
       && tar -xzf cmake-3.11.2-Linux-x86_64.tar.gz \
       && cp -fR cmake-3.11.2-Linux-x86_64/* /usr \
       && rm -rf cmake-3.11.2-Linux-x86_64 \
       && rm cmake-3.11.2-Linux-x86_64.tar.gz \
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
