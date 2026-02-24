#ifndef _MESH_MESH_H_
#define _MESH_MESH_H_

#include <vector>
#include "../math/vector.h"

namespace mesh
{
    struct Face
    {
        int v0, v1, v2;
    };

    class Mesh
    {
    public:
        std::vector<math::Vector3> vertices;
        std::vector<Face> faces;

        void computeVertexNormals(std::vector<math::Vector3>& normals) const;
    };

}

#endif//_MESH_MESH_H_