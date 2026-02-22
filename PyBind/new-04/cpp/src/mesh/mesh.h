#pragma once
#include <vector>
#include "../math/vector.h"

namespace mesh {

struct Face {
    int v0, v1, v2;
};

class Mesh {
public:
    std::vector<math::Vector3> vertices;
    std::vector<Face> faces;

    void computeVertexNormals(std::vector<math::Vector3>& normals) const;
};

}