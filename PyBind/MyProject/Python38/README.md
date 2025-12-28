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