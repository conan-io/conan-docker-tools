FROM conanio/gcc8

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ARG CONAN_VERSION

ENV CC=x86_64-w64-mingw32-gcc \
    CXX=x86_64-w64-mingw32-g++ \
    CMAKE_C_COMPILER=x86_64-w64-mingw32-gcc \
    CMAKE_CXX_COMPILER=x86_64-w64-mingw32-g++ \
    STRIP=x86_64-w64-mingw32-strip \
    RANLIB=x86_64-w64-mingw32-gcc-ranlib \
    AS=x86_64-w64-mingw32-gcc-as \
    AR=x86_64-w64-mingw32-gcc-ar \
    LD=x86_64-w64-mingw32-ld \
    FC=x86_64-w64-mingw32-gcc-gfortran \
    WINDRES=x86_64-w64-mingw32-windres \
    RC=x86_64-w64-mingw32-windres

RUN sudo apt-get -qq update \
    && sudo apt-get -qq install -y --force-yes --no-install-recommends --no-install-suggests \
       g++-mingw-w64-x86-64=7.* \
    && sudo pip install -q --no-cache-dir conan==${CONAN_VERSION} conan-package-tools --upgrade \
    && sudo rm -rf /var/lib/apt/lists/* \
    && conan profile new default --detect \
    && conan profile update settings.os=Windows default
