#!/usr/bin/env bash
set -euo pipefail

# -----------------------------
# Configurable environment
# -----------------------------
export TORCHSPARSE_REF="v2.0.0"
export TORCH_SPEC="torch==2.2.0+cu121"
export TORCH_INDEX_URL="https://download.pytorch.org/whl/cu121"
export WHEELHOUSE="$(pwd)/wheelhouse-cu121"

export CXXFLAGS="-O3 -DNDEBUG"
export NVCC_FLAGS="-O3"
export MAX_JOBS=1
export TORCH_NVCC_FLAGS="-Xfatbin -compress-all"

export TORCH_CUDA_ARCH_LIST="8.6"

# -----------------------------
# Directories
# -----------------------------
export WORKDIR="$(pwd)/.build/torchsparse"
mkdir -p "$WORKDIR" "$WHEELHOUSE"
rm -rf "$WORKDIR"

# -----------------------------
# Check tools
# -----------------------------
if ! command -v git >/dev/null 2>&1; then
  echo "git is required" >&2
  exit 1
fi
if ! command -v nvcc >/dev/null 2>&1; then
  echo "nvcc not found on PATH; CUDA toolkit is required" >&2
  exit 1
fi
if ! command -v auditwheel >/dev/null 2>&1; then
  echo "auditwheel not found, installing..."
  uv run pip install --upgrade --no-deps auditwheel
fi

# -----------------------------
# Python / Torch info
# -----------------------------
uv run python - <<'PY'
import sys, torch
print(f"Python: {sys.version}")
print(f"torch: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA version: {torch.version.cuda}")
PY

# Ensure correct C++ ABI
export TORCH_CXX_ABI="$(uv run python - <<'PY'
import torch
print(int(bool(torch._C._GLIBCXX_USE_CXX11_ABI)))
PY
)"
export CXXFLAGS="${CXXFLAGS} -D_GLIBCXX_USE_CXX11_ABI=${TORCH_CXX_ABI}"

# -----------------------------
# Clone TorchSparse
# -----------------------------
REPO_URL="https://github.com/mit-han-lab/torchsparse.git"

git clone --depth 1 --branch "$TORCHSPARSE_REF" "$REPO_URL" "$WORKDIR" || {
    git -C "$WORKDIR" fetch --tags --force
    git -C "$WORKDIR" checkout -f "$TORCHSPARSE_REF"
}

# -----------------------------
# Patch for scalar_type()
# -----------------------------
uv run python - <<'PY'
import os
from pathlib import Path

workdir = Path(os.environ["WORKDIR"]).resolve()

replacements = {
    "inputs.type()": "inputs.scalar_type()",
    "top_grad.type()": "top_grad.scalar_type()",
    "feat.type()": "feat.scalar_type()",
    "in_feat.type()": "in_feat.scalar_type()",
}

targets = [
    workdir / "torchsparse/backend/voxelize/voxelize_cuda.cu",
    workdir / "torchsparse/backend/devoxelize/devoxelize_cuda.cu",
    workdir / "torchsparse/backend/convolution/convolution_cuda.cu"
]

for path in targets:
    if not path.exists():
        raise SystemExit(f"Expected file not found: {path}")
    text = path.read_text(encoding="utf-8")
    updated = text
    for old, new in replacements.items():
        updated = updated.replace(old, new)
    if updated != text:
        path.write_text(updated, encoding="utf-8")
PY

# -----------------------------
# Install build prerequisites via UV
# -----------------------------
uv run pip install --upgrade --no-deps pip setuptools wheel
uv run pip install --upgrade --no-deps "numpy<=1.26.4"
uv run pip install --upgrade --no-deps "ninja" "cmake" "pybind11" "typing_extensions" "tqdm" "packaging<26"

# -----------------------------
# Patch project name to steveprotorchsparse
# -----------------------------
PROJECT_NAME="steveprotorchsparse"
PYPROJECT="$WORKDIR/pyproject.toml"
SETUP="$WORKDIR/setup.py"

if [ -f "$PYPROJECT" ]; then
    sed -i "s/^name = \".*\"/name = \"$PROJECT_NAME\"/" "$PYPROJECT"
fi

if [ -f "$SETUP" ]; then
    sed -i "s/name=.*,/name=\"$PROJECT_NAME\",/" "$SETUP"
fi
echo "Patched project name to $PROJECT_NAME"

# -----------------------------
# Build wheel
# -----------------------------
pushd "$WORKDIR" >/dev/null
uv run python -m pip wheel . -w "$WHEELHOUSE" --no-deps --no-build-isolation
popd >/dev/null

# -----------------------------
# Repair with auditwheel (manylinux)
# -----------------------------
for whl in "$WHEELHOUSE"/${PROJECT_NAME}-*.whl; do
    uv run auditwheel repair "$whl" -w "$WHEELHOUSE"
done

echo "Built manylinux wheels in $WHEELHOUSE:"
ls -1 "$WHEELHOUSE" | sed 's/^/ - /'