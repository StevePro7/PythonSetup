#include <pybind11/pybind11.h>
#include <string>
#include "api/my_api.h"

namespace py = pybind11;

PYBIND11_MODULE(my_api_py, m)
{
    m.doc() = "Guitar example";

    py::class_<Guitar>(m, "Guitar")
        .def(py::init<const std::string&, const float, const int>())
        .def(py::init<const std::string&, const float>())
        .def(py::init<>())
        .def("set_manufacturer", &Guitar::SetManufacturer)
        .def("set_price", &Guitar::SetPrice)
        .def_readwrite("num_strings", &Guitar::mNumStrings)
        .def_readonly("manufacturer", &Guitar::mManufacturerName)
        .def_readonly("price", &Guitar::mPrice);
}

