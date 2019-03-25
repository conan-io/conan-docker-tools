FROM conanio/android-clang8

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV ANDROID_ABI=armeabi-v7a \
    ANDROID_PLATFORM=android-16 \
    CC=$STANDALONE_TOOLCHAIN/bin/armv7a-linux-androideabi16-clang \
    CXX=$STANDALONE_TOOLCHAIN/bin/armv7a-linux-androideabi16-clang++ \
    LD=$STANDALONE_TOOLCHAIN/bin/arm-linux-androideabi-ld \
    AR=$STANDALONE_TOOLCHAIN/bin/arm-linux-androideabi-ar \
    AS=$STANDALONE_TOOLCHAIN/bin/arm-linux-androideabi-as \
    RANLIB=$STANDALONE_TOOLCHAIN/bin/arm-linux-androideabi-ranlib \
    STRIP=$STANDALONE_TOOLCHAIN/bin/arm-linux-androideabi-strip \
    ADDR2LINE=$STANDALONE_TOOLCHAIN/bin/arm-linux-androideabi-addr2line \
    NM=$STANDALONE_TOOLCHAIN/bin/arm-linux-androideabi-nm \
    OBJCOPY=$STANDALONE_TOOLCHAIN/bin/arm-linux-androideabi-objcopy \
    OBJDUMP=$STANDALONE_TOOLCHAIN/bin/arm-linux-androideabi-objdump \
    READELF=$STANDALONE_TOOLCHAIN/bin/arm-linux-androideabi-readelf

RUN conan profile update settings.arch=armv7 default \
    && conan profile update settings.os=Android default \
    && conan profile update settings.os.api_level=16 default \
    && conan profile update settings.compiler.libcxx=libc++ default
