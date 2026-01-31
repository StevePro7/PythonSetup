#include <pybind11/pybind11.h>

float AddCpp(float a, float b)
{
    return a + b;
}

PYBIND11_MODULE(example, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring
    m.def("add", &AddCpp, "A function that adds two numbers");
}