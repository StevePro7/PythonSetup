// my_api.cpp
#include "my_api.h"






























void build_edge_topology(const py::array_t<int, py::array::c_style> &input_mesh_faces_arr,
                         const py::array_t<int, py::array::c_style> &input_mesh_edges_arr,
                         py::list &edge_topology_results)
{
    // build the local topology (edge connectivity) for each edge
    auto input_mesh_faces_arr_r = input_mesh_faces_arr.unchecked<2>();
    auto input_mesh_edges_arr_r = input_mesh_edges_arr.unchecked<2>();
    int edges_count = input_mesh_edges_arr_r.shape(0);

    // initialize four neighbor edges and sides info for each edge
    auto output_gemm_edges_arr = py::array_t<int, py::array::c_style>({edges_count, 4});
    auto output_gemm_edges_arr_r = output_gemm_edges_arr.mutable_unchecked<2>();
    auto output_sides_arr = py::array_t<int, py::array::c_style>({edges_count, 4});
    auto output_sides_arr_r = output_sides_arr.mutable_unchecked<2>();
    // the number of neighbor edges for each edge (also indicating the index of next neighbor edge to store)
    std::vector<int> edge_neighbors_count(edges_count, 0);
    // convert unidirectional edges to dictionary
    std::map<std::pair<int, int>, int> edge2key;
    std::vector<int> edge_vec(2, -1);
    std::pair<int, int> edge(-1, -1);
    // initialization
    for (int i=0; i < edges_count; ++i)
    {
        for (int j=0; j < 4; ++j)
        {
            output_gemm_edges_arr_r(i, j) = -1;
            output_sides_arr_r(i, j) = -1;
        }

        edge_vec[0] = input_mesh_edges_arr_r(i, 0);
        edge_vec[1] = input_mesh_edges_arr_r(i, 1);
        if (edge_vec[0] > edge_vec[1])
            std::swap(edge_vec[0], edge_vec[1]);
        edge.first = edge_vec[0];
        edge.second = edge_vec[1];
        edge2key[edge] = i;
    }

    // check each edge of each face
    int faces_count = input_mesh_faces_arr_r.shape(0);
    std::pair<int, int> cur_edge(-1, -1);
    int edge_key = -1;
    std::vector<int> face_edge_keys(3, -1);
    for (int face_id = 0; face_id < faces_count; ++face_id)
    {
        // get three undirectional edges for this face
        for (size_t i = 0; i < 3; ++i)
        {
            edge_vec[0] = input_mesh_faces_arr_r(face_id, i);
            edge_vec[1] = input_mesh_faces_arr_r(face_id, (i + 1) % 3);
            if (edge_vec[0] > edge_vec[1])
                std::swap(edge_vec[0], edge_vec[1]);

            cur_edge.first = edge_vec[0];
            cur_edge.second = edge_vec[1];
            face_edge_keys[i] = edge2key[cur_edge];
        }

        // update the info of the neighbor edges info for each edge of this face
        for (size_t idx = 0; idx < 3; ++idx)
        {
            edge_key = face_edge_keys[idx];
            // store two neighbor edges (indices)
            output_gemm_edges_arr_r(edge_key, edge_neighbors_count[edge_key]) = face_edge_keys[(idx + 1) % 3];
            output_gemm_edges_arr_r(edge_key, edge_neighbors_count[edge_key] + 1) = face_edge_keys[(idx + 2) % 3];
            // update the current total number of neighbor edges
            edge_neighbors_count[edge_key] += 2;
        }

        // update the sides info for each edge
        for (size_t idx = 0; idx < 3; ++idx)
        {
            edge_key = face_edge_keys[idx];
            // store the indices of current edge in its two neighbor edge's edge_neighbor_edges
            output_sides_arr_r(edge_key, edge_neighbors_count[edge_key] - 2) =
                    edge_neighbors_count[face_edge_keys[(idx + 1) % 3]] - 1;
            output_sides_arr_r(edge_key, edge_neighbors_count[edge_key] - 1) =
                    edge_neighbors_count[face_edge_keys[(idx + 2) % 3]] - 2;
        }
    }

    // outputs
    edge_topology_results.append(output_gemm_edges_arr);
    edge_topology_results.append(output_sides_arr);
}

// C++ version for unit testing
void build_edge_topology_cpp(const std::vector<std::vector<int>>& faces,
                             const std::vector<std::vector<int>>& edges,
                             std::vector<int>& results)
{
    // TODO: Implement edge topology logic
}


py::array_t<int> edge_side_points(const py::array_t<int, py::array::c_style> &input_mesh_edges_arr,
                                  const py::array_t<int, py::array::c_style> &input_gemm_edges_arr)
{
    auto output_side_points_arr = py::array_t<int>();
    return output_side_points_arr;
}


int add(int a, int b)
{
    return a + b;
}


void build_edge_topology_01(const py::array_t<double, py::array::c_style> &input_mesh_vertices_arr,
                         const py::array_t<int, py::array::c_style> &input_mesh_faces_arr,
                         py::list &edge_topology_results)
{
}