Using Python with C++. Part1.
28-Oct-2024

https://medium.com/@stevechange/using-python-with-c-part1-3e894912214d

Create folder
Launch CLion
New project
~/GitHub/StevePro9/PythonSetup/PyBind/Medium/Pybind11Example
Create from existing sources

mkdir source
mkdir ThirdPartyLib
move main.cpp to source
create source/example.cpp
include in CMakeLists.txt
ERROR

Copy pybind library to ThirdPartyLib

IMPORTANT
had to remove the add_executable() now

mkdir build
cd build
cmake ../
cmake --build .

example.cpython-38-x86_64-linux-gnu.so
Move to same directory as AddTest.py

Works