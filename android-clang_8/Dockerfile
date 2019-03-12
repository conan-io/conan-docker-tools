FROM conanio/gcc8

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ARG ANDROID_NDK=/android-ndk-r19c
ARG STANDALONE_TOOLCHAIN=/android-ndk-r19c/toolchains/llvm/prebuilt/linux-x86_64

ENV ANDROID_NDK=$ANDROID_NDK \
    ANDROID_NDK_HOME=$ANDROID_NDK \
    STANDALONE_TOOLCHAIN=$STANDALONE_TOOLCHAIN \
    ANDROID_STL=c++_shared \
    ANDROID_ABI=x86_64 \
    ANDROID_PLATFORM=android-21 \
    ANDROID_TOOLCHAIN=clang \
    CC=$STANDALONE_TOOLCHAIN/bin/x86_64-linux-android21-clang \
    CXX=$STANDALONE_TOOLCHAIN/bin/x86_64-linux-android21-clang++ \
    LD=$STANDALONE_TOOLCHAIN/bin/x86_64-linux-android-ld \
    AR=$STANDALONE_TOOLCHAIN/bin/x86_64-linux-android-ar \
    AS=$STANDALONE_TOOLCHAIN/bin/x86_64-linux-android-as \
    RANLIB=$STANDALONE_TOOLCHAIN/bin/x86_64-linux-android-ranlib \
    STRIP=$STANDALONE_TOOLCHAIN/bin/x86_64-linux-android-strip \
    ADDR2LINE=$STANDALONE_TOOLCHAIN/bin/x86_64-linux-android-addr2line \
    NM=$STANDALONE_TOOLCHAIN/bin/x86_64-linux-android-nm \
    OBJCOPY=$STANDALONE_TOOLCHAIN/bin/x86_64-linux-android-objcopy \
    OBJDUMP=$STANDALONE_TOOLCHAIN/bin/x86_64-linux-android-objdump \
    READELF=$STANDALONE_TOOLCHAIN/bin/x86_64-linux-android-readelf \
    SYSROOT=$STANDALONE_TOOLCHAIN/sysroot \
    CONAN_CMAKE_FIND_ROOT_PATH=$STANDALONE_TOOLCHAIN/sysroot \
    CONAN_CMAKE_TOOLCHAIN_FILE=$ANDROID_NDK/build/cmake/android.toolchain.cmake \
    CONAN_CMAKE_PROGRAM=/cmake-wrapper \
    CMAKE_FIND_ROOT_PATH_MODE_PROGRAM=BOTH \
    CMAKE_FIND_ROOT_PATH_MODE_LIBRARY=BOTH \
    CMAKE_FIND_ROOT_PATH_MODE_INCLUDE=BOTH \
    CMAKE_FIND_ROOT_PATH_MODE_PACKAGE=BOTH \
    PATH=$PATH:$STANDALONE_TOOLCHAIN/bin

COPY cmake-wrapper /cmake-wrapper

RUN sudo apt-get update \
    && sudo apt-get -qq install -y --no-install-recommends unzip \
    && sudo rm -rf /var/lib/apt/lists/* \
    && sudo curl -s https://dl.google.com/android/repository/android-ndk-r19c-linux-x86_64.zip -O \
    && sudo unzip -qq android-ndk-r19c-linux-x86_64.zip -d / \
    && sudo rm -f android-ndk-r19c-linux-x86_64.zip \
    && sudo chmod +x /cmake-wrapper \
    && conan profile new default --detect \
    && conan profile update settings.os=Android default \
    && conan profile update settings.os.api_level=21 default \
    && conan profile update settings.compiler.libcxx=libc++ default
