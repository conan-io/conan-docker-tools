FROM alpine:3.15.4
LABEL maintainer="Conan.io <info@conan.io>"

ARG CONAN_VERSION

RUN apk add --no-cache python3 py3-pip \
    && python3 -m pip install https://github.com/conan-io/conan/archive/${CONAN_VERSION}.zip
