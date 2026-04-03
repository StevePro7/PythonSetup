# tests/test_pointcloud_service.py
import numpy as np
from app.services.pointcloud_service import PointCloudService


def test_to_open3d_creates_pointcloud():
    service = PointCloudService()

    points = np.random.rand(100, 3).astype(np.float32)

    pcd = service.to_open3d(points)

    # Validate type via duck-typing (avoid strict Open3D import dependency)
    assert hasattr(pcd, "points")

    pts = np.asarray(pcd.points)
    assert pts.shape == (100, 3)


def test_to_open3d_estimates_normals():
    service = PointCloudService()

    points = np.random.rand(50, 3).astype(np.float32)

    pcd = service.to_open3d(points)

    normals = np.asarray(pcd.normals)

    # Normals should exist and match size
    assert normals.shape == (50, 3)

    # Normals shouldn't be all zeros
    assert not np.allclose(normals, 0)
