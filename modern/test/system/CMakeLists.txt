cmake_minimum_required(VERSION 3.1)
project(package_test CXX)

set(CMAKE_VERBOSE_MAKEFILE ON)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(${CMAKE_PROJECT_NAME} main.cpp)
target_link_libraries(${CMAKE_PROJECT_NAME} ${CONAN_LIBS})
set_target_properties(${CMAKE_PROJECT_NAME} PROPERTIES CXX_STANDARD 11)
target_compile_options(${CMAKE_PROJECT_NAME} PRIVATE -v)
