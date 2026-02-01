28-Dec-2025

cd ~/GitHub/StevePro9/PythonSetup/PyBind/MyProject/Python

uv init --python 3.11.11
uv venv --python 3.11.11

source .venv/bin/activate
uv add pybind11
uv sync


cp /home/stevepro/GitHub/StevePro9/PythonSetup/PyBind/MyProject/cmake-build-debug/Cpp/bindings/myproject.cpython-39-x86_64-linux-gnu.so /home/stevepro/GitHub/StevePro9/PythonSetup/PyBind/MyProject/Python/.venv/lib/python3.11/site-packages



/home/stevepro/GitHub/StevePro9/PythonSetup/PyBind/org/04-project-bindings/MyProject/Python/.venv/lib/python3.11/site-packages