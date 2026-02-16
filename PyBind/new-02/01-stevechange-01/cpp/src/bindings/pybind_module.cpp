#include <pybind11/pybind11.h>
#include "api/my_api.h"

PYBIND11_MODULE(my_api_py, m)
{
    m.def("build_edge_topology", &build_edge_topology);
    m.def("edge_side_points", &edge_side_points);
    m.def("add", &add, "A function that adds two numbers");
}
