
export $(cat .env | xargs)

echo Docker username: $DOCKER_USERNAME
echo Conan version: $CONAN_VERSION
echo GCC_VERSION $GCC_VERSION
echo CLANG_VERSION $CLANG_VERSION

if [ -z ${GCC_VERSION+x} ]; then
  deploy_image="docker.io/$DOCKER_USERNAME/clang$CLANG_VERSION-ubuntu16.04:$CONAN_VERSION"
  jenkins_image="docker.io/$DOCKER_USERNAME/clang$CLANG_VERSION-ubuntu16.04-jenkins:$CONAN_VERSION"
  echo "deploy_image: $deploy_image"
  echo "jenkins_image: $jenkins_image"
  pytest tests --image $deploy_image
  pytest tests --image $jenkins_image
else
  deploy_image="docker.io/$DOCKER_USERNAME/gcc$GCC_VERSION-ubuntu16.04:$CONAN_VERSION"
  jenkins_image="docker.io/$DOCKER_USERNAME/gcc$GCC_VERSION-ubuntu16.04-jenkins:$CONAN_VERSION"
  echo "deploy_image: $deploy_image"
  echo "jenkins_image: $jenkins_image"
  pytest tests --image $deploy_image
  pytest tests --image $jenkins_image
fi
