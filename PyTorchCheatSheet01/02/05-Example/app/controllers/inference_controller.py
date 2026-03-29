# app/controllers/inference_controller.py
from app.models.dto import InferenceResponse

class InferenceController:

    def __init__(self, pc_service, mesh_service, render_service, device):
        self.pc_service = pc_service
        self.mesh_service = mesh_service
        self.render_service = render_service
        self.device = device

    def handle(self, request):
        pcd = self.pc_service.to_open3d(request.points)

        verts, faces = self.mesh_service.reconstruct(pcd)

        mesh = self.mesh_service.to_pytorch3d(verts, faces)

        img = self.render_service.render(mesh)

        return InferenceResponse(
            num_vertices=len(verts),
            num_faces=len(faces),
            mean_pixel=float(img.mean()),
            image_shape=img.shape,
            device=str(self.device),
        )
