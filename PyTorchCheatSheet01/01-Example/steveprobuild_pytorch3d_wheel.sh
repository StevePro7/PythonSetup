#!/usr/bin/env bash
set -euo pipefail

export PYTORCH3D_REF=v0.7.7
export TORCHSPARSE_REF=master
export TORCH_SPEC="torch==2.2.0+cu121"
export TORCH_INDEX_URL="https://download.pytorch.org/whl/cu121"
export WHEELHOUSE="/home/stevepro/GitHub/StevePro7/FelixTesting/StevePro/PyPi/scripts01/wheelhouse-cu121"

# Build a local PyTorch3D wheel compatible with the current Python + installed torch.
# Outputs wheels into ./wheelhouse

PYTORCH3D_REF_DEFAULT="main"
PYTORCH3D_REF="${PYTORCH3D_REF:-$PYTORCH3D_REF_DEFAULT}"

REPO_URL="https://github.com/facebookresearch/pytorch3d.git"
WORKDIR="${WORKDIR:-$(pwd)/.build/pytorch3d}"
WHEELHOUSE="${WHEELHOUSE:-$(pwd)/wheelhouse}"

export WORKDIR
rm -rf "$WORKDIR"
mkdir -p "$WORKDIR" "$WHEELHOUSE"

if ! command -v git >/dev/null 2>&1; then
  echo "git is required" >&2
  exit 1
fi

python - <<'PY'
import sys
print(f"Python: {sys.version}")
PY

python - <<'PY'
import torch
print(f"torch: {torch.__version__}")
print(f"cuda available: {torch.cuda.is_available()}")
print(f"cxx11abi: {bool(getattr(torch._C, '_GLIBCXX_USE_CXX11_ABI', True))}")
PY

export TORCH_CUDA_ARCH_LIST="8.6"
TORCH_CXX_ABI="$(python - <<'PY'
import torch
print(int(bool(torch._C._GLIBCXX_USE_CXX11_ABI)))
PY
)"
export TORCH_CXX_ABI
export CXXFLAGS="${CXXFLAGS:-} -D_GLIBCXX_USE_CXX11_ABI=${TORCH_CXX_ABI}"

if ! python -m pip --version </dev/null 2>&1; then
  python -m ensurepip --upgrade
fi

# Clone / update repo
if [[ ! -d $"WORKDIR/.git" ]]; then
  git clone --depth 1 --branch "$PYTORCH3D_REF" "$REPO_URL" "$WORKDIR"
else
  git -C "$WORKDIR" fetch --tags --force
  git -C "$WORKDIR" checkout -f "$PYTORCH3D_REF"
fi

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

# Build pre-requisites
python -m pip install --upgrade --no-deps pip setuptools wheel
python -m pip install --upgrade --no-deps "ninja" "cmake" "pybind11" "typing_extensions" "packaging<26"

# Build wheel
pushd "$WORKDIR" >/dev/null
python -m pip wheel . -w "$WHEELHOUSE" --no-deps --no-build-isolation
popd "$WORKDIR" >/dev/null

echo "Built wheels in $WHEELHOUSE"
ls -1 "$WHEELHOUSE" | sed 's/^/ - /'