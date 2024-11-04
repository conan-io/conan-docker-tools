cmake_minimum_required(VERSION 3.1)
project(foobar C CXX)

set(CMAKE_VERBOSE_MAKEFILE ON)

find_package(Threads REQUIRED)

add_executable(example-c main.c)
set_target_properties(example-c PROPERTIES C_STANDARD 99)
target_compile_options(example-c PRIVATE -v)
target_link_libraries(example-c ${CMAKE_THREAD_LIBS_INIT})

add_executable(example-cpp main.cpp)
set_target_properties(example-cpp PROPERTIES CXX_STANDARD 11)
target_compile_options(example-cpp PRIVATE -v)
target_link_libraries(example-cpp ${CMAKE_THREAD_LIBS_INIT})


if (CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
    target_compile_options(example-cpp  PRIVATE -v -stdlib=libc++)
    target_link_options(example-cpp  PRIVATE  --rtlib=compiler-rt -lc++abi -lc++)
else()
    target_compile_options(example-cpp PRIVATE -v)
endif()
