#include "mesh.h"

namespace mesh {

void Mesh::computeVertexNormals(
    std::vector<math::Vector3>& normals) const
{
    normals.clear();
    normals.resize(vertices.size(), math::Vector3());

    // Accumulate face normals into vertices
    for (const auto& f : faces) {
        const auto& v0 = vertices[f.v0];
        const auto& v1 = vertices[f.v1];
        const auto& v2 = vertices[f.v2];

        math::Vector3 e1 = v1 - v0;
        math::Vector3 e2 = v2 - v0;

        math::Vector3 faceNormal =
            math::Vector3::cross(e1, e2);

        normals[f.v0] = normals[f.v0] + faceNormal;
        normals[f.v1] = normals[f.v1] + faceNormal;
        normals[f.v2] = normals[f.v2] + faceNormal;
    }

    // Normalize all normals
    for (auto& n : normals) {
        double len = n.norm();
        if (len > 1e-12)
            n = n * (1.0 / len);
    }
}

}