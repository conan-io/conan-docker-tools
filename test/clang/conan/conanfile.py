from conans import ConanFile, CMake

class Pkg(ConanFile):
    name = "foo"
    version = "0.1"
    settings = "os", "compiler", "arch", "build_type"
    requires = "zlib/1.2.11", "spdlog/1.8.5"
    options = {"with_unwind": [True, False]}
    default_options = {"with_unwind": True}
    exports_sources = "CMakeLists.txt", "main.cpp", "main.c"
    generators = "cmake", "cmake_find_package_multi"

    def requirements(self):
        if self.options.with_unwind:
            self.requires("libunwind/1.5.0")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["WITH_UNWIND"] = self.options.with_unwind
        cmake.configure()
        cmake.build()

    def deploy(self):
        self.copy("*")
        self.copy_deps("*.so*")

    def package(self):
        self.copy("*")
