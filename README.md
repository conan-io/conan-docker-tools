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
- [lasote/conangcc71: gcc 7.2](https://hub.docker.com/r/lasote/conangcc72/)

#### Clang
- [lasote/conanclang39: clang 3.8](https://hub.docker.com/r/lasote/conanclang38/)
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
