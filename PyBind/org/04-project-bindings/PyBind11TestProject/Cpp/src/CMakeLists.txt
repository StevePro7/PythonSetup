# Build the pure C++ static/shared library
add_library(myproject_cpp src/hello.cpp)

target_include_directories(myproject_cpp PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src)

# Build the PyBind module separately
pybind11_add_module(myproject bindings/bindings.cpp)

# Link bindings ? C++ library
target_link_libraries(myproject PRIVATE myproject_cpp)
