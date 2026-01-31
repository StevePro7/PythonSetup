cmake_minimum_required(VERSION 3.16)
project(MyPyBindTest)

set(CMAKE_CXX_STANDARD 14)

# Add src library
add_library(core STATIC src/core.cpp)
target_include_directories(core PUBLIC src)

# GoogleTest setup
enable_testing()
add_subdirectory(tests)

# PyBind11 setup
add_subdirectory(python)