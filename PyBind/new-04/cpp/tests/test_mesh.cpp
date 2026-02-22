#include <gtest/gtest.h>
#include "mock_logger.h"
#include "../src/core/mesh_processor.h"

TEST(MeshProcessorTest, LogsDuringSmoothing) {
    MockLogger logger;
    mesh::Mesh mesh;

    EXPECT_CALL(logger, log("Starting smoothing")).Times(1);
    EXPECT_CALL(logger, log("Finished smoothing")).Times(1);

    core::MeshProcessor proc(logger);
    proc.smooth(mesh);
}