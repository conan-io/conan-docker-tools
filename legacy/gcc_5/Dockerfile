FROM ubuntu:xenial

LABEL maintainer="Conan.io <info@conan.io>"

ENV PYENV_ROOT=/opt/pyenv \
    PATH=/opt/pyenv/shims:${PATH} \
    CXX=/usr/bin/g++ \
    CC=/usr/bin/gcc \
    FC=/usr/bin/gfortran

RUN apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends software-properties-common \
    && add-apt-repository ppa:git-core/ppa -y \
    && apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends --no-install-suggests \
       sudo \
       build-essential \
       wget \
       git \
       libc6-dev-i386 \
       g++-multilib \
       gfortran-multilib \
       libgmp-dev \
       libmpfr-dev \
       libmpc-dev \
       libc6-dev \
       nasm \
       dh-autoreconf \
       ninja-build  \
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
       && rm -rf /var/lib/apt/lists/*

ARG CMAKE_VERSION=3.18.6

RUN wget -q --no-check-certificate https://cmake.org/files/v${CMAKE_VERSION%.*}/cmake-${CMAKE_VERSION}-Linux-x86_64.tar.gz \
       && tar -xzf cmake-${CMAKE_VERSION}-Linux-x86_64.tar.gz \
          --exclude=bin/cmake-gui \
          --exclude=doc/cmake \
          --exclude=share/cmake-${CMAKE_VERSION%.*}/Help \
       --exclude=share/vim \
       && cp -fR cmake-${CMAKE_VERSION}-Linux-x86_64/* /usr \
       && rm -rf cmake-${CMAKE_VERSION}-Linux-x86_64 \
       && rm cmake-${CMAKE_VERSION}-Linux-x86_64.tar.gz

RUN curl -fL https://getcli.jfrog.io | sh \
       && mv jfrog /usr/local/bin/jfrog \
       && chmod +x /usr/local/bin/jfrog \
       && groupadd -f conan-1001 -g 1001 \
       && groupadd -f conan-1000 -g 1000 \
       && groupadd -f conan-2000 -g 2000 \
       && groupadd -f conan-999 -g 999 \
       && useradd -ms /bin/bash conan -g 1001 -G 1000,2000,999 \
       && printf "conan:conan" | chpasswd \
       && adduser conan sudo \
       && printf "conan ALL= NOPASSWD: ALL\\n" >> /etc/sudoers

# TODO: Comsume from .env file only
ARG PYTHON_VERSION=3.7.17

RUN wget --no-check-certificate --quiet -O /tmp/pyenv-installer https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer \
       && chmod +x /tmp/pyenv-installer \
       && /tmp/pyenv-installer \
       && rm /tmp/pyenv-installer \
       && update-alternatives --install /usr/bin/pyenv pyenv /opt/pyenv/bin/pyenv 100 \
       && PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install ${PYTHON_VERSION} \
       && pyenv global ${PYTHON_VERSION} \
       && ln -s /usr/lib/python3/dist-packages/lsb_release.py /opt/pyenv/versions/${PYTHON_VERSION}/lib/python${PYTHON_VERSION%.*}/lsb_release.py

RUN chown -R conan:1001 /opt/pyenv \
       # remove all __pycache__ directories created by pyenv
       && find /opt/pyenv -iname __pycache__ -print0 | xargs -0 rm -rf \
       && update-alternatives --install /usr/bin/python python /opt/pyenv/shims/python 100 \
       && update-alternatives --install /usr/bin/python3 python3 /opt/pyenv/shims/python3 100 \
       && update-alternatives --install /usr/bin/pip pip /opt/pyenv/shims/pip 100 \
       && update-alternatives --install /usr/bin/pip3 pip3 /opt/pyenv/shims/pip3 100

RUN apt-get -qq purge -y \
          libgmp-dev \
          libmpfr-dev \
          libmpc-dev \
          ninja-build \
          libffi-dev \
          libssl-dev \
          zlib1g-dev \
          libbz2-dev \
          libsqlite3-dev \
          libreadline-dev \
          libncurses5-dev \
          libncursesw5-dev \
          liblzma-dev \
       && apt-get -qq autoremove -y \
       && apt-get -qq autoclean \
       && apt-get -qq update \
       && rm -rf /var/lib/apt/lists/*

ARG CONAN_VERSION

RUN pip install -q --upgrade --no-cache-dir pip \
    && pip install -q --no-cache-dir conan==${CONAN_VERSION}

USER conan
WORKDIR /home/conan

RUN mkdir -p /home/conan/.conan \
    && printf 'eval "$(pyenv init -)"\n' >> ~/.bashrc \
    && printf 'eval "$(pyenv virtualenv-init -)"\n' >> ~/.bashrc
