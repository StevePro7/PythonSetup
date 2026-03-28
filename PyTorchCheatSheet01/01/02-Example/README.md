## Example II
#### 01-Apr-2026

### Hello PyTorch3d
Launch PyCharm | New Project

| KEY | VALUE            |
| :---   |:-----------------|
| Location: | ~/HelloPyTorch3d |
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

UV update pyproject.toml
```sh
uv lock
uv sync
```

Create app directory and move main to app/scoring.py
```sh
app/scoring.py
```

Configure Azure ML environment
```sh
which azmlinfsrv
~/.venv/bin/azmlinfsrv
```

Finally hit F5 to run Python code
```sh
~/.venv/bin/azmlinfsrv --entry app/scoring.py
```

Submit POST request
```sh
curl --location --request POST 'http://localhost:5001/score' \
	--header 'Content-Type: application/json' \
	--data-raw '{}'
```

OUTPUT
```sh
{
    "message": "Hello PyTorch3d",
    "torch_version": "2.2.0+cu121",
    "pytorch3d_version": "0.7.7",
    "cuda_version": "12.1",
    "cuda_available": true,
    "torch_geometric_version": "2.7.0",
    "torch_scatter_version": "2.1.2+pt22cu121",
    "torch_sparse_version": "0.6.18+pt22cu121",
    "torch_cluster_version": "1.6.3+pt22cu121",
    "torch_spline_conv_version": "1.2.2+pt22cu121",
    "torchsparse_version": "2.0.0b"
}
```

Cleanup - as necessary
```sh
sudo fuser -k 5001/tcp    # Linux
lsof                 TODO # MacOS
```