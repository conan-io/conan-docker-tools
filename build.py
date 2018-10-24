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
        docker_upload = self._get_boolean_var("DOCKER_UPLOAD")
        build_server = self._get_boolean_var("BUILD_CONAN_SERVER_IMAGE")
        docker_password = os.getenv("DOCKER_PASSWORD", "").replace('"', '\\"')
        docker_username = os.getenv("DOCKER_USERNAME", "conanio")
        docker_login_username = os.getenv("DOCKER_LOGIN_USERNAME", "lasote")
        docker_build_tag = os.getenv("DOCKER_BUILD_TAG", "latest")
        sudo_command = self._get_boolean_var("DOCKER_SUDO")
        docker_archs = os.getenv("DOCKER_ARCHS").split(",") if os.getenv("DOCKER_ARCHS") else ["x86_64"]
        os.environ["DOCKER_USERNAME"] = docker_username
        os.environ["DOCKER_BUILD_TAG"] = docker_build_tag
        gcc_versions = os.getenv("GCC_VERSIONS").split(",") if os.getenv("GCC_VERSIONS") else []
        clang_versions = os.getenv("CLANG_VERSIONS").split(",") \
            if os.getenv("CLANG_VERSIONS") else []

        Variables = collections.namedtuple("Variables", "docker_upload, docker_password, "
                                                        "docker_username, docker_login_username, "
                                                        "gcc_versions, "
                                                        "clang_versions, build_server, docker_build_tag, "
                                                        "docker_archs, sudo_command")
        return Variables(docker_upload, docker_password, docker_username, docker_login_username,
                         gcc_versions, clang_versions, build_server, docker_build_tag, docker_archs
                         , sudo_command)

    def _get_sudo_command(self):
        """ Return sudo command name when required
        """
        return "sudo" if self.variables.sudo_command else ""

    def _get_boolean_var(self, var):
        """ Parse environment variable as boolean type
        :param var: Environment variable name
        """
        return os.getenv(var, "false").lower() in ["1", "true", "yes"]

    def build(self, service):
        """Call docker build to create a image
        :param service: service in compose e.g gcc54
        """
        logging.info("Starting build for service %s." % service)
        subprocess.check_call("docker-compose build %s" % service, shell=True)

    def linter(self, build_dir):
        """Execute hadolint to check possible prone errors

        :param build_dir: Directory with Dockerfile
        """
        logging.info("Executing hadolint on directory %s." % build_dir)
        subprocess.call('docker run --rm -i lukasmartinelli/hadolint < %s/Dockerfile' % build_dir,
                        shell=True)

    def test(self, arch, compiler_name, compiler_version, service, sudo_command):
        """Validate Docker image by Conan install
        :param arch: Name of he architecture
        :param compiler_name: Compiler to be specified as conan setting e.g. clang
        :param compiler_version: Compiler version to be specified as conan setting e.g. 3.8
        :param service: Docker compose service name
        :param sudo_command: Linux sudo command
        """
        logging.info("Testing Docker by service %s." % service)
        try:
            image = "%s/%s:%s" % (self.variables.docker_username, service, self.variables.docker_build_tag)
            libcxx_list = ["libstdc++"] if compiler_name == "gcc" else ["libstdc++", "libc++"]
            subprocess.check_call("docker run -t -d --name %s %s" % (service, image), shell=True)

            output = subprocess.check_output("docker exec %s python3 --version" % service, shell=True)
            assert "Python 3" in output.decode()
            logging.info("Found %s" % output.decode().rstrip())

            output = subprocess.check_output("docker exec %s pip --version" % service, shell=True)
            assert "python 3" in output.decode()
            logging.info("Found pip (Python 3)")

            output = subprocess.check_output("docker exec %s pip show conan" % service, shell=True)
            assert "python3" in output.decode()
            logging.info("Found Conan (Python 3)")

            output = subprocess.check_output("docker exec %s python --version" % service, shell=True)
            # Don't override when both python2 and python3 are present
            if compiler_name != "gcc" or str(compiler_version) != "4.6":
                assert "Python 3" in output.decode()
            logging.info("Python version: %s" % output.decode().rstrip())

            subprocess.check_call("docker exec %s %s pip install --no-cache-dir -U conan_package_tools" %
                                  (service, sudo_command), shell=True)
            subprocess.check_call("docker exec %s %s pip install --no-cache-dir -U conan" %
                                 (service, sudo_command), shell=True)
            subprocess.check_call("docker exec %s conan user" % service, shell=True)

            if compiler_name == "clang" and compiler_version == "7":
                    compiler_version = "7.0" # FIXME: Remove this when fixed in conan

            subprocess.check_call("docker exec %s conan install lz4/1.8.3@bincrafters/stable -s "
                                  "arch=%s -s compiler=%s -s compiler.version=%s --build" %
                                  (service, arch, compiler_name,
                                   compiler_version), shell=True)

            for libcxx in libcxx_list:
                subprocess.check_call("docker exec %s conan install gtest/1.8.1@bincrafters/stable -s "
                                      "arch=%s -s compiler=%s -s compiler.version=%s "
                                      "-s compiler.libcxx=%s --build" %
                                      (service, arch, compiler_name,
                                       compiler_version, libcxx), shell=True)
        finally:
            subprocess.call("docker stop %s" % service, shell=True)
            subprocess.call("docker rm %s" % service, shell=True)

    def deploy(self, service):
        """Upload Docker image to dockerhub
        :param service: Service that contains the docker image
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
                                  self.variables.docker_login_username])
        if result != os.EX_OK:
            raise RuntimeError("Could not login username %s "
                               "to Docker hub." % self.variables.docker_login_username)

        logging.info("Upload Docker image from service %s to Docker hub." % service)
        subprocess.check_call("docker-compose push %s" % service, shell=True)

    def run(self):
        """Execute all 3 stages for all versions in compilers list
        """
        for arch in self.variables.docker_archs:
            for compiler in [self.gcc_compiler, self.clang_compiler]:
                for version in compiler.versions:
                    tag_arch = "" if arch == "x86_64" else "-%s" % arch
                    service = "%s%s%s" % (compiler.name, version.replace(".", ""), tag_arch)
                    build_dir = "%s_%s%s" % (compiler.name, version, tag_arch)
                    sudo_command =  self._get_sudo_command()

                    self.linter(build_dir)
                    self.build(service)
                    self.test(arch, compiler.name, version, service, sudo_command)
                    self.deploy(service)

        if self.variables.build_server:
            logging.info("Bulding conan_server image...")
            self.linter("conan_server")
            self.build("conan_server")
            self.deploy("conan_server")
        else:
            logging.info("Skipping conan_server image creation")


if __name__ == "__main__":
    conan_docker_tools = ConanDockerTools()
    conan_docker_tools.run()
