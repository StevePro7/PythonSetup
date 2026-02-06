#include <gtest/gtest.h>
#include "api/my_api.h"

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

TEST_F(APITest, AddPositiveNumbers)
{
    EXPECT_EQ(add(2, 3), 5);
}

TEST_F(APITest, AddNegativeNumbers)
{
    EXPECT_EQ(add(-2, -3), -5);
}

TEST_F(APITest, AddMixedNumbers)
{
    EXPECT_EQ(add(5, -3), 2);
    EXPECT_EQ(add(-5, 3), -2);
}

TEST_F(APITest, AddZero)
{
    EXPECT_EQ(add(0, 5), 5);
    EXPECT_EQ(add(5, 0), 5);
    EXPECT_EQ(add(0, 0), 0);
}
