# Cpp/CMakeLists.txt

# ---- Build pure C++ library ----------------------------------------
add_library(myproject_cpp src/hello.cpp)

target_include_directories(myproject_cpp PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src)

# ---- PyBind11 module (bindings) ------------------------------------
# The module is defined in bindings/bindings.cpp
pybind11_add_module(myproject bindings/bindings.cpp )

# Bindings depend on the core C++ library
target_link_libraries(myproject PRIVATE myproject_cpp)

