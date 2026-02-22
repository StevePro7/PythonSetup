## Example II
#### 31-Mar-2026

### Hello PyBind
Launch PyCharm | New Project

| KEY | VALUE    |
| :---   | :--- |
| Location: | ~/HelloPyBind   |
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
UV install dependencies
```sh
uv add pybind11
uv add setuptools
uv lock
uv sync
```

Write code for C++ and setup
```sh
example.cpp
setup.py
```
Build C++ code using setup
```sh
uv run setup.py build
uv run setup.py install

```
OUTPUT
```sh
./build/lib.linux-x86_64-cpython-311/example.cpython-311-x86_64-linux-gnu.so
```
Write code for Python code to test
```sh
test.py
```
Finally hit F5 to run Python code to test C++ code or execute
```sh
uv run test.py
```
OUTPUT
```sh
3 + 5 = 8
9 - 5 = 4
```
