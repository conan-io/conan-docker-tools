"""Execute all stages
"""
from variables import Variables
from compiler import GccCompiler, ClangCompiler
from image import Image
from build import Build
from test import Test
from deploy import Deploy
from arguments import Arguments
import logging


class Application(object):

    def __init__(self):
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
        logging.info("Starting Conan Docker Tools")
        self.__arguments = Arguments()
        self.__variables = Variables()

    def run(self):
        gcc_versions, clang_versions = self.__get_compiler_versions()
        self.__process_compiler(GccCompiler(), gcc_versions)
        self.__process_compiler(ClangCompiler(), clang_versions)

    def __process_compiler(self, compiler, versions):
        if not versions:
            logging.info("Skip process for %s" % compiler.name)
            return

        self.__assert_versions(compiler, versions)
        logging.info("Starting process for %s" % compiler.name)
        for version in versions:
            image = Image(compiler.name, version)
            if self.__arguments.build:
                logging.info("Building docker image %s" % image.name)
                self.__build(image)
            else:
                logging.info("Skip build stage for docker image %s" % image.name)
            if self.__arguments.test:
                logging.info("Testing docker image %s" % image.name)
                self.__test(image)
            else:
                logging.info("Skip test stage for docker image %s" % image.name)
            if self.__variables.docker_upload:
                logging.info("Deploying docker image %s" % image.name)
                self.__deploy(image)
            else:
                logging.info("Skip deploy stage for docker image %s" % image.name)

    def __assert_versions(self, compiler, versions):
        for version in versions:
            if version not in compiler.versions:
                raise RuntimeError("Invalid compiler version: %s-%s" % (compiler.name, version))

    def __get_compiler_versions(self):
        if not self.__variables.conan_gcc_versions and not self.__variables.conan_clang_versions:
            return GccCompiler().versions, ClangCompiler().versions
        return self.__variables.conan_gcc_versions, self.__variables.conan_clang_versions

    def __build(self, image):
        build = Build()
        build.run(image)

    def __test(self, image):
        test = Test.make(image)
        test.run(image)

    def __deploy(self, image):
        deploy = Deploy()
        deploy.run(image)
