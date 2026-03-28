# app/container.py
from functools import lru_cache
from app.services.pointcloud_service import PointCloudService
from app.services.mesh_service import MeshService
from app.services.render_service import RenderService
from app.controllers.inference_controller import InferenceController
from app.utils.device import get_device


@lru_cache(maxsize=1)
def build_controller() -> InferenceController:
    device = get_device()

    pc_service = PointCloudService()
    mesh_service = MeshService(device)
    render_service = RenderService(device)

    controller = InferenceController(
        pc_service,
        mesh_service,
        render_service,
        device,
    )

    return controller
