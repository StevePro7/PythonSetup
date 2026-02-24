#ifndef _MESH_MESH_ALGORITHMS_H_
#define _MESH_MESH_ALGORITHMS_H_

#include "mesh.h"

namespace mesh 
{
	void laplacianSmooth(Mesh& mesh, int iterations, double lambda);
}

#endif//_MESH_MESH_ALGORITHMS_H_