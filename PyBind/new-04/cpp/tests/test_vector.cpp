#include <gtest/gtest.h>
#include "../src/math/vector.h"

using math::Vector3;

TEST(Vector3Test, DefaultConstructor) {
    Vector3 v;
    EXPECT_DOUBLE_EQ(v.x, 0.0);
    EXPECT_DOUBLE_EQ(v.y, 0.0);
    EXPECT_DOUBLE_EQ(v.z, 0.0);
}

TEST(Vector3Test, Norm) {
    Vector3 v(3,0,4);
    EXPECT_DOUBLE_EQ(v.norm(), 5.0);
}

TEST(Vector3Test, Normalized) {
    Vector3 v(0,0,5);
    auto n = v.normalized();
    EXPECT_NEAR(n.norm(), 1.0, 1e-12);
}

TEST(Vector3Test, AdditionSubtraction) {
    Vector3 a(1,2,3);
    Vector3 b(4,5,6);

    auto c = a + b;
    EXPECT_DOUBLE_EQ(c.x, 5);
    EXPECT_DOUBLE_EQ(c.y, 7);
    EXPECT_DOUBLE_EQ(c.z, 9);

    auto d = b - a;
    EXPECT_DOUBLE_EQ(d.x, 3);
    EXPECT_DOUBLE_EQ(d.y, 3);
    EXPECT_DOUBLE_EQ(d.z, 3);
}

TEST(Vector3Test, ScalarMultiply) {
    Vector3 a(1,2,3);
    auto r = a * 2.0;
    EXPECT_DOUBLE_EQ(r.x, 2);
    EXPECT_DOUBLE_EQ(r.y, 4);
    EXPECT_DOUBLE_EQ(r.z, 6);
}

TEST(Vector3Test, DotProduct) {
    Vector3 a(1,0,0);
    Vector3 b(0,1,0);
    EXPECT_DOUBLE_EQ(Vector3::dot(a,b), 0.0);
}

TEST(Vector3Test, CrossProduct) {
    Vector3 a(1,0,0);
    Vector3 b(0,1,0);
    auto c = Vector3::cross(a,b);

    EXPECT_DOUBLE_EQ(c.x, 0);
    EXPECT_DOUBLE_EQ(c.y, 0);
    EXPECT_DOUBLE_EQ(c.z, 1);
}