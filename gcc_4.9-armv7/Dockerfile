FROM ubuntu:wily AS basics

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV CMAKE_VERSION_MAJOR_MINOR=3.18 \ 
    CMAKE_VERSION_FULL=3.18.5 \
    CMAKE_RREV=fabfeac4dd61c45dc0a0451408769226 \
    PYENV_ROOT=/opt/pyenv \
    PATH=/opt/pyenv/shims:${PATH}

COPY sources.list /etc/apt/sources.list

RUN apt-get -qq update \
    && apt-get install -y --no-install-recommends \
    ".*4\.9.*arm-linux-gnueabi.*" \
    sudo=1.8.* \
    build-essential=12.* \
    wget=1.16.* \
    git=1:2.5.* \
    nasm=2.11.* \
    dh-autoreconf=10 \
    ninja-build=1.3.* \
    libffi-dev=3.2.* \
    libssl-dev=1.0.2* \
    pkg-config=0.28-1ubuntu1 \
    subversion=1.8.13-1ubuntu3 \
    zlib1g-dev=1:1.* \
    libbz2-dev=1.* \
    libsqlite3-dev=3.* \
    libreadline-dev=6.* \
    xz-utils=5.* \
    curl=7.* \
    libncurses5-dev=5.* \
    libncursesw5-dev=5.* \
    liblzma-dev=5.* \
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

ENV CC=arm-linux-gnueabi-gcc-4.9 \
    CXX=arm-linux-gnueabi-g++-4.9 \
    CMAKE_C_COMPILER=arm-linux-gnueabi-gcc-4.9 \
    CMAKE_CXX_COMPILER=arm-linux-gnueabi-g++-4.9 \
    STRIP=arm-linux-gnueabi-strip \
    RANLIB=arm-linux-gnueabi-gcc-ranlib-4.9\
    AS=arm-linux-gnueabi-as \
    AR=arm-linux-gnueabi-gcc-ar-4.9 \
    LD=arm-linux-gnueabi-ld \
    FC=arm-linux-gnueabi-gfortran-4.9


FROM basics AS building_layer 

ENV CXX=/usr/bin/g++-4.9 \
    CC=/usr/bin/gcc-4.9 \
    CMAKE_C_COMPILER=gcc-4.9 \
    CMAKE_CXX_COMPILER=g++-4.9

RUN mkdir conan_packages \
    && cd conan_packages \
    # Temporary dependencies for (potential) boostrapping purposes 
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
    && CONAN_REVISIONS_ENABLED=1 conan install cmake/${CMAKE_VERSION_FULL}@#${CMAKE_RREV} --build missing -g deploy \
    && cd cmake/licenses \
    && mkdir cmake \ 
    && ls | grep -v cmake | xargs mv -t cmake


FROM basics AS final_image 

USER conan
WORKDIR /home/conan

COPY --from=building_layer /conan_packages/cmake/ /usr/

RUN mkdir -p /home/conan/.conan \
    && printf 'eval "$(pyenv init -)"\n' >> ~/.bashrc \
    && printf 'eval "$(pyenv virtualenv-init -)"\n' >> ~/.bashrc \
    && conan profile new default --detect \
    && conan profile update settings.arch=armv7 default
