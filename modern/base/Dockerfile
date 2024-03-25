ARG DISTRO_VERSION

FROM ubuntu:${DISTRO_VERSION}

LABEL maintainer="Conan.io <info@conan.io>"

ENV PYENV_ROOT=/opt/pyenv \
    PATH=/opt/pyenv/shims:/opt/conan/binutils/bin:${PATH} \
    CONAN_USER_HOME=/home/conan \
    LC_ALL="en_US.UTF-8" \
    LANG="en_US.UTF-8" \
    LANGUAGE="en_US.UTF-8"

WORKDIR /root

COPY conan.lock conanfile.txt /opt/conan/

RUN apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends software-properties-common \
    && add-apt-repository ppa:git-core/ppa -y \
    && apt-get -qq update \
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
       language-pack-en \
    && locale-gen en_US.UTF-8 \
    && rm -rf /var/lib/apt/lists/*

ARG CMAKE_VERSION

RUN wget -q --no-check-certificate https://cmake.org/files/v${CMAKE_VERSION%.*}/cmake-${CMAKE_VERSION}-Linux-x86_64.tar.gz \
    && tar -xzf cmake-${CMAKE_VERSION}-Linux-x86_64.tar.gz \
       --exclude=bin/cmake-gui \
       --exclude=doc/cmake \
       --exclude=share/cmake-${CMAKE_VERSION%.*}/Help \
       --exclude=share/vim \
       --exclude=share/vim \
    && cp -fR cmake-${CMAKE_VERSION}-Linux-x86_64/* /usr \
    && rm -rf /root/cmake-${CMAKE_VERSION}-Linux-x86_64 \
    && rm /root/cmake-${CMAKE_VERSION}-Linux-x86_64.tar.gz

RUN curl -fL https://getcli.jfrog.io | sh -s 1.48.1 \
    && mv jfrog /usr/local/bin/jfrog \
    && chmod +x /usr/local/bin/jfrog

RUN groupadd -f conan-1001 -g 1001 \
    && groupadd -f conan-1000 -g 1000 \
    && groupadd -f conan-2000 -g 2000 \
    && groupadd -f conan-999 -g 999 \
    && useradd -ms /bin/bash conan -g 1001 -G 1000,2000,999 \
    && printf "conan:conan" | chpasswd \
    && adduser conan sudo \
    && printf "conan ALL= NOPASSWD: ALL\\n" >> /etc/sudoers

ARG PYTHON_VERSION

RUN wget --no-check-certificate --quiet -O /tmp/pyenv-installer https://raw.githubusercontent.com/pyenv/pyenv-installer/56d708c8bda56370c4bc1e2fce68087cfcd007eb/bin/pyenv-installer \
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
    && ln -s /usr/share/pyshared/lsb_release.py /opt/pyenv/versions/${PYTHON_VERSION}/lib/python${PYTHON_VERSION%.*}/site-packages/lsb_release.py \
    && pip install -q --upgrade --no-cache-dir pip

RUN printf '/usr/local/lib\n' > /etc/ld.so.conf.d/20local-lib.conf \
    && printf '/usr/local/lib64\n' >> /etc/ld.so.conf.d/20local-lib.conf \
    && mv /etc/ld.so.conf.d/libc.conf /etc/ld.so.conf.d/10libc.conf \
    && rm /etc/ld.so.cache \
    && ldconfig -C /etc/ld.so.cache \
    && apt-get -qq purge -y \
       g++-multilib \
       gcc \
       libgmp-dev \
       libmpfr-dev \
       libmpc-dev \
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
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/*

RUN runuser -u conan -- printf 'eval "$(pyenv init -)"\n' >> /home/conan/.bashrc \
    && runuser -u conan -- printf 'eval "$(pyenv virtualenv-init -)"\n' >> /home/conan/.bashrc \
    && chown -R conan:1001 /opt/pyenv \
    && chown -R conan:1001 /opt/conan

USER conan
WORKDIR /home/conan

ARG CONAN_VERSION

RUN pip install conan~=1.0 \
    && CONAN_REVISIONS_ENABLED=1 CONAN_USER_HOME=/tmp/conan conan install -r conancenter -g deploy -if /opt/conan -l /opt/conan/conan.lock /opt/conan/conanfile.txt \
    && rm -rf /tmp/conan \
    && pip install conan==${CONAN_VERSION}
