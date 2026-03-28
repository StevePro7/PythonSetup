# Core & Utilities
import numpy as np
import packaging
import imageio
import openpyxl

# PyTorch Ecosystem
import torch
import torch_geometric
import torch_scatter
import torch_sparse
import torch_cluster
import torch_spline_conv
import pyg_lib

# 3D / Graphics
import pytorch3d
import torchsparse
import open3d as o3d
import cv2
import pyrender

# Training / Experimentation
import lightning as L
import tensorboard

# NLP / Transformers
import transformers

# Optional “Realistic Imports” Snippet
from pytorch3d.structures import Meshes
from pytorch3d.renderer import MeshRenderer

from torch_geometric.data import Data
from torch.utils.tensorboard import SummaryWriter

import http
import json
from azureml.contrib.services.aml_response import AMLResponse


def init() -> None:
    pass


def run(raw_data) -> AMLResponse:
    results: dict = {}
    results["message"] = "Hello PyTorch3d"

    results["torch_version"] = torch.__version__
    results["pytorch3d_version"] = pytorch3d.__version__
    results["cuda_version"] = torch.version.cuda
    results["cuda_available"] = torch.cuda.is_available()

    results["torch_geometric_version"] = torch_geometric.__version__
    results["torch_scatter_version"] = torch_scatter.__version__
    results["torch_sparse_version"] = torch_sparse.__version__
    results["torch_cluster_version"] = torch_cluster.__version__
    results["torch_spline_conv_version"] = torch_spline_conv.__version__
    results["torchsparse_version"] = torchsparse.__version__

    data = json.dumps(results)
    return AMLResponse(message=data, status_code=http.HTTPStatus.OK)
