"""Build docker images and upload to hub.docker
"""
import os
import argparse


class Arguments(object):
    """Collect user arguments from CLI
    """
    def __init__(self):
        self.__parser = argparse.ArgumentParser(
            description="Build and Upload Docker images")
        self.__parser.add_argument(
            "--upload",
            help="Upload image to hub docker after build",
            type=bool,
            default=False)
        self.__args = self.__parser.parse_args()

    @property
    def upload(self):
        """If image should be uploaded to hub.docker
        """
        return self.__args.upload

    @property
    def versions(self):
        """Compiler versions to be used on build
        """
        version = os.getenv("CONAN_COMPILER_VERSION")
        return version.split(',') if version else None

    @property
    def compilers(self):
        """Compiler names to be used on build
        """
        compilers = os.getenv("CONAN_COMPILER_NAME")
        return compilers.split(',') if compilers else ['gcc', 'clang']


class Builder(object):
    """Base builder for docker image
    """
    def __init__(self, compiler_name, compiler_versions):
        self.__compiler_name = compiler_name
        self.__compiler_versions = compiler_versions

    def build_and_upload(self, upload_after_build, versions):
        """Build docker image and upload to server
        """
        compiler_versions = versions or self.__compiler_versions
        for compiler_version in compiler_versions:
            folder_name = "%s_%s" % (self.__compiler_name, compiler_version)
            image_name = "lasote/conan%s%s" % (
                self.__compiler_name, compiler_version.replace(".", ""))
            os.system("cd %s && ./build.sh" % folder_name)
            if upload_after_build:
                os.system("sudo docker push %s" % image_name)

    @property
    def name(self):
        """Retrieve compiler name used by builder
        """
        return self.__compiler_name


class GccBuilder(Builder):
    """Specilized builder for GCC
    """
    def __init__(self):
        Builder.__init__(
            self, "gcc",
            ["4.6", "4.8", "4.9", "5.2", "5.3", "5.4", "6.2", "6.3", "7.2"])


class ClangBuilder(Builder):
    """Specialized builder for Clang
    """
    def __init__(self):
        Builder.__init__(self, "clang", ["3.8", "3.9", "4.0"])


if __name__ == "__main__":
    ARGS = Arguments()
    for builder in [GccBuilder(), ClangBuilder()]:
        if builder.name in ARGS.compilers:
            builder.build_and_upload(ARGS.upload, ARGS.versions)
