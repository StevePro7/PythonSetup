SimpsonsTest
30-May-2026

Launch Terminal
cd ~/GitHub/StevePro7/PythonSetup/PyGame
mkdir SimpsonsTest
cd SimpsonsTest

uv init --python 3.11
uv venv --python 3.11

source .venv/bin/activate
#.\.venv\Scripts\activate


Launch PyCharm
Open project
~/GitHub/StevePro7/PythonSetup/PyGame/SimpsonsTest

which python
`which python` --version

uv lock
uv sync

uv add pytest