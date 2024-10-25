#include "foo.h"
#include <Python.h>

int bar()
{
    Py_Initialize();
    Py_Finalize();
    return 9;
}
