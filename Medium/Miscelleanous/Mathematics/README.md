Math for ML: The Essential Foundations for Understanding Deep Learning
03-Dec-2025

https://medium.com/@ryassminh/math-for-ml-the-essential-foundations-for-understanding-deep-learning-950e37daf0f3

New project
Base conda
~/anaconda

import torch
pip install --upgrade pip setuptools wheel

ERROR

lspci | grep -i nvidia
01:00.0 VGA compatible controller: NVIDIA Corporation Device 24dc (rev a1)
01:00.1 Audio device: NVIDIA Corporation Device 228b (rev a1)


nvidia-smi
NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver. Make sure that the latest NVIDIA driver is installed and running.



Install GPU
ubuntu-drivers devices
sudo apt update
sudo apt install nvidia-driver-570

sudo reboot
nvidia-smi

Expected result:
A table showing:
Driver Version: 570.xx
CUDA Version: 12.x
Your GPU name
If that appears → GPU is now working.