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