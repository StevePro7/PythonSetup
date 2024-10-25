cmake_minimum_required(VERSION 3.19)
project(Ex01 C)

set(CMAKE_C_STANDARD 11)

find_package(PythonLibs REQUIRED)
include_directories(${PYTHON_INCLUDE_DIRS})

add_executable(Ex01 main.c foo.c)
target_link_libraries(Ex01 ${PYTHON_LIBRARIES})