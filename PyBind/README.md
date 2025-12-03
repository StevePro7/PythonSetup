# PyBind
03-Dec-2025
~/Steven/Cpp/MyPyBindTest


19-Oct-2024

Example debugging mixed Python C++ in VS Code
https://nadiah.org/2020/03/01/example-debug-mixed-python-c-in-visual-studio-code


16-Aug-2024

chat.openai.com
clion python c++ pybind cmakelist example 



IMPORTANT
If you'd like to write C or C++ code that will be called by Python in CLion
then you can follow these notes

Reference
~/GitHub/StevePro9/PythonSetup/Medium/Performance/CompGuide/CExtns


#include <Python.h>
https://stackoverflow.com/questions/11041299/python-h-no-such-file-or-directory

find_package(PythonLibs REQUIRED)
include_directories(${PYTHON_INCLUDE_DIRS})


Linker error
ld error PyArg_ParseTuple

https://stackoverflow.com/questions/28817266/cmake-not-linking-python
/usr/lib/x86_64-linux-gnu/libpython3.9.so" which is not built by this

Actually this did work
https://stackoverflow.com/questions/28817266/cmake-not-linking-python
but there were 2x things I had to correct:
01. target_link_libraries MUST go after add_executable
02. target_link_libraries MUST include the binary name first