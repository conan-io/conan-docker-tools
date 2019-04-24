FROM conanio/android-clang8

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV ANDROID_ABI=arm64-v8a \
    CC=$STANDALONE_TOOLCHAIN/bin/aarch64-linux-android21-clang \
    CXX=$STANDALONE_TOOLCHAIN/bin/aarch64-linux-android21-clang++ \
    LD=$STANDALONE_TOOLCHAIN/bin/aarch64-linux-android-ld \
    AR=$STANDALONE_TOOLCHAIN/bin/aarch64-linux-android-ar \
    AS=$STANDALONE_TOOLCHAIN/bin/aarch64-linux-android-as \
    RANLIB=$STANDALONE_TOOLCHAIN/bin/aarch64-linux-android-ranlib \
    STRIP=$STANDALONE_TOOLCHAIN/bin/aarch64-linux-android-strip \
    ADDR2LINE=$STANDALONE_TOOLCHAIN/bin/aarch64-linux-android-addr2line \
    NM=$STANDALONE_TOOLCHAIN/bin/aarch64-linux-android-nm \
    OBJCOPY=$STANDALONE_TOOLCHAIN/bin/aarch64-linux-android-objcopy \
    OBJDUMP=$STANDALONE_TOOLCHAIN/bin/aarch64-linux-android-objdump \
    READELF=$STANDALONE_TOOLCHAIN/bin/aarch64-linux-android-readelf

RUN conan profile update settings.arch=armv8 default \
    && conan profile update settings.os=Android default \
    && conan profile update settings.os.api_level=21 default \
    && conan profile update settings.compiler.libcxx=libc++ default
