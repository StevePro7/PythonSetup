# Dependencies.cmake - External dependencies configuration

include(FetchContent)

# ---- pybind11 ----
# Uncomment below if you have pybind11 as a git submodule in third_party/
# add_subdirectory(third_party/pybind11)

# For system install, use:
# find_package(pybind11 REQUIRED)

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
