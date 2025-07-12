UV 
cd /Users/stevepro/Steven/Python/ProjectTypes
mkdir FF-uv
cd FF-uv
uv init

uv env
source .venv/bin/activate


import sklearn
uv pip install scikit-learn


IMPORTANT
running main.py inside PyCharm getting Module not found
running the base Python interpreter 3.12 NOT uv venv

Click Python 3.12 interpreter | Interpreter Settings
Add Python interpreter
Existing environment
enter fully qualified path to VENV
~/Steven/Python/ProjectTypes/FF-uv/.venv

Finally see in PyCharm
Python 3.12 (FF-uv)


SUMMARY
01.
open in PyCharm
uv venv
uv pip list
uv pip install scikit-learn
pyproject.toml

02.
open in PyCharm
uv venv
uv pip list
uv pip install pyproject.toml
uv pip list