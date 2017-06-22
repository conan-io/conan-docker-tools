[![Build Status](https://travis-ci.org/conan-io/conan-docker-tools.svg?branch=master)](https://travis-ci.org/conan-io/conan-docker-tools)
# conan-docker-tools

Dockerfiles for different gcc compiler versions.
You can use these images directly in your project or with the [conan-package-tools project](https://github.com/conan-io/conan-package-tools).

The images are uploaded to Dockerhub:

#### GCC
- [lasote/conangcc46: gcc 4.6](https://hub.docker.com/r/lasote/conangcc46/)
- [lasote/conangcc48: gcc 4.8](https://hub.docker.com/r/lasote/conangcc48/)
- [lasote/conangcc49: gcc 4.9](https://hub.docker.com/r/lasote/conangcc49/)
- [lasote/conangcc52: gcc 5.2](https://hub.docker.com/r/lasote/conangcc52/)
- [lasote/conangcc53: gcc 5.3](https://hub.docker.com/r/lasote/conangcc53/)
- [lasote/conangcc54: gcc 5.4](https://hub.docker.com/r/lasote/conangcc54/)
- [lasote/conangcc62: gcc 6.2](https://hub.docker.com/r/lasote/conangcc62/)
- [lasote/conangcc63: gcc 6.3](https://hub.docker.com/r/lasote/conangcc63/)

#### Clang
- [lasote/conanclang38: clang 3.8](https://hub.docker.com/r/lasote/conanclang38/)
- [lasote/conanclang39: clang 3.9](https://hub.docker.com/r/lasote/conanclang39/)
- [lasote/conanclang40: clang 4.0](https://hub.docker.com/r/lasote/conanclang40/)

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
docker run -v/tmp/.conan:/home/conan/.conan lasote/conangcc63 bash -c "conan install Boost/1.62.0@lasote/stable --build missing"
```

This command is sharing ``/tmp/.conan`` as a shared folder with the conan home, so the Boost package will be built there.
You can change the directory or execute any other command that works for your needs.


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
The final stage pushes the image to docker server (hub.docker). First, ``DOCKER_UPLOAD`` should be true and ``CONAN_STABLE_BRANCH_PATTERN`` should match with your current branch.

The login uses ``DOCKER_USERNAME`` and ``DOCKER_PASSWORD`` to authenticate.

By default, this stage is **NOT** executed and Docker username is **"lasote"**.

E.g Upload Docker images to Docker hub, after build and test:
```
$ DOCKER_USERNAME="lasote" DOCKER_PASSWORD="conan" DOCKER_UPLOAD="TRUE" python build.py
```


## Environment configuration

You can also use environment variables to change the behavior of Conan Docker Tools.

This is especially useful for CI integration.

Build and Test variables:

- **CONAN_GCC_VERSIONS**: GCC versions to build, test and deploy, comma separated, e.g. "4.6,4.8,4.9,5.2,5.3,5.4,6.2.6.3"
- **CONAN_CLANG_VERSIONS**: Clang versions to build, test and deploy, comma separated, e.g. "3.8,3.9,4.0"

Upload related variables:

- **DOCKER_USERNAME**: Your Docker username to authenticate in Docker server. Default "lasote".
- **DOCKER_PASSWORD**: Your Docker password to authenticate in Docker server
- **DOCKER_UPLOAD**:         If attributed to true, it will upload the generated docker image, positive words are accepted, e.g "True", "1", "Yes". Default "False"
- **CONAN_STABLE_BRANCH_PATTERN**: Regular expression, if current git branch matches this pattern, the packages will be uploaded to dockerhub. Default "master". e.g. "feature/*"
