# tests/test_controller.py
import numpy as np
from unittest.mock import Mock
from app.controllers.inference_controller import InferenceController
from app.models.dto import InferenceRequest


def test_controller_happy_path():
    pc_service = Mock()
    mesh_service = Mock()
    render_service = Mock()

    pc_service.to_open3d.return_value = "pcd"
    mesh_service.reconstruct.return_value = (np.zeros((10, 3)), np.zeros((5, 3)))
    mesh_service.to_pytorch3d.return_value = "mesh"
    render_service.render.return_value = np.ones((128, 128, 3))

    controller = InferenceController(
        pc_service,
        mesh_service,
        render_service,
        device="cpu"
    )

    request = InferenceRequest(points=np.random.rand(10, 3))

    response = controller.handle(request)

    assert response.num_vertices == 10
    assert response.num_faces == 5