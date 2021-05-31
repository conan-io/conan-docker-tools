from conans import ConanFile, CMake

class Pkg(ConanFile):
    settings = "os", "compiler", "arch", "build_type"
    requires = "zlib/1.2.11", "spdlog/1.8.5"
    exports_sources = "CMakeLists.txt", "main.cpp", "main.c"
    generators = "cmake", "cmake_find_package_multi"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def deploy(self):
        self.copy("*")
        self.copy_deps("*.so*")

    def package(self):
        self.copy("*")