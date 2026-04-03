## Example III
#### 05-May-2026

### Upload Custom Wheels
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

Copy custom wheels built from previous example
```sh
mkdir -p wheelhouse-cu121
cp -r ../01-Example/wheelhouse-cu121 .
```

Install local devpi client and server and twine to upload
```sh
uv pip install devpi-server
uv pip install devpi-client
uv pip install devpi-web
uv pip install twine
```

Launch Terminal | Initialize server and start
```sh
devpi-init
devpi-server --host 127.0.0.1 --port 3141
# Launch browser | Navigate http://localhost:3141
```

Launch Terminal | Connect client and login
```sh
devpi use http://localhost:3141
devpi login root --password=''
```

Create custom index and activate
```sh
devpi index -c cuda-wheels bases=root/pypi
devpi use root/cuda-wheels
```

Finally upload 2x custom wheel files locally
```sh
twine upload --repository-url http://localhost:3141/root/cuda-wheels/ wheelhouse-cu121/*
```
