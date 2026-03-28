# app/services/pointcloud_service.py
import open3d as o3d
import numpy as np


class PointCloudService:

    def to_open3d(self, points: np.ndarray):
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(points)
        pcd.estimate_normals()
        return pcd
