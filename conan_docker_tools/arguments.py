import argparse
import os


class Arguments(object):

    def __init__(self):
        self.__args = self.__load_arguments()
        self.__overload_compiler_versions(self.__args)

    def __load_arguments(self):
        parser = argparse.ArgumentParser(description="Build docker images for Conan.io")
        parser.add_argument("--no-build", dest="build", action="store_false", default=True, help="Do not execute build stage.")
        parser.add_argument("--no-test", dest="test", action="store_false", default=True, help="Do not execute test stage.")
        parser.add_argument("--conan-gcc-versions", help="GCC versions to build.")
        parser.add_argument("--conan-clang-versions", help="Clang versions to build.")
        return parser.parse_args()

    def __overload_compiler_versions(self, arguments):
        if arguments.conan_gcc_versions:
            os.environ["CONAN_GCC_VERSIONS"] = arguments.conan_gcc_versions
        if arguments.conan_clang_versions:
            os.environ["CONAN_CLANG_VERSIONS"] = arguments.conan_clang_versions

    @property
    def build(self):
        return self.__args.build

    @property
    def test(self):
        return self.__args.test
