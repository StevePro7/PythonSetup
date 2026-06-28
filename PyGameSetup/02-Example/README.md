## Example II
#### 15-Sep-2026

### Hello Splash
Launch PyCharm | New Project

| KEY | VALUE           |
| :---   |:----------------|
| Location: | ~/HelloSplash     |
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
![Example02](https://github.com/StevePro7/PythonSetup/blob/master/PyGameSetup/02-Example/Ex02.png)
