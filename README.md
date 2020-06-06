[![Build Status](https://dev.azure.com/conanio/conan-docker-tools/_apis/build/status/conan-io.conan-docker-tools?branchName=master)](https://dev.azure.com/conanio/conan-docker-tools/_build/latest?definitionId=1&branchName=master)
# Conan Docker Tools

![logo](logo.png)

Dockerfiles for different gcc compiler versions.
You can use these images directly in your project or with the [conan-package-tools project](https://github.com/conan-io/conan-package-tools).

> :warning: **Warning:**
The images listed below are intended for **generating open-source library packages** and we cannot guarantee any kind of stability. We strongly recommend using your own generated images for production environments taking the dockerfiles in this repository as a reference.

The images are uploaded to Docker Hub:

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
| [conanio/gcc9-x86: gcc 9](https://hub.docker.com/r/conanio/gcc9-x86/)              | x86     |  Supported           |
| [conanio/gcc9: gcc 9](https://hub.docker.com/r/conanio/gcc9/)                      | x86_64  |  Supported           |
| [conanio/gcc9-armv7: gcc 9](https://hub.docker.com/r/conanio/gcc9-armv7/)          | armv7   |  Supported           |
| [conanio/gcc9-armv7hf: gcc 9](https://hub.docker.com/r/conanio/gcc9-armv7hf/)      | armv7hf |  Supported           |
| [conanio/gcc9-centos7: gcc 9](https://hub.docker.com/r/conanio/gcc9-centos7/)      | x86_64  |  Supported           |
| [conanio/gcc10: gcc 10](https://hub.docker.com/r/conanio/gcc10/)                   | x86_64  |  Supported           |
| [conanio/gcc10-armv7: gcc 10](https://hub.docker.com/r/conanio/gcc10-armv7/)       | armv7   |  Supported           |
| [conanio/gcc10-armv7hf: gcc 10](https://hub.docker.com/r/conanio/gcc10-armv7hf/)   | armv7hf |  Supported           |


#### Clang

| Version                                                                                       | Arch   |  Status, Life cycle  |
|-----------------------------------------------------------------------------------------------|--------|------------|
| - [conanio/clang38: clang 3.8](https://hub.docker.com/r/conanio/clang38/)             | x86_64 |  Supported |
| - [conanio/clang39-x86: clang 3.9](https://hub.docker.com/r/conanio/clang39-x86/)     | x86    |  Supported |
| - [conanio/clang39: clang 3.9](https://hub.docker.com/r/conanio/clang39/)             | x86_64 |  Supported |
| - [conanio/clang40-x86: clang 4.0](https://hub.docker.com/r/conanio/clang40-x86)      | x86    |  Supported |
| - [conanio/clang40: clang 4.0](https://hub.docker.com/r/conanio/clang40/)             | x86_64 |  Supported |
| - [conanio/clang50-x86: clang 5.0](https://hub.docker.com/r/conanio/clang50-x86/)     | x86    |  Supported |
| - [conanio/clang50: clang 5.0](https://hub.docker.com/r/conanio/clang50/)             | x86_64 |  Supported |
| - [conanio/clang60-x86: clang 6.0](https://hub.docker.com/r/conanio/clang60-x86/)     | x86    |  Supported |
| - [conanio/clang60: clang 6.0](https://hub.docker.com/r/conanio/clang60/)             | x86_64 |  Supported |
| - [conanio/clang7-x86: clang 7](https://hub.docker.com/r/conanio/clang7-x86/)         | x86    |  Supported |
| - [conanio/clang7: clang 7](https://hub.docker.com/r/conanio/clang7/)                 | x86_64 |  Supported |
| - [conanio/clang8-x86: clang 8](https://hub.docker.com/r/conanio/clang8-x86/)         | x86    |  Supported |
| - [conanio/clang8: clang 8](https://hub.docker.com/r/conanio/clang8/)                 | x86_64 |  Supported |
| - [conanio/clang9-x86: clang 9](https://hub.docker.com/r/conanio/clang9-x86/)         | x86    |  Supported |
| - [conanio/clang9: clang 9](https://hub.docker.com/r/conanio/clang9/)                 | x86_64 |  Supported |
| - [conanio/clang10: clang 10](https://hub.docker.com/r/conanio/clang10/)              | x86_64 |  Supported |


#### Visual Studio

We can not re-distribute Windows docker images, since Visual Studio Build Tools is licensed as supplemental license for Visual Studio.
To have more information about: https://github.com/Microsoft/vs-dockerfiles#samples
However, you can download the Docker recipe and build.


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

**conanio/gcc9-centos7** is a special image version based on CentOS 7, GCC 9 and **glibc 2.17** (very old glibc version). This is intended to build executables that run almost on any Linux because **glibc** guarantees backward compatibility. You can use this image to build your Conan build tools packages (`build_requires`). This image is **ONLY** able to build **x86_64** binaries.

Use the images to test your C++ project in Travis CI
======================================================

These Docker images can be used to build your project using the Travis CI CI service, even if you are not using Conan.
It's always recommended to build and test your C/C++ projects in a Docker image running in travis:

- Travis CI images are old, so installing a newer version of gcc and the needed tools can be hard. Check [this thread](https://github.com/travis-ci/travis-ci/issues/6300).
- The generated binaries will use the old **libc/libstdc++*| [conanio/gcc5-jnlp-slave: gcc 4.6](https://hub.docker.com/r/conanio/gcc46-jnlp-slave/)        | x86_64  |  Supported |* installed in the system, so ABI incompatibilities
      can occur if you use these packages in more modern di| [conanio/gcc5-jnlp-slave: gcc 4.6](https://hub.docker.com/r/conanio/gcc46-jnlp-slave/)        | x86_64  |  Supported |stributions.
| [conanio/gcc5-jnlp-slave: gcc 4.6](https://hub.docker.com/r/conanio/gcc46-jnlp-slave/)        | x86_64  |  Supported |
To setup your project, copy the contents of the folder **ex| [conanio/gcc5-jnlp-slave: gcc 4.6](https://hub.docker.com/r/conanio/gcc46-jnlp-slave/)        | x86_64  |  Supported |ample_project_test** to your project.
You need to modify:| [conanio/gcc5-jnlp-slave: gcc 4.6](https://hub.docker.com/r/conanio/gcc46-jnlp-slave/)        | x86_64  |  Supported |
| [conanio/gcc5-jnlp-slave: gcc 4.6](https://hub.docker.com/r/conanio/gcc46-jnlp-slave/)        | x86_64  |  Supported |
- ``.travis.yml`` file to enable or disable more ``GCC`` or| [conanio/gcc5-jnlp-slave: gcc 4.6](https://hub.docker.com/r/conanio/gcc46-jnlp-slave/)        | x86_64  |  Supported | ``CLang`` versions add more entries to the matrix using DOCKER_IMAGE
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
        - DOCKER_IMAGE=conanio/gcc8 # GCC 8.x
        - DOCKER_IMAGE=conanio/clang7 # Clang 7

    matrix:
       include:
           - os: osx
             osx_image: xcode11.3 # Apple-Clang 11.0
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
| [conanio/gcc46-jnlp-slave: gcc 4.6](https://hub.docker.com/r/conanio/gcc46-jnlp-slave/)        | x86_64  |  Supported |
| [conanio/gcc46-jnlp-slave-x86: gcc 4.6](https://hub.docker.com/r/conanio/gcc46-jnlp-slave-x86/)  | x86  |  Supported |
| [conanio/gcc48-jnlp-slave: gcc 4.8](https://hub.docker.com/r/conanio/gcc48-jnlp-slave/)        | x86_64  |  Supported |
| [conanio/gcc48-jnlp-slave-x86: gcc 4.8](https://hub.docker.com/r/conanio/gcc48-jnlp-slave-x86/)  | x86  |  Supported |
| [conanio/gcc49-jnlp-slave: gcc 4.9](https://hub.docker.com/r/conanio/gcc49-jnlp-slave/)        | x86_64  |  Supported |
| [conanio/gcc49-jnlp-slave-x86: gcc 4.9](https://hub.docker.com/r/conanio/gcc49-jnlp-slave-x86/)  | x86  |  Supported |
| [conanio/gcc5-jnlp-slave: gcc 5](https://hub.docker.com/r/conanio/gcc5-jnlp-slave/)        | x86_64  |  Supported |
| [conanio/gcc5-jnlp-slave-x86: gcc 5](https://hub.docker.com/r/conanio/gcc5-jnlp-slave-x86/)  | x86  |  Supported |
| [conanio/gcc6-jnlp-slave: gcc 6](https://hub.docker.com/r/conanio/gcc6-jnlp-slave/)        | x86_64  |  Supported |
| [conanio/gcc6-jnlp-slave-x86: gcc 6](https://hub.docker.com/r/conanio/gcc6-jnlp-slave-x86/)  | x86  |  Supported |
| [conanio/gcc7-jnlp-slave: gcc 7](https://hub.docker.com/r/conanio/gcc7-jnlp-slave/)        | x86_64  |  Supported |
| [conanio/gcc7-jnlp-slave-x86: gcc 7](https://hub.docker.com/r/conanio/gcc7-jnlp-slave-x86/)  | x86  |  Supported |
| [conanio/gcc8-jnlp-slave: gcc 8](https://hub.docker.com/r/conanio/gcc8-jnlp-slave/)        | x86_64  |  Supported |
| [conanio/gcc8-jnlp-slave-x86: gcc 8](https://hub.docker.com/r/conanio/gcc8-jnlp-slave-x86/)  | x86  |  Supported |
| [conanio/gcc9-jnlp-slave: gcc 9](https://hub.docker.com/r/conanio/gcc9-jnlp-slave/)        | x86_64  |  Supported |
| [conanio/gcc9-jnlp-slave-x86: gcc 9](https://hub.docker.com/r/conanio/gcc9-jnlp-slave-x86/)  | x86  |  Supported |
| [conanio/gcc10-jnlp-slave: gcc 10](https://hub.docker.com/r/conanio/gcc10-jnlp-slave/)        | x86_64  |  Supported |
| [conanio/gcc7-jnlp-slave-centos6: gcc 7](https://hub.docker.com/r/conanio/gcc7-jnlp-slave-centos6/)        | x86_64  |  Supported |
| [conanio/gcc7-jnlp-slave-centos6-x86: gcc 7](https://hub.docker.com/r/conanio/gcc7-jnlp-slave-centos6-x86/)  | x86  |  Supported |
| [conanio/gcc9-jnlp-slave-centos7: gcc 9](https://hub.docker.com/r/conanio/gcc9-jnlp-slave-centos7/)        | x86_64  |  Supported |


#### Clang

| Version                                                                                       | Arch   |  Status, Life cycle  |
|-----------------------------------------------------------------------------------------------|--------|------------|
| - [conanio/clang38-jnlp-slave: clang 3.8](https://hub.docker.com/r/conanio/clang38-jnlp-slave/)             | x86_64 |  Supported |
| - [conanio/clang39-jnlp-slave-x86: clang 3.9](https://hub.docker.com/r/conanio/clang39-jnlp-slave-x86/)     | x86    |  Supported |
| - [conanio/clang39-jnlp-slave: clang 3.9](https://hub.docker.com/r/conanio/clang39-jnlp-slave/)             | x86_64 |  Supported |
| - [conanio/clang40-jnlp-slave-x86: clang 4.0](https://hub.docker.com/r/conanio/clang40-jnlp-slave-x86)      | x86    |  Supported |
| - [conanio/clang40-jnlp-slave: clang 4.0](https://hub.docker.com/r/conanio/clang40-jnlp-slave/)             | x86_64 |  Supported |
| - [conanio/clang50-jnlp-slave-x86: clang 5.0](https://hub.docker.com/r/conanio/clang50-jnlp-slave-x86/)     | x86    |  Supported |
| - [conanio/clang50-jnlp-slave: clang 5.0](https://hub.docker.com/r/conanio/clang50-jnlp-slave/)             | x86_64 |  Supported |
| - [conanio/clang60-jnlp-slave-x86: clang 6.0](https://hub.docker.com/r/conanio/clang60-jnlp-slave-x86/)     | x86    |  Supported |
| - [conanio/clang60-jnlp-slave: clang 6.0](https://hub.docker.com/r/conanio/clang60-jnlp-slave/)             | x86_64 |  Supported |
| - [conanio/clang7-jnlp-slave-x86: clang 7](https://hub.docker.com/r/conanio/clang7-jnlp-slave-x86/)         | x86    |  Supported |
| - [conanio/clang7-jnlp-slave: clang 7](https://hub.docker.com/r/conanio/clang7-jnlp-slave/)                 | x86_64 |  Supported |
| - [conanio/clang8-jnlp-slave-x86: clang 8](https://hub.docker.com/r/conanio/clang8-jnlp-slave-x86/)         | x86    |  Supported |
| - [conanio/clang8-jnlp-slave: clang 8](https://hub.docker.com/r/conanio/clang8-jnlp-slave/)                 | x86_64 |  Supported |
| - [conanio/clang8-jnlp-slave-x86: clang 9](https://hub.docker.com/r/conanio/clang9-jnlp-slave-x86/)         | x86    |  Supported |
| - [conanio/clang8-jnlp-slave: clang 9](https://hub.docker.com/r/conanio/clang9-jnlp-slave/)                 | x86_64 |  Supported |
| - [conanio/clang8-jnlp-slave: clang 10](https://hub.docker.com/r/conanio/clang10-jnlp-slave/)               | x86_64 |  Supported |



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
The images are already built and uploaded to **"conanio(https://hub.docker.com/r/conanio/)"** dockerhub account, If you want to build your own images you can do it by:

```
$ python build.py
```

The script *build.py* will build, test and deploy your Docker image. You can configure all stages by environment variables listed below.

Also, you can build only a version:

E.g Build and test only a image with Conan and gcc-6
```
$ CONAN_GCC_VERSIONS="6" python build.py
```

E.g Build and test only the images with Conan and clang-8, clang-9
```
$ CONAN_CLANG_VERSIONS="8,9" python build.py
```

E.g Build and test only the images with Conan and Visual Studio 14.0 (It **ONLY** works on Windows).
```
$ CONAN_VISUAL_VERSIONS="14.0" python build.py
```

The stages that compose the script will be described below:

### Build
The first stage collect all compiler versions listed in ``CONAN_GCC_VERSIONS`` for ``Gcc``, in ``CONAN_CLANG_VERSIONS`` for ``Clang`` and ``CONAN_VISUAL_VERSIONS`` for ``Visual Studio``. If you do not set any compiler version, the script will execute all supported versions for ``Gcc`` and ``Clang``.

You can configure only a compiler version or a list, by these variables. If you skipped a compiler list, the build will not be executed for that compiler.

The image tag can be configured by ``DOCKER_BUILD_TAG``. Build default will used **latest**.

Each image created on this stage will be tagged as  ``DOCKER_USERNAME/conan_compiler_version``.

The image will not be removed after build.

### Test
The second stage runs the new image created and builds the Conan package ``gtest/1.8.1``.
The same build variables, as ``CONAN_GCC_VERSIONS``, ``CONAN_CLANG_VERSIONS`` and ``CONAN_VISUAL_VERSIONS`` are used to select the compiler and version.

All tests build the package ``gtest/1.8.1``, for x86 and x86_64.

``Gcc`` images use libstdc++.
``Clang`` images use libc++ and libstdc++.
``Visual Studio`` images use MD for runtime.

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
- **VISUAL_VERSIONS**: Visual Studio versions to build, test and deploy, comma separated, e.g. "14,15"
- **DOCKER_BUILD_TAG**: Docker image tag, e.g "latest", "0.28.1"
- **SUDO_COMMAND**: Sudo command used on Linux distros, e.g. "sudo"
- **DOCKER_CACHE**: Allow to cache docker layers during the build, to speed up local testing
- **DOCKER_CROSS**: Cross-compiling image prefix, currently only "android" is supported

Upload related variables:

- **DOCKER_USERNAME**: Your Docker username to authenticate in Docker server.
- **DOCKER_PASSWORD**: Your Docker password to authenticate in Docker server
- **DOCKER_UPLOAD**: If attributed to true, it will upload the generated docker image, positive words are accepted, e.g "True", "1", "Yes". Default "False"
- **BUILD_CONAN_SERVER_IMAGE**: If attributest to true, it will build and upload an image with the conan_server
- **DOCKER_UPLOAD_ONLY_WHEN_STABLE**: Only upload only when is master branch.
