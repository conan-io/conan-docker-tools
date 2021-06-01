[![Build Status](https://dev.azure.com/conanio/conan-docker-tools/_apis/build/status/conan-io.conan-docker-tools?branchName=master)](https://dev.azure.com/conanio/conan-docker-tools/_build/latest?definitionId=1&branchName=master)
# Conan Docker Tools

![logo](logo.png)

Dockerfiles for Conan Center Continuous Integration.

You can use these images directly in your project or with the [conan-package-tools project](https://github.com/conan-io/conan-package-tools).

> :warning: **Warning:**
The images listed below are intended for **generating open-source library packages** and we CAN NOT guarantee any kind of stability. We strongly recommend using your own generated images for production environments taking the dockerfiles in this repository as a reference.

### New Docker Strategy

After many updates, new compiler releases, instability and incompatibility problems, we decided to clean the house, move a step forward with Conan Docker Tools. So far, we usually follow the same recipe, when a compiler version is released, we also release a new docker image, but we have two main problems:

- Ubuntu doesn’t package new compiler versions for each distro release, so we need to use a new Ubuntu version as base image. As a consequence, non LTS versions become a problem when EOL comes.
- Each Ubuntu release uses different package versions, including very important projects, like glibc, which results in incompatibility from a package created by distro version to another version.

To sanity our problems, we decided to keep focused on the purpose of this project: Docker files for Conan Center CI. So, first we removed older compiler versions which are no longer popular (based on Conan Center download counter).

Second, we decided to use a single base image, not too old and not the latest, something in the middle, to keep a glibc still compatible for some old distro releases. Thus, we choose Ubuntu 16.04 LTS (Xenial) which its EOL is in 2024. When close to the EOL date, we can move to 18.04 and so on.

As the compiler version is always a problem to align according to the distro release, we decided to build all compilers from sources, which includes GCC and Clang. Although this increased the build time considerably, we still now have full control over the compiler used in our images.

We totally understand that companies and users are still using our “legacy” docker images, so we won’t deprecate them soon. This kind of change requires rebuilding all packages again, and depending on the number, it could take weeks. Thus, don’t worry, we won’t remove them from Docker hub.

**TL;DR** New Docker images will use Ubuntu 16.04 as base and build all compilers from sources.

### Legacy Docker Images

If you are looking for legacy docker images (e.g. conanio/gcc10), visit [legacy](legacy) folder.

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
| - [conanio/clang9-ubuntu16.04: clang 9](https://hub.docker.com/r/conanio/clang9-ubuntu16.04/)        | x86_64 |  Supported           |
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
| - [conanio/clang8-ubuntu16.04-jenkins: clang 9](https://hub.docker.com/r/conanio/clang9-ubuntu16.04-jenkins/)            | x86_64 |  Supported |
| - [conanio/clang8-ubuntu16.04-jenkins: clang 10](https://hub.docker.com/r/conanio/clang10-ubuntu16.04-jenkins/)          | x86_64 |  Supported |
| - [conanio/clang8-ubuntu16.04-jenkins: clang 11](https://hub.docker.com/r/conanio/clang11-ubuntu16.04-jenkins/)          | x86_64 |  Supported |
| - [conanio/clang8-ubuntu16.04-jenkins: clang 12](https://hub.docker.com/r/conanio/clang12-ubuntu16.04-jenkins/)          | x86_64 |  Supported |



Use the images locally
======================

You can also use the images locally to build or test packages, this is an example command:

```
docker run --rm -v /tmp/.conan:/home/conan/.conan conanio/gcc63 bash -c "conan install boost/1.74.0@ --build"
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
The images are already built and uploaded to **"conanio(https://hub.docker.com/r/conanio/)"** dockerhub account, If you want to build your own images you can do it by:

```
$ GCC_VERSIONS=10 python build.py
```

The script *build.py* will build, test and deploy your Docker image. You can configure all stages by environment variables listed below.

Also, you can build only a version:

E.g Build and test only a image with Conan and gcc-6
```
$ CONAN_GCC_VERSIONS="6" python build.py
```

E.g Build and test only the images with Conan and clang-9, clang-10
```
$ CONAN_CLANG_VERSIONS="9,10" python build.py
```

The stages that compose the script will be described below:

### Build
The first stage collect all compiler versions listed in ``CONAN_GCC_VERSIONS`` for ``Gcc`` and in ``CONAN_CLANG_VERSIONS`` for ``Clang``. If you do not set any compiler version, the script will execute all supported versions for ``Gcc`` and ``Clang``.

You can configure only a compiler version or a list, by these variables. If you skipped a compiler list, the build will not be executed for that compiler.

The image tag can be configured by ``DOCKER_BUILD_TAG``. Build default will used **latest**. The Conan version installed, is the same listed as Docker image tag.

Each image created on this stage will be tagged as  ``${DOCKER_USERNAME}/conan-<compiler><compiler.version>-<distro><distro.version>``.

The image will not be removed after build.

### Test
The second stage runs the new image created, build some Conan packages, check for correct standard libraries installed and validate standard C++ supported.
The same build variables, as ``CONAN_GCC_VERSIONS``, ``CONAN_CLANG_VERSIONS`` are used to select the compiler and version.

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
- **SUDO_COMMAND**: Sudo command used on Linux distros, e.g. "sudo"
- **DOCKER_CACHE**: Allow to cache docker layers during the build, to speed up local testing

Upload related variables:

- **DOCKER_USERNAME**: Your Docker username to authenticate in Docker server.
- **DOCKER_PASSWORD**: Your Docker password to authenticate in Docker server
- **DOCKER_UPLOAD**: If attributed to true, it will upload the generated docker image, positive words are accepted, e.g "True", "1", "Yes". Default "False"
- **BUILD_CONAN_SERVER_IMAGE**: If attributest to true, it will build and upload an image with the conan_server
- **DOCKER_UPLOAD_ONLY_WHEN_STABLE**: Only upload only when is master branch.
