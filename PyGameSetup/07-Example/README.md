## Example VII
#### 15-Sep-2026

### Hello Music
Launch PyCharm | New Project

| KEY | VALUE           |
| :---   |:----------------|
| Location: | ~/HelloMusic    |
| Interpreter type: | uv              |
| Python version: | 3.11            |
| Path to uv: | ~/.local/bin/uv |

Create

Setup environment - if not auto created by PyCharm
```sh
uv venv --python 3.11
source .venv/bin/activate       # OR .\.venv\Scripts\activate
which python
`which python` --version	# Python 3.11.11
```

UV update pyproject.toml
```sh
uv lock
uv sync
```

Write code for main program
```sh
main.py
```

Finally hit F5 to run Python code
```sh
uv run main.py
```

OUTPUT

![Example07](https://github.com/StevePro7/PythonSetup/blob/master/PyGameSetup/07-Example/Ex07.png)