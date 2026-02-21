#include <gtest/gtest.h>
#include "api/my_api.h"

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

// Test Default Constructor
TEST_F(APITest, DefaultConstructor)
{
    Guitar g;

    EXPECT_EQ(g.mManufacturerName, "");
    EXPECT_FLOAT_EQ(g.mPrice, 0.f);
    EXPECT_EQ(g.mNumStrings, 0);
}

// Test Full Constructor
TEST_F(APITest, FullConstructorInitializesAllFields)
{
    Guitar g("Fender", 999.99f, 6);

    EXPECT_EQ(g.mManufacturerName, "Fender");
    EXPECT_FLOAT_EQ(g.mPrice, 999.99f);
    EXPECT_EQ(g.mNumStrings, 6);
}

// Test Partial Constructor (No num_strings)
TEST_F(APITest, PartialConstructorInitializesCorrectly)
{
    Guitar g("Gibson", 1499.0f);

    EXPECT_EQ(g.mManufacturerName, "Gibson");
    EXPECT_FLOAT_EQ(g.mPrice, 1499.0f);
    EXPECT_EQ(g.mNumStrings, 0);  // important check
}

// Test SetManufacturer
TEST_F(APITest, SetManufacturerUpdatesValue)
{
    Guitar g;

    g.SetManufacturer("Ibanez");

    EXPECT_EQ(g.mManufacturerName, "Ibanez");
}

// Test SetPrice
TEST_F(APITest, SetPriceUpdatesValue)
{
    Guitar g;

    g.SetPrice(799.5f);

    EXPECT_FLOAT_EQ(g.mPrice, 799.5f);
}

// Test Updating Existing Object
TEST_F(APITest, SettersOverrideConstructorValues)
{
    Guitar g("Yamaha", 500.0f, 12);

    g.SetManufacturer("PRS");
    g.SetPrice(2500.0f);

    EXPECT_EQ(g.mManufacturerName, "PRS");
    EXPECT_FLOAT_EQ(g.mPrice, 2500.0f);
    EXPECT_EQ(g.mNumStrings, 12);  // unchanged
}

// Prevent negative price
TEST_F(APITest, PreventNegativePrice)
{
    Guitar g;
    EXPECT_THROW(g.SetPrice(-100.0f), std::invalid_argument);
}
