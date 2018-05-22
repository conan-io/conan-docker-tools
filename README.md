[![Build Status](https://travis-ci.org/conan-io/conan-docker-tools.svg?branch=master)](https://travis-ci.org/conan-io/conan-docker-tools)
# conan-docker-tools

Dockerfiles for different gcc compiler versions.
You can use these images directly in your project or with the [conan-package-tools project](https://github.com/conan-io/conan-package-tools).

The images are uploaded to Dockerhub:

#### GCC
| Version                                                                                       | Arch    |  Status, Life cycle  |
|-----------------------------------------------------------------------------------------------|---------|------------|
| [lasote/conangcc46: gcc 4.6](https://hub.docker.com/r/lasote/conangcc46/)                     | x86_64  |  Supported |
| [lasote/conangcc46: gcc 4.6](https://hub.docker.com/r/lasote/conangcc46/)                     | x86_64  |  Supported |
| [lasote/conangcc48: gcc 4.8](https://hub.docker.com/r/lasote/conangcc48/)                     | x86_64  |  Supported |
| [lasote/conangcc49: gcc 4.9](https://hub.docker.com/r/lasote/conangcc49/)                     | x86_64  |  Supported |
| [lasote/conangcc49-x86: gcc 4.9](https://hub.docker.com/r/lasote/conangcc49-x86/)             | x86     |  Supported |
| [lasote/conangcc49-armv7: gcc 4.9](https://hub.docker.com/r/lasote/conangcc49-armv7/)         | armv7   |  Supported |
| [lasote/conangcc49-armv7hf: gcc 4.9](https://hub.docker.com/r/lasote/conangcc49-armv7hf/)     | armv7hf |  Supported |
| [lasote/conangcc52: gcc 5.2](https://hub.docker.com/r/lasote/conangcc52/)                     | x86_64  |  Supported |
| [lasote/conangcc53: gcc 5.3](https://hub.docker.com/r/lasote/conangcc53/)                     | x86_64  | Supported  |
| [lasote/conangcc54: gcc 5.4](https://hub.docker.com/r/lasote/conangcc54/)                     | x86_64  | Supported  |
| [lasote/conangcc62: gcc 6.2](https://hub.docker.com/r/lasote/conangcc62/)                     | x86_64  | DEPRECATED, only frozen binary image support, No Dockerfile |
| [lasote/conangcc63: gcc 6.3](https://hub.docker.com/r/lasote/conangcc63/)                     | x86_64  | Supported  |
| [lasote/conangcc64: gcc 6.4](https://hub.docker.com/r/lasote/conangcc64/)                     | x86_64  | Supported  |
| [lasote/conangcc71: gcc 7.1](https://hub.docker.com/r/lasote/conangcc71/)                     | x86_64  | DEPRECATED, only frozen binary image support, No Dockerfile |
| [lasote/conangcc72: gcc 7.2](https://hub.docker.com/r/lasote/conangcc72/)                     | x86_64  | Supported  |


GCC>=5 is ABI compatible for minor versions. To solve multiple minors, there are generic images by major version. If you are interested to understand the motivation, read this [issue](https://github.com/conan-io/conan/issues/1214).

| Version                                                                                    | Arch    |  Status, Life cycle  |
|--------------------------------------------------------------------------------------------|---------|----------------------|
| [lasote/conangcc5: gcc 5](https://hub.docker.com/r/lasote/conangcc5/)                      | x86_64  |  Supported           |
| [lasote/conangcc5-x86: gcc 5](https://hub.docker.com/r/lasote/conangcc5-x86/)              | x86     |  Supported           |
| [lasote/conangcc5-armv7: gcc 5](https://hub.docker.com/r/lasote/conangcc5-armv7/)          | armv7   |  Supported           |
| [lasote/conangcc5-armv7hf: gcc 5](https://hub.docker.com/r/lasote/conangcc5-armv7hf/)      | armv7hf |  Supported           |
| [lasote/conangcc6: gcc 6](https://hub.docker.com/r/lasote/conangcc6/)                      | x86_64  |  Supported           |
| [lasote/conangcc6-x86: gcc 6](https://hub.docker.com/r/lasote/conangcc6-x86/)              | x86     |  Supported           |
| [lasote/conangcc6-armv7: gcc 6](https://hub.docker.com/r/lasote/conangcc6-armv7/)          | armv7   |  Supported           |
| [lasote/conangcc6-armv7hf: gcc 6](https://hub.docker.com/r/lasote/conangcc6-armv7hf/)      | armv7hf |  Supported           |
| [lasote/conangcc7-x86: gcc 7](https://hub.docker.com/r/lasote/conangcc7-x86/)              | x86     |  Supported           |
| [lasote/conangcc7: gcc 7](https://hub.docker.com/r/lasote/conangcc7/)                      | x86_64  |  Supported           |
| [lasote/conangcc7-armv7: gcc 7](https://hub.docker.com/r/lasote/conangcc7-armv7/)          | armv7   |  Supported           |
| [lasote/conangcc7-armv7hf: gcc 7](https://hub.docker.com/r/lasote/conangcc7-armv7hf/)      | armv7hf |  Supported           |
| [lasote/conangcc8-x86: gcc 8](https://hub.docker.com/r/lasote/conangcc8-x86/)              | x86     |  Supported           |
| [lasote/conangcc8: gcc 8](https://hub.docker.com/r/lasote/conangcc8/)                      | x86_64  |  Supported           |
| [lasote/conangcc8-armv7: gcc 8](https://hub.docker.com/r/lasote/conangcc8-armv7/)          | armv7   |  Supported           |


#### Clang

| Version                                                                                       | Arch   |  Status, Life cycle  |
|-----------------------------------------------------------------------------------------------|--------|------------|
| - [lasote/conanclang38: clang 3.8](https://hub.docker.com/r/lasote/conanclang38/)             | x86_64 |  Supported |
| - [lasote/conanclang39-x86: clang 3.9](https://hub.docker.com/r/lasote/conanclang39-x86/)     | x86    |  Supported |
| - [lasote/conanclang39: clang 3.9](https://hub.docker.com/r/lasote/conanclang39/)             | x86_64 |  Supported |
| - [lasote/conanclang40-x86: clang 4.0](https://hub.docker.com/r/lasote/conanclang40/-x86)     | x86    |  Supported |
| - [lasote/conanclang40: clang 4.0](https://hub.docker.com/r/lasote/conanclang40/)             | x86_64 |  Supported |
| - [lasote/conanclang50-x86: clang 5.0](https://hub.docker.com/r/lasote/conanclang50-x86/)     | x86    |  Supported |
| - [lasote/conanclang50: clang 5.0](https://hub.docker.com/r/lasote/conanclang50/)             | x86_64 |  Supported |
| - [lasote/conanclang60-x86: clang 6.0](https://hub.docker.com/r/lasote/conanclang60-x86/)     | x86    |  Supported |
| - [lasote/conanclang60: clang 6.0](https://hub.docker.com/r/lasote/conanclang60/)             | x86_64 |  Supported |


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
        - DOCKER_IMAGE=lasote/conangcc63 # 6.3
        - DOCKER_IMAGE=lasote/conanclang39 # 3.9

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


Use the images locally
======================

You can also use the images locally to build or test packages, this is an example command:

```
docker run -v/tmp/.conan:/home/conan/.conan lasote/conangcc63 bash -c "conan install zlib/1.2.11@conan/stable --build missing"
```

This command is sharing ``/tmp/.conan`` as a shared folder with the conan home, so the Boost package will be built there.
You can change the directory or execute any other command that works for your needs.

If you are familiarized with Docker compose, also it's possible to start a new container by:

```
docker-compose run -v/tmp/.conan:/home/conan/.conan conangcc63 bash -c "conan install zlib/1.2.11@conan/stable --build missing"
```


Build, Test and Deploy
======================

## Introduce
The images are already built and uploaded to **"lasote"** dockerhub account, If you want to build your own images you can do it by:

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

The login uses ``DOCKER_USERNAME`` and ``DOCKER_PASSWORD`` to authenticate.


E.g Upload Docker images to Docker hub, after build and test:
```
$ DOCKER_USERNAME="lasote" DOCKER_PASSWORD="conan" DOCKER_UPLOAD="TRUE" python build.py
```


## Environment configuration

You can also use environment variables to change the behavior of Conan Docker Tools.

This is especially useful for CI integration.

Build and Test variables:

- **GCC_VERSIONS**: GCC versions to build, test and deploy, comma separated, e.g. "4.6,4.8,4.9,5.2,5.3,5.4,6.2.6.3"
- **CLANG_VERSIONS**: Clang versions to build, test and deploy, comma separated, e.g. "3.8,3.9,4.0"
- **DOCKER_BUILD_TAG**: Docker image tag, e.g "latest", "0.28.1"

Upload related variables:

- **DOCKER_USERNAME**: Your Docker username to authenticate in Docker server.
- **DOCKER_PASSWORD**: Your Docker password to authenticate in Docker server
- **DOCKER_UPLOAD**: If attributed to true, it will upload the generated docker image, positive words are accepted, e.g "True", "1", "Yes". Default "False"
- **BUILD_CONAN_SERVER_IMAGE**: If attributest to true, it will build and upload an image with the conan_server
