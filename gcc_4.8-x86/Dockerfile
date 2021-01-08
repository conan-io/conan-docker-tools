FROM i386/ubuntu:trusty AS basics
ENTRYPOINT ["linux32", "--"]

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV CMAKE_VERSION_MAJOR_MINOR=3.18 \ 
    CMAKE_VERSION_FULL=3.18.5 \
    CONAN_ENV_ARCH=x86 \
    PYENV_ROOT=/opt/pyenv \
    PATH=/opt/pyenv/shims:${PATH} \
    CXX=/usr/bin/g++ \
    CC=/usr/bin/gcc

RUN dpkg --add-architecture i386 \
    && apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends \
       sudo \
       build-essential \
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
    && groupadd 1001 -g 1001 \
    && groupadd 1000 -g 1000 \
    && groupadd 2000 -g 2000 \
    && groupadd 999 -g 999 \
    && useradd -ms /bin/bash conan -g 1001 -G 1000,2000,999 \
    && printf "conan:conan" | chpasswd \
    && adduser conan sudo \
    && printf "conan ALL= NOPASSWD: ALL\\n" >> /etc/sudoers \
    && sed -i '0,/python3/s//python2.7/' /usr/bin/lsb_release \
    && wget --no-check-certificate --quiet -O /tmp/pyenv-installer https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer \
    && chmod +x /tmp/pyenv-installer \
    && /tmp/pyenv-installer \
    && rm /tmp/pyenv-installer \
    && update-alternatives --install /usr/bin/pyenv pyenv /opt/pyenv/bin/pyenv 100 \
    && PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.6.7 \
    && pyenv global 3.6.7 \
    && pip install -q --upgrade --no-cache-dir pip \
    && pip install -q --no-cache-dir conan conan-package-tools \
    && chown -R conan:1001 /opt/pyenv \
    # remove all __pycache__ directories created by pyenv
    && find /opt/pyenv -iname __pycache__ -print0 | xargs -0 rm -rf \
    && update-alternatives --install /usr/bin/python python /opt/pyenv/shims/python 100 \
    && update-alternatives --install /usr/bin/python3 python3 /opt/pyenv/shims/python3 100 \
    && update-alternatives --install /usr/bin/pip pip /opt/pyenv/shims/pip 100 \
    && update-alternatives --install /usr/bin/pip3 pip3 /opt/pyenv/shims/pip3 100


FROM basics AS building_layer 

RUN mkdir conan_packages \
    && cd conan_packages \
    # Temporary dependencies for boostrapping purposes
    && wget --no-check-certificate --quiet https://cmake.org/files/v${CMAKE_VERSION_MAJOR_MINOR}/cmake-${CMAKE_VERSION_FULL}.tar.gz \
    && tar -xzf cmake-${CMAKE_VERSION_FULL}.tar.gz \
    && cd cmake-${CMAKE_VERSION_FULL} \
    && ./bootstrap > /dev/null \
    && make -s -j`nproc` \
    && make -s install > /dev/null \
    && cd - \
    && rm -rf cmake-* \
    # Install Packages which we want to deploy
    # Install CMake + move license files to specific licenses/cmake subdirectory for deploy
    # To avoid GLIBC/CXX compatibility issues, we have to (re)build the package
    && conan install cmake/${CMAKE_VERSION_FULL}@ --build -g deploy \
    && cd cmake/licenses \
    && mkdir cmake \ 
    && ls | grep -v cmake | xargs mv -t cmake


FROM basics AS final_image 

USER conan
WORKDIR /home/conan

COPY --from=building_layer /conan_packages/cmake/ /usr/

RUN mkdir -p /home/conan/.conan \
    && printf 'eval "$(pyenv init -)"\n' >> ~/.bashrc \
    && printf 'eval "$(pyenv virtualenv-init -)"\n' >> ~/.bashrc
