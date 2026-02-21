### ExampleI
#### 31-Mar-2026

Hello PyBind
```sh
mkdir ~/HelloPyBind
cd ~/HelloPyBind
touch example.cpp
touch setup.py
touch test.py
```

Setup environment
```sh
python  -m venv .venv
source .venv/bin/activate
which python
`which python` --version	# Python 3.8.10
```

Pip install dependencies
```sh
pip install pybind11
pip install --upgrade pip
```

Write code for C++ and setup
```sh
example.cpp
setup.py
```

Build C++ code using setup
```sh
python setup.py build_ext --inplace
```

Output
```sh
example.cpython-38-x86_64-linux-gnu.so
```

Write code for Python code to test
```sh
test.py
```

Finally run Python code to test C++ code
```sh
python test.py
```

Output
```sh
1 + 2 = 3
```
