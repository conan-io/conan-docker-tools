FROM ubuntu:bionic

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ARG CONAN_VERSION

ENV LLVM_VERSION=11 \
    CMAKE_VERSION_FULL=3.18.2 \
    CC=clang \
    CXX=clang++ \
    CMAKE_C_COMPILER=clang \
    CMAKE_CXX_COMPILER=clang++ \
    PYENV_ROOT=/opt/pyenv \
    PYTHON_VERSION=3.7.13 \
    PATH=/opt/pyenv/shims:${PATH}

RUN apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends software-properties-common \
    && add-apt-repository ppa:git-core/ppa -y \
    && apt-get -qq update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
       sudo \
       wget \
       git \
       subversion \
       make \
       gnupg \
       ca-certificates \
       dh-autoreconf \
       pkg-config \
       lsb-release \
       libreadline-dev \
       libsqlite3-dev \
       libffi-dev \
       libssl-dev \
       zlib1g-dev \
       libbz2-dev \
       xz-utils \
       curl \
       libncurses5-dev \
       libncursesw5-dev \
       liblzma-dev \
    && printf 'deb http://apt.llvm.org/bionic/   llvm-toolchain-bionic-11  main' >> /etc/apt/sources.list \
    && wget --no-check-certificate --quiet -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \
    && apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends --no-install-suggests \
       clang-11 \
       lldb-11 \
       lld-11 \
       clangd-11 \
       libc++-11-dev \
       libc++abi-11-dev \
    && apt-get -qq autoremove -y \
    && apt-get -qq clean all \
    # Update default compiler
    && update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-${LLVM_VERSION} 100 \
    && update-alternatives --install /usr/bin/clang clang /usr/bin/clang-${LLVM_VERSION} 100 \
    && update-alternatives --install /usr/bin/cc cc /usr/bin/clang-${LLVM_VERSION} 100 \
    && update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++-${LLVM_VERSION} 100 \
    && update-alternatives --install /usr/bin/cpp cpp /usr/bin/clang++-${LLVM_VERSION} 100 \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    && rm -rf /var/lib/apt/lists/* \
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
    && wget --no-check-certificate --quiet -O /tmp/pyenv-installer https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer \
    && chmod +x /tmp/pyenv-installer \
    && /tmp/pyenv-installer \
    && rm /tmp/pyenv-installer \
    && update-alternatives --install /usr/bin/pyenv pyenv /opt/pyenv/bin/pyenv 100 \
    && PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install ${PYTHON_VERSION} \
    && pyenv global ${PYTHON_VERSION} \
    && ln -s /usr/lib/python3/dist-packages/lsb_release.py /opt/pyenv/versions/${PYTHON_VERSION}/lib/python3.7/lsb_release.py \
    && pip install -q --upgrade --no-cache-dir pip \
    && pip install -q --no-cache-dir conan==${CONAN_VERSION} conan-package-tools cmake==${CMAKE_VERSION_FULL} \
    && chown -R conan:1001 /opt/pyenv \
    # remove all __pycache__ directories created by pyenv
    && find /opt/pyenv -iname __pycache__ -print0 | xargs -0 rm -rf \
    && update-alternatives --install /usr/bin/python python /opt/pyenv/shims/python 100 \
    && update-alternatives --install /usr/bin/python3 python3 /opt/pyenv/shims/python3 100 \
    && update-alternatives --install /usr/bin/pip pip /opt/pyenv/shims/pip 100 \
    && update-alternatives --install /usr/bin/pip3 pip3 /opt/pyenv/shims/pip3 100 \
    && apt-get -qq purge -y \
          libreadline-dev \
          libsqlite3-dev \
          libffi-dev \
          libssl-dev \
          zlib1g-dev \
          libbz2-dev \
          libncurses5-dev \
          libncursesw5-dev \
          liblzma-dev \
       && apt-get -qq autoremove -y \
       && apt-get -qq autoclean \
       && apt-get -qq update \
       && rm -rf /var/lib/apt/lists/*

USER conan
WORKDIR /home/conan

RUN mkdir -p /home/conan/.conan \
    && printf 'eval "$(pyenv init -)"\n' >> ~/.bashrc \
    && printf 'eval "$(pyenv virtualenv-init -)"\n' >> ~/.bashrc
