
export $(cat .env | xargs)

echo Docker username: $DOCKER_USERNAME
echo Conan version: $CONAN_VERSION
echo GCC_VERSION $GCC_VERSION
echo CLANG_VERSION $CLANG_VERSION

if [ -z ${GCC_VERSION+x} ]; then
  docker_image="docker.io/$DOCKER_USERNAME/clang$CLANG_VERSION-ubuntu16.04:$CONAN_VERSION"
  echo "docker image: $docker_image"
  pytest tests --image $docker_image
else
  docker_image="docker.io/$DOCKER_USERNAME/gcc$GCC_VERSION-ubuntu16.04:$CONAN_VERSION"
  echo "docker image: $docker_image"
  pytest tests --image $docker_image
fi
