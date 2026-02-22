#include <gtest/gtest.h>
#include <gmock/gmock.h>

#include "mock_logger.h"
#include "../src/core/mesh_processor.h"

using ::testing::Exactly;

TEST(MeshProcessorTest, LogsCorrectly) {
    MockLogger logger;
    mesh::Mesh m;

    EXPECT_CALL(logger, log("Starting smoothing")).Times(Exactly(1));
    EXPECT_CALL(logger, log("Finished smoothing")).Times(Exactly(1));

    core::MeshProcessor proc(logger);
    proc.smooth(m);
}