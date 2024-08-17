cmake_minimum_required(VERSION 3.12)
project(Test02)

#set(CMAKE_CXX_STANDARD 11)

add_executable(Test02 main.cpp)

set(Python3_FIND_UNVERSIONED_NAMES NEVER)
find_package(Python3)
#find_package(Python3 COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11)

#pybind11_add_module(example main.cpp)
#target_include_directories(example PRIVATE ${Python3_INCLUDE_DIRS})
#target_link_libraries(example PRIVATE ${Python3_LIBRARIES})