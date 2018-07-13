FROM i386/ubuntu:artful
ENTRYPOINT ["linux32", "--"]  # https://github.com/conan-io/conan-docker-tools/issues/36

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV CONAN_ENV_ARCH=x86

RUN apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends \
       python-dev=2.7.* \
       sudo=1.* \
       binutils=2.29.* \
       wget=1.19.* \
       git=1:2.* \
       vim=2:8.* \
       libc6-dev=2.26* \
       linux-libc-dev=4.13* \
       g++-6=6.4.* \
       libgmp-dev=2:6.1.2+dfsg-1 \
       libmpfr-dev=3.1.6-1 \
       libmpc-dev=1.0.3-2 \
       libc6-dev=2.26-0ubuntu2.1 \
       nasm=2.13.01-2 \
       dh-autoreconf=14 \
       valgrind=1:3.13.0-1ubuntu3 \
       ninja-build=1.7.2-3 \
       libffi-dev=3.2.1-6 \
       libssl-dev=1.0.2* \
       pkg-config=0.29.1-0ubuntu2 \
       ca-certificates=20170717 \
    && update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-6 100 \
    && update-alternatives --install /usr/bin/c++ c++ /usr/bin/g++-6 100 \
    && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6 100 \
    && update-alternatives --install /usr/bin/cc cc /usr/bin/gcc-6 100 \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    && rm -rf /var/lib/apt/lists/* \
    && wget --no-check-certificate --quiet https://cmake.org/files/v3.11/cmake-3.11.2.tar.gz \
    && tar -xzf cmake-3.11.2.tar.gz \
    && cd cmake-3.11.2 \
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
