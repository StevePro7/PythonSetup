#define _USE_MATH_DEFINES
#include <gtest/gtest.h>
#include "../src/math/matrix.h"

using math::Matrix3;
using math::Vector3;

TEST(Matrix3Test, Identity) {
    Matrix3 m;
    Vector3 v(1,2,3);
    auto r = m * v;

    EXPECT_DOUBLE_EQ(r.x, 1);
    EXPECT_DOUBLE_EQ(r.y, 2);
    EXPECT_DOUBLE_EQ(r.z, 3);
}

TEST(Matrix3Test, MatrixMultiply) {
    Matrix3 a = Matrix3::identity();
    Matrix3 b = Matrix3::identity();

    Matrix3 c = a * b;
    EXPECT_DOUBLE_EQ(c(0,0), 1);
    EXPECT_DOUBLE_EQ(c(1,1), 1);
    EXPECT_DOUBLE_EQ(c(2,2), 1);
}

TEST(Matrix3Test, Transpose) {
    Matrix3 m({1,2,3,
               4,5,6,
               7,8,9});

    auto t = m.transpose();

    EXPECT_DOUBLE_EQ(t(0,1), 4);
    EXPECT_DOUBLE_EQ(t(1,0), 2);
}

TEST(Matrix3Test, RotationZ90) {
    Matrix3 r = Matrix3::rotationZ(M_PI/2);
    Vector3 v(1,0,0);

    auto result = r * v;

    EXPECT_NEAR(result.x, 0.0, 1e-6);
    EXPECT_NEAR(result.y, 1.0, 1e-6);
}