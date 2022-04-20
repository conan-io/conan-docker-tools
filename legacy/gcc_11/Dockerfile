FROM ubuntu:focal

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV GCC_VERSION=11 \
    CMAKE_VERSION_FULL=3.18.2 \
    CC=/usr/bin/gcc \
    CXX=/usr/bin/g++ \
    PYENV_ROOT=/opt/pyenv \
    PYTHON_VERSION=3.7.13 \
    PATH=/opt/pyenv/shims:${PATH} \
    DEBIAN_FRONTEND=noninteractive

RUN dpkg --add-architecture i386 \


    && apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends --no-install-suggests gnupg software-properties-common \
    && printf "deb http://ppa.launchpad.net/ubuntu-toolchain-r/test/ubuntu focal main\n" >> /etc/apt/sources.list \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 60C317803A41BA51845E371A1E9377A2BA9EF27F \
    && add-apt-repository ppa:git-core/ppa -y \
    && apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends --no-install-suggests \
       sudo \
       binutils \
       wget \
       git \
       libc6-dev \
       g++-${GCC_VERSION} \
       libgmp-dev \
       libmpfr-dev \
       libmpc-dev \
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
    && update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-${GCC_VERSION} 100 \
    && update-alternatives --install /usr/bin/c++ c++ /usr/bin/g++-${GCC_VERSION} 100 \
    && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-${GCC_VERSION} 100 \
    && update-alternatives --install /usr/bin/cc cc /usr/bin/gcc-${GCC_VERSION} 100 \
    && update-alternatives --install /usr/bin/gcov gcov /usr/bin/gcov-${GCC_VERSION} 100 \
    && update-alternatives --install /usr/bin/gcov-dump gcov-dump /usr/bin/gcov-dump-${GCC_VERSION} 100 \
    && update-alternatives --install /usr/bin/gcov-tool gcov-tool /usr/bin/gcov-tool-${GCC_VERSION} 100 \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    && rm -rf /var/lib/apt/lists/* \
    && curl -fL https://getcli.jfrog.io | sh \
    && mv jfrog /usr/local/bin/jfrog \
    && chmod +x /usr/local/bin/jfrog \
    && groupadd _1001 -g 1001 \
    && groupadd _1000 -g 1000 \
    && groupadd _2000 -g 2000 \
    && groupadd _999 -g 999 \
    && useradd -ms /bin/bash conan -g _1001 -G _1000,_2000,_999 \
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
    && ln -s /usr/lib/python3/dist-packages/lsb_release.py /opt/pyenv/versions/3.7.13/lib/python3.7/lsb_release.py \
    && pip install -q --upgrade --no-cache-dir pip \
    && pip install -q --no-cache-dir conan conan-package-tools cmake==${CMAKE_VERSION_FULL} \
    && chown -R conan:1001 /opt/pyenv \
    && find /opt/pyenv -iname __pycache__ -print0 | xargs -0 rm -rf \
    && update-alternatives --install /usr/bin/python python /opt/pyenv/shims/python 100 \
    && update-alternatives --install /usr/bin/python3 python3 /opt/pyenv/shims/python3 100 \
    && update-alternatives --install /usr/bin/pip pip /opt/pyenv/shims/pip 100 \
    && update-alternatives --install /usr/bin/pip3 pip3 /opt/pyenv/shims/pip3 100

USER conan
WORKDIR /home/conan

RUN mkdir -p /home/conan/.conan \
    && printf 'eval "$(pyenv init -)"\n' >> ~/.bashrc \
    && printf 'eval "$(pyenv virtualenv-init -)"\n' >> ~/.bashrc
