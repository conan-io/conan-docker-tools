# Jenkins JNLP Agent Docker image

This Dockerfile adds java jre and jenkins slave support to conanio dockerhub images.
Generated docker image can be used as Jenkins JNLP agent and can be utilized in Jenkins pipeline jobs.

## Usage 
docker build -t \<docker image\> --build-arg SOURCE_CONANIO_IMAGE=\<conanio dockerhub image\> .

## Example
docker build -t conanio/jnlp-slave-gcc8 --build-arg SOURCE_CONANIO_IMAGE=conanio/gcc8 .
