cmake_minimum_required(VERSION 3.19)
project(PyObjectsC C)

set(CMAKE_C_STANDARD 11)

find_package(PythonLibs REQUIRED)
include_directories(${PYTHON_INCLUDE_DIRS})

add_executable(PyObjectsC main.c factorial.c foo.c)
target_link_libraries(PyObjectsC ${PYTHON_LIBRARIES})