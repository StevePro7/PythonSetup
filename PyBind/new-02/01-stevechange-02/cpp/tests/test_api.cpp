#include <gtest/gtest.h>
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <vector>
#include "api/my_api.h"

namespace py = pybind11;

class APITest : public ::testing::Test
{
protected:
    void SetUp() override
    {
        // Setup before each test
    }

    void TearDown() override
    {
        // Cleanup after each test
    }
};

//TEST_F(APITest, StevePro)
//{
//    // Create faces as 2D vector
//    std::vector<std::vector<int>> faces = {
//        {0, 1, 2},
//        {0, 3, 2},
//        {0, 5, 1},
//        {0, 4, 5}
//    };
//
//    // Create edges (empty for now)
//    std::vector<std::vector<int>> edges = {};
//
//    // Create results vector
//    std::vector<int> results;
//
//    // Call C++ version (no pybind11 types needed)
//    build_edge_topology_cpp(faces, edges, results);
//
//    EXPECT_EQ(5, 7);
//}

TEST_F(APITest, AddZero)
{
    EXPECT_EQ(4, 4);
}
