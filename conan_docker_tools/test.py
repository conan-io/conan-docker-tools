"""Test Docker image
"""

from image import Image
import subprocess


class Test(object):
    """Base builder for docker image
    """

    def run(self, image):
        """Build docker image
        """
        try:
            subprocess.check_call("sudo docker run -t -d --name %s %s" % (image.build_dir, image.name), shell=True)
            subprocess.check_call("sudo docker exec %s sudo pip install -U conan_package_tools" % image.build_dir, shell=True)
            subprocess.check_call("sudo docker exec %s sudo pip install -U conan" % image.build_dir, shell=True)
            subprocess.check_call("sudo docker exec %s conan user" % image.build_dir, shell=True)
            self._steps(image)
        finally:
            subprocess.call("docker stop %s" % image.build_dir, shell=True)
            subprocess.call("docker rm %s" % image.build_dir, shell=True)

    def _steps(self, image):
        pass

    @staticmethod
    def make(image):
        return TestGcc() if image.compiler == "gcc" else TestClang()


class TestGcc(Test):
    def _steps(self, image):
        try:
            subprocess.check_call("sudo docker exec %s conan install gtest/1.8.0@lasote/stable -s arch=x86_64 -s compiler=%s -s compiler.version=%s -s compiler.libcxx=libstdc++ --build" % (image.build_dir, image.compiler, image.version), shell=True)
            subprocess.check_call("sudo docker exec %s conan install gtest/1.8.0@lasote/stable -s arch=x86 -s compiler=%s -s compiler.version=%s -s compiler.libcxx=libstdc++ --build" % (image.build_dir,  image.compiler, image.version), shell=True)
        except:
            raise


class TestClang(TestGcc):
    def _steps(self, image):
        try:
            TestGcc._steps(self, image)
            subprocess.check_call("sudo docker exec %s conan install gtest/1.8.0@lasote/stable -s arch=x86_64 -s compiler=%s -s compiler.version=%s -s compiler.libcxx=libstdc++ --build" % (image.build_dir, image.compiler, image.version), shell=True)
            subprocess.check_call("sudo docker exec %s conan install gtest/1.8.0@lasote/stable -s arch=x86 -s compiler=%s -s compiler.version=%s -s compiler.libcxx=libstdc++ --build" % (image.build_dir, image.compiler, image.version), shell=True)
        except:
            raise
