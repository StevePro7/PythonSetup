# tests/test_mesh_service.py
import numpy as np
from app.services.mesh_service import MeshService


def test_to_pytorch3d():
    service = MeshService(device="cpu")

    verts = np.random.rand(10, 3)
    faces = np.random.randint(0, 10, (5, 3))

    mesh = service.to_pytorch3d(verts, faces)

    assert mesh.num_verts_per_mesh().item() == 10
