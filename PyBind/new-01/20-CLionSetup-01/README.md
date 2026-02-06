06-Feb-2026

/home/stevepro/GitHub/StevePro9/PythonSetup/PyBind/new-01/20-CLionSetup-01

C++ Executable
Language standard C++17
Create

my_project/
├── CMakeLists.txt          # top-level, CLion entry point
├── src/
│   ├── CMakeLists.txt
│   ├── api/
│   │   ├── my_api.h
│   │   └── my_api.cpp
│   ├── main.cpp            # C++ executable entry point
│   └── pybind_module.cpp   # pybind11 bindings
├── tests/
│   ├── CMakeLists.txt
│   └── test_api.cpp
└── third_party/
└── pybind11/            # optional: git submodule


Tidy up CMakeLists.txt
Move pybind_module beneath bindings directory

Build directory
In CLion, go to File → Settings (or CLion → Preferences on macOS)
Navigate to Build, Execution, Deployment → CMake
Find the "Build directory" field (it currently shows cmake-build-debug)
Change it to build
Click OK


IMPORTANT
CLion | Build menu | Clean | Rebuild

This creates the Shared Object SO file
my_api_py.cpython-38-x86_64-linux-gnu.so
/home/stevepro/GitHub/StevePro9/PythonSetup/PyBind/new-01/20-CLionSetup-01/build/python



Python 3.11
uv venv --python 3.11
source .venv/bin/activate
`which python` --version
Python 3.11.11

which python
.venv/bin/python


//This only works if you use the full path to .venv
//Project | Settings
//Build, Execution ...
//CMake
//CMake options
//-DPython3_EXECUTABLE=/home/stevepro/GitHub/StevePro9/PythonSetup/PyBind/new-01/20-CLionSetup-01/.venv/bin/python
//-DPython3_EXECUTABLE=`which python`


Update src CMakeLists.txt file instead
if(EXISTS "${CMAKE_SOURCE_DIR}/.venv/bin/python")
# Using project venv (Python 3.11)
set(Python3_EXECUTABLE "${CMAKE_SOURCE_DIR}/.venv/bin/python")
message(STATUS "Using project venv Python: ${Python3_EXECUTABLE}")
find_package(Python3 3.11 REQUIRED COMPONENTS Interpreter Development)
endif()

IMPORTANT 
I believe you must delete build directory and Rebuild project in order to get 311 SO 

my_api_py.cpython-311-x86_64-linux-gnu.so
/home/stevepro/GitHub/StevePro9/PythonSetup/PyBind/new-01/20-CLionSetup-01/build/python


CLion
Run | Edit configurations...
delete any unused entries
OR
set_target_properties(my_api_py PROPERTIES EXCLUDE_FROM_ALL TRUE)