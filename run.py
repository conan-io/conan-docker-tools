#!/usr/bin/env python
"""Build, Test and Deploy Docker images for Conan project"""
import collections
import os
import logging
import subprocess
import sys
import re
from conans import __version__ as client_version
from conans import tools
from cpt.ci_manager import CIManager
from cpt.printer import Printer


class ConanDockerTools(object):
    """Build, Test and Deploy Official Docker images
    """

    def __init__(self):
        logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)s', level=logging.INFO)

        self.variables = self._get_variables()

        Compiler = collections.namedtuple("Compiler", "name, versions, pretty")
        self.gcc_compiler = Compiler(name="gcc", versions=self.variables.gcc_versions, pretty="gcc")
        self.clang_compiler = Compiler(name="clang", versions=self.variables.clang_versions, pretty="clang")
        self.loggedin = False
        self.service = None

        logging.info("""
    The follow compiler versions will be built:
        GCC: %s
        CLANG: %s
    The Conan client will be installed:
        Conan: %s
        Is Latest: %s
        """ % (self.gcc_compiler.versions, self.clang_compiler.versions,
               self.variables.docker_build_tag, self._is_latest_version))

    def _get_variables(self):
        """Load environment variables to configure
        :return: Variables
        """
        docker_upload = self._get_boolean_var("DOCKER_UPLOAD")
        docker_upload_retry = os.getenv("DOCKER_UPLOAD_RETRY", 10)
        docker_upload_only_when_stable = self._get_boolean_var("DOCKER_UPLOAD_ONLY_WHEN_STABLE", True)
        build_jenkins = self._get_boolean_var("BUILD_JENKINS_IMAGE", True)

        docker_password = os.getenv("DOCKER_PASSWORD", "").replace('"', '\\"')
        docker_username = os.getenv("DOCKER_USERNAME", "conanio")
        docker_login_username = os.getenv("DOCKER_LOGIN_USERNAME", "lasote")
        artifactory_repo = os.getenv("ARTIFACTORY_REPOSITORY", "https://c3istg.jfrog.io/artifactory/dad-generic")

        docker_build_tag = self._get_conan_target_version()
        docker_cache = self._get_boolean_var("DOCKER_CACHE")
        build_base = self._get_boolean_var("BUILD_BASE", True)

        os.environ["DOCKER_USERNAME"] = docker_username
        os.environ["ARTIFACTORY_REPOSITORY"] = artifactory_repo

        gcc_versions = os.getenv("GCC_VERSIONS").split(",") if os.getenv("GCC_VERSIONS") else []
        clang_versions = os.getenv("CLANG_VERSIONS").split(",") if os.getenv("CLANG_VERSIONS") else []

        sudo_command = os.getenv("SUDO_COMMAND", "")
        if tools.os_info.is_linux and not sudo_command:
            sudo_command = "sudo" if os.geteuid() != 0 else sudo_command

        Variables = collections.namedtuple(
            "Variables", "docker_upload, docker_password, "
            "docker_username, docker_login_username, "
            "gcc_versions, "
            "clang_versions, build_jenkins, "
            "docker_build_tag, sudo_command, "
            "docker_upload_only_when_stable, docker_cache, "
            "docker_upload_retry, build_base")
        return Variables(docker_upload, docker_password, docker_username, docker_login_username,
                         gcc_versions, clang_versions, build_jenkins,
                         docker_build_tag, sudo_command, docker_upload_only_when_stable,
                         docker_cache, docker_upload_retry, build_base, )

    def _get_boolean_var(self, var, default=False):
        """ Parse environment variable as boolean type
        :param var: Environment variable name
        """
        return os.getenv(var, str(default).lower()).lower() in ["1", "true", "yes"]

    def _get_conan_target_version(self):
        """ Read Docker Compose env file and extract the target Conan version
        """
        env_file = open(".env", "r")
        match = re.search("CONAN_VERSION=(.*)", env_file.read())
        if not match:
            raise Exception("Could not find target Conan version.")
        return match.group(1)

    @property
    def _is_latest_version(self):
        """ Compare the target Conan version against the host Conan version
        """
        return tools.Version(self.variables.docker_build_tag) >= client_version

    @property
    def _ubuntu_version(self):
        return "ubuntu16.04"

    @property
    def _jenkins_name(self):
        return "jenkins"

    def login(self):
        """ Perform login on Docker server (hub.docker by default)
        """
        if self.variables.docker_upload_only_when_stable:
            printer = Printer()
            ci_manager = CIManager(printer)
            if ci_manager.get_branch() != "master" or ci_manager.is_pull_request():
                logging.info("Skipped login, is not stable branch")
                return

        if not self.variables.docker_upload:
            logging.info("Skipped login, DOCKER_UPLOAD is not activated")
            return

        if not self.variables.docker_password:
            logging.warning("Skipped login, DOCKER_PASSWORD is missing!")
            return

        if not self.variables.docker_login_username:
            logging.warning("Skipped login, DOCKER_LOGIN_USERNAME is missing!")
            return

        logging.info("Login to Docker hub account")
        result = subprocess.call([
            "docker", "login", "-u", self.variables.docker_login_username, "-p",
            self.variables.docker_password
        ])
        if result != os.EX_OK:
            raise RuntimeError("Could not login username %s "
                               "to Docker hub." % self.variables.docker_login_username)

        logging.info("Logged in Docker hub account with success")
        self.loggedin = True

    @property
    def created_image_name(self):
        """ Retrieve Docker image name created
        """
        if self._jenkins_name in self.service:
            compiler = self.service[:self.service.find("-%s" % self._jenkins_name)]
            return "%s/%s-%s-%s:%s" % (self.variables.docker_username,
                                       compiler,
                                       self._ubuntu_version,
                                       self._jenkins_name,
                                       self.variables.docker_build_tag)
        return "%s/%s-%s:%s" % (self.variables.docker_username,
                                self.service,
                                self._ubuntu_version,
                                self.variables.docker_build_tag)

    @property
    def latest_image_name(self):
        return self.created_image_name[:self.created_image_name.rfind(":") + 1] + "latest"

    def build(self):
        """Call docker-compose build to create a image based on service
        """
        no_cache = "" if self.variables.docker_cache else "--no-cache"
        logging.info("Starting build for service %s." % self.service)
        subprocess.check_call("docker-compose build %s %s" % (no_cache, self.service), shell=True)

    def test(self, compiler_name, compiler_version):
        """Validate Docker image by Conan install
        :param compiler_name: Compiler to be specified as conan setting e.g. clang
        :param compiler_version: Compiler version to be specified as conan setting e.g. 3.8
        :param service: Docker compose service name
        """
        logging.info("Testing Docker by service %s." % self.service)
        try:
                if self._jenkins_name in self.service:
                    self.test_jenkins()
                else:
                    self.test_linux(compiler_name, compiler_version)
        finally:
            subprocess.call("docker rm -f %s" % self.service, shell=True)

    def test_linux(self, compiler_name, compiler_version):
        """ Validate Linux Docker image by Conan install
        :param compiler_name: Compiler to be specified as conan setting e.g. clang
        :param compiler_version: Compiler version to be specified as conan setting e.g. 3.8
        :param service: Docker compose service name
        """
        libcxx_list = ["libstdc++", "libstdc++11"] if compiler_name == "gcc" else ["libstdc++", "libstdc++11", "libc++"]
        sudo_commands = ["", "sudo", "sudo -E"]
        subprocess.check_call("docker run -t -d --name %s %s" % (self.service,
            self.created_image_name), shell=True)

        for sudo_command in sudo_commands:

            logging.info("Testing command prefix: '{}'".format(sudo_command))
            output = subprocess.check_output(
                "docker exec %s %s python3 --version" % (self.service, sudo_command), shell=True)
            assert "Python 3" in output.decode()
            logging.info("Found %s" % output.decode().rstrip())

            output = subprocess.check_output(
                "docker exec %s %s pip --version" % (self.service, sudo_command), shell=True)
            assert "python 3" in output.decode()
            logging.info("Found pip (Python 3)")

            output = subprocess.check_output(
                "docker exec %s %s pip3 --version" % (self.service, sudo_command), shell=True)
            assert "python 3" in output.decode()
            logging.info("Found pip3 (Python 3)")

            output = subprocess.check_output(
                "docker exec %s %s pip show conan" % (self.service, sudo_command), shell=True)
            assert "python3" in output.decode()
            logging.info("Found Conan (Python 3)")

            output = subprocess.check_output(
                "docker exec %s %s python --version" % (self.service, sudo_command), shell=True)
            assert "Python 3" in output.decode()
            logging.info("Default Python version: %s" % output.decode().rstrip())

            subprocess.check_call(
                "docker exec %s %s pip install --no-cache-dir -U conan_package_tools" %
                (self.service, sudo_command),
                shell=True)
            subprocess.check_call(
                "docker exec %s %s pip install --no-cache-dir -U conan==%s" % (self.service,
                                                                        sudo_command,
                                                                        self.variables.docker_build_tag),
                                                                        shell=True)
            subprocess.check_call("docker exec %s conan user" % self.service, shell=True)

        subprocess.check_call(
            "docker exec %s conan install lz4/1.9.2@ "
            "-s compiler=%s -s compiler.version=%s --build" %
            (self.service, compiler_name, compiler_version),
            shell=True)

        for libcxx in libcxx_list:
            subprocess.check_call(
                "docker exec %s conan install gtest/1.10.0@ -s "
                "compiler=%s -s compiler.version=%s "
                "-s compiler.libcxx=%s --build" % (self.service, compiler_name,
                                                compiler_version, libcxx),
                shell=True)

        subprocess.check_call(
            "docker exec %s conan install cmake/3.18.6@ "
            "--build" % self.service, shell=True)

        logging.info("Starting new Test: Simple")
        subprocess.check_call([sys.executable, "test/simple/run.py", self.service])
        logging.info("Starting new Test: Standard")
        subprocess.check_call([sys.executable, "test/standard/run.py", self.service])
        logging.info("Starting new Test: System")
        subprocess.check_call([sys.executable, "test/system/run.py", self.service])
        logging.info("Starting new Test: Package")
        subprocess.check_call([sys.executable, "test/package/run.py", self.service])

        if "gcc" in self.service:
            logging.info("Starting new Test: Fortran")
            subprocess.check_call([sys.executable, "test/gcc/fortran/run.py",self.service])
            logging.info("Starting new Test: GCC")
            subprocess.check_call([sys.executable, "test/gcc/conan/run.py", self.service])
        else:
            logging.info("Starting new Test: Clang")
            subprocess.check_call([sys.executable, "test/clang/conan/run.py", self.service])

        try:
            subprocess.check_call(
                "docker exec %s ls /usr/local/bin/jfrog" % self.service)
        except:
            pass
        else:
            subprocess.check_call("docker exec %s jfrog --version" % self.service)

    def test_jenkins(self):
        logging.info("Testing Jenkins Docker: running service %s." % self.service)
        output = subprocess.check_output("docker run --rm -t --name %s %s" % (self.service,
                                         self.created_image_name), shell=True)
        assert "java -jar agent.jar [options...]" in output.decode()

    def deploy(self):
        """Upload Docker image to dockerhub
        """
        if not self.loggedin:
            logging.info("Skipping upload. Docker account is not connected.")
            return


        for retry in range(int(self.variables.docker_upload_retry)):
            try:
                logging.info("Upload Docker image from service %s to Docker hub." % self.service)
                subprocess.check_call("docker-compose push %s" % self.service, shell=True)
                if self._is_latest_version:
                    logging.info("Upload Docker image %s" % self.latest_image_name)
                    subprocess.check_call("docker push %s" % self.latest_image_name, shell=True)
                break
            except:
                if retry == int(self.variables.docker_upload_retry):
                    raise RuntimeError("Could not upload Docker image {}".format(self.created_image_name))
                logging.warn("Could not upload Docker image. Retry({})".format(retry+1))
                time.sleep(3)
                pass

    def tag(self):
        """Apply Docker tag name
        """
        if self._is_latest_version:
            logging.info("Creating Docker tag %s" % self.latest_image_name)
            subprocess.check_call("docker tag %s %s" % (self.created_image_name,
                self.latest_image_name), shell=True)

    def info(self):
        """Show Docker image info
        """
        logging.info("Show Docker image %s size:" % self.created_image_name)
        subprocess.call('docker images %s' % self.created_image_name, shell=True)
        logging.info("Show Docker image %s info:" % self.created_image_name)
        subprocess.call('docker inspect %s' % self.created_image_name, shell=True)

    def process_regular_images(self):
        for compiler in [self.gcc_compiler, self.clang_compiler]:
            for version in compiler.versions:
                service = "%s%s" % (compiler.name, version.replace(".", ""))
                self.service = service
                self.login()
                self.build()
                self.tag()
                self.test(compiler.name, version)
                self.info()
                self.deploy()

    def process_jenkins_image(self):
        if self.variables.build_jenkins:
            for compiler in [self.gcc_compiler, self.clang_compiler]:
                for version in compiler.versions:
                    service = "%s%s-%s" % (compiler.name, version.replace(".", ""), self._jenkins_name)

                    self.service = service
                    self.login()
                    self.build()
                    self.tag()
                    self.test(compiler.name, version)
                    self.info()
                    self.deploy()

    def process_base_image(self):
        if self.variables.build_base:
            self.service = "base"
            self.login()
            self.build()
            self.tag()
            self.info()
            self.deploy()
        else:
            logging.info("Skipped base image build.")

    def run(self):
        """Execute all 3 stages for all versions in compilers list
        """
        self.process_base_image()
        self.process_regular_images()
        self.process_jenkins_image()


if __name__ == "__main__":
    conan_docker_tools = ConanDockerTools()
    conan_docker_tools.run()
