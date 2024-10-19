factorial.c
setup.py
python setup.py build_ext --inplace
main.py
F5




https://blog.devgenius.io/python-performance-optimization-a-comprehensive-guide-21bc4f40dcfd


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