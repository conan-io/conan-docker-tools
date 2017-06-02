"""Build, Test and Deploy Docker images for Conan.io
"""
import collections
import os
import logging
import re
import subprocess


class ConanDockerTools(object):
    """Execute all build process for Docker image
    """

    def __init__(self):
        logging.basicConfig(format='%(message)s', level=logging.INFO)
        default_gcc_versions = ["4.6", "4.8", "4.9", "5.2", "5.3", "5.4", "6.2", "6.3"]
        default_clang_versions = ["3.8", "3.9", "4.0"]

        self.variables = self._get_variables()
        self._assert_versions(default_gcc_versions, self.variables.conan_gcc_versions)
        self._assert_versions(default_clang_versions, self.variables.conan_clang_versions)

        filter_gcc_compiler_version = self.variables.conan_gcc_versions
        filter_clang_compiler_version = self.variables.conan_clang_versions
        if not self.variables.conan_gcc_versions and not self.variables.conan_clang_versions:
            filter_gcc_compiler_version = default_gcc_versions
            filter_clang_compiler_version = default_clang_versions

        Compiler = collections.namedtuple("Compiler", "name, versions")
        self.gcc_compiler = Compiler(name="gcc", versions=filter_gcc_compiler_version)
        self.clang_compiler = Compiler(name="clang", versions=filter_clang_compiler_version)

        logging.info("""
    The follow compiler versions will be built:
        GCC: %s
        CLANG: %s
        """ % (self.gcc_compiler.versions, self.clang_compiler.versions))

    def _assert_versions(self, compiler_versions, versions):
        """Validate user arguments over default compiler versions
        :param compiler_versions: Default compiler versions
        :param versions: User compiler versions
        """
        for version in versions:
            if version not in compiler_versions:
                raise RuntimeError("Invalid compiler version: %s." % version)

    def _get_variables(self):
        """Load environment variables to configure
        :return: Variables
        """
        docker_upload = os.getenv("DOCKER_UPLOAD", "false").lower() in ["true", "1"]
        docker_password = os.getenv("DOCKER_PASSWORD", "").replace('"', '\\"')
        docker_username = os.getenv("DOCKER_USERNAME", "lasote")
        conan_gcc_versions = os.getenv("CONAN_GCC_VERSIONS").split(",") if os.getenv("CONAN_GCC_VERSIONS") else []
        conan_clang_versions = os.getenv("CONAN_CLANG_VERSIONS").split(",") if os.getenv("CONAN_CLANG_VERSIONS") else []
        conan_stable_branch_pattern = os.getenv("CONAN_STABLE_BRANCH_PATTERN", "master")

        Variables = collections.namedtuple("Variables", "docker_upload, docker_password, docker_username, conan_gcc_versions, conan_clang_versions, conan_stable_branch_pattern")
        return Variables(docker_upload, docker_password, docker_username, conan_gcc_versions, conan_clang_versions, conan_stable_branch_pattern)

    def build(self, image_name, build_dir):
        """Call docker build to create a image
        :param image_name: Docker image name e.g. lasote/conangcc54
        :param build_dir: Directory with Dockerfile
        """
        logging.info("Stating build for Docker image %s." % image_name)
        subprocess.check_call("sudo docker build --no-cache -t %s %s" % (image_name, build_dir), shell=True)

    def test(self, compiler_name, compiler_version, image_name):
        """Validate Docker image by Conan install
        :param compiler_name: Compiler to be specified as conan setting e.g. clang
        :param compiler_version: Compiler version to be specified as conan setting e.g. 3.8
        :param image_name:
        """
        logging.info("Testing Docker image %s." % image_name)
        container_name = image_name.replace("/", "-")
        try:
            subprocess.check_call("sudo docker run -t -d --name %s %s" % (container_name, image_name), shell=True)
            subprocess.check_call("sudo docker exec %s sudo pip install -U conan_package_tools" % container_name, shell=True)
            subprocess.check_call("sudo docker exec %s sudo pip install -U conan" % container_name, shell=True)
            subprocess.check_call("sudo docker exec %s conan user" % container_name, shell=True)

            subprocess.check_call("sudo docker exec %s conan install gtest/1.8.0@lasote/stable -s arch=x86_64 -s compiler=%s -s compiler.version=%s -s compiler.libcxx=libstdc++ --build" % (container_name, compiler_name, compiler_version), shell=True)
            subprocess.check_call("sudo docker exec %s conan install gtest/1.8.0@lasote/stable -s arch=x86 -s compiler=%s -s compiler.version=%s -s compiler.libcxx=libstdc++ --build" % (container_name, compiler_name, compiler_version), shell=True)

            if compiler_name == "clang":
                subprocess.check_call("sudo docker exec %s conan install gtest/1.8.0@lasote/stable -s arch=x86_64 -s compiler=%s -s compiler.version=%s -s compiler.libcxx=libstdc++ --build" % (container_name, compiler_name, compiler_version), shell=True)
                subprocess.check_call("sudo docker exec %s conan install gtest/1.8.0@lasote/stable -s arch=x86 -s compiler=%s -s compiler.version=%s -s compiler.libcxx=libstdc++ --build" % (container_name, compiler_name, compiler_version), shell=True)

        finally:
            subprocess.call("docker stop %s" % container_name, shell=True)
            subprocess.call("docker rm %s" % container_name, shell=True)

    def deploy(self, image_name):
        """Upload Docker image to dockerhub
        :param image_name: Pre-built image name
        """
        if not self.variables.docker_upload:
            logging.info("Skipped upload.")
            return

        if not self.variables.docker_username or not self.variables.docker_password:
            logging.warning("Skipped upload, some parameter (username or password) is missing!")
            return

        current_branch = subprocess.check_output(['git', 'name-rev', '--name-only', 'HEAD']).decode()
        prog = re.compile(self.variables.conan_stable_branch_pattern)
        if not prog.match(current_branch):
            logging.warning("Skipped upload, stable branch pattern does not match!")
            return

        logging.info("Login to Docker hub account")
        result = subprocess.call(['sudo', 'docker', 'login', '-p', self.variables.docker_password, '-u', self.variables.docker_username])
        if result != os.EX_OK:
            raise RuntimeError("Could not login username %s to Docker hub." % self.variables.docker_username)

        logging.info("Upload Docker image %s to Docker hub." % image_name)
        subprocess.check_call("sudo docker push %s" % image_name, shell=True)

    def run(self):
        """Execute all 3 stages for all versions in compilers list
        """
        for compiler in [self.gcc_compiler, self.clang_compiler]:
            for version in compiler.versions:
                image_name = "%s/conan%s%s" % (self.variables.docker_username, compiler.name, version.replace(".", ""))
                build_dir = "%s_%s" % (compiler.name, version)

                self.build(image_name, build_dir)
                self.test(compiler.name, version, image_name)
                self.deploy(image_name)


if __name__ == "__main__":
    conan_docker_tools = ConanDockerTools()
    conan_docker_tools.run()
