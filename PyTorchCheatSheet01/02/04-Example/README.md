## Example II
#### 05-May-2026

### Use Custom Wheels
Launch PyCharm | New Project

| KEY | VALUE            |
| :---   |:-----------------|
| Location: | ~/HelloPyTorch3dWheels |
| Interpreter type: | uv               |
| Python version: | 3.10             |
| Path to uv: | ~/.local/bin/uv  |

Create

Setup environment - if not auto created by PyCharm
```sh
uv venv --python 3.10
source .venv/bin/activate       # OR .\.venv\Scripts\activate
which python
`which python` --version	# Python 3.10.19
```

Install local devpi client and server and twine to upload
```sh
uv pip install devpi-server
uv pip install devpi-web
```

Launch Terminal | Initialize server and start
```sh
devpi-server --host 127.0.0.1 --port 3141
# Launch browser | Navigate http://localhost:3141
```

UV update pyproject.toml
```sh
export MAX_JOBS=1
export NVCC_THREADS=1
uv lock
uv sync
```

Write code for main program
```sh
main.py
```

Finally hit F5 to run Python code
```sh
uv run main.py
```

OUTPUT
```sh
Hello PyTorch3d
torch 2.2.0+cu121
pytorch3d 0.7.7
cuda 12.1
cuda True
torch_geometric 2.7.0
torch_scatter 2.1.2+pt22cu121
torch_sparse 0.6.18+pt22cu121
torch_cluster 1.6.3+pt22cu121
torch_spline_conv 1.2.2+pt22cu121
torchsparse 2.0.0b
```
