#include <pybind11/pybind11.h>
#include "core.h"

namespace py = pybind11;

PYBIND11_MODULE(mycore, m)
{
    py::class_<Processor>(m, "Processor")
            .def(py::init<int>())
            .def("process", &Processor::process);
}
