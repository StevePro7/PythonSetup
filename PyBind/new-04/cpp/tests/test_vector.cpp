#include <gtest/gtest.h>
#include "../src/math/vector.h"

TEST(VectorTest, Norm) {
    math::Vector3 v(3,0,4);
    EXPECT_DOUBLE_EQ(v.norm(), 5.0);
}