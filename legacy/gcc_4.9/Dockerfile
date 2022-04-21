FROM ubuntu:trusty

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ARG CONAN_VERSION

ENV CMAKE_VERSION_MAJOR_MINOR=3.18 \
    CMAKE_VERSION_FULL=3.18.2 \
    PYENV_ROOT=/opt/pyenv \
    PATH=/opt/pyenv/shims:${PATH} \
    CXX=/usr/bin/g++ \
    CC=/usr/bin/gcc

RUN dpkg --add-architecture i386 \
    && printf "deb http://ppa.launchpad.net/ubuntu-toolchain-r/test/ubuntu trusty main\n" >> /etc/apt/sources.list \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 60C317803A41BA51845E371A1E9377A2BA9EF27F \
    && apt-get -qq update \
    && apt-get install -y --force-yes --no-install-recommends --no-install-suggests \
       sudo \
       g++-4.9 \
       g++-4.9-multilib \
       libc6-dev-i386 \
       gcc-multilib \
       wget \
       git \
       nasm \
       dh-autoreconf \
       ninja-build \
       libffi-dev \
       libssl-dev \
       pkg-config \
       subversion \
       zlib1g-dev \
       libbz2-dev \
       libsqlite3-dev \
       libreadline-dev \
       xz-utils \
       curl \
       libncurses5-dev \
       libncursesw5-dev \
       liblzma-dev \
       ca-certificates \
       autoconf-archive \
    && update-ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.9 100 \
    && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 100 \
    && update-alternatives --install /usr/bin/cc cc /usr/bin/gcc-4.9 100 \
    && update-alternatives --install /usr/bin/c++ c++ /usr/bin/g++-4.9 100 \
    && update-alternatives --install /usr/bin/gcov gcov /usr/bin/gcov-4.9 100 \
    && wget -q --no-check-certificate https://cmake.org/files/v${CMAKE_VERSION_MAJOR_MINOR}/cmake-${CMAKE_VERSION_FULL}-Linux-x86_64.tar.gz \
    && tar -xzf cmake-${CMAKE_VERSION_FULL}-Linux-x86_64.tar.gz \
       --exclude=bin/cmake-gui \
       --exclude=doc/cmake \
       --exclude=share/cmake-${CMAKE_VERSION_MAJOR_MINOR}/Help \
       --exclude=share/vim \
       --exclude=share/vim \
    && cp -fR cmake-${CMAKE_VERSION_FULL}-Linux-x86_64/* /usr \
    && rm -rf cmake-${CMAKE_VERSION_FULL}-Linux-x86_64 \
    && rm cmake-${CMAKE_VERSION_FULL}-Linux-x86_64.tar.gz \
    && curl -fL https://getcli.jfrog.io | sh \
    && mv jfrog /usr/local/bin/jfrog \
    && chmod +x /usr/local/bin/jfrog \
    && groupadd -f conan-1001 -g 1001 \
    && groupadd -f conan-1000 -g 1000 \
    && groupadd -f conan-2000 -g 2000 \
    && groupadd -f conan-999 -g 999 \
    && useradd -ms /bin/bash conan -g 1001 -G 1000,2000,999 \
    && printf "conan:conan" | chpasswd \
    && adduser conan sudo \
    && printf "conan ALL= NOPASSWD: ALL\\n" >> /etc/sudoers \
    && sed -i '0,/python3/s//python/' /usr/bin/lsb_release \
    && rm /etc/ssl/certs/DST_Root_CA_X3.pem \
    && wget -q --no-check-certificate https://www.openssl.org/source/openssl-1.1.1l.tar.gz \
    && tar -xzf openssl-1.1.1l.tar.gz \
    && cd openssl-1.1.1l \
    && ./config no-unit-test shared \
    && make -s \
    && make install_sw \
    && rm -rf openssl-* \
    && ln -sf /usr/local/bin/openssl /usr/bin/openssl \
    && ldconfig \
    && wget --no-check-certificate --quiet -O /tmp/pyenv-installer https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer \
    && chmod +x /tmp/pyenv-installer \
    && /tmp/pyenv-installer \
    && rm /tmp/pyenv-installer \
    && update-alternatives --install /usr/bin/pyenv pyenv /opt/pyenv/bin/pyenv 100 \
    && PYTHON_CONFIGURE_OPTS="--enable-shared" CFLAGS=-I/usr/local/include LDFLAGS=-L/usr/local/lib pyenv install 3.7.13 \
    && pyenv global 3.7.13 \
    && sed -e 's/! \/usr/!\/usr\/local/g' -i /usr/bin/lsb_release \
    && ln -s /usr/lib/python3/dist-packages/lsb_release.py /opt/pyenv/versions/3.7.13/lib/python3.7/lsb_release.py \
    && pip install -q --upgrade --no-cache-dir pip \
    && pip install -q --no-cache-dir conan==${CONAN_VERSION} conan-package-tools \
    && chown -R conan:1001 /opt/pyenv \
    # remove all __pycache__ directories created by pyenv
    && find /opt/pyenv -iname __pycache__ -print0 | xargs -0 rm -rf \
    && update-alternatives --install /usr/bin/python3 python3 /opt/pyenv/shims/python3 100 \
    && update-alternatives --install /usr/bin/pip3 pip3 /opt/pyenv/shims/pip3 100 \
    && update-alternatives --install /usr/local/bin/python python /opt/pyenv/shims/python 100 \
    && update-alternatives --install /usr/local/bin/pip pip /opt/pyenv/shims/pip 100

USER conan
WORKDIR /home/conan

RUN mkdir -p /home/conan/.conan \
    && printf 'eval "$(pyenv init -)"\n' >> ~/.bashrc \
    && printf 'eval "$(pyenv virtualenv-init -)"\n' >> ~/.bashrc
