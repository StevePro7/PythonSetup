Example debugging mixed Python C++ in VS Code
19-Oct-2024

https://nadiah.org/2020/03/01/example-debug-mixed-python-c-in-visual-studio-code

Set breakpoint
myscript.py
x = myadd.myadd(5,6)

myadd.cpp
z = x + y;


Debugger
Python: Current File
F5

Terminal
ps aux | grep myscript.py

IMPORTANT
there will be many entries here
look for the one that has debugpy --connect entry
e.g.
stevepro   64722  1.7  0.1 428380 50060 pts/2    Sl+  15:40   0:00 /home/stevepro/.local/share/virtualenvs/PythonProject1-P01eNqsw/bin/python /home/stevepro/.vscode/extensions/ms-python.debugpy-2025.18.0-linux-x64/bundled/libs/debugpy/adapter/../../debugpy/launcher/../../debugpy --connect 127.0.0.1:40547 --configure-qt none --adapter-access-token 0bfbb40fb12d0db839737e790d8d1c460ec766775068f072bc56ed9a15178c69 /home/stevepro/GitHub/StevePro9/PythonSetup/PyBind/org/05-debugging/DebugEX00/myscript.py


WANT the PID to the right of user stevepro
stevepro   64722

Debugger
(gdb) Attach
Click play button
Enter PID
64722

Terminal
prompted to enter "y"
enter "y"
enter password

F5
switch debuggers in the popup
should now break into C++ code and debug step!
