FROM i386/ubuntu:trusty
ENTRYPOINT ["linux32", "--"]

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV CONAN_ENV_ARCH=x86

RUN dpkg --add-architecture i386 \
    && apt-get -qq update \
    && apt-get -qq install -y software-properties-common \
    && add-apt-repository ppa:fkrull/deadsnakes-python2.7 \
    && add-apt-repository -y ppa:ubuntu-toolchain-r/test \
    && apt-get -qq update \
    && apt-get install -y --force-yes --no-install-recommends \
       python-dev=2.7.5-5ubuntu3 \
       sudo=1.8.9p5-1ubuntu1.4 \
       g++-4.9=4.9.4-2ubuntu1~14.04.1 \
       g++-4.9-multilib=4.9.4-2ubuntu1~14.04.1 \
       wget=1.15-1ubuntu1.14.04.4 \
       git \
       vim=2:7.4.052-1ubuntu3.1 \
       nasm=2.10.09-1 \
       dh-autoreconf=9 \
       valgrind=1:3.10.1-1ubuntu3~14.5 \
       ninja-build=1.3.4-1.1ubuntu0.14.04.1 \
       libffi-dev=3.1~rc1+r3.0.13-12ubuntu0.2 \
       libssl-dev=1.* \
       pkg-config=0.26-1ubuntu4 \
       subversion=1.8.8-1ubuntu3.3 \
       ca-certificates=20170717~14.04.1 \
    && rm -rf /var/lib/apt/lists/* \
    && update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.9 100 \
    && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 100 \
    && update-alternatives --install /usr/bin/cc cc /usr/bin/gcc-4.9 100 \
    && update-alternatives --install /usr/bin/c++ c++ /usr/bin/g++-4.9 100 \
    && wget --no-check-certificate --quiet https://cmake.org/files/v3.12/cmake-3.12.0.tar.gz \
    && tar -xzf cmake-3.12.0.tar.gz \
    && cd cmake-3.12.0 \
    && ./bootstrap > /dev/null \
    && make -s -j`nproc` \
    && make -s install > /dev/null \
    && cd - \
    && rm -rf cmake-* \
    && wget -q --no-check-certificate https://bootstrap.pypa.io/get-pip.py \
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
