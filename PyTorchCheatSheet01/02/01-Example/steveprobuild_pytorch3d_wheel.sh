#!/usr/bin/env bash
set -euo pipefail

# -----------------------------
# Configurable environment
# -----------------------------
export PYTORCH3D_REF=v0.7.7
export WHEELHOUSE="$(pwd)/wheelhouse-cu121"

# Build a local PyTorch3D wheel compatible with the current Python + installed torch.
# Outputs wheels into ./wheelhouse

PYTORCH3D_REF_DEFAULT="main"
PYTORCH3D_REF="${PYTORCH3D_REF:-$PYTORCH3D_REF_DEFAULT}"

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
# Clone PyTorch3d
# -----------------------------
REPO_URL="https://github.com/facebookresearch/pytorch3d.git"

# Clone / update repo
if [[ ! -d $"WORKDIR/.git" ]]; then
  git clone --depth 1 --branch "$PYTORCH3D_REF" "$REPO_URL" "$WORKDIR"
else
  git -C "$WORKDIR" fetch --tags --force
  git -C "$WORKDIR" checkout -f "$PYTORCH3D_REF"
fi

# -----------------------------
# Install build prerequisites via UV
# -----------------------------
uv run pip install --upgrade --no-deps pip setuptools wheel
uv run pip install --upgrade --no-deps "numpy<=1.26.4"
uv run pip install --upgrade --no-deps "ninja" "cmake" "pybind11" "typing_extensions" "tqdm" "packaging<26"

# -----------------------------
# Patch project name for custom PyPI wheel
# -----------------------------
PROJECT_NAME="stevepropytorch3d"

# pyproject.toml
PYPROJECT="$WORKDIR/pyproject.toml"
if [ -f "$PYPROJECT" ]; then
    sed -i "s/^name = \".*\"/name = \"$PROJECT_NAME\"/" "$PYPROJECT"
fi

# setup.py fallback
SETUP="$WORKDIR/setup.py"
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

echo "Built wheels in $WHEELHOUSE"
ls -1 "$WHEELHOUSE" | sed 's/^/ - /'