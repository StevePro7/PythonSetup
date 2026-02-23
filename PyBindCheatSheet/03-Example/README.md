## Example III
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
uv sync
```

Write code for C++ and CMakeLists.txt
```sh
example.cpp
CMakeLists.txt
```
Build C++ code using cmake
```sh
mkdir -p build
cd build
cmake -DPython3_EXECUTABLE=$(which python) ..
make -j$(grep -c ^processor /proc/cpuinfo)
```
OUTPUT
```sh
./build/example.cpython-311-x86_64-linux-gnu.so
```

Automate copy SO file to be consumed by Python code
```sh
python -c "import sysconfig, shutil, glob; \
dst = sysconfig.get_paths()['platlib']; \
so = glob.glob('*.so')[0]; \
shutil.copy2(so, dst)"
```

Write code for Python code to test
```sh
cd ..
test.py
```

Finally hit F5 to run Python code to test C++ code or execute
```sh
uv run test.py
```
OUTPUT
```sh
Hello, World!
```
