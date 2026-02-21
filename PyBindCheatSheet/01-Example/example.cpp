#include <pybind11/pybind11.h>

int add(int x, int y)
{
    return x + y;
}

PYBIND11_MODULE(example, m)
{
    // Optional module docstring
    m.doc() = "pybind11 example module";
    m.def("add", &add, "A function that adds two numbers");
}