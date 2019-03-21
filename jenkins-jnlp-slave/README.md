# Jenkins JNLP Agent Docker image

This Dockerfile adds java jre and jenkins slave support to conanio dockerhub images.
Generated docker image can be used as Jenkins JNLP agent and can be utilized in Jenkins pipeline jobs.

## Usage 
docker build -t \<docker image\> --build-arg SOURCE_CONANIO_IMAGE=\<conanio dockerhub image\> .

## Example
docker build -t conanio/jnlp-slave-gcc8 --build-arg SOURCE_CONANIO_IMAGE=conanio/gcc8 .

**Note**: This Dockerfile ie: 'jenkins-jnlp-slave/Dockerfile' can not process following dockerhub conanio images. Use the Dockerfile mentioned in corresponding brackets.
- conanio/gcc46  (Use jenkins-jnlp-slave/gcc_4.6/Dockerfile)
- conanio/gcc48  (Use jenkins-jnlp-slave/gcc_4.8/Dockerfile)
- conanio/gcc48-x86  (Use jenkins-jnlp-slave/gcc_4.8/Dockerfile)
- conanio/gcc49  (Use jenkins-jnlp-slave/gcc_4.8/Dockerfile)
- conanio/gcc49-x86  (Use jenkins-jnlp-slave/gcc_4.8/Dockerfile)
- conanio/gcc49-armv7  (Use jenkins-jnlp-slave/gcc_4.8/Dockerfile)
- conanio/gcc49-armv7hf  (Use jenkins-jnlp-slave/gcc_4.8/Dockerfile)
- conanio/gcc7-centos6  (Use jenkins-jnlp-slave/gcc_7-centos6/Dockerfile)
- conanio/gcc7-centos6-x86  (Use jenkins-jnlp-slave/gcc_7-centos6-x86/Dockerfile)

Notice that same 'jenkins-jnlp-slave/gcc_4.8/Dockerfile' file is being used for 'conanio/gcc48', 'conanio/gcc48-x86','conanio/gcc49',
'conanio/gcc49-x86','conanio/gcc49-armv7' and 'conanio/gcc49-armv7hf' images.