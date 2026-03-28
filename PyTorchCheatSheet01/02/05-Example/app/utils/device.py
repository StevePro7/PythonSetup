# app/utils/device.py
import torch
import torch._C


def get_device():
    cuda: torch._C.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    return cuda
