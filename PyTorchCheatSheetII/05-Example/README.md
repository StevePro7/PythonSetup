## Example V
#### 05-May-2026

### Containerize AzureML
Launch PyCharm | New Project

| KEY | VALUE            |
| :---   |:-----------------|
| Location: | ~/HelloAzureML |
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
export MAX_JOBS=1
export NVCC_THREADS=1
uv lock
uv sync
```

Create app and tests directories | Enter all code for app/scoring.py
```sh
app/scoring.py
```

Complete all app and tests code | Test all code using pytest
```sh
pytest
```

Create Dockerfile | Build image + Run container

```sh
docker build -t azml-gpu-local:latest .
docker run --gpus all -p 5001:5001 azml-gpu-local:latest
```

Submit POST request
```sh
curl --location --request POST 'http://localhost:5001/score' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "points": [
    [0.0, 0.0, 1.0],
    [0.1, 0.0, 0.99],
    [-0.1, 0.0, 0.99],
    [0.0, 0.1, 0.99],
    [0.0, -0.1, 0.99],
    [0.7, 0.7, 0.0],
    [-0.7, 0.7, 0.0],
    [0.7, -0.7, 0.0],
    [-0.7, -0.7, 0.0],
    [0.0, 0.0, -1.0]
  ]
}'
```

OUTPUT
```sh
{
    "num_vertices": 1524, 
    "num_faces": 2892, 
    "mean_pixel": 0.9926620125770569,
    "image_shape": [
		128, 
		128, 
		3
	], 
    "device": "cuda:0"
}
```

Cleanup - as necessary
```sh
docker stop $(docker ps -q)
docker rm -f $(docker ps -q)
```