#include <pybind11/pybind11.h>

std::string say_hello()
{
    return "Hello, World!";
}

PYBIND11_MODULE(hello, m)
{
    m.def("say_hello", &say_hello, "A function that returns Hello World");
}