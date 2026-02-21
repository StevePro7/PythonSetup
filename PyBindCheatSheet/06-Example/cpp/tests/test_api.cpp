#include <gtest/gtest.h>
#include "api/my_api.h"
#include <string>

class APITest : public ::testing::Test
{
protected:
    void SetUp() override
    {
    }

    void TearDown() override
    {
    }
};

// Basic Construction + Write/Read
TEST_F(APITest, ConstructAndAccessInt)
{
    Container<int> c(5);

    c[0] = 10;
    c[1] = 20;
    c[2] = 30;
    c[3] = 40;
    c[4] = 50;

    EXPECT_EQ(c[0], 10);
    EXPECT_EQ(c[1], 20);
    EXPECT_EQ(c[2], 30);
    EXPECT_EQ(c[3], 40);
    EXPECT_EQ(c[4], 50);
}

// Test Default Initialization Behavior
TEST_F(APITest, OverwriteAllVAlues)
{
    Container<int> c(3);

    for (size_t i = 0; i < 3; ++i)
    {
        c[i] = static_cast<int>(i * 2);
    }

    EXPECT_EQ(c[0], 0);
    EXPECT_EQ(c[1], 2);
    EXPECT_EQ(c[2], 4);
}

// Test Const Access Operator
TEST_F(APITest, ConstAccess)
{
    Container<int> c(2);
    c[0] = 7;
    c[1] = 9;

    const Container<int>& const_ref = c;

    EXPECT_EQ(const_ref[0], 7);
    EXPECT_EQ(const_ref[1], 9);
}

// Test With Another Type (double)
TEST_F(APITest, WorksWithDouble)
{
    Container<double> c(3);

    c[0] = 1.5;
    c[1] = 2.5;
    c[2] = 3.5;

    EXPECT_DOUBLE_EQ(c[0], 1.5);
    EXPECT_DOUBLE_EQ(c[1], 2.5);
    EXPECT_DOUBLE_EQ(c[2], 3.5);
}

// Test With std::string (Non-POD Type)
TEST_F(APITest, WorksWithString)
{
    Container<std::string> c(2);

    c[0] = "hello";
    c[1] = "world";

    EXPECT_EQ(c[0], "hello");
    EXPECT_EQ(c[1], "world");
}

// Test out of range
TEST_F(APITest, ThrowsOnOutOfRange)
{
    Container<int> c(3);
    EXPECT_THROW(c[3], std::out_of_range);
}