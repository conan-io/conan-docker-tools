[![Build Status](https://dev.azure.com/conanio/conan-docker-tools/_apis/build/status/conan-io.conan-docker-tools?branchName=master)](https://dev.azure.com/conanio/conan-docker-tools/_build/latest?definitionId=1&branchName=master)
# Conan Docker Tools

![logo](logo.png)

Dockerfiles for different gcc compiler versions.
You can use these images directly in your project or with the [conan-package-tools project](https://github.com/conan-io/conan-package-tools).

The images are uploaded to Dockerhub:

#### GCC
| Version                                                                                       | Arch    |  Status, Life cycle  |
|-----------------------------------------------------------------------------------------------|---------|------------|
| [conanio/gcc46: gcc 4.6](https://hub.docker.com/r/conanio/gcc46/)                     | x86_64  |  Supported |
| [conanio/gcc48: gcc 4.8](https://hub.docker.com/r/conanio/gcc48/)                     | x86_64  |  Supported |
| [conanio/gcc48-x86: gcc 4.8](https://hub.docker.com/r/conanio/gcc48-x86/)             | x86     |  Supported |
| [conanio/gcc49: gcc 4.9](https://hub.docker.com/r/conanio/gcc49/)                     | x86_64  |  Supported |
| [conanio/gcc49-x86: gcc 4.9](https://hub.docker.com/r/conanio/gcc49-x86/)             | x86     |  Supported |
| [conanio/gcc49-armv7: gcc 4.9](https://hub.docker.com/r/conanio/gcc49-armv7/)         | armv7   |  Supported |
| [conanio/gcc49-armv7hf: gcc 4.9](https://hub.docker.com/r/conanio/gcc49-armv7hf/)     | armv7hf |  Supported |
| [conanio/gcc52: gcc 5.2](https://hub.docker.com/r/conanio/gcc52/)                     | x86_64  |  Supported |
| [conanio/gcc53: gcc 5.3](https://hub.docker.com/r/conanio/gcc53/)                     | x86_64  | Supported  |
| [conanio/gcc54: gcc 5.4](https://hub.docker.com/r/conanio/gcc54/)                     | x86_64  | Supported  |
| [conanio/gcc63: gcc 6.3](https://hub.docker.com/r/conanio/gcc63/)                     | x86_64  | Supported  |
| [conanio/gcc64: gcc 6.4](https://hub.docker.com/r/conanio/gcc64/)                     | x86_64  | Supported  |
| [conanio/gcc72: gcc 7.2](https://hub.docker.com/r/conanio/gcc72/)                     | x86_64  | Supported  |


GCC>=5 is ABI compatible for minor versions. To solve multiple minors, there are generic images by major version. If you are interested to understand the motivation, read this [issue](https://github.com/conan-io/conan/issues/1214).

| Version                                                                                    | Arch    |  Status, Life cycle  |
|--------------------------------------------------------------------------------------------|---------|----------------------|
| [conanio/gcc5: gcc 5](https://hub.docker.com/r/conanio/gcc5/)                      | x86_64  |  Supported           |
| [conanio/gcc5-x86: gcc 5](https://hub.docker.com/r/conanio/gcc5-x86/)              | x86     |  Supported           |
| [conanio/gcc5-armv7: gcc 5](https://hub.docker.com/r/conanio/gcc5-armv7/)          | armv7   |  Supported           |
| [conanio/gcc5-armv7hf: gcc 5](https://hub.docker.com/r/conanio/gcc5-armv7hf/)      | armv7hf |  Supported           |
| [conanio/gcc6: gcc 6](https://hub.docker.com/r/conanio/gcc6/)                      | x86_64  |  Supported           |
| [conanio/gcc6-x86: gcc 6](https://hub.docker.com/r/conanio/gcc6-x86/)              | x86     |  Supported           |
| [conanio/gcc6-armv7: gcc 6](https://hub.docker.com/r/conanio/gcc6-armv7/)          | armv7   |  Supported           |
| [conanio/gcc6-armv7hf: gcc 6](https://hub.docker.com/r/conanio/gcc6-armv7hf/)      | armv7hf |  Supported           |
| [conanio/gcc7-x86: gcc 7](https://hub.docker.com/r/conanio/gcc7-x86/)              | x86     |  Supported           |
| [conanio/gcc7: gcc 7](https://hub.docker.com/r/conanio/gcc7/)                      | x86_64  |  Supported           |
| [conanio/gcc7-centos6: gcc 7](https://hub.docker.com/r/conanio/gcc7-centos6/)      | x86_64  |  Supported           |
| [conanio/gcc7-centos6-x86: gcc 7](https://hub.docker.com/r/conanio/gcc7-centos6-x86/) | x86  |  Supported           |
| [conanio/gcc7-armv7: gcc 7](https://hub.docker.com/r/conanio/gcc7-armv7/)          | armv7   |  Supported           |
| [conanio/gcc7-armv7hf: gcc 7](https://hub.docker.com/r/conanio/gcc7-armv7hf/)      | armv7hf |  Supported           |
| [conanio/gcc8-x86: gcc 8](https://hub.docker.com/r/conanio/gcc8-x86/)              | x86     |  Supported           |
| [conanio/gcc8: gcc 8](https://hub.docker.com/r/conanio/gcc8/)                      | x86_64  |  Supported           |
| [conanio/gcc8-armv7: gcc 8](https://hub.docker.com/r/conanio/gcc8-armv7/)          | armv7   |  Supported           |
| [conanio/gcc8-armv7hf: gcc 8](https://hub.docker.com/r/conanio/gcc8-armv7hf/)      | armv7hf |  Supported           |


#### Clang

| Version                                                                                       | Arch   |  Status, Life cycle  |
|-----------------------------------------------------------------------------------------------|--------|------------|
| - [conanio/clang38: clang 3.8](https://hub.docker.com/r/conanio/clang38/)             | x86_64 |  Supported |
| - [conanio/clang39-x86: clang 3.9](https://hub.docker.com/r/conanio/clang39-x86/)     | x86    |  Supported |
| - [conanio/clang39: clang 3.9](https://hub.docker.com/r/conanio/clang39/)             | x86_64 |  Supported |
| - [conanio/clang40-x86: clang 4.0](https://hub.docker.com/r/conanio/clang40/-x86)     | x86    |  Supported |
| - [conanio/clang40: clang 4.0](https://hub.docker.com/r/conanio/clang40/)             | x86_64 |  Supported |
| - [conanio/clang50-x86: clang 5.0](https://hub.docker.com/r/conanio/clang50-x86/)     | x86    |  Supported |
| - [conanio/clang50: clang 5.0](https://hub.docker.com/r/conanio/clang50/)             | x86_64 |  Supported |
| - [conanio/clang60-x86: clang 6.0](https://hub.docker.com/r/conanio/clang60-x86/)     | x86    |  Supported |
| - [conanio/clang60: clang 6.0](https://hub.docker.com/r/conanio/clang60/)             | x86_64 |  Supported |
| - [conanio/clang7-x86: clang 7](https://hub.docker.com/r/conanio/clang7-x86/)         | x86    |  Supported |
| - [conanio/clang7: clang 7](https://hub.docker.com/r/conanio/clang7/)                 | x86_64 |  Supported |


#### Android

| Version                                                                                       | Arch   |  Status, Life cycle  |
|-----------------------------------------------------------------------------------------------|--------|------------|
| - [conanio/android-clang8: Android clang 3.8](https://hub.docker.com/r/conanio/android-clang8/)             | x86_64 |  Supported |
| - [conanio/android-clang8-x86: Android clang 3.8](https://hub.docker.com/r/conanio/android-clang8-x86/)     | x86    |  Supported |
| - [conanio/android-clang8-armv7: Android clang 3.8](https://hub.docker.com/r/conanio/android-clang8-armv7/) | x86    |  Supported |
| - [conanio/android-clang8-armv8: Android clang 3.8](https://hub.docker.com/r/conanio/android-clang8-armv8/) | x86    |  Supported |

#### Conan Server

Conan Docker Tools provides an image version with only Conan Server installed, very useful for the cases it is necessary to run a server without touching the host.

| Version                                                                                       | Arch   |  Status, Life cycle  |
|-----------------------------------------------------------------------------------------------|--------|------------|
| - [conanio/conan_server](https://hub.docker.com/r/conanio/conan_server/)             | ANY |  Supported |

#### Conan Installer

**conanio/gcc7-centos6** is a special image version based on CentOS 6, GCC 7 and **glibc 2.12** (very old glibc version). This is intended to build executables that run almost on any Linux because **glibc** guarantees backward compatibility. You can use this image to build your Conan build tools packages (`build_requires`). This image is **ONLY** able to build **x86_64** binaries.

**conanio/gcc7-centos6-x86** is a special image version based on CentOS 6 i386, GCC 7 and **glibc 2.12** (very old glibc version). This is intended to build executables that run almost on any Linux because **glibc** guarantees backward compatibility. You can use this image to build your Conan build tools packages (`build_requires`). This image is **ONLY** able to build **x86** binaries.

Use the images to test your c++ project in travis-ci
======================================================

These Docker images can be used to build your project using the travis-ci CI service, even if you are not using Conan.
It's always recommended to build and test your C/C++ projects in a Docker image running in travis:

- Travis CI images are old, so installing a newer version of gcc and the needed tools can be hard. Check [this thread](https://github.com/travis-ci/travis-ci/issues/6300).
- The generated binaries will use the old **libc/libstdc++** installed in the system, so ABI incompatibilities
      can occur if you use these packages in more modern distributions.

To setup your project, copy the contents of the folder **example_project_test** to your project.
You need to modify:

- ``.travis.yml`` file to enable or disable more ``GCC`` or ``CLang`` versions add more entries to the matrix using DOCKER_IMAGE
- ``.travis/run_project_build.sh`` With the lines that you need to build or test your project

**.travis.yml**

```
    os: linux
    services:
       - docker
    sudo: required
    language: python
    env:
      matrix:
        - DOCKER_IMAGE=conanio/gcc63 # 6.3
        - DOCKER_IMAGE=conanio/clang39 # 3.9

    matrix:
       include:
           - os: osx
             osx_image: xcode8.2 # apple-clang 8.0
             language: generic
             env:

    before_install:
      - ./.travis/before_install.sh

    install:
      - ./.travis/install.sh

    script:
      - ./.travis/run.sh


```

**.travis/run_project_build.sh**. Change it according your project build needed commands:

```
    #!/bin/bash

    rm -rf build && mkdir -p build && cd build
    conan install ../ --build=missing
    cmake -G Ninja -DCMAKE_BUILD_TYPE=Release ..
    cmake --build .

```

#### Jenkins Slave

If you use Jenkins to build your packages and also you use Jenkins Slave to run each docker container, you could use our Docker images prepared for Jenkins Slave. Those images run the script [jenkins-slave.sh](jenkins-jenkins/jenkins-slave), which starts the slave during the container entrypoint.

#### GCC
| Version                                                                                       | Arch    |  Status, Life cycle  |
|-----------------------------------------------------------------------------------------------|---------|------------|
| [conanio/gcc5-jenkins: gcc 5](https://hub.docker.com/r/conanio/gcc5-jenkins/)           | x86_64  |  Supported |


Use the images locally
======================

You can also use the images locally to build or test packages, this is an example command:

```
docker run -v/tmp/.conan:/home/conan/.conan conanio/gcc63 bash -c "conan install lz4/1.8.3@bincrafters/stable --build missing"
```

This command is sharing ``/tmp/.conan`` as a shared folder with the conan home, so the Boost package will be built there.
You can change the directory or execute any other command that works for your needs.

If you are familiarized with Docker compose, also it's possible to start a new container by:

```
docker-compose run -v/tmp/.conan:/home/conan/.conan gcc63 bash -c "conan install lz4/1.8.3@bincrafters/stable --build missing"
```


Build, Test and Deploy
======================

## Introduce
The images are already built and uploaded to **"conanio"** dockerhub account, If you want to build your own images you can do it by:

```
$ python build.py
```

The script *build.py* will build, test and deploy your Docker image. You can configure all stages by environment variables listed below.

Also, you can build only a version:

E.g Build and test only a image with Conan and gcc-6.3
```
$ CONAN_GCC_VERSIONS="6.3" python build.py
```

E.g Build and test only the images with Conan and clang-4.0, clang-3.9
```
$ CONAN_CLANG_VERSIONS="3.9,4.0" python build.py
```

The stages that compose the script will be described below:

### Build
The first stage collect all compiler versions listed in ``CONAN_GCC_VERSIONS`` for ``Gcc`` and in ``CONAN_CLANG_VERSIONS`` for ``Clang``. If you do not set any compiler version, the script will execute all supported versions for ``Gcc`` and ``Clang``.

You can configure only a compiler version or a list, by these variables. If you skipped a compiler list, the build will not be executed for that compiler.

The image tag can be configured by ``DOCKER_BUILD_TAG``. Build default will used **latest**.

Each image created on this stage will be tagged as  ``DOCKER_USERNAME/conan_compiler_version``.

The image will not be removed after build.

### Test
The second stage runs the new image created and builds the Conan package ``gtest/1.8.0``.
The same build variables, as ``CONAN_GCC_VERSIONS`` and ``CONAN_CLANG_VERSIONS`` are used to select the compiler and version.

All tests build the package ``gtest/1.8.0``, for x86 and x86_64.

``Gcc`` images use libstdc++.
``Clang`` images use libc++ and libstdc++.

The packages created on test, are not uploaded to Conan server, Are just to validate the image.

### Deploy
The final stage pushes the image to docker server (hub.docker). ``DOCKER_UPLOAD`` should be true.

The login uses ``DOCKER_LOGIN_USERNAME`` and ``DOCKER_PASSWORD`` to authenticate.


E.g Upload Docker images to Docker hub, after build and test:
```
$ DOCKER_USERNAME="conanio" DOCKER_PASSWORD="conan" DOCKER_UPLOAD="TRUE" python build.py
```


## Environment configuration

You can also use environment variables to change the behavior of Conan Docker Tools.

This is especially useful for CI integration.

Build and Test variables:

- **GCC_VERSIONS**: GCC versions to build, test and deploy, comma separated, e.g. "4.6,4.8,4.9,5.2,5.3,5.4,6.2.6.3"
- **CLANG_VERSIONS**: Clang versions to build, test and deploy, comma separated, e.g. "3.8,3.9,4.0"
- **DOCKER_BUILD_TAG**: Docker image tag, e.g "latest", "0.28.1"
- **DOCKER_CACHE**: Allow to cache docker layers during the build, to speed up local testing
- **DOCKER_CROSS**: Cross-compiling image prefix, currently only "android" is supported

Upload related variables:

- **DOCKER_USERNAME**: Your Docker username to authenticate in Docker server.
- **DOCKER_PASSWORD**: Your Docker password to authenticate in Docker server
- **DOCKER_UPLOAD**: If attributed to true, it will upload the generated docker image, positive words are accepted, e.g "True", "1", "Yes". Default "False"
- **BUILD_CONAN_SERVER_IMAGE**: If attributest to true, it will build and upload an image with the conan_server
- **DOCKER_UPLOAD_ONLY_WHEN_STABLE**: Only upload only when is master branch.
