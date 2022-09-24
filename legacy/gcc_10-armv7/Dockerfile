FROM conanio/gcc10

LABEL maintainer="Conan.io <info@conan.io>"

ARG CONAN_VERSION

RUN sudo apt-get -qq update \
    && sudo apt-get install -y --no-install-recommends --no-install-suggests ".*10.*arm-linux-gnueabi.*" \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabi-gcc arm-linux-gnueabi-gcc /usr/bin/arm-linux-gnueabi-gcc-10 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabi-g++ arm-linux-gnueabi-g++ /usr/bin/arm-linux-gnueabi-g++-10 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabi-gcov arm-linux-gnueabi-gcov /usr/bin/arm-linux-gnueabi-gcov-10 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabi-gcov-dump arm-linux-gnueabi-gcov-dump /usr/bin/arm-linux-gnueabi-gcov-dump-10 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabi-gcov-tool arm-linux-gnueabi-gcov-tool /usr/bin/arm-linux-gnueabi-gcov-tool-10 100 \
    && sudo rm -rf /var/lib/apt/lists/* \
    && pip install -q conan==${CONAN_VERSION} conan-package-tools --upgrade \
    && conan profile new default --detect \
    && conan profile update settings.compiler.libcxx=libstdc++11 default \
    && conan profile new armv7 --detect \
    && conan profile update settings.arch=armv7 armv7 \
    && conan profile update settings.compiler.libcxx=libstdc++11 armv7 \
    && conan profile update env.CC=/usr/bin/arm-linux-gnueabi-gcc-10 armv7 \
    && conan profile update env.CXX=/usr/bin/arm-linux-gnueabi-g++-10 armv7 \
    && conan profile update env.CMAKE_C_COMPILER=/usr/bin/arm-linux-gnueabi-gcc-10 armv7 \
    && conan profile update env.CMAKE_CXX_COMPILER=/usr/bin/arm-linux-gnueabi-g++-10 armv7 \
    && conan profile update env.STRIP=/usr/bin/arm-linux-gnueabi-strip armv7 \
    && conan profile update env.AS=/usr/bin/arm-linux-gnueabi-as armv7 \
    && conan profile update env.AR=/usr/bin/arm-linux-gnueabi-ar armv7 \
    && conan profile update env.LD=/usr/bin/arm-linux-gnueabi-ld armv7 \
    && conan profile update env.FC=/usr/bin/arm-linux-gnueabi-gfortran-10 armv7 \
    && conan profile update env.GCOV=/usr/bin/arm-linux-gnueabi-gcov-10 armv7
