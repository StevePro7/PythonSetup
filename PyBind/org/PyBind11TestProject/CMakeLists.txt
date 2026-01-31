cmake_minimum_required(VERSION 3.16)
project(MyProject LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# ------------------------------------------------------------
# IMPORTANT: DO NOT USE FindPython3 ON OLD CMAKE + PYTHON 3.11
# ------------------------------------------------------------
# Instead, get the pybind11 cmake directory directly from the Python venv.
execute_process(
        COMMAND python3 -m pybind11 --cmakedir
        OUTPUT_VARIABLE pybind11_DIR
        OUTPUT_STRIP_TRAILING_WHITESPACE
)
find_package(pybind11 REQUIRED CONFIG)

# Now load the C++ + Python subdirectories
add_subdirectory(Cpp)
#add_subdirectory(Python)

enable_testing()
add_subdirectory(Cpp/tests)
