cmake_minimum_required(VERSION 3.16)
project(my_project LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Enable testing
include(CTest)
enable_testing()

# ---- Dependencies ----
include(cmake/Dependencies.cmake)

# ---- Project subdirs ----
add_subdirectory(src)
add_subdirectory(tests)
