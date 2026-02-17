16-Feb-2026

Using Python with C++. Part2.
https://medium.com/@stevechange/using-python-with-c-part2-e1db73185c9e


Copy from previous directory
01-stevechange-01


Launch PyCharm
Open
~/GitHub/StevePro9/PythonSetup/PyBind/new-02/01-stevechange-02/python

uv venv --python 3.11.11
source .venv/bin/activate
OR
.venv\Scripts\activate



Launch CLion
build

mkdir build
cd build
cmake ..
make


Close CLion
Delete .idea
re-launch CLion


Windows
Launch VS 2022
File | Open | CMake...
Navigate to root level 
CMakeLists.txt


Launch PyCharm
File | New | Project
weird had to create new project to choose UV package manager
overwrite main.py