#include <pybind11/pybind11.h>
#include "hello.h"

namespace py = pybind11;

PYBIND11_MODULE(myproject, m)
{
    m.doc() = "PyBind11 bindings for MyProject";
    m.def("greet", &greet, "Return a hello message");
}
