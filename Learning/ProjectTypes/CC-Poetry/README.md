Create project
23-Jun-2023

Interpreter type
Custom environment

Type            poetry
Base python     Python 3.12.3	/usr/local/bin/python3.12
Path to poetry  /Users/stevepro/.local/bin/poetry

(cc-poetry-py3.12) 


IMPORTANT
poetry do NOT do pip install <package> because this does not update pyproject.toml file
instead do this

poetry add <package>

ERROR
Thanks but getting error pyteset 8.4.1 requires Python >=3.9 although I'm sure python interpreter is 3.12

Reference:
https://chatgpt.com/c/68723688-db50-8005-89f9-47cfa7a81f93

poetry env info
poetry env use python3.12

Update pyproject.toml
[tool.poetry.dependencies]
python = "^3.12"

poetry install
poetry lock

poetry add pytest

Now all is working!!