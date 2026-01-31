cmake_minimum_required(VERSION 3.16)
project(example)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_BUILD_TYPE Debug)
set(SOURCE "${PROJECT_SOURCE_DIR}/source")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g")
set(THIRDPARTYLIB "${PROJECT_SOURCE_DIR}/ThirdPartyLib")

# pybind11
add_subdirectory(${THIRDPARTYLIB}/pybind11)

# module
pybind11_add_module (
        example
        ${SOURCE}/example.cpp
)


