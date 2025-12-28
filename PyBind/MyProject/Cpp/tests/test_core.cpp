#include "core.h"
#include <gtest/gtest.h>

TEST(HelloTest, Basic)
{
EXPECT_EQ(hello(), 8);
}
