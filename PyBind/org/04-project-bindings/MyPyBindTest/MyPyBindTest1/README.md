PyBind test
29-Nov-2025

Reference:
https://github.com/StevePro7/Blogger/blob/master/Retrospective/RetroXVII/chatgpt.txt

****
Launch CLion
New project
C++ Library

add all files and folders


cd build
cmake ..
make

find . -type f -name '*.so'

./python/mycore.cpython-39-x86_64-linux-gnu.so




~/Steven/Cpp/MyPyBindTest3/.venv


/home/stevepro/Steven/Cpp/MyPyBindTest2/.venv/bin/python3 -m pip install pybind11
cmake -DPython3_EXECUTABLE=/home/stevepro/Steven/Cpp/MyPyBindTest2/.venv/bin/python ..
make
