#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "../mesh/mesh.h"
#include "../mesh/mesh_algorithms.h"

namespace py = pybind11;

PYBIND11_MODULE(meshcore, m)
{
    py::class_<math::Vector3>(m, "Vector3")
            .def(py::init<double,double,double>())
            .def_readwrite("x", &math::Vector3::x)
            .def_readwrite("y", &math::Vector3::y)
            .def_readwrite("z", &math::Vector3::z);

    py::class_<mesh::Mesh>(m, "Mesh")
            .def(py::init<>())
            .def_readwrite("vertices", &mesh::Mesh::vertices)
            .def("smooth", [](mesh::Mesh& self){
                mesh::laplacianSmooth(self, 1, 0.5);
            });
}