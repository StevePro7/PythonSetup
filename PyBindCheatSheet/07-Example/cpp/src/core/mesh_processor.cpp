#include "mesh_processor.h"
#include "../mesh/mesh_algorithms.h"

namespace core
{
    MeshProcessor::MeshProcessor(ILogger& logger)
        : logger_(logger)
        {}

    void MeshProcessor::smooth(mesh::Mesh& mesh)
    {
        logger_.log("Starting smoothing");
        mesh::laplacianSmooth(mesh, 1, 0.5);
        logger_.log("Finished smoothing");
    }

}