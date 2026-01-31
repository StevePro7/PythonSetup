# Tell pybind11 to run its own Python detection logic
set(PYBIND11_FINDPYTHON ON)

find_package(pybind11 REQUIRED)

pybind11_add_module(myproject bindings.cpp)
target_link_libraries(myproject PRIVATE MyProject)