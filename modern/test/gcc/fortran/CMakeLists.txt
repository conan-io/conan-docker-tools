cmake_minimum_required(VERSION 3.1)
project(hello Fortran)

set(CMAKE_VERBOSE_MAKEFILE ON)

add_executable(${CMAKE_PROJECT_NAME} hello.f90)
target_compile_options(${CMAKE_PROJECT_NAME} PRIVATE -v)
