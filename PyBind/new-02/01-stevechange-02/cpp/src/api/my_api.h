#ifndef _MY_API_H_
#define _MY_API_H_







#include <math.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include <iostream>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <limits>
#include <algorithm>
#include <functional>
#include <chrono>
#include <random>
#include <iterator>
#include <cassert>
#include <utility>
#include <vector>
#include <string>
#include <float.h>      // FLT_EPSILON, DBL_EPSILON

namespace py = pybind11;


void build_edge_topology(const py::array_t<int, py::array::c_style> &input_mesh_faces_arr,
                         const py::array_t<int, py::array::c_style> &input_mesh_edges_arr,
                         py::list &edge_topology_results);

// C++ version for unit testing (no pybind11 types)
void build_edge_topology_cpp(const std::vector<std::vector<int>>& faces,
                             const std::vector<std::vector<int>>& edges,
                             std::vector<int>& results);

py::array_t<int> edge_side_points(const py::array_t<int, py::array::c_style> &input_mesh_edges_arr,
                                  const py::array_t<int, py::array::c_style> &input_gemm_edges_arr);

int add(int a, int b);

void build_edge_topology_01(const py::array_t<double, py::array::c_style> &input_mesh_vertices_arr,
                            const py::array_t<int, py::array::c_style> &input_mesh_faces_arr,
                            py::list &edge_topology_results);

#endif//_MY_API_H_