## Example I
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

UV install dependencies
```sh
uv pip install twine
uv pip install numpy==1.26.4
uv pip install --index-url https://download.pytorch.org/whl/cu121 \
    "torch==2.2.0+cu121" "torchvision==0.17.0"  "torchaudio==2.2.0"
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

OUTPUT
```sh
stevepropytorch3d-0.7.7-cp310-cp310-linux_x86_64.whl
steveprotorchsparse-2.0.0b0-cp310-cp310-linux_x86_64.whl
```
