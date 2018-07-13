FROM lasote/conangcc52

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV CC=arm-linux-gnueabihf-gcc-4.9 \
    CXX=arm-linux-gnueabihf-g++-4.9 \
    CMAKE_C_COMPILER=arm-linux-gnueabihf-gcc-4.9 \
    CMAKE_CXX_COMPILER=arm-linux-gnueabihf-g++-4.9 \
    STRIP=arm-linux-gnueabihf-strip \
    RANLIB=arm-linux-gnueabihf-gcc-ranlib-4.9\
    AS=arm-linux-gnueabihf-as \
    AR=arm-linux-gnueabihf-gcc-ar-4.9 \
    LD=arm-linux-gnueabihf-ld \
    FC=arm-linux-gnueabihf-gfortran-4.9

RUN sudo apt-get -qq update \
    && sudo apt-get -qq install -y --force-yes --no-install-recommends \
       ".*4\.9.*arm-linux-gnueabihf.*" \
    && sudo rm -rf /var/lib/apt/lists/* \
    && sudo pip install conan --update \
    && conan profile new default --detect \
    && conan profile update settings.arch=armv7hf default
