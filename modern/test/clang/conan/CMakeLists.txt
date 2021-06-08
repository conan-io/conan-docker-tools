cmake_minimum_required(VERSION 3.1)
project(foobar C CXX)

set(CMAKE_VERBOSE_MAKEFILE ON)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

option(WITH_UNWIND "Build example with external libunwind" ON)

find_package(ZLIB CONFIG REQUIRED)
find_package(spdlog CONFIG REQUIRED)
find_package( Threads REQUIRED)

add_executable(${CMAKE_PROJECT_NAME} main.cpp)
add_executable(${CMAKE_PROJECT_NAME}_c main.c)

if(WITH_UNWIND)
    find_package(libunwind CONFIG REQUIRED)
    set(UNWIND_TARGET libunwind::libunwind)
    target_compile_definitions(${CMAKE_PROJECT_NAME} PRIVATE WITH_UNWIND)
    target_compile_definitions(${CMAKE_PROJECT_NAME}_c PRIVATE WITH_UNWIND)
endif()


target_link_libraries(${CMAKE_PROJECT_NAME} ZLIB::ZLIB spdlog::spdlog ${UNWIND_TARGET} ${CMAKE_THREAD_LIBS_INIT})
set_target_properties(${CMAKE_PROJECT_NAME} PROPERTIES CXX_STANDARD 11)
target_compile_options(${CMAKE_PROJECT_NAME} PRIVATE -v)


target_link_libraries(${CMAKE_PROJECT_NAME}_c ZLIB::ZLIB ${UNWIND_TARGET} ${CMAKE_THREAD_LIBS_INIT})
set_target_properties(${CMAKE_PROJECT_NAME}_c PROPERTIES C_STANDARD 99)
target_compile_options(${CMAKE_PROJECT_NAME}_c PRIVATE -v)
