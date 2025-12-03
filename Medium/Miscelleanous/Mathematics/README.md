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


ACTUAL
could not reboot!

Reboot
Advanced options for Ubuntu
kernel 6.0.9 (recovery mode)

FIX
root
sudo apt remove --purge nvidia-driver-570
sudo apt autoremove

sudo update-initramfs -u
error
sudo apt install initramfs-tools
sudo update-initramfs -u
error

sudo reboot
NOW all good

sudo apt update
sudo apt upgrade

sudo add-apt-repository ppa:graphics-drivers/ppa


Driver 580 is intended for newer Ubuntu releases such as 22.04 or 24.04.
Using it on 20.04 can cause:
boot failures
black screens
broken DKMS module builds


Option 1 (best stability):
sudo apt install nvidia-driver-535

nvidia-smi
NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver. Make sure that the latest NVIDIA driver is installed and running.


update-initramfs

boot failure
common pain point with Alienware laptops, dual boot, and NVIDIA drivers on Linux.



The mainline kernel 6.0.19 is the reason DKMS cannot build the NVIDIA module. Either install the headers manually for that kernel, or switch to an Ubuntu-supported kernel — only then will NVIDIA 535 work without breaking boot.

sudo apt install linux-image-generic linux-headers-generic



New approach - downgrade to 5.17.0-19 kernel that is compatible with nvidia-535

sudo apt install linux-headers-5.15.0-97-generic
dpkg -l | grep 5.15.0-97
ls /usr/src | grep 5.15

sudo update-grub


AFTER
sudo apt install dkms build-essential
sudo apt install nvidia-driver-535

nvidia-smi
