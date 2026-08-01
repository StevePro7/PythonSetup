## Simpsons Trivia
#### 15-Nov-2026

### PyGame Sample
Launch PyCharm | New Project

| KEY | VALUE           |
| :---   |:----------------|
| Location: | ~/SimpsonsTrivia   |
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

Write code for main program and all supporting code
```sh
SimpsonsTrivia.py
```

Run all unit and system tests via pytest
```sh
pytest
```

Finally hit F5 to run Python code
```sh
uv run SimpsonsTrivia.py
```

OUTPUT

![SimpsonsTrivia](https://github.com/StevePro7/PythonSetup/blob/master/PyGameSample/SimpsonsTrivia/Game.png)