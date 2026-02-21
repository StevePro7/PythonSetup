#include <pybind11/pybind11.h>

std::string say_hello()
{
    return "Hello, World!";
}

PYBIND11_MODULE(example, m)
{
	// Optional module docstring
    m.doc() = "pybind11 example module";
    m.def("say_hello", &say_hello, "A function that returns Hello World");
}