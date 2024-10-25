GSM
25-Oct-2024

New project
C11

touch 
foo.h
foo.c
write all Python code to be consumed in foo.c


Update CMakeLists.txt
add_executable(Ex01 main.c foo.c)

foo.c
#include <Python.h>

Compiler error
CMakeLists.txt
find_package(PythonLibs REQUIRED)
include_directories(${PYTHON_INCLUDE_DIRS})


foo.c
Py_Initialize();
Py_Finalize();

Linker error
collect2: error: ld returned 1 exit status

add_executable(Ex01 main.c foo.c)
target_link_libraries(Ex01 ${PYTHON_LIBRARIES})

IMPORTANT
order is critical here otherwise will not work!