cmake_minimum_required(VERSION 3.16)
project(meshcore)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

add_subdirectory(src)
add_subdirectory(tests)find_package(pybind11 REQUIRED)

file(GLOB_RECURSE SRC_FILES
    math/*.cpp
    mesh/*.cpp
    core/*.cpp
)

add_library(meshcore SHARED
    ${SRC_FILES}
    bindings/pybind_module.cpp
)

target_include_directories(meshcore PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

add_executable(mesh_driver main.cpp ${SRC_FILES})