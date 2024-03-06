# Conan Docker Tools

![logo](../logo.png)

force change

Dockerfiles for Conan Center Continuous Integration system.

> :warning: **Warning:**
The images listed below are intended for **generating open-source library packages** and we CAN NOT guarantee any kind of stability. We strongly recommend using your own generated images for production environments taking the dockerfiles in this repository as a reference.

## New Docker Strategy (June 2021)

> **TL;DR** New Docker images will use Ubuntu 16.04 as base and build all compilers from sources. Thus, all binaries generated will link with the same system library versions (smae `glibc` version).

> :warning: **Warning:**
The docker images with Ubuntu 18.04 are not used in ConanCenterIndex anymore, but they are still available in DockerHub. They are unmaintained and untested, you can use them at your own risk.

After many updates, new compiler releases, instability and incompatibility problems, we decided to clean the house, move a step forward with Conan Docker Tools. So far, we usually follow the same recipe, when a compiler version is released, we also release a new docker image, but we have two main problems:

- Ubuntu doesn't package new compiler versions for each distro release, so we need to use a new Ubuntu version as base image. As a consequence, non LTS versions become a problem when EOL comes.
- Each Ubuntu release uses different package versions, including very important projects, like `glibc`, which results in incompatibility and runtime errors when a package is built using one distro and we try to run in a different one.

With these two problems in mind we defined one objective: **use the same
Ubuntu distribution to generate all the packages in ConanCenter**, at least
we will ensure that every binary will be linked with the same system libraries
and the same `glibc` version.

As a consequence, we need to choose one base distribution and we will need
to build from sources all the compiler versions that are not already available.
In the end, we will be building from sources all the compiler versions we will
be using. As a side-effect, some version might be deprecated if we cannot
manage to build them from sources.

We decided to use a single base image, not too old and not the latest, something in the middle, to keep a `glibc` still compatible for some old distro releases. Thus, we choose Ubuntu 16.04 LTS (Xenial) which its EOL is in 2024. When close to the EOL date, we can move to a newer distro.

We totally understand that companies and users are still using our "legacy" docker images, so we won't deprecate them soon. This kind of change requires rebuilding all packages again, and depending on the number, it could take weeks.
Also, take into account that we won't activaley remove them from Docker hub.

Now the future of ConanCenter binaries is defined, it will take time to design
the transition and move everything forward, don't expect it to change soon.

## `stdlibc++` and `libc++` versions

With this approach, we manage to use the same `glibc` version for all the
binaries, and a version old enough that will be available in most of the
distros out there. Nevertheless, still each GCC compiler version will use its
matching `stdlibc++` version.

In general terms, it means that C++ binaries that are not linking statically
the `stdlibc++` library (most of them) are only forward compatible, they will
work only in images that provide a library version equal or newer that the
one used to compile them.

The same applies to `libc++` library version used together with Clang compiler,
the running system should provide a version equal or newer than the one used
to link the compiled binary.

What about Clang and `stdlibc++` version? We decided that all the Clang images
will use the same library version as there is no one correspondence between
Clang compiler and `stdlibc++` version like it is for GCC compiler. All these
Clang images will use the `stdlibc++` that corresponds to the latest LTS
Ubuntu distribution (at the time of this writting, it is the one corresponding
to GCC 10). This version should be new enough to provide most features and
widespread enough to be available for consumers that need to install it to
run pre-compiled binaries.

## Legacy Docker Images

Legacy docker images will be moved to "legacy" folder and eventually their dockerfiles will no longer be maintained in this repository (EOL to be decided).
Anyway, they should always be available in DockerHub.

## Official Docker Images

