Example
01-Feb-2026

Reference
PyBind.doc
~/GitHub/StevePro10/Blogger/Python/PyBind/old/OpenAI_Retro_ChatGPT

BUT also replicate of
~/GitHub/StevePro9/PythonSetup/PyBind/org/01-setupTools/pybind/test01
~/GitHub/StevePro9/PythonSetup/PyBind/org/01-setupTools/pybind/test02

cd ~/GitHub/StevePro9/PythonSetup/PyBind/new-01/01-example
touch README.md
touch example.cpp
touch setup.py
touch test.py

python  -m venv .venv
source .venv/bin/activate
which python
`which python` --version
Python 3.8.10

pip install pybind11
pip install --upgrade pip
pip list
Package       Version
------------- -------
pip           20.0.2
pkg-resources 0.0.0
pybind11      3.0.1
setuptools    44.0.0

example.cpp
setup.py

python setup.py build_ext --inplace

Produces
example.cpython-38-x86_64-linux-gnu.so

test.py

python test.py
3


IMPORTANT
in this small example all the files are on the same level
thus
python setup.py build_ext --inplace
will build the SO file at the same level as python files
example.cpython-38-x86_64-linux-gnu.so

Therefore - no issue consuming in test.py with intellisense etc.


further confirmation
https://medium.com/@ahmedfgad/pybind11-tutorial-binding-c-code-to-python-337da23685dc
Just make sure the .so file is in the same directory of the test.py script
(unless you opted to install the module).
