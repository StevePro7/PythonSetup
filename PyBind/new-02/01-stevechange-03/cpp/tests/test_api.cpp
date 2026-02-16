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
TEST_F(APITest, AddZero)
{
    EXPECT_EQ(4, 4);
}
