[![Build Status](https://dev.azure.com/conanio/conan-docker-tools/_apis/build/status/conan-io.conan-docker-tools?branchName=master)](https://dev.azure.com/conanio/conan-docker-tools/_build/latest?definitionId=1&branchName=master)
# Conan Docker Tools

![logo](logo.png)

Dockerfiles for Conan Center Continuous Integration.

You can use these images directly in your project or with the [conan-package-tools project](https://github.com/conan-io/conan-package-tools).

> :warning: **Warning:**
The images listed below are intended for **generating open-source library packages** and we CAN NOT guarantee any kind of stability. We strongly recommend using your own generated images for production environments taking the dockerfiles in this repository as a reference.

### New Docker Strategy (June 2021)

**TL;DR** New Docker images will use Ubuntu 16.04 as base and build all compilers from sources. Thus, all binaries generated will link with the same glibc and stdlibc++ versions.


After many updates, new compiler releases, instability and incompatibility problems, we decided to clean the house, move a step forward with Conan Docker Tools. So far, we usually follow the same recipe, when a compiler version is released, we also release a new docker image, but we have two main problems:

- Ubuntu doesn’t package new compiler versions for each distro release, so we need to use a new Ubuntu version as base image. As a consequence, non LTS versions become a problem when EOL comes.
- Each Ubuntu release uses different package versions, including very important projects, like glibc, which results in incompatibility from a package created by distro version to another version.

Given this priority (same base images, glibc and stdlibc++ versions for all) we will support only the compilers that we managed to build and run in the base image, the rest will be deprecated from ConanCenter because on this technical reasons.

Second, we decided to use a single base image, not too old and not the latest, something in the middle, to keep a glibc still compatible for some old distro releases. Thus, we choose Ubuntu 16.04 LTS (Xenial) which its EOL is in 2024. When close to the EOL date, we can move to 18.04 and so on.

As the compiler version is always a problem to align according to the distro release, we decided to build all compilers from sources, which includes GCC and Clang. Although this increased the build time considerably, we still now have full control over the compiler used in our images.

We totally understand that companies and users are still using our “legacy” docker images, so we won’t deprecate them soon. This kind of change requires rebuilding all packages again, and depending on the number, it could take weeks. Thus, don’t worry, we won’t remove them from Docker hub.

### Legacy Docker Images

Legacy docker images will be moved to "legacy" folder and eventually their dockerfiles will no longer be maintained in this repository (EOL to be decided).

### Official Docker Images

These are the images uploaded to Docker Hub and currently used by [Conan Center](https://conan.io/center):

#### GCC

| Version                                                                            | Arch    |  Status, Life cycle  |
|------------------------------------------------------------------------------------|---------|----------------------|
| [conanio/gcc5-ubuntu16.04: gcc 5](https://hub.docker.com/r/conanio/gcc5-ubuntu16.04/)          | x86_64  |  Supported           |
| [conanio/gcc6-ubuntu16.04: gcc 6](https://hub.docker.com/r/conanio/gcc6-ubuntu16.04/)          | x86_64  |  Supported           |
| [conanio/gcc7-ubuntu16.04: gcc 7](https://hub.docker.com/r/conanio/gcc7-ubuntu16.04/)          | x86_64  |  Supported           |
| [conanio/gcc8-ubuntu16.04: gcc 8](https://hub.docker.com/r/conanio/gcc8-ubuntu16.04/)          | x86_64  |  Supported           |
| [conanio/gcc9-ubuntu16.04: gcc 9](https://hub.docker.com/r/conanio/gcc9-ubuntu16.04/)          | x86_64  |  Supported           |
| [conanio/gcc10-ubuntu16.04: gcc 10](https://hub.docker.com/r/conanio/gcc10-ubuntu16.04/)       | x86_64  |  Supported           |
| [conanio/gcc11-ubuntu16.04: gcc 11](https://hub.docker.com/r/conanio/gcc11-ubuntu16.04/)       | x86_64  |  Supported           |


#### Clang

| Version                                                                                  | Arch   |  Status, Life cycle  |
|------------------------------------------------------------------------------------------|--------|----------------------|
| - [conanio/clang10-ubuntu16.04: clang 10](https://hub.docker.com/r/conanio/clang10-ubuntu16.04/)     | x86_64 |  Supported           |
| - [conanio/clang11-ubuntu16.04: clang 11](https://hub.docker.com/r/conanio/clang11-ubuntu16.04/)     | x86_64 |  Supported           |
| - [conanio/clang12-ubuntu16.04: clang 12](https://hub.docker.com/r/conanio/clang12-ubuntu16.04/)     | x86_64 |  Supported           |


#### Conan Server

Conan Docker Tools provides an image version with only Conan Server installed, very useful for the cases it is necessary to run a server without touching the host. It's based on Alpine.

| Version                                                                              | Arch   |  Status, Life cycle  |
|--------------------------------------------------------------------------------------|--------|----------------------|
| - [conanio/conan_server](https://hub.docker.com/r/conanio/conan_server/)             | ANY    |  Supported           |


#### Jenkins Client

If you use Jenkins to build your packages and also you use Jenkins clients to run each docker container, you could use our Docker images prepared for Jenkins. Those images run the script [jenkins-client.sh](jenkins/jenkins-client), which starts the client during the container entrypoint.
These images are mainly focused for Conan Center CI.

#### GCC

| Version                                                                                                   | Arch    |  Status, Life cycle  |
|-----------------------------------------------------------------------------------------------------------|---------|----------------------|
| [conanio/gcc5-ubuntu16.04-jenkins: gcc 5](https://hub.docker.com/r/conanio/gcc5-ubuntu16.04-jenkins/)     | x86_64  |  Supported           |
| [conanio/gcc6-ubuntu16.04-jenkins: gcc 6](https://hub.docker.com/r/conanio/gcc6-ubuntu16.04-jenkins/)     | x86_64  |  Supported           |
| [conanio/gcc7-ubuntu16.04-jenkins: gcc 7](https://hub.docker.com/r/conanio/gcc7-ubuntu16.04-jenkins/)     | x86_64  |  Supported           |
| [conanio/gcc8-ubuntu16.04-jenkins: gcc 8](https://hub.docker.com/r/conanio/gcc8-ubuntu16.04-jenkins/)     | x86_64  |  Supported           |
| [conanio/gcc9-ubuntu16.04-jenkins: gcc 9](https://hub.docker.com/r/conanio/gcc9-ubuntu16.04-jenkins/)     | x86_64  |  Supported           |
| [conanio/gcc10-ubuntu16.04-jenkins: gcc 10](https://hub.docker.com/r/conanio/gcc10-ubuntu16.04-jenkins/)  | x86_64  |  Supported           |
| [conanio/gcc11-ubuntu16.04-jenkins: gcc 11](https://hub.docker.com/r/conanio/gcc11-ubuntu16.04-jenkins/)  | x86_64  |  Supported           |


#### Clang

| Version                                                                                                                  | Arch   |  Status, Life cycle  |
|--------------------------------------------------------------------------------------------------------------------------|--------|------------|
| - [conanio/clang8-ubuntu16.04-jenkins: clang 10](https://hub.docker.com/r/conanio/clang10-ubuntu16.04-jenkins/)          | x86_64 |  Supported |
| - [conanio/clang8-ubuntu16.04-jenkins: clang 11](https://hub.docker.com/r/conanio/clang11-ubuntu16.04-jenkins/)          | x86_64 |  Supported |
| - [conanio/clang8-ubuntu16.04-jenkins: clang 12](https://hub.docker.com/r/conanio/clang12-ubuntu16.04-jenkins/)          | x86_64 |  Supported |



Use the images locally
======================

You can also use the images locally to build or test packages, this is an example command:

```
docker run --rm -v /tmp/.conan:/home/conan/.conan conanio/gcc11-ubuntu16.04 bash -c "conan install boost/1.76.0@ --build"
```

This command is sharing ``/tmp/.conan`` as a shared folder with the conan home, so the Boost package will be built there.
You can change the directory or execute any other command that works for your needs.

If you are familiarized with Docker compose, also it's possible to start a new container by:

```
docker-compose run -v /tmp/.conan:/home/conan/.conan gcc11 bash -c "conan install boost/1.74.0@ --build"
```


Build, Test and Deploy
======================

## Introduce

The images are already built and uploaded to [conanio](https://hub.docker.com/r/conanio/) dockerhub account, but if you want to build your own images, read this section.

The `docker-compose.yml` file list all possible combinations of images and it will be explained below:

### Build

Each image created on this stage will be tagged as  ``conanio/<compiler><compiler.version>-<distro><distro.version>``.

For instance, building Clang 12 complete image:

    $ docker-compose build clang12

The produced image will be named as ``conanio/clang12-ubuntu16.04``. The tag will follow the `CONAN_VERSION` in `.env` file.

#### Pre-Build stage (Base)

Besides the final compiler image, there are other important images which can be built separately and are part of the final image.

The Docker image `base` (same service name), installs all basic system APT packages, CMake, Python and Conan. So, if you are looking for an
image without compiler, `base` is your candidate.

    $ docker-compose build base

The produced image can be configured by `.env`. Most important package versions installed in Base are listed there.

#### Build stage (Builder)

All compilers are built in specific image called `builder`, which does not use `base`. The image is only used to build the compiler.
The decision made serves to avoid possible rebuilds when updating Base for some reason.

The Builder image can be built directly, it's useful if you want to investigate compiler building steps and all artifacts produced.

    $ docker-compose build gcc10-builder

It will the Builder image for GCC 10, which takes around 15 minutes. For Clang case, it can take 1 hour.


#### Final stage (Deploy)

As final build step, `deploy` will combine `base` image with the compiler produced by `builder`. This approach allow us keeping a smaller
image, easier to be maintained and isolated from the environment used to build the compiler.

This image avoids all Builder cache, using Docker multi-stage feature, we copy only the compiler installation folder.

It's the default build command, for instance:

    $ docker-compose build gcc10

#### Update Conan version

After having all images built and uploaded, probably you don't need to build all again. Eventually, Conan will release a new version and to
avoid a massive build again, the argument `CONAN_VERSION` is separated in Base, which means, if you have your Docker cache, it will update
Conan client version and tag your new image only.

    $ cd modern/
    $ sed -i 's/1.37.0/1.37.2/g' .env # Replace 1.37.0 Conan version in .env by 1.37.2
    $ docker-compose build gcc10

The Conan version used for the update is the same listed in `.env` file.

### Test

Testing is an important step to validate each produced image. To summarize each one:

#### Simple

Build a simple app using CMake, threads and show the date.

To execute the entire test:

    $ cd modern && python test/simple/run.py clang12

It will run Docker container for Clang 12, mount a volume and run test/simple/test_simple.sh internally.

#### Standard

Build projects which require C++17 and C++20. It validates if a compiler supports a specific C++ standard.

To execute the entire test:

    $ cd modern && python test/standard/run.py gcc10

It will run Docker container for GCC 10, mount a volume, run both test/simple/build_imagl.sh and test/simple/build_libsolace.sh

#### System

Some Conan packages can use `SystemPackageTool` to install system packages, which should not affect the compiler built and installed
into the Docker image. To validate that case, this test installs GCC9 and libusb to try sabotage the image, but it must prefer the
compiler already installed, including its libstdc++ version.

To execute the entire test:

    $ cd modern && python test/system/run.py gcc7

It will run Docker container for GCC 7, mount a volume and run CMake to build test/system/CMakeLists.txt

#### GCC

It's a dedicated validation for GCC compiler. It builds a Conan project, using `libstdc++` and `libstdc++11`.
Also, it builds a Fortran simple application, to validate if fortran is correctly built.

To execute the entire GCC test:

    $ cd modern && python test/gcc/conan/run.py gcc10

It will build a Conan project, validate if both libstdc++ and libgcc_s are correctly used from /usr/local.
Also, there is a second phase where the produced application is copied to a vanilla Ubuntu Xenial container,
including the libstdc++ from the target container, and the application must work nicely.

To execute the Fortran test:

    $ cd modern && python test/gcc/fortran/run.py gcc10

It will run Docker container for GCC 10, mount a volume and run CMake to build test/gcc/fortran/CMakeLists.txt

#### Clang

It's a dedicated validation for Clang compiler. It builds a Conan project using `libstdc++`, `libstdc++11` and `libc++`.

To execute the entire Clang test:

    $ cd modern && python test/clang/conan/run.py clang12

It will build a Conan project, validate if the c++ library and runtime are correct. The Clang built for those images
don't use GCC as dependency, instead, they use libunwind, compiler-rt, libc++ and libc++-abi.

Also, there is a second phase where the produced application is copied to a vanilla Ubuntu Xenial container,
including the libstdc++ and libc++ from the target container, and the application must work nicely.

### Deploy

If you want to distribute your image, you have to upload it to somewhere. There two ways to upload an image:

    $ docker login -p <password> -u <username>
    $ docker push conanio/gcc10-ubuntu16.04

Or, using Docker compose

    $ docker login -p <password> -u <username>
    $ docker-compose push gcc10

If you don't want to use hub.docker as default Docker registry, you may use [Artifactory](https://jfrog.com/start-free/#saas), which
is free and well supported for Docker, Conan and more.

### The run.py Script

Now that you learned how to build, test and deploy manually, there is the script `run.py`, which automates all these steps for you.
That script is configured by environment variables due CI, so we can build different images without changing any file or doing a new commit.

#### Build Step

The first stage collect all compiler versions listed in ``CONAN_GCC_VERSIONS`` for ``Gcc`` and in ``CONAN_CLANG_VERSIONS`` for ``Clang``. If you do not set any compiler version, the script will execute all supported versions for ``Gcc`` and ``Clang``.

For instance, to build GCC 10 image, you should execute:

    $ GCC_VERSIONS=10 python run.py

You can configure only a compiler version or a list, by these variables. If you skipped a compiler list, the build will not be executed for that compiler.

The image tag can be configured by ``DOCKER_BUILD_TAG``. Build default will used **latest**. The Conan version installed, is the same listed as Docker image tag.

#### Test Step

The second stage runs the new image created, build some Conan packages, check for correct standard libraries installed and validate standard C++ supported.
The same build variables, as ``CONAN_GCC_VERSIONS``, ``CONAN_CLANG_VERSIONS`` are used to select the compiler and version.

``Gcc`` images use libstdc++.
``Clang`` images use libc++ and libstdc++.

The packages created on test, are not uploaded to Conan server, Are just to validate the image.

#### Deploy Step

The final stage pushes the image to docker server (hub.docker). ``DOCKER_UPLOAD`` should be true.

The login uses ``DOCKER_LOGIN_USERNAME`` and ``DOCKER_PASSWORD`` to authenticate.


E.g Upload Docker images to Docker hub, after build and test:

    $ DOCKER_USERNAME="<username>" DOCKER_PASSWORD="<password>" DOCKER_UPLOAD="TRUE" python run.py

To see all supported variables, read the section below.

## Environment configuration

You can also use environment variables to change the behavior of Conan Docker Tools building.
These variables are only consumed by `run.py` script and `docker` command, running `docker-compose` directly won't be affect by environment variables.
This is especially useful for CI integration.

Build and Test variables:

- **GCC_VERSIONS**: GCC versions to build, test and deploy, comma separated, e.g. "4.6,4.8,4.9,5.2,5.3,5.4,6.2.6.3"
- **CLANG_VERSIONS**: Clang versions to build, test and deploy, comma separated, e.g. "3.8,3.9,4.0"
- **SUDO_COMMAND**: Sudo command used on Linux distros, e.g. "sudo"
- **DOCKER_CACHE**: Allow to cache docker layers during the build, to speed up local testing

Upload related variables:

- **DOCKER_USERNAME**: Your Docker username to authenticate in Docker server.
- **DOCKER_PASSWORD**: Your Docker password to authenticate in Docker server
- **DOCKER_UPLOAD**: If attributed to true, it will upload the generated docker image, positive words are accepted, e.g "True", "1", "Yes". Default "False"
- **BUILD_CONAN_SERVER_IMAGE**: If attributed to true, it will build and upload an image with the conan_server
- **DOCKER_UPLOAD_ONLY_WHEN_STABLE**: Only upload only when is master branch.
FOOBAR
