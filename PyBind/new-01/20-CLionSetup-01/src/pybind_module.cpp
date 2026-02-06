#include <pybind11/pybind11.h>
#include "api/my_api.h"

PYBIND11_MODULE(my_api_py, m) {
    m.def("add", &add, "A function that adds two numbers");
}
