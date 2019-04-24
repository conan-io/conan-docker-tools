FROM conanio/android-clang8

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV ANDROID_ABI=x86 \
    ANDROID_PLATFORM=android-16 \
    CC=$STANDALONE_TOOLCHAIN/bin/i686-linux-android16-clang \
    CXX=$STANDALONE_TOOLCHAIN/bin/i686-linux-android16-clang++ \
    LD=$STANDALONE_TOOLCHAIN/bin/i686-linux-android-ld \
    AR=$STANDALONE_TOOLCHAIN/bin/i686-linux-android-ar \
    AS=$STANDALONE_TOOLCHAIN/bin/i686-linux-android-as \
    RANLIB=$STANDALONE_TOOLCHAIN/bin/i686-linux-android-ranlib \
    STRIP=$STANDALONE_TOOLCHAIN/bin/i686-linux-android-strip \
    ADDR2LINE=$STANDALONE_TOOLCHAIN/bin/i686-linux-android-addr2line \
    NM=$STANDALONE_TOOLCHAIN/bin/i686-linux-android-nm \
    OBJCOPY=$STANDALONE_TOOLCHAIN/bin/i686-linux-android-objcopy \
    OBJDUMP=$STANDALONE_TOOLCHAIN/bin/i686-linux-android-objdump \
    READELF=$STANDALONE_TOOLCHAIN/bin/i686-linux-android-readelf

RUN conan profile update settings.arch=x86 default \
    && conan profile update settings.os=Android default \
    && conan profile update settings.os.api_level=16 default \
    && conan profile update settings.compiler.libcxx=libc++ default
