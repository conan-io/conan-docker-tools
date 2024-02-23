# Jenkins JNLP Agent Docker image

This Dockerfile adds java jre and jenkins slave support to conanio dockerhub images.
Generated docker image can be used as Jenkins JNLP agent and can be utilized in Jenkins pipeline jobs.

## Usage
docker build -t \<docker image\> --build-arg SOURCE_CONANIO_IMAGE=\<conanio dockerhub image\> .

## Example
docker build -t conanio/jenkins-gcc46 --build-arg SOURCE_CONANIO_IMAGE=conanio/gcc46 .
docker build -t conanio/jenkins-gcc8 --build-arg SOURCE_CONANIO_IMAGE=conanio/gcc8 .
docker build -t conanio/jenkins-gcc7-centos6 --build-arg SOURCE_CONANIO_IMAGE=conanio/gcc7-centos6 --file centos6/Dockerfile .
docker build -t conanio/jenkins-gcc7-centos6-x86 --build-arg SOURCE_CONANIO_IMAGE=conanio/gcc7-centos6-x86 --file centos6/Dockerfile .

**Note**: This Dockerfile ie: 'jenkins/Dockerfile' can not process following dockerhub conanio images. Use the Dockerfile mentioned in corresponding brackets.
- conanio/gcc7-centos6  (Use jenkins/centos6/Dockerfile)
- conanio/gcc7-centos6-x86  (Use jenkins/centos6/Dockerfile)
