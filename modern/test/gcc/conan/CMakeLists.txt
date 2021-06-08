cmake_minimum_required(VERSION 3.1)
project(foobar C CXX)

set(CMAKE_VERBOSE_MAKEFILE ON)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(ZLIB CONFIG REQUIRED)
find_package(spdlog CONFIG REQUIRED)

add_executable(${CMAKE_PROJECT_NAME} main.cpp)
target_link_libraries(${CMAKE_PROJECT_NAME} ZLIB::ZLIB spdlog::spdlog)
set_target_properties(${CMAKE_PROJECT_NAME} PROPERTIES CXX_STANDARD 11)
target_compile_options(${CMAKE_PROJECT_NAME} PRIVATE -v)

add_executable(${CMAKE_PROJECT_NAME}_c main.c)
target_link_libraries(${CMAKE_PROJECT_NAME}_c ZLIB::ZLIB)
set_target_properties(${CMAKE_PROJECT_NAME}_c PROPERTIES C_STANDARD 99)
target_compile_options(${CMAKE_PROJECT_NAME}_c PRIVATE -v)
