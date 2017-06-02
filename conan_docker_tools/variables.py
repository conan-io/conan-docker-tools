"""Collect environment variables
"""
from os import getenv


class Variables(object):
    """Read env vars for docker tools
    """
    def __init__(self):
        self.__docker_upload = Variables.str2bool(getenv("DOCKER_UPLOAD") or "False")
        self.__docker_password = getenv("DOCKER_PASSWORD") or ""
        self.__docker_username = getenv("DOCKER_USERNAME") or "lasote"
        self.__conan_gcc_versions = getenv("CONAN_GCC_VERSIONS").split(",") if getenv("CONAN_GCC_VERSIONS") else []
        self.__conan_clang_versions = getenv("CONAN_CLANG_VERSIONS").split(",") if getenv("CONAN_CLANG_VERSIONS") else []

    @property
    def docker_upload(self):
        return self.__docker_upload

    @property
    def docker_password(self):
        return self.__docker_password

    @property
    def docker_username(self):
        return self.__docker_username

    @property
    def conan_gcc_versions(self):
        return self.__conan_gcc_versions

    @property
    def conan_clang_versions(self):
        return self.__conan_clang_versions

    @staticmethod
    def str2bool(word):
        """Convert word to boolean
        """
        return word.lower() in ("yes", "true", "t", "y", "1")

