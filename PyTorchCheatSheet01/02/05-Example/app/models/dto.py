# app/models/dto.py
from dataclasses import dataclass
import numpy as np


@dataclass
class InferenceRequest:
    points: np.ndarray


@dataclass
class InferenceResponse:
    num_vertices: int
    num_faces: int
    mean_pixel: float
    image_shape: tuple
    device: str
