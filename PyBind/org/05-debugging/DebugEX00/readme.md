Example debugging mixed Python C++ in VS Code
19-Oct-2024

https://nadiah.org/2020/03/01/example-debug-mixed-python-c-in-visual-studio-code



python -m venv .venv
source .venv/bin/activate

CODE
myadd.cpp
myscript.py
setup.py

RUN
python setup.py install

python myscript.py
going to ADD SOME NUMBERS
11


Launch VS Code
settings.json
{
  "python.pythonPath": "${workspaceRoot}/.venv/bin/python",


launch.json
      "name": "Python: Current File",
      "type": "debugpy",

      "name": "(gdb) Attach",
      "type": "cppdbg",


Debugger
Python: Current File
F5

Terminal
ps aux | grep myscript.py

IMPORTANT
there will be many entries here
look for the one that has debugpy --connect entry
e.g.
debugpy --connect 127.0.0.1:42509
stevepro   42341

Debugger
(gdb) Attach
Click play button
Enter PID
42341

Terminal
prompted to enter "y"
enter "y"
enter password

F5
switch debuggers in the popup
should now break into C++ code and debug step


