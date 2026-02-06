# ---- Python ----
if(EXISTS "${CMAKE_SOURCE_DIR}/.venv/bin/python")
    # Using project venv (Python 3.11)
    set(Python3_EXECUTABLE "${CMAKE_SOURCE_DIR}/.venv/bin/python")
    message(STATUS "Using project venv Python: ${Python3_EXECUTABLE}")
    find_package(Python3 3.11 REQUIRED COMPONENTS Interpreter Development)
else()
    # Using system python (Python 3.8)
    message(STATUS "Using system Python")
    find_package(Python3 3.8 REQUIRED COMPONENTS Interpreter Development)
endif()

# ---- pybind11 ----
include(FetchContent)
FetchContent_Declare(
        pybind11
        GIT_REPOSITORY https://github.com/pybind/pybind11.git
        GIT_TAG v2.11.1
)
FetchContent_MakeAvailable(pybind11)

# ---- Core C++ library ----
add_library(my_api
        api/my_api.cpp
        )

target_include_directories(my_api
        PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}
        )

target_compile_features(my_api PUBLIC cxx_std_17)

# ---- C++ executable ----
add_executable(my_app
        main.cpp
        )

target_link_libraries(my_app
        PRIVATE my_api
        )

# ---- Python module (pybind11) ----
pybind11_add_module(my_api_py
        bindings/pybind_module.cpp
        )

target_link_libraries(my_api_py
        PRIVATE my_api
        )

# Optional: nicer output location for Python
set_target_properties(my_api_py PROPERTIES
        LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/python
        )
