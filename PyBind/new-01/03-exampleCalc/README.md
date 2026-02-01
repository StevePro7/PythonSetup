Hello Pybind
01-Feb-2026

References
https://medium.com/@ahmedfgad/pybind11-tutorial-binding-c-code-to-python-337da23685dc

PyBind.doc
~/GitHub/StevePro10/Blogger/Python/PyBind/old/OpenAI_Retro_ChatGPT
~/GitHub/StevePro9/PythonSetup/PyBind/new-01/01-example/README.md

Launch PyCharm | New Project | 
03-exampleCalc
~/GitHub/StevePro9/PythonSetup/PyBind/new-01
Python 3.8
/usr/bin/python3

Created virtual environment
python  -m venv .venv
source .venv/bin/activate
which python
`which python` --version
Python 3.8.10


touch README.md
touch example.cpp
touch setup.py
touch test.py


pip install pybind11
pip install --upgrade pip

example.cpp
setup.py

python setup.py build
python setup.py install

IMPORTANT
these 2x commands
build the example.cpp file and produce binary file
example.cpython-38-x86_64-linux-gnu.so

This is located beneath directory
example-0.1-py3.8-linux-x86_64.egg
as this is legacy packaging

then installs in the virtual environment for consumption
from test.py

