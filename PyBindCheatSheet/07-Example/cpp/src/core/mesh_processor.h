#pragma once

#include <string>
#include "../mesh/mesh.h"

namespace core {

class ILogger {
public:
    virtual ~ILogger() = default;
    virtual void log(const std::string& msg) = 0;
};

class MeshProcessor {
public:
    MeshProcessor(ILogger& logger);

    void smooth(mesh::Mesh& mesh);

private:
    ILogger& logger_;
};

}