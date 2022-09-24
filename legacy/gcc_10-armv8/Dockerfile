FROM conanio/gcc10

LABEL maintainer="Conan.io <info@conan.io>"

ARG CONAN_VERSION

RUN echo 'deb [arch=arm64] http://ports.ubuntu.com/ focal main multiverse universe' | sudo tee -a /etc/apt/sources.list \
    && echo 'deb [arch=arm64] http://ports.ubuntu.com/ focal-security main multiverse universe' | sudo tee -a /etc/apt/sources.list \
    && echo 'deb [arch=arm64] http://ports.ubuntu.com/ focal-backports main multiverse universe' | sudo tee -a /etc/apt/sources.list \
    && echo 'deb [arch=arm64] http://ports.ubuntu.com/ focal-updates main multiverse universe' | sudo tee -a /etc/apt/sources.list \
    && sudo apt-get -qq update \
    && sudo apt-get install -y --no-install-recommends --no-install-suggests ".*10.*aarch64-linux-gnu.*" \
    && sudo update-alternatives --install /usr/bin/aarch64-linux-gnu-gcc aarch64-linux-gnu-gcc /usr/bin/aarch64-linux-gnu-gcc-10 100 \
    && sudo update-alternatives --install /usr/bin/aarch64-linux-gnu-g++ aarch64-linux-gnu-g++ /usr/bin/aarch64-linux-gnu-g++-10 100 \
    && sudo update-alternatives --install /usr/bin/aarch64-linux-gnu-gcov aarch64-linux-gnu-gcov /usr/bin/aarch64-linux-gnu-gcov-10 100 \
    && sudo update-alternatives --install /usr/bin/aarch64-linux-gnu-gcov-dump aarch64-linux-gnu-gcov-dump /usr/bin/aarch64-linux-gnu-gcov-dump-10 100 \
    && sudo update-alternatives --install /usr/bin/aarch64-linux-gnu-gcov-tool aarch64-linux-gnu-gcov-tool /usr/bin/aarch64-linux-gnu-gcov-tool-10 100 \
    && sudo rm -rf /var/lib/apt/lists/* \
    && pip install -q --no-cache-dir conan==${CONAN_VERSION} conan-package-tools --upgrade \
    && conan profile new default --detect \
    && conan profile update settings.compiler.libcxx=libstdc++11 default \
    && conan profile new armv8 --detect \
    && conan profile update settings.arch=armv8 armv8 \
    && conan profile update settings.compiler.libcxx=libstdc++11 armv8 \
    && conan profile update env.CC=/usr/bin/aarch64-linux-gnu-gcc-10 armv8 \
    && conan profile update env.CXX=/usr/bin/aarch64-linux-gnu-g++-10 armv8 \
    && conan profile update env.CMAKE_C_COMPILER=/usr/bin/aarch64-linux-gnu-gcc-10 armv8 \
    && conan profile update env.CMAKE_CXX_COMPILER=/usr/bin/aarch64-linux-gnu-g++-10 armv8 \
    && conan profile update env.STRIP=/usr/bin/aarch64-linux-gnu-strip armv8 \
    && conan profile update env.AS=/usr/bin/aarch64-linux-gnu-as armv8 \
    && conan profile update env.AR=/usr/bin/aarch64-linux-gnu-ar armv8 \
    && conan profile update env.LD=/usr/bin/aarch64-linux-gnu-ld armv8 \
    && conan profile update env.FC=/usr/bin/aarch64-linux-gnu-gfortran-10 armv8 \
    && conan profile update env.GCOV=/usr/bin/aarch64-linux-gnu-gcov-10 armv8
