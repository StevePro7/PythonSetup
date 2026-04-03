## Example I
#### 05-May-2026

### Build Custom Wheels
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

UV install dependencies
```sh
uv pip install twine
uv pip install numpy==1.26.4
uv pip install --index-url https://download.pytorch.org/whl/cu121 \
    "torch==2.2.0+cu121" "torchvision==0.17.0"  "torchaudio==2.2.0"
```

Create directory to house custom wheels
```sh
mkdir -p wheelhouse-cu121
```

Write shell scripts to build custom wheels
```sh
chmod +x steveprobuild_pytorch3d_wheel.sh
chmod +x steveprobuild_torchsparse_wheel.sh
```

Execute shell scripts to build custom wheels
```sh
bash steveprobuild_pytorch3d_wheel.sh
bash steveprobuild_torchsparse_wheel.sh
```

OUTPUT - in wheelhouse-121
```sh
stevepropytorch3d-0.7.7-cp310-cp310-linux_x86_64.whl
steveprotorchsparse-2.0.0b0-cp310-cp310-linux_x86_64.whl
```
