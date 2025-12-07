#include "hello.h"
#include <gtest/gtest.h>

TEST(HelloTest, Basic)
{
    EXPECT_EQ(greet("World"), "Hello, World?!");
}
