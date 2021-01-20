FROM ubuntu:bionic

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV LLVM_VERSION=10 \
    CC=clang \
    CXX=clang++ \
    CMAKE_C_COMPILER=clang \
    CMAKE_CXX_COMPILER=clang++ \
    PYENV_ROOT=/opt/pyenv \
    PYTHON_VERSION=3.8.2 \
    PATH=/opt/pyenv/shims:${PATH} \
    CMAKE_VERSION_FULL=3.18.2

RUN dpkg --add-architecture i386 \
    && apt-get -qq update \
    # Install basics
    && apt-get install -y --no-install-recommends \
       sudo \
       wget \
       git \
       subversion \
       make \
       gnupg \
       ca-certificates \
       dh-autoreconf \
    # Install compiler toolset
    && apt-get install -y --no-install-recommends \
       lsb-release \
       software-properties-common \
    && wget https://apt.llvm.org/llvm.sh \
    && chmod +x llvm.sh \
    && sudo ./llvm.sh ${LLVM_VERSION} \
    && rm llvm.sh \
    # Further LLVM packages not installed by the llvm.sh script
    && apt-get install -y --no-install-recommends \
       libc++-10-dev \
       libc++abi-10-dev \
    && apt-get remove -y lsb-release software-properties-common \
    # Install dependencies of Python
    && apt-get install -y --no-install-recommends \
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
    && apt-get autoremove -y \
    && apt-get clean all \
    # Update default compiler
    && update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-${LLVM_VERSION} 100 \
    && update-alternatives --install /usr/bin/clang clang /usr/bin/clang-${LLVM_VERSION} 100 \
    && update-alternatives --install /usr/bin/cc cc /usr/bin/clang-${LLVM_VERSION} 100 \
    && update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++-${LLVM_VERSION} 100 \
    && update-alternatives --install /usr/bin/cpp cpp /usr/bin/clang++-${LLVM_VERSION} 100 \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    && rm -rf /var/lib/apt/lists/* \
    && wget -q --no-check-certificate -O /usr/local/bin/jfrog https://api.bintray.com/content/jfrog/jfrog-cli-go/\$latest/jfrog-cli-linux-amd64/jfrog?bt_package=jfrog-cli-linux-amd64 \
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
    && pip install -q --upgrade --no-cache-dir pip \
    && pip install -q --no-cache-dir conan conan-package-tools cmake==${CMAKE_VERSION_FULL} \
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
