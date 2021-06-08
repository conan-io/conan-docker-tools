FROM ubuntu:xenial

LABEL maintainer="Conan.io <info@conan.io>"

ENV PYENV_ROOT=/opt/pyenv \
    PATH=/opt/pyenv/shims:${PATH}

ARG CONAN_VERSION CMAKE_VERSION CMAKE_VERSION_FULL PYTHON_VERSION

WORKDIR /root

RUN apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends --no-install-suggests -o=Dpkg::Use-Pty=0 \
       sudo \
       binutils \
       wget \
       git \
       g++-multilib \
       libgmp-dev \
       libmpfr-dev \
       libmpc-dev \
       nasm \
       dh-autoreconf \
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
    && rm -rf /var/lib/apt/lists/* \
    && wget -q --no-check-certificate https://cmake.org/files/v${CMAKE_VERSION}/cmake-${CMAKE_VERSION_FULL}-Linux-x86_64.tar.gz \
    && tar -xzf cmake-${CMAKE_VERSION_FULL}-Linux-x86_64.tar.gz \
       --exclude=bin/cmake-gui \
       --exclude=doc/cmake \
       --exclude=share/cmake-${CMAKE_VERSION}/Help \
       --exclude=share/vim \
       --exclude=share/vim \
    && cp -fR cmake-${CMAKE_VERSION_FULL}-Linux-x86_64/* /usr \
    && rm -rf /root/cmake-${CMAKE_VERSION_FULL}-Linux-x86_64 \
    && rm /root/cmake-${CMAKE_VERSION_FULL}-Linux-x86_64.tar.gz \
    && curl -fL https://getcli.jfrog.io | sh \
    && mv jfrog /usr/local/bin/jfrog \
    && chmod +x /usr/local/bin/jfrog \
    && groupadd 1001 -g 1001 \
    && groupadd 1000 -g 1000 \
    && groupadd 2000 -g 2000 \
    && groupadd 999 -g 999 \
    && useradd -ms /bin/bash conan -g 1001 -G 1000,2000,999 \
    && printf "conan:conan" | chpasswd \
    && adduser conan sudo \
    && printf "conan ALL= NOPASSWD: ALL\\n" >> /etc/sudoers \
    && wget --no-check-certificate --quiet -O /tmp/pyenv-installer https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer \
    && chmod +x /tmp/pyenv-installer \
    && /tmp/pyenv-installer \
    && rm /tmp/pyenv-installer \
    && update-alternatives --install /usr/bin/pyenv pyenv /opt/pyenv/bin/pyenv 100 \
    && PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install ${PYTHON_VERSION} \
    && pyenv global ${PYTHON_VERSION} \
    && find /opt/pyenv -iname __pycache__ -print0 | xargs -0 rm -rf \
    && update-alternatives --install /usr/bin/python3 python3 /opt/pyenv/shims/python3 100 \
    && update-alternatives --install /usr/bin/pip3 pip3 /opt/pyenv/shims/pip3 100 \
    && update-alternatives --install /usr/local/bin/python python /opt/pyenv/shims/python 100 \
    && update-alternatives --install /usr/local/bin/pip pip /opt/pyenv/shims/pip 100 \
    && pip install -q --upgrade --no-cache-dir pip \
    && pip install -q --no-cache-dir conan==${CONAN_VERSION} conan-package-tools \
    && printf '/usr/local/lib\n' > /etc/ld.so.conf.d/20local-lib.conf \
    && printf '/usr/local/lib64\n' >> /etc/ld.so.conf.d/20local-lib.conf \
    && mv /etc/ld.so.conf.d/libc.conf /etc/ld.so.conf.d/10libc.conf \
    && mv /etc/ld.so.conf.d/x86_64-linux-gnu.conf /etc/ld.so.conf.d/30x86_64-linux-gnu.conf \
    && mv /etc/ld.so.conf.d/zz_i386-biarch-compat.conf /etc/ld.so.conf.d/40zz_i386-biarch-compat.conf \
    && mv /etc/ld.so.conf.d/zz_x32-biarch-compat.conf /etc/ld.so.conf.d/50zz_x32-biarch-compat.conf \
    && rm /etc/ld.so.cache \
    && ldconfig -C /etc/ld.so.cache \
    && apt-get -qq purge -y g++-multilib gcc gcc-5 \
    && apt-get -qq autoremove -y \
    && apt-get -qq autoclean \
    && apt-get -qq update \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/* \
    && runuser -u conan -- printf 'eval "$(pyenv init -)"\n' >> /home/conan/.bashrc \
    && runuser -u conan -- printf 'eval "$(pyenv virtualenv-init -)"\n' >> ~/.bashrc \
    && chown -R conan:1001 /opt/pyenv

USER conan
WORKDIR /home/conan