These are the images uploaded to Docker Hub and currently used by [Conan Center](https://conan.io/center):

> **Note:**
Tags will use the Conan version available in those images.

### GCC

| Version                                                                                   | Arch   | Status, Life cycle           |
|-------------------------------------------------------------------------------------------|--------|------------------------------|
| [conanio/gcc5-ubuntu18.04: gcc 5](https://hub.docker.com/r/conanio/gcc5-ubuntu18.04/)     | x86_64 | :warning: Deprecated         |
| [conanio/gcc6-ubuntu18.04: gcc 6](https://hub.docker.com/r/conanio/gcc6-ubuntu18.04/)     | x86_64 | :warning: Deprecated         |
| [conanio/gcc7-ubuntu18.04: gcc 7](https://hub.docker.com/r/conanio/gcc7-ubuntu18.04/)     | x86_64 | :warning: Deprecated         |
| [conanio/gcc8-ubuntu18.04: gcc 8](https://hub.docker.com/r/conanio/gcc8-ubuntu18.04/)     | x86_64 | :warning: Deprecated         |
| [conanio/gcc9-ubuntu18.04: gcc 9](https://hub.docker.com/r/conanio/gcc9-ubuntu18.04/)     | x86_64 | :warning: Deprecated         |
| [conanio/gcc10-ubuntu18.04: gcc 10](https://hub.docker.com/r/conanio/gcc10-ubuntu18.04/)  | x86_64 | :warning: Deprecated         |
| [conanio/gcc11-ubuntu18.04: gcc 11](https://hub.docker.com/r/conanio/gcc11-ubuntu18.04/)  | x86_64 | :warning: Deprecated         |
| [conanio/gcc12-ubuntu18.04: gcc 12](https://hub.docker.com/r/conanio/gcc12-ubuntu18.04/)  | x86_64 | :warning: Deprecated         |
| [conanio/gcc13-ubuntu18.04: gcc 13](https://hub.docker.com/r/conanio/gcc13-ubuntu18.04/)  | x86_64 | :warning: Deprecated         |
| [conanio/gcc5-ubuntu16.04: gcc 5](https://hub.docker.com/r/conanio/gcc5-ubuntu16.04/)     | x86_64 | :warning: Deprecated         |
| [conanio/gcc6-ubuntu16.04: gcc 6](https://hub.docker.com/r/conanio/gcc6-ubuntu16.04/)     | x86_64 | :warning: Deprecated         |
| [conanio/gcc7-ubuntu16.04: gcc 7](https://hub.docker.com/r/conanio/gcc7-ubuntu16.04/)     | x86_64 | :warning: Deprecated         |
| [conanio/gcc8-ubuntu16.04: gcc 8](https://hub.docker.com/r/conanio/gcc8-ubuntu16.04/)     | x86_64 | :warning: Deprecated         |
| [conanio/gcc9-ubuntu16.04: gcc 9](https://hub.docker.com/r/conanio/gcc9-ubuntu16.04/)     | x86_64 | :warning: Deprecated         |
| [conanio/gcc10-ubuntu16.04: gcc 10](https://hub.docker.com/r/conanio/gcc10-ubuntu16.04/)  | x86_64 | :warning: Deprecated         |
| [conanio/gcc11-ubuntu16.04: gcc 11](https://hub.docker.com/r/conanio/gcc11-ubuntu16.04/)  | x86_64 | :white_check_mark: Supported |
| [conanio/gcc12-ubuntu16.04: gcc 12](https://hub.docker.com/r/conanio/gcc12-ubuntu16.04/)  | x86_64 | :warning: Deprecated         |
| [conanio/gcc13-ubuntu16.04: gcc 13](https://hub.docker.com/r/conanio/gcc13-ubuntu16.04/)  | x86_64 | :warning: Deprecated         |


### Clang

| Version                                                                                        | Arch   | Status, Life cycle           |
|------------------------------------------------------------------------------------------------|--------|------------------------------|
| [conanio/clang10-ubuntu18.04: clang 10](https://hub.docker.com/r/conanio/clang10-ubuntu18.04/) | x86_64 | :warning: Deprecated         |
| [conanio/clang11-ubuntu18.04: clang 11](https://hub.docker.com/r/conanio/clang11-ubuntu18.04/) | x86_64 | :warning: Deprecated         |
| [conanio/clang12-ubuntu18.04: clang 12](https://hub.docker.com/r/conanio/clang12-ubuntu18.04/) | x86_64 | :warning: Deprecated         |
| [conanio/clang13-ubuntu18.04: clang 13](https://hub.docker.com/r/conanio/clang13-ubuntu18.04/) | x86_64 | :warning: Deprecated         |
| [conanio/clang14-ubuntu18.04: clang 14](https://hub.docker.com/r/conanio/clang14-ubuntu18.04/) | x86_64 | :warning: Deprecated         |
| [conanio/clang10-ubuntu16.04: clang 10](https://hub.docker.com/r/conanio/clang10-ubuntu16.04/) | x86_64 | :warning: Deprecated         |
| [conanio/clang11-ubuntu16.04: clang 11](https://hub.docker.com/r/conanio/clang11-ubuntu16.04/) | x86_64 | :warning: Deprecated         |
| [conanio/clang12-ubuntu16.04: clang 12](https://hub.docker.com/r/conanio/clang12-ubuntu16.04/) | x86_64 | :warning: Deprecated         |
| [conanio/clang13-ubuntu16.04: clang 13](https://hub.docker.com/r/conanio/clang13-ubuntu16.04/) | x86_64 | :white_check_mark: Supported |
| [conanio/clang14-ubuntu16.04: clang 14](https://hub.docker.com/r/conanio/clang14-ubuntu16.04/) | x86_64 | :warning: Deprecated         |


### Jenkins Client

If you use Jenkins to build your packages and also you use Jenkins clients to run each docker container, you could use our Docker images prepared for Jenkins. Those images run the script [jenkins-client.sh](jenkins/jenkins-client), which starts the client during the container entrypoint.
These images are mainly focused for Conan Center CI.

#### GCC

| Version                                                                                                   | Arch    | Status, Life cycle           |
|-----------------------------------------------------------------------------------------------------------|---------|------------------------------|
| [conanio/gcc5-ubuntu18.04-jenkins: gcc 5](https://hub.docker.com/r/conanio/gcc5-ubuntu18.04-jenkins/)     | x86_64  | :warning: Deprecated         |
| [conanio/gcc6-ubuntu18.04-jenkins: gcc 6](https://hub.docker.com/r/conanio/gcc6-ubuntu18.04-jenkins/)     | x86_64  | :warning: Deprecated         |
| [conanio/gcc7-ubuntu18.04-jenkins: gcc 7](https://hub.docker.com/r/conanio/gcc7-ubuntu18.04-jenkins/)     | x86_64  | :warning: Deprecated         |
| [conanio/gcc8-ubuntu18.04-jenkins: gcc 8](https://hub.docker.com/r/conanio/gcc8-ubuntu18.04-jenkins/)     | x86_64  | :warning: Deprecated         |
| [conanio/gcc9-ubuntu18.04-jenkins: gcc 9](https://hub.docker.com/r/conanio/gcc9-ubuntu18.04-jenkins/)     | x86_64  | :warning: Deprecated         |
| [conanio/gcc10-ubuntu18.04-jenkins: gcc 10](https://hub.docker.com/r/conanio/gcc10-ubuntu18.04-jenkins/)  | x86_64  | :warning: Deprecated         |
| [conanio/gcc11-ubuntu18.04-jenkins: gcc 11](https://hub.docker.com/r/conanio/gcc11-ubuntu18.04-jenkins/)  | x86_64  | :warning: Deprecated         |
| [conanio/gcc12-ubuntu18.04-jenkins: gcc 12](https://hub.docker.com/r/conanio/gcc12-ubuntu18.04-jenkins/)  | x86_64  | :warning: Deprecated         |
| [conanio/gcc13-ubuntu18.04-jenkins: gcc 13](https://hub.docker.com/r/conanio/gcc13-ubuntu18.04-jenkins/)  | x86_64  | :warning: Deprecated         |
| [conanio/gcc5-ubuntu16.04-jenkins: gcc 5](https://hub.docker.com/r/conanio/gcc5-ubuntu16.04-jenkins/)     | x86_64  | :warning: Deprecated         |
| [conanio/gcc6-ubuntu16.04-jenkins: gcc 6](https://hub.docker.com/r/conanio/gcc6-ubuntu16.04-jenkins/)     | x86_64  | :warning: Deprecated         |
| [conanio/gcc7-ubuntu16.04-jenkins: gcc 7](https://hub.docker.com/r/conanio/gcc7-ubuntu16.04-jenkins/)     | x86_64  | :warning: Deprecated         |
| [conanio/gcc8-ubuntu16.04-jenkins: gcc 8](https://hub.docker.com/r/conanio/gcc8-ubuntu16.04-jenkins/)     | x86_64  | :warning: Deprecated         |
| [conanio/gcc9-ubuntu16.04-jenkins: gcc 9](https://hub.docker.com/r/conanio/gcc9-ubuntu16.04-jenkins/)     | x86_64  | :warning: Deprecated         |
| [conanio/gcc10-ubuntu16.04-jenkins: gcc 10](https://hub.docker.com/r/conanio/gcc10-ubuntu16.04-jenkins/)  | x86_64  | :warning: Deprecated         |
| [conanio/gcc11-ubuntu16.04-jenkins: gcc 11](https://hub.docker.com/r/conanio/gcc11-ubuntu16.04-jenkins/)  | x86_64  | :warning: Supported          |
| [conanio/gcc12-ubuntu16.04-jenkins: gcc 12](https://hub.docker.com/r/conanio/gcc12-ubuntu16.04-jenkins/)  | x86_64  | :warning: Deprecated         |
| [conanio/gcc13-ubuntu16.04-jenkins: gcc 13](https://hub.docker.com/r/conanio/gcc13-ubuntu16.04-jenkins/)  | x86_64  | :warning: Deprecated         |


#### Clang

| Version                                                                                                        | Arch   | Status, Life cycle           |
|----------------------------------------------------------------------------------------------------------------|--------|------------------------------|
| [conanio/clang10-ubuntu18.04-jenkins: clang 10](https://hub.docker.com/r/conanio/clang10-ubuntu18.04-jenkins/) | x86_64 | :warning: Deprecated         |
| [conanio/clang11-ubuntu18.04-jenkins: clang 11](https://hub.docker.com/r/conanio/clang11-ubuntu18.04-jenkins/) | x86_64 | :warning: Deprecated         |
| [conanio/clang12-ubuntu18.04-jenkins: clang 12](https://hub.docker.com/r/conanio/clang12-ubuntu18.04-jenkins/) | x86_64 | :warning: Deprecated         |
| [conanio/clang13-ubuntu18.04-jenkins: clang 13](https://hub.docker.com/r/conanio/clang13-ubuntu18.04-jenkins/) | x86_64 | :warning: Deprecated         |
| [conanio/clang14-ubuntu18.04-jenkins: clang 14](https://hub.docker.com/r/conanio/clang14-ubuntu18.04-jenkins/) | x86_64 | :warning: Deprecated         |
| [conanio/clang10-ubuntu16.04-jenkins: clang 10](https://hub.docker.com/r/conanio/clang10-ubuntu16.04-jenkins/) | x86_64 | :warning: Deprecated         |
| [conanio/clang11-ubuntu16.04-jenkins: clang 11](https://hub.docker.com/r/conanio/clang11-ubuntu16.04-jenkins/) | x86_64 | :warning: Deprecated         |
| [conanio/clang12-ubuntu16.04-jenkins: clang 12](https://hub.docker.com/r/conanio/clang12-ubuntu16.04-jenkins/) | x86_64 | :warning: Deprecated         |
| [conanio/clang13-ubuntu16.04-jenkins: clang 13](https://hub.docker.com/r/conanio/clang13-ubuntu16.04-jenkins/) | x86_64 | :warning: Supported          |
| [conanio/clang14-ubuntu16.04-jenkins: clang 14](https://hub.docker.com/r/conanio/clang14-ubuntu16.04-jenkins/) | x86_64 | :warning: Deprecated         |


### Library Versions

The system libraries used by those new Docker images vary according to the Linux distribution and compiler installed as explained above.
Here is a list of installed libraries and their versions:


| Docker Image                 | glibc    | libstdc++   | libc++   |
|------------------------------|----------|-------------|----------|
| conanio/gcc5-ubuntu18.04     | 2.27     | 3.4.21      | ---      |
| conanio/gcc6-ubuntu18.04     | 2.27     | 3.4.22      | ---      |
| conanio/gcc7-ubuntu18.04     | 2.27     | 3.4.24      | ---      |
| conanio/gcc8-ubuntu18.04     | 2.27     | 3.4.25      | ---      |
| conanio/gcc9-ubuntu18.04     | 2.27     | 3.4.28      | ---      |
| conanio/gcc10-ubuntu18.04    | 2.27     | 3.4.28      | ---      |
| conanio/gcc11-ubuntu18.04    | 2.27     | 3.4.29      | ---      |
| conanio/gcc12-ubuntu18.04    | 2.27     | 3.4.29      | ---      |
| conanio/gcc13-ubuntu18.04    | 2.27     | 3.4.31      | ---      |
| conanio/clang10-ubuntu18.04  | 2.27     | 3.4.28      | 10000    |
| conanio/clang11-ubuntu18.04  | 2.27     | 3.4.28      | 11000    |
| conanio/clang12-ubuntu18.04  | 2.27     | 3.4.28      | 12000    |
| conanio/clang13-ubuntu18.04  | 2.27     | 3.4.28      | 13000    |
| conanio/clang14-ubuntu18.04  | 2.27     | 3.4.28      | 14000    |
| conanio/gcc5-ubuntu16.04     | 2.23     | 3.4.21      | ---      |
| conanio/gcc6-ubuntu16.04     | 2.23     | 3.4.22      | ---      |
| conanio/gcc7-ubuntu16.04     | 2.23     | 3.4.24      | ---      |
| conanio/gcc8-ubuntu16.04     | 2.23     | 3.4.25      | ---      |
| conanio/gcc9-ubuntu16.04     | 2.23     | 3.4.28      | ---      |
| conanio/gcc10-ubuntu16.04    | 2.23     | 3.4.28      | ---      |
| conanio/gcc11-ubuntu16.04    | 2.23     | 3.4.29      | ---      |
| conanio/gcc12-ubuntu16.04    | 2.23     | 3.4.29      | ---      |
| conanio/gcc13-ubuntu16.04    | 2.23     | 3.4.31      | ---      |
| conanio/clang10-ubuntu16.04  | 2.23     | 3.4.28      | 10000    |
| conanio/clang11-ubuntu16.04  | 2.23     | 3.4.28      | 11000    |
| conanio/clang12-ubuntu16.04  | 2.23     | 3.4.28      | 12000    |
| conanio/clang13-ubuntu16.04  | 2.23     | 3.4.28      | 13000    |
| conanio/clang14-ubuntu16.04  | 2.23     | 3.4.28      | 14000    |


##### How to detect library versions

To understand which version is installed, the follow commands should be executed:


* GLIBC: `ldd --version`
* libstdc++: `strings /usr/local/lib64/libstdc++.so.6 | grep LIBCXX`
* libc++: `printf "#include <ciso646>\nint main(){}" | clang -E -stdlib=libc++ -x c++ -dM - | grep _LIBCPP_VERSION`


Use the images locally
======================

You can also use the images locally to build or test packages, this is an example command:

```shell
docker run --rm -v /tmp/.conan:/home/conan/.conan conanio/gcc11-ubuntu16.04 bash -c "conan install boost/1.76.0@ --build"
```

This command is sharing ``/tmp/.conan`` as a shared folder with the conan home, so the Boost package will be built there.
You can change the directory or execute any other command that works for your needs.

If you are familiarized with Docker compose, also it's possible to start a new container by:

```shell
docker-compose run -v /tmp/.conan:/home/conan/.conan gcc11 bash -c "conan install boost/1.74.0@ --build"
```


Build, Test and Deploy
======================

## Introduction

The images are already built and uploaded to [conanio](https://hub.docker.com/r/conanio/) dockerhub account, we recommend you to use the images that are
already avaiable, but if you want to build your own images, read this section.

We are using multistage dockerfiles, and some of them require to build other
images first, so please, read carefully all the steps below.

We will be using docker compose command to build the images just for
convenience. It will help to ensure that the same configuration is used to
build all the images and the names match, but you can also use raw
`docker build` command and provide all the required arguments in the
command line.

Each image created will be tagged as  `conanio/<compiler><compiler.version>-<distro><distro.version>:<conan-version>`.

### Configuration

All the configuration is declared in the `.env` file that docker-compose will
load automatically when running commands. Feel free to modify that file
to match your requirements.

#### Pre-Build stage (Base)

The Docker image `base` (same service name), installs all basic system APT packages, CMake, Python and Conan. So, if you are looking for an
image without compiler, `base` is your candidate.

```shell
$ docker-compose build base
```

The produced image can be configured by `.env`. Most important package versions installed in Base are listed there.

#### Build stage (Builder)

All compilers are built in specific image called `builder`, which does not use `base`. The image is only used to build the compiler.
The decision made serves to avoid possible rebuilds when updating Base for some reason.

The Builder image can be built directly, it's useful if you want to investigate compiler building steps and all artifacts produced.

```shell
$ docker-compose build gcc10-builder
```

It will build image for GCC 10, which takes around 15 minutes. For Clang case, it can take 1 hour.

#### Final stage (Deploy)

As final build step, `deploy` will combine `base` image with the compiler produced by `builder`. This approach allow us keeping a smaller
image, easier to be maintained and isolated from the environment used to build the compiler.

This image avoids all Builder cache, using Docker multi-stage feature, we copy only the compiler installation folder.

It's the default build command, for instance:

```shell
$ docker-compose build gcc10
```

> Take into account that in order to build Clang images it is required to build
first the GCC image that will provide the `stdlibc++` version (whatever is
defined in `LIBSTDCPP_MAJOR_VERSION` inside `.env` file).


### Test

Besides manual testing you could do by building packages in these images and
running them in different images, there is a test-suite with some tests you
can run to validate that images contain the applications expected, the
versions match and the committed compatibility works.

You will need Python to run the test-suite, only `pytest` is required:

```shell
pip install pytest
```

To run the tests, just pass the name of the image to the command line
and declare the _service_ you are testing:

```shell
pytest tests --image conanio/base-ubuntu16.04:1.53.0 --service base
pytest tests --image conanio/gcc10-ubuntu16.04:1.53.0 --service deploy
```

It's also possible to test compatibility between images by building a binary
on one of them and running that same binary in the others. In order to run
these tests you will need to build all images for all compiler versions, all
the test suite will try to run the binary in all of them. Once you have
built all the images, you can run:

```shell
pytest tests --image conanio/gcc10-ubuntu16.04:1.53.0
```


### Deploy

If you want to distribute your image, you have to upload it to somewhere. There two ways to upload an image:

```shell
$ docker login -p <password> -u <username>
$ docker push conanio/gcc10-ubuntu16.04
```

Or, using Docker compose

```shell
$ docker login -p <password> -u <username>
$ docker-compose push gcc10
```

If you don't want to use hub.docker as default Docker registry, you may use [Artifactory](https://jfrog.com/start-free/#saas), which
is free and well supported for Docker, Conan and more.
