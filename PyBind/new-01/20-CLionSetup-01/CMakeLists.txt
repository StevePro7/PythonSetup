cmake_minimum_required(VERSION 3.16)
project(my_project LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Enable testing
include(CTest)
enable_testing()

# ---- pybind11 ----
# Uncomment below if you have pybind11 as a git submodule in third_party/
# add_subdirectory(third_party/pybind11)

# For now, use system install or FetchContent
# find_package(pybind11 REQUIRED)
include(FetchContent)
FetchContent_Declare(
        pybind11
        GIT_REPOSITORY https://github.com/pybind/pybind11.git
        GIT_TAG v2.11.1
)
FetchContent_MakeAvailable(pybind11)

# ---- GoogleTest ----
FetchContent_Declare(
        googletest
        GIT_REPOSITORY https://github.com/google/googletest.git
        GIT_TAG v1.14.0
)
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

# ---- Project subdirs ----
add_subdirectory(src)
add_subdirectory(tests)
