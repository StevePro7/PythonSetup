#include "mesh_algorithms.h"

namespace mesh 
{
    void laplacianSmooth(Mesh& mesh, int iterations, double lambda)
    {
        for (int iter = 0; iter < iterations; ++iter)
        {
            std::vector<math::Vector3> newVerts = mesh.vertices;

            // If no faces then smooth by averaging each vertex with all others
            if (mesh.faces.empty())
            {
                math::Vector3 totalSum;
                int totalCount = static_cast<int>(mesh.vertices.size());
                for (const auto& v : mesh.vertices)
                {
                    totalSum = totalSum + v;
                }
                for (size_t i = 0; i < mesh.vertices.size(); ++i)
                {
                    newVerts[i] = mesh.vertices[i] * (1 - lambda)
                                + (totalSum * (1.0 / totalCount)) * lambda;
                }
            }
            else
            {
                for (size_t i = 0; i < mesh.vertices.size(); ++i)
                {
                    math::Vector3 sum;
                    int count = 0;

                    for (const auto& f : mesh.faces)
                    {
                        if (f.v0 == i || f.v1 == i || f.v2 == i)
                        {
                            sum = sum + mesh.vertices[f.v0]
                                  + mesh.vertices[f.v1]
                                  + mesh.vertices[f.v2];
                            count += 3;
                        }
                    }

                    if (count > 0)
                    {
                        newVerts[i] = mesh.vertices[i] * (1 - lambda)
                                      + (sum * (1.0 / count)) * lambda;
                    }
                }
            }

            mesh.vertices = newVerts;
        }
    }

}