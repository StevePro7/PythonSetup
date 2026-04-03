# app/services/mesh_service.py
import numpy as np
import open3d as o3d
import torch
from pytorch3d.structures import Meshes
from pytorch3d.renderer.mesh.textures import TexturesVertex


class MeshService:

    def __init__(self, device):
        self.device = device

    def reconstruct(self, pcd):
        mesh, _ = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=6)
        verts = np.asarray(mesh.vertices)
        faces = np.asarray(mesh.triangles)
        return verts, faces

    def to_pytorch3d(self, verts, faces):
        verts = torch.tensor(verts, dtype=torch.float32, device=self.device).unsqueeze(0)
        faces = torch.tensor(faces, dtype=torch.int64, device=self.device).unsqueeze(0)

        textures = TexturesVertex(verts_features=torch.ones_like(verts))
        return Meshes(verts=verts, faces=faces, textures=textures)
