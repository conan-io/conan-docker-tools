FROM conanio/gcc5

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV CC=arm-linux-gnueabihf-gcc-5 \
    CXX=arm-linux-gnueabihf-g++-5 \
    CMAKE_C_COMPILER=arm-linux-gnueabihf-gcc-5 \
    CMAKE_CXX_COMPILER=arm-linux-gnueabihf-g++-5 \
    STRIP=arm-linux-gnueabihf-strip \
    RANLIB=arm-linux-gnueabihf-ranlib\
    AS=arm-linux-gnueabihf-as \
    AR=arm-linux-gnueabihf-ar \
    LD=arm-linux-gnueabihf-ld \
    FC=arm-linux-gnueabihf-gfortran-5

RUN sudo dpkg --add-architecture armhf
RUN sudo sed -i 's/deb\s/deb \[arch=amd64,i386\] /' /etc/apt/sources.list

USER root
RUN PREFIX="deb [arch=armhf] http://ports.ubuntu.com/ubuntu-ports/" \
  && SUFFIX="main restricted universe multiverse" \
  && DEST="/etc/apt/sources.list.d/armel.list" \
  && echo "${PREFIX} xenial ${SUFFIX}" >> ${DEST} \
  && echo "${PREFIX} xenial-updates ${SUFFIX}" >> ${DEST} \
  && echo "${PREFIX} xenial-security ${SUFFIX}" >> ${DEST} \
  && echo "${PREFIX} xenial-backports ${SUFFIX}" >> ${DEST}
USER conan

RUN sudo apt-get -q update \
    && sudo apt-get -q install -y --no-install-recommends \
       ".*5.*arm-linux-gnueabihf.*" \
       binutils-arm-linux-gnueabi \
    && sudo rm -rf /var/lib/apt/lists/* \
    && sudo pip install -q --no-cache-dir conan --upgrade \
    && conan profile new default --detect \
    && conan profile update settings.arch=armv7hf default
