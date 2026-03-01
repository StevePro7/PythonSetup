# ---- Python ----
if(EXISTS "${CMAKE_SOURCE_DIR}/.venv/bin/python")
    # Using project venv (Python 3.8)
    set(Python3_EXECUTABLE "${CMAKE_SOURCE_DIR}/.venv/bin/python")
    message(STATUS "Using project venv Python: ${Python3_EXECUTABLE}")
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

# Install directly into venv site-packages when project .venv exists
if(EXISTS "${CMAKE_SOURCE_DIR}/.venv/bin/python")
    set(PY_VENV_SITE_PACKAGES "${CMAKE_SOURCE_DIR}/.venv/lib/python3.8/site-packages")
    # Ensure the directory exists at build time
    add_custom_command(TARGET my_api_py
                       POST_BUILD
                       COMMAND ${CMAKE_COMMAND} -E make_directory "${PY_VENV_SITE_PACKAGES}"
                       COMMENT "Ensuring venv site-packages exists: ${PY_VENV_SITE_PACKAGES}")

    set_target_properties(my_api_py PROPERTIES
            LIBRARY_OUTPUT_DIRECTORY ${PY_VENV_SITE_PACKAGES}
            )
    message(STATUS "Python module will be built into venv site-packages: ${PY_VENV_SITE_PACKAGES}")
else()
    # Default to build output
    set_target_properties(my_api_py PROPERTIES
            LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/python
            )
    message(STATUS "Python module will be built into: ${CMAKE_BINARY_DIR}/python")
endif()
