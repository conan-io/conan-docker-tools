FROM conanio/gcc10

LABEL maintainer="Conan.io <info@conan.io>"

ARG ANDROID_NDK_VERSION=r25
ARG ANDROID_NDK_API_LEVEL=21
ARG CONAN_VERSION=1.52.0

RUN pip install conan==${CONAN_VERSION} \
    && conan profile new default --detect \
    && conan profile update settings.compiler.libcxx=libstdc++11 default \
    && conan profile new android --detect \
    && conan profile update settings.os=Android android \
    && conan profile update settings.arch=armv7 android \
    && conan profile update settings.os.api_level=${ANDROID_NDK_API_LEVEL} android \
    && conan profile update settings.compiler=clang android \
    && conan profile update settings.compiler.version=14 android \
    && conan profile update settings.compiler.libcxx=libc++ android \
    && printf "[tool_requires]\nandroid-ndk/${ANDROID_NDK_VERSION}@\n" >> ${HOME}/.conan/profiles/android
