## Example IV
#### 31-Mar-2026

### Hello PyBind
Launch Terminal
```sh
mkdir ~/HelloPyBind
cd ~/HelloPyBind
```

Launch PyCharm | New Project

| KEY | VALUE    |
| :---   | :--- |
| Location: | ~/HelloPyBind/python   |
| Interpreter type: | uv   |
| Python version: | 3.11   |
| Path to uv: | ~/.local/bin/uv   |

Create

Setup environment - if not auto created by PyCharm
```sh
uv venv --python 3.11
source .venv/bin/activate       # OR .\.venv\Scripts\activate
which python
`which python` --version	# Python 3.11.11
```

Launch CLion | New Project

| KEY | VALUE    |
| :---   | :--- |
| C++ | C++ Executable   |
| Location: | ~/HelloPyBind/cpp   |
| Language standard: | C++ 17   |

Create

Ensure build directory set | File menu | Settings...
```sh
Build, Execution, Deployment
CMake
Build directory: build
```

Setup C++ folder structure for src and tests folders
```sh
cpp/
├── src/
│   ├── api/
│   │   ├── my_api.h
│   │   └── my_api.cpp
│   ├── bindings/
│   │   └── pybind_module.cpp	# pybind11 bindings
│   ├── CMakeLists.txt
│   ├── main.cpp            	# C++ executable entry point
├── tests/
│   ├── CMakeLists.txt
│   └── test_api.cpp
├── CMakeLists.txt          	# top-level, CLion entry point
```

Write all C++ code for src and tests plus CMakeLists.txt
```sh
main.cpp
test_api.cpp
```

Rebuild entire solution in Debug mode | Build menu
```sh
Rebuild all in 'Debug'
```

IMPORTANT - CMakeLists.txt files are configured to copy SO file into .venv directory!

Launch PyCharm | Write code for Python code to test
```sh
test.py
```

Finally hit F5 to run Python code to test C++ code or execute
```sh
uv run test.py
```
OUTPUT
```sh
1 + 2 = 3
```
