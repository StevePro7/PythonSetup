#pragma once
#include "mesh.h"

namespace mesh 
{
	void laplacianSmooth(Mesh& mesh, int iterations, double lambda);
}