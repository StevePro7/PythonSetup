# ----------------------------
# Base image: CUDA 12.1 (DEVEL for compilation)
# ----------------------------
FROM nvidia/cuda:12.1.1-cudnn8-devel-ubuntu22.04

# ----------------------------
# Environment variables
# ----------------------------
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    NVIDIA_VISIBLE_DEVICES=all \
    NVIDIA_DRIVER_CAPABILITIES=compute,utility \
    PATH="/opt/venv/bin:$PATH" \
    CUDA_HOME=/usr/local/cuda \
    FORCE_CUDA=1 \
    TORCH_CUDA_ARCH_LIST="8.6" \
    MAX_JOBS=8

# ----------------------------
# System dependencies
# ----------------------------
RUN apt-get update && apt-get install -y \
        python3.10 python3.10-venv python3.10-distutils python3-pip \
        git wget curl \
        build-essential cmake ninja-build \
        libgl1-mesa-glx libglib2.0-0 \
        libsm6 libxext6 libxrender-dev \
        libsparsehash-dev \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# ----------------------------
# Python virtual environment
# ----------------------------
RUN python3.10 -m venv /opt/venv
RUN pip install --upgrade pip setuptools wheel

# ----------------------------
# Core Python build dependencies
# ----------------------------
RUN pip install \
    numpy==1.26.4 \
    ninja \
    fvcore \
    iopath \
    tqdm

# ----------------------------
# Install PyTorch 2.2 (CUDA 12.1)
# ----------------------------
RUN pip install \
    torch==2.2.0+cu121 \
    torchvision==0.17.0 \
    torchaudio==2.2.0 \
    --index-url https://download.pytorch.org/whl/cu121

# ----------------------------
# Verify CUDA is visible at build time
# ----------------------------
RUN python -c "import torch; print('CUDA available:', torch.cuda.is_available()); print('CUDA version:', torch.version.cuda)"

# ----------------------------
# PyTorch Geometric compiled ops
# ----------------------------
RUN pip install \
    pyg-lib==0.4.0+pt22cu121 \
    torch-scatter==2.1.2+pt22cu121 \
    torch-sparse==0.6.18+pt22cu121 \
    torch-cluster==1.6.3+pt22cu121 \
    torch-spline-conv==1.2.2+pt22cu121 \
    -f https://data.pyg.org/whl/torch-2.2.0+cu121.html

# ----------------------------
# Install torch-geometric
# ----------------------------
RUN pip install torch-geometric==2.7.0

# ----------------------------
# Install torchsparse (CUDA build)
# ----------------------------
RUN pip install --no-build-isolation --verbose \
    git+https://github.com/mit-han-lab/torchsparse.git@v2.0.0

# ----------------------------
# Install PyTorch3D (FORCED CUDA BUILD)
# ----------------------------
RUN pip install --no-build-isolation --verbose \
    git+https://github.com/facebookresearch/pytorch3d.git@v0.7.7

# ----------------------------
# Validate PyTorch3D CUDA build
# ----------------------------
RUN python - <<EOF
import torch
from pytorch3d import _C
print("CUDA available (runtime):", torch.cuda.is_available())
print("PyTorch3D rasterizer loaded:", hasattr(_C, "rasterize_meshes"))
EOF

# ----------------------------
# Remaining Python dependencies
# ----------------------------
RUN pip install \
    "azureml-inference-server-http>=1.5.0" \
    "azureml-sdk>=1.48.0" \
    "azure-storage-blob>=12.27.1" \
    "hydra-core>=1.3.2" \
    "imageio>=2.37.2" \
    "lightning>=2.5.6" \
    "open3d>=0.19.0" \
    "opencv-python-headless<4.12.0" \
    "openpyxl>=3.1.5" \
    "pillow>=12.0.0" \
    "prettytable>=3.17.0" \
    "pyrender>=0.1.45" \
    "ray[tune]>=2.51.1" \
    "seaborn>=0.13.2" \
    "tensorboard>=2.20.0" \
    "transformers>=4.38,<4.45" \
    websockets

# ----------------------------
# App setup
# ----------------------------
WORKDIR /app
COPY . /app

# Add /app to PYTHONPATH so 'app' package imports work
ENV PYTHONPATH=/app:$PYTHONPATH

# ----------------------------
# Azure ML port
# ----------------------------
EXPOSE 5001

# ----------------------------
# Start Azure ML inference server
# ----------------------------
CMD ["azmlinfsrv", "--entry_script", "/app/app/scoring.py", "--port", "5001", "--worker_count", "1"]