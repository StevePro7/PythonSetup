#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject* factorial(PyObject* self, PyObject* args) {
    long n;
    if (!PyArg_ParseTuple(args, "l", &n))
        return NULL;

    long result = 1;
    for (long i = 2; i <= n; i++) {
        result *= i;
    }

    return PyLong_FromLong(result);
}

static PyMethodDef FactorialMethods[] = {
    {"factorial", factorial, METH_VARARGS, "Calculate factorial."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef factorialmodule = {
    PyModuleDef_HEAD_INIT,
    "factorial",
    NULL,
    -1,
    FactorialMethods
};

PyMODINIT_FUNC PyInit_factorial(void) {
    return PyModule_Create(&factorialmodule);
}