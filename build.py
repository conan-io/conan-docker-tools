"""Build, Test and Deploy Docker images for Conan project"""
import collections
import os
import logging
import subprocess


class ConanDockerTools(object):
    """Execute all build process for Docker image
    """

    def __init__(self):
        logging.basicConfig(format='%(message)s', level=logging.INFO)

        self.variables = self._get_variables()

        filter_gcc_compiler_version = self.variables.gcc_versions
        filter_clang_compiler_version = self.variables.clang_versions

        Compiler = collections.namedtuple("Compiler", "name, versions")
        self.gcc_compiler = Compiler(name="gcc", versions=filter_gcc_compiler_version)
        self.clang_compiler = Compiler(name="clang", versions=filter_clang_compiler_version)

        logging.info("""
    The follow compiler versions will be built:
        GCC: %s
        CLANG: %s
        """ % (self.gcc_compiler.versions, self.clang_compiler.versions))

    def _get_variables(self):
        """Load environment variables to configure
        :return: Variables
        """
        docker_upload = os.getenv("DOCKER_UPLOAD", "false").lower() in ["true", "1"]
        build_server = os.getenv("BUILD_CONAN_SERVER_IMAGE", "false").lower() in ["true", "1"]
        docker_password = os.getenv("DOCKER_PASSWORD", "").replace('"', '\\"')
        docker_username = os.getenv("DOCKER_USERNAME", "lasote")
        if not docker_username:
            raise Exception("Specify the DOCKER_USERNAME environment variable")
        gcc_versions = os.getenv("GCC_VERSIONS").split(",") if os.getenv("GCC_VERSIONS") else []
        clang_versions = os.getenv("CLANG_VERSIONS").split(",") \
            if os.getenv("CLANG_VERSIONS") else []

        Variables = collections.namedtuple("Variables", "docker_upload, docker_password, "
                                                        "docker_username, gcc_versions, "
                                                        "clang_versions build_server")
        return Variables(docker_upload, docker_password, docker_username,
                         gcc_versions, clang_versions, build_server)

    def build(self, image_name, build_dir):
        """Call docker build to create a image
        :param image_name: Docker image name e.g. lasote/conangcc54
        :param build_dir: Directory with Dockerfile
        """
        logging.info("Stating build for Docker image %s." % image_name)
        subprocess.check_call("docker build --no-cache -t %s %s" % (image_name, build_dir),
                              shell=True)

    def linter(self, build_dir):
        """Execute hadolint to check possible prone errors

        :param build_dir: Directory with Dockerfile
        """
        logging.info("Executing hadolint on directory %s." % build_dir)
        subprocess.call('docker run --rm -i lukasmartinelli/hadolint < %s/Dockerfile' % build_dir,
                        shell=True)

    def test(self, compiler_name, compiler_version, image_name):
        """Validate Docker image by Conan install
        :param compiler_name: Compiler to be specified as conan setting e.g. clang
        :param compiler_version: Compiler version to be specified as conan setting e.g. 3.8
        :param image_name:
        """
        logging.info("Testing Docker image %s." % image_name)
        container_name = image_name.replace("/", "-")
        try:
            subprocess.check_call("docker run -t -d --name %s %s" % (container_name, image_name),
                                  shell=True)
            subprocess.check_call("docker exec %s sudo pip install -U conan_package_tools" %
                                  container_name, shell=True)
            subprocess.check_call("docker exec %s sudo pip install -U conan" % container_name,
                                  shell=True)
            subprocess.check_call("docker exec %s conan user" % container_name, shell=True)

            subprocess.check_call("docker exec %s conan install zlib/1.2.11@conan/stable -s "
                                  "arch=x86_64 -s compiler=%s -s compiler.version=%s "
                                  "-s compiler.libcxx=libstdc++ --build" %
                                  (container_name, compiler_name, compiler_version), shell=True)
            subprocess.check_call("docker exec %s conan install zlib/1.2.11@conan/stable "
                                  "-s arch=x86 -s compiler=%s -s compiler.version=%s "
                                  "-s compiler.libcxx=libstdc++ --build" %
                                  (container_name, compiler_name, compiler_version), shell=True)

            if compiler_name == "clang":
                subprocess.check_call("docker exec %s conan install zlib/1.2.11@conan/stable "
                                      "-s arch=x86_64 -s compiler=%s -s compiler.version=%s "
                                      "-s compiler.libcxx=libstdc++ --build" %
                                      (container_name, compiler_name, compiler_version), shell=True)
                subprocess.check_call("docker exec %s conan install zlib/1.2.11@conan/stable "
                                      "-s arch=x86 -s compiler=%s -s compiler.version=%s "
                                      "-s compiler.libcxx=libstdc++ --build" %
                                      (container_name, compiler_name, compiler_version), shell=True)

        finally:
            subprocess.call("docker stop %s" % container_name, shell=True)
            subprocess.call("docker rm %s" % container_name, shell=True)

    def deploy(self, image_name):
        """Upload Docker image to dockerhub
        :param image_name: Pre-built image name
        """
        if not self.variables.docker_upload:
            logging.info("Skipped upload, not DOCKER_UPLOAD")
            return

        if not self.variables.docker_password:
            logging.warning("Skipped upload, DOCKER_PASSWORD is missing!")
            return

        logging.info("Login to Docker hub account")
        result = subprocess.call(['docker', 'login', '-p',
                                  self.variables.docker_password, '-u',
                                  self.variables.docker_username])
        if result != os.EX_OK:
            raise RuntimeError("Could not login username %s "
                               "to Docker hub." % self.variables.docker_username)

        logging.info("Upload Docker image %s to Docker hub." % image_name)
        subprocess.check_call("docker push %s" % image_name, shell=True)

    def run(self):
        """Execute all 3 stages for all versions in compilers list
        """
        for compiler in [self.gcc_compiler, self.clang_compiler]:
            for version in compiler.versions:
                image_name = "%s/conan%s%s" % (self.variables.docker_username,
                                               compiler.name,
                                               version.replace(".", ""))
                build_dir = "%s_%s" % (compiler.name, version)

                self.linter(build_dir)
                self.build(image_name, build_dir)
                self.test(compiler.name, version, image_name)
                self.deploy(image_name)

        if self.variables.build_server:
            logging.info("Bulding conan_server image...")
            image_name = "%s/conan_server" % self.variables.docker_username
            self.linter("conan_server")
            self.build(image_name, "conan_server")
            self.deploy(image_name)
        else:
            logging.info("Skipping conan_server image creation")


if __name__ == "__main__":
    conan_docker_tools = ConanDockerTools()
    conan_docker_tools.run()
