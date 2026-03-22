cmake_minimum_required(VERSION 3.16)
project(example)

# Find the Python 3.11-specific pybind11 CONFIG from pip
execute_process(
        COMMAND ${Python3_EXECUTABLE} -m pybind11 --cmakedir
        OUTPUT_VARIABLE pybind11_DIR
        OUTPUT_STRIP_TRAILING_WHITESPACE
)
find_package(pybind11 REQUIRED CONFIG)

pybind11_add_module(example example.cpp)
