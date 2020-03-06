FROM ubuntu:focal

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV LLVM_VERSION=10.0 \
    CC=clang \
    CXX=clang++ \
    CMAKE_C_COMPILER=clang \
    CMAKE_CXX_COMPILER=clang++ \
    PYENV_ROOT=/opt/pyenv \
    PATH=/opt/pyenv/shims:${PATH}

RUN dpkg --add-architecture i386 \
    && apt-get -qq update \
    && apt-get install -y --no-install-recommends \
       sudo=1.* \
       wget=1.* \
       git=1:2.* \
       subversion=1.* \
       g++-10-multilib \
       clang-10=1:10* \
       make=4.* \
       libc6-dev-i386=2.* \
       # libgmp-dev=2:6.* \
       # libmpfr-dev=4.* \
       # libmpc-dev=1.* \
       dh-autoreconf=19 \
       libc++-dev=1:9.* \
       libc++abi-dev=1:9.* \
       gnupg=2.* \
       ca-certificates \
       # Dependencies of Python
       libreadline-dev=8.* \
       libsqlite3-dev=3.* \
       libffi-dev=3.* \
       libssl-dev=1* \
       zlib1g-dev=1:1.* \
       libbz2-dev=1.* \
       xz-utils=5.* \
       curl=7.* \
       libncurses5-dev=6.* \
       libncursesw5-dev=6.* \
       liblzma-dev=5.* \
    && update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-10 100 \
    && update-alternatives --install /usr/bin/clang clang /usr/bin/clang-10 100 \
    && update-alternatives --install /usr/bin/cc cc /usr/bin/clang-10 100 \
    && update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++-10 100 \
    && update-alternatives --install /usr/bin/cpp cpp /usr/bin/clang++-10 100 \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    && rm -rf /var/lib/apt/lists/* \
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
    && PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.8.2 \
    && pyenv global 3.8.2 \
    && pip install -q --upgrade --no-cache-dir pip \
    && pip install -q --no-cache-dir conan conan-package-tools cmake==3.16.3 \
    && chown -R conan:1001 /opt/pyenv \
    # remove all __pycache__ directories created by pyenv
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
