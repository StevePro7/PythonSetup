# app/services/render_service.py
import torch
from pytorch3d.renderer import (
    FoVPerspectiveCameras,
    RasterizationSettings,
    MeshRenderer,
    MeshRasterizer,
    SoftPhongShader,
    PointLights,
)


class RenderService:

    def __init__(self, device):
        self.device = device
        self.renderer = self._build_renderer()

    def _build_renderer(self):
        cameras = FoVPerspectiveCameras(device=self.device)

        raster_settings = RasterizationSettings(
            image_size=128,
            blur_radius=0.0,
            faces_per_pixel=1,
        )

        lights = PointLights(device=self.device, location=[[2.0, 2.0, -2.0]])

        return MeshRenderer(
            rasterizer=MeshRasterizer(
                cameras=cameras,
                raster_settings=raster_settings,
            ),
            shader=SoftPhongShader(
                device=self.device,
                cameras=cameras,
                lights=lights,
            ),
        )

    def render(self, mesh):
        images = self.renderer(mesh)
        img = images[0, ..., :3].detach().cpu().numpy()
        return img
