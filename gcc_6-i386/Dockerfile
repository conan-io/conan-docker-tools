FROM i386/ubuntu:artful

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV CONAN_ENV_ARCH=x86

RUN apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends \
       python-dev=2.7.14-2ubuntu1 \
       sudo=1.8.20p2-1ubuntu1 \
       binutils=2.29.1-4ubuntu1 \
       wget=1.19.1-3ubuntu1.1 \
       git=1:2.14.1-1ubuntu4 \
       vim=2:8.0.0197-4ubuntu5 \
       libc6-dev=2.26-0ubuntu2.1 \
       linux-libc-dev=4.13.0-32.35 \
       g++-6=6.4.0-8ubuntu1 \
       libgmp-dev=2:6.1.2+dfsg-1 \
       libmpfr-dev=3.1.6-1 \
       libmpc-dev=1.0.3-2 \
       libc6-dev=2.26-0ubuntu2.1 \
       nasm=2.13.01-2 \
       dh-autoreconf=14 \
       valgrind=1:3.13.0-1ubuntu3 \
       ninja-build=1.7.2-3 \
       libffi-dev=3.2.1-6 \
       libssl-dev=1.0.2g-1ubuntu13.3 \
       ca-certificates=20170717 \
    && update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-6 100 \
    && update-alternatives --install /usr/bin/c++ c++ /usr/bin/g++-6 100 \
    && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6 100 \
    && update-alternatives --install /usr/bin/cc cc /usr/bin/gcc-6 100 \
    && rm -rf /var/lib/apt/lists/* \
    && wget --no-check-certificate --quiet https://cmake.org/files/v3.10/cmake-3.10.1.tar.gz \
    && tar -xzf cmake-3.10.1.tar.gz \
    && cd cmake-3.10.1 \
    && ./bootstrap > /dev/null \
    && make -s -j`nproc` \
    && make -s install > /dev/null \
    && cd - \
    && rm -rf cmake-* \
    && wget --no-check-certificate --quiet https://bootstrap.pypa.io/get-pip.py \
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
