#include <gtest/gtest.h>
#include "../src/mesh/mesh.h"

using mesh::Mesh;
using mesh::Face;
using math::Vector3;

TEST(MeshTest, ComputeVertexNormalsSingleTriangle) {
    Mesh m;

    m.vertices = {
        {0,0,0},
        {1,0,0},
        {0,1,0}
    };

    m.faces.push_back({0,1,2});

    std::vector<Vector3> normals;
    m.computeVertexNormals(normals);

    ASSERT_EQ(normals.size(), 3);

    for (const auto& n : normals) {
        EXPECT_NEAR(n.x, 0.0, 1e-6);
        EXPECT_NEAR(n.y, 0.0, 1e-6);
        EXPECT_NEAR(n.z, 1.0, 1e-6);
    }
}

TEST(MeshTest, EmptyMeshNormals) {
    Mesh m;
    std::vector<Vector3> normals;
    m.computeVertexNormals(normals);

    EXPECT_TRUE(normals.empty());
}