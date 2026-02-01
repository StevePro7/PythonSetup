01-Feb-2026
CLion does NOT specify version of Python compatible
therefore must target the global version 3.8.10

Run all the code in CLion
Build | Rebuild project
output is cmake-build-debug | Cpp | bindings
myproject.cpython-38-x86_64-linux-gnu.so

uv init --python 3.11.11
uv venv --python 3.11.11
source .venv/bin/activate

uv add pybind11  
uv sync

main.py

Therefore MUST manually copy this file to v3.8. VENV
cd ~/GitHub/StevePro9/PythonSetup/PyBind/org/04-project-bindings/MyProject/Python38/.venv/lib/python3.8/site-packages
cp ~/GitHub/StevePro9/PythonSetup/PyBind/org/04-project-bindings/MyProject/cmake-build-debug/Cpp/bindings/myproject.cpython-38-x86_64-linux-gnu.so .

Run main.py

OR can copy at the same level as main.py
as only one file

cp /home/stevepro/GitHub/StevePro9/PythonSetup/PyBind/org/04-project-bindings/MyProject/cmake-build-debug/Cpp/bindings/myproject.cpython-38-x86_64-linux-gnu.so .




/**
uv add pybind11  
uv sync

cd /home/stevepro/GitHub/StevePro9/PythonSetup/PyBind/MyProject/Python38/.venv/lib/python3.8/site-packages

cd /home/stevepro/GitHub/StevePro9/PythonSetup/PyBind/MyProject/Python38/.venv/lib64/python3.8/site-packages


cp ~/GitHub/StevePro9/PythonSetup/PyBind/MyProject/Python38/.venv/lib/python3.8/site-packages/myproject.cpython-38-x86_64-linux-gnu.so .


PYI reference
mesh Ops pvt

Use mypy and stubgen to auto create myproject.pyi for intellisense

uv add pybind11-stubgen
uv run pybind11-stubgen myproject --output .
**/