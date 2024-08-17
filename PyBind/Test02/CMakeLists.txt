cmake_minimum_required(VERSION 3.12)
project(Test02)

#set(CMAKE_CXX_STANDARD 11)

add_executable(Test02 main.cpp)

#find_package(Python3 3.8 REQUIRED COMPONENTS Interpreter Development)
find_package(Python 3.9.5 REQUIRED COMPONENTS Interpreter Development)
find_package(pybind11 REQUIRED)

#pybind11_add_module(example main.cpp)
#target_include_directories(example PRIVATE ${Python3_INCLUDE_DIRS})
#target_link_libraries(example PRIVATE ${Python3_LIBRARIES})