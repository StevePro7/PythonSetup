#include <pybind11/pybind11.h>
#include "api/my_api.h"

namespace py = pybind11;

PYBIND11_MODULE(my_api_py, m)
{
    // Optional module docstring
    m.doc() = "pybind11 API module";

    py::class_<Container<double>>(m, "Container")
        .def(py::init<const size_t>())
        .def("__getitem__", [](const Container<double>&cont, size_t index){
            return cont[index];
        })
        .def("__setitem__", [](Container<double>&cont, size_t index, double value){
            cont[index] = value;
        });
}
