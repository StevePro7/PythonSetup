#include <pybind11/pybind11.h>
#include "core.h"

namespace py = pybind11;

PYBIND11_MODULE(myproject, m)
{
    m.doc() = "PyBind11 bindings for MyProject";
    m.def("hello", &hello, "Return a hello message");
}
