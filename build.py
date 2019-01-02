"""Build, Test and Deploy Docker images for Conan project"""
import collections
import os
import logging
import subprocess
import platform


class ConanDockerTools(object):
    """Execute all build process for Docker image
    """

    def __init__(self):
        logging.basicConfig(format='%(message)s', level=logging.INFO)

        self.variables = self._get_variables()

        filter_gcc_compiler_version = self.variables.gcc_versions
        filter_clang_compiler_version = self.variables.clang_versions
        filter_visual_compiler_version = self.variables.visual_versions

        Compiler = collections.namedtuple("Compiler", "name, versions, pretty")
        self.gcc_compiler = Compiler(name="gcc", versions=filter_gcc_compiler_version, pretty="gcc")
        self.clang_compiler = Compiler(name="clang", versions=filter_clang_compiler_version, pretty="clang")
        self.visual_compiler = Compiler(name="msvc", versions=filter_visual_compiler_version, pretty="Visual Studio")

        logging.info("""
    The follow compiler versions will be built:
        GCC: %s
        CLANG: %s
        VISUAL STUDIO: %s
        """ % (self.gcc_compiler.versions, self.clang_compiler.versions, self.visual_compiler.versions))

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
        docker_archs = os.getenv("DOCKER_ARCHS").split(",") if os.getenv("DOCKER_ARCHS") else ["x86_64"]
        os.environ["DOCKER_USERNAME"] = docker_username
        os.environ["DOCKER_BUILD_TAG"] = docker_build_tag
        gcc_versions = os.getenv("GCC_VERSIONS").split(",") if os.getenv("GCC_VERSIONS") else []
        clang_versions = os.getenv("CLANG_VERSIONS").split(",") if os.getenv("CLANG_VERSIONS") else []
        visual_versions = os.getenv("VISUAL_VERSIONS").split(",") if os.getenv("VISUAL_VERSIONS") else []
        sudo_command = os.getenv("SUDO_COMMAND", "")
        if platform.system() == "Linux" and not sudo_command:
            sudo_command = "sudo" if os.geteuid() != 0 else sudo_command

        Variables = collections.namedtuple("Variables", "docker_upload, docker_password, "
                                                        "docker_username, docker_login_username, "
                                                        "gcc_versions, clang_versions, visual_versions, "
                                                        "build_server, docker_build_tag, docker_archs, sudo_command")
        return Variables(docker_upload, docker_password, docker_username, docker_login_username,
                         gcc_versions, clang_versions, visual_versions, build_server, docker_build_tag, docker_archs, sudo_command)

    def _get_boolean_var(self, var, default="false"):
        """ Parse environment variable as boolean type
        :param var: Environment variable name
        """
        return os.getenv(var, default.lower()).lower() in ["1", "true", "yes"]

    def _get_image_name(self, service):
        """Get Docker image name based on service name
        :param service: service in compose
        :return: Docker images name
        """
        return "%s/%s:%s" % (self.variables.docker_username, service, self.variables.docker_build_tag)

    def build(self, service, context):
        """Call docker build to create a image
        :param service: service in compose e.g gcc54
        :param context: image dir
        """
        logging.info("Starting build for service %s." % service)
        subprocess.check_call("docker-compose build --no-cache %s" % service, shell=True)

    def linter(self, build_dir):
        """Execute hadolint to check possible prone errors

        :param build_dir: Directory with Dockerfile
        """
        logging.info("Executing hadolint on directory %s." % build_dir)
        subprocess.call('docker run --rm -i lukasmartinelli/hadolint < %s/Dockerfile' % build_dir,
                        shell=True)

    def test(self, arch, compiler_name, compiler_version, service):
        """Validate Docker image by Conan install
        :param arch: Name of he architecture
        :param compiler_name: Compiler to be specified as conan setting e.g. clang
        :param compiler_version: Compiler version to be specified as conan setting e.g. 3.8
        :param service: Docker compose service name
        """
        logging.info("Testing Docker by service %s." % service)
        try:
            image = self._get_image_name(service)
            if compiler_name == "Visual Studio":
                subprocess.check_call("docker exec %s %s pip -q install -U conan" % (service, self.variables.sudo_command), shell=True)
                subprocess.check_call("docker exec %s %s pip -q install -U conan_package_tools" % (service, self.variables.sudo_command), shell=True)
                subprocess.check_call("docker exec %s conan user" % service, shell=True)

                subprocess.check_call('docker exec %s conan install lz4/1.8.3@bincrafters/stable -s '
                                    'arch=%s -s compiler="%s" -s compiler.version=%s '
                                    '-s compiler.runtime=MD --build' %
                                    (service, arch, compiler_name,
                                    compiler_version), shell=True)

                subprocess.check_call('docker exec %s conan install gtest/1.8.1@bincrafters/stable -s '
                                    'arch=%s -s compiler="%s" -s compiler.version=%s '
                                    '-s compiler.runtime=MD --build' %
                                    (service, arch, compiler_name,
                                    compiler_version), shell=True)
            else:
                libcxx_list = ["libstdc++"] if compiler_name == "gcc" else ["libstdc++", "libc++"]
                subprocess.check_call("docker run -t -d --name %s %s" % (service, image), shell=True)

                for sudo_command in ["", "sudo", "sudo -E"]:
                    logging.info("Testing command prefix: '{}'".format(sudo_command))
                    output = subprocess.check_output("docker exec %s %s python3 --version" % (service, sudo_command), shell=True)
                    assert "Python 3" in output.decode()
                    logging.info("Found %s" % output.decode().rstrip())

                    output = subprocess.check_output("docker exec %s %s pip --version" % (service, sudo_command), shell=True)
                    assert "python 3" in output.decode()
                    logging.info("Found pip (Python 3)")

                    output = subprocess.check_output("docker exec %s %s pip3 --version" % (service, sudo_command), shell=True)
                    assert "python 3" in output.decode()
                    logging.info("Found pip3 (Python 3)")

                    output = subprocess.check_output("docker exec %s %s pip show conan" % (service, sudo_command), shell=True)
                    assert "python3" in output.decode()
                    logging.info("Found Conan (Python 3)")

                    output = subprocess.check_output("docker exec %s %s python --version" % (service, sudo_command), shell=True)
                    assert "Python 3" in output.decode()
                    logging.info("Default Python version: %s" % output.decode().rstrip())

                    for module in ["lzma", "sqlite3", "bz2", "zlib", "readline"]:
                        subprocess.check_call('docker exec %s %s python -c "import %s"' % (service, sudo_command, module), shell=True)

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

    def info(self, service):
        """Show Docker image info
        :param service: Docker compose service name
        """
        image = self._get_image_name(service)
        logging.info("Show Docker image %s size:" % image)
        subprocess.call('docker images %s' % image, shell=True)
        logging.info("Show Docker image %s info:" % image)
        subprocess.call('docker inspect %s' % image, shell=True)

    def run(self):
        """Execute all 3 stages for all versions in compilers list
        """
        # TODO (uilian): Only for Azure DevOps
        if platform.system() == "Windows" and os.getenv("AZURE_HTTP_USER_AGENT"):
            programdata = os.getenv("PROGRAMDATA")
            daemon_path = os.path.join(programdata, "docker", "config", "daemon.json")
            logging.info("Daemon Json: %s" % os.path.exists(daemon_path))
            with open(daemon_path, "w") as fd:
                fd.write('{"storage-opts": ["size=20G"]}')
            logging.info("Daemon Json: %s" % os.path.exists(daemon_path))

        for arch in self.variables.docker_archs:
            for compiler in [self.gcc_compiler, self.clang_compiler, self.visual_compiler]:
                for version in compiler.versions:
                    tag_arch = "" if arch == "x86_64" else "-%s" % arch
                    service = "%s%s%s" % (compiler.name, version.replace(".", ""), tag_arch)
                    build_dir = "%s_%s%s" % (compiler.name, version, tag_arch)

                    if platform.system() == "Linux":
                        self.linter(build_dir)

                    self.build(service, build_dir)
                    self.info(service)
                    self.test(arch, compiler.pretty, version, service)
                    self.deploy(service)

        if self.variables.build_server:
            service = "conan_server"
            logging.info("Bulding %s image..." % service)
            self.linter(service)
            self.build(service)
            self.info(service)
            self.deploy(service)
        else:
            logging.info("Skipping conan_server image creation")


if __name__ == "__main__":
    conan_docker_tools = ConanDockerTools()
    conan_docker_tools.run()
