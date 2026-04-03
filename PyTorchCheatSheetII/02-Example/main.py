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

print("Hello PyTorch3d")

print("torch", torch.__version__)
print("pytorch3d", pytorch3d.__version__)
print("cuda", torch.version.cuda)
print("cuda", torch.cuda.is_available())

print("torch_geometric", torch_geometric.__version__)
print("torch_scatter", torch_scatter.__version__)
print("torch_sparse", torch_sparse.__version__)
print("torch_cluster", torch_cluster.__version__)
print("torch_spline_conv", torch_spline_conv.__version__)
print("torchsparse", torchsparse.__version__)
