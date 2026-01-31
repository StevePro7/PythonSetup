#include <gtest/gtest.h>
#include "core.h"

TEST(CoreTest, ProcessWorks)
{
Processor p(3);

EXPECT_EQ(p.process(5), 15);
}