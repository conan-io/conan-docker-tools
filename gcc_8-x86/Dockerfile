FROM i386/ubuntu:bionic
ENTRYPOINT ["linux32", "--"] # https://github.com/conan-io/conan-docker-tools/issues/36

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV CONAN_ENV_ARCH=x86

RUN apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends \
       python-dev=2.7.15~rc1-1 \
       sudo=1.8.21p2-3ubuntu1 \
       binutils=2.* \
       wget=1.19.4-1ubuntu2.1 \
       git \
       vim=2:8.0.1453-1ubuntu1 \
       libc6-dev=2.27-3ubuntu1 \
       linux-libc-dev=4.* \
       g++-8=8-20180414-1ubuntu2 \
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
    && update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-8 100 \
    && update-alternatives --install /usr/bin/c++ c++ /usr/bin/g++-8 100 \
    && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 100 \
    && update-alternatives --install /usr/bin/cc cc /usr/bin/gcc-8 100 \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    && rm -rf /var/lib/apt/lists/* \
    && wget --no-check-certificate --quiet https://cmake.org/files/v3.12/cmake-3.12.0.tar.gz \
    && tar -xzf cmake-3.12.0.tar.gz \
    && cd cmake-3.12.0 \
    && ./bootstrap > /dev/null \
    && make -s -j`nproc` \
    && make -s install > /dev/null \
    && cd - \
    && rm -rf cmake-* \
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
