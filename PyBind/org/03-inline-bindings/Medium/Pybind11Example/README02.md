Using Python with C++. Part1.
04-Jan-2025

https://medium.com/@stevechange/using-python-with-c-part1-3e894912214d

IMPORTANT
mkdir build
cd build
cmake ../
cmake --build .

IMPORTANT !!
example.cpython-38-x86_64-linux-gnu.so

Must move the SO [shared object] file to the same location as
AddTest.py

AddTest.py
Set breakpoint
F5

Terminal
ps aux | grep AddTest.py

OUTPUT
stevepro   27690  2.0  0.0 262048 29136 ?        
Sl   14:28   0:00 ~/GitHub/StevePro9/PythonSetup/PyBind/Medium/Pybind11Example/.venv/bin/python -X pycache_prefix=~/.cache/JetBrains/PyCharmCE2024.3/cpython-cache /snap/pycharm-community/439/plugins/python-ce/helpers/pydev/pydevd.py --multiprocess --qt-support=auto --port 29781 --file ~/GitHub/StevePro9/PythonSetup/PyBind/Medium/Pybind11Example/AddTest.py

PID
27690

VS Code
Debugger
(gdb) Attach
Click play button
Enter PID
27690

Terminal
prompted to enter "y"
enter "y"
enter password

PyCharm F5
VS Code break


Reference:
~/GitHub/StevePro9/PythonSetup/PyBind/DebugEX00


source
https://nadiah.org/2020/03/01/example-debug-mixed-python-c-in-visual-studio-code
