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
