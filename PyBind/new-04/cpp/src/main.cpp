#include <iostream>
#include "mesh/mesh.h"
#include "mesh/mesh_algorithms.h"

int main() {
    mesh::Mesh mesh;

    mesh.vertices.push_back({0,0,0});
    mesh.vertices.push_back({1,0,0});
    mesh.vertices.push_back({0,1,0});
    mesh.faces.push_back({0,1,2});

    mesh::laplacianSmooth(mesh, 1, 0.5);

    std::cout << "Mesh processed.\n";
    return 0;
}