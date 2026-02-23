#include <gtest/gtest.h>
#include "../src/mesh/mesh_algorithms.h"

using mesh::Mesh;
using mesh::Face;
using math::Vector3;

TEST(MeshAlgorithmsTest, LaplacianSmoothChangesVertices) {
    Mesh m;

    m.vertices = {
        {0,0,0},
        {1,0,0},
        {0,1,0}
    };

    m.faces.push_back({0,1,2});

    auto original = m.vertices[0];

    mesh::laplacianSmooth(m, 1, 0.5);

    EXPECT_NE(m.vertices[0].x, original.x);
}

TEST(MeshAlgorithmsTest, ZeroIterationsDoesNothing) {
    Mesh m;

    m.vertices = {{0,0,0}};
    auto original = m.vertices[0];

    mesh::laplacianSmooth(m, 0, 0.5);

    EXPECT_DOUBLE_EQ(m.vertices[0].x, original.x);
}