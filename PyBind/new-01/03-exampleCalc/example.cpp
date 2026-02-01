#include <pybind11/pybind11.h>

class Calculator
{
public:
    Calculator(int value) : value(value) {}
    int add(int x)
    {
        return value + x;
    }

private:
    int value;
};

PYBIND11_MODULE(example, m)
{
    pybind11::class_<Calculator>(m, "Calculator")
        // Constructor with docstring
        .def(pybind11::init<int>(), "Constructor that initializes the Calculator with a value")

        // Method with docstring
        .def("add", &Calculator::add, "Add a number to the stored value and return the result");
}