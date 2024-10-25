#include "foo.h"
#include <Python.h>

int bar()
{
    PyObject * pName = PyUnicode_FromString ( "test_0" );
    PyObject * pModule = PyImport_Import ( pName );
    if ( ! pModule )
    {
        printf ( "Could not open script.\n" );
        return 0;
    }

    return 9;
}
