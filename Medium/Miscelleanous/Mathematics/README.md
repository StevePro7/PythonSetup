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

sudo nano /etc/default/grub
GRUB_DEFAULT="Ubuntu, with Linux 5.15.0-139-generic"

I change this and also to
GRUB_DEFAULT=4

but each reboot
uname -r
6.0.19-060019-generic


grep menuentry /boot/grub/grub.cfg
grep menuentry /boot/grub/grub.cfg | grep 5.15
	menuentry 'Ubuntu, with Linux 5.15.0-139-generic' --class ubuntu --class gnu-linux --class gnu --class os $menuentry_id_option 'gnulinux-5.15.0-139-generic-advanced-2f802f18-99ea-4d72-b536-d80db99ecf90' {

Apparently 5.15.0-139-generic is supposed to be compatible with nvidia-535
but I could not get this to auto default select on GRUB


cd /boot/grub
grep 5.15.0-139-generic grub.cfg

5.15.0-139-generic grub.cfg
	menuentry 'Ubuntu, with Linux 5.15.0-139-generic' --class ubuntu --class gnu-linux --class gnu --class os $menuentry_id_option 'gnulinux-5.15.0-139-generic-advanced-2f802f18-99ea-4d72-b536-d80db99ecf90' {
		echo	'Loading Linux 5.15.0-139-generic ...'
		linux	/boot/vmlinuz-5.15.0-139-generic root=UUID=2f802f18-99ea-4d72-b536-d80db99ecf90 ro  quiet splash $vt_handoff
		initrd	/boot/initrd.img-5.15.0-139-generic

nano /etc/default/grub
GRUB_DEFAULT="Advanced options for Ubuntu>Ubuntu, with Linux 5.15.0-139-generic"
GRUB_SAVEDEFAULT=false


sudo apt purge linux-image-6.0.19-060019-generic linux-headers-6.0.19-060019-generic
sudo update-grub



04-Dec-2025
uname -r
5.15.0-139-generic

nvidia-smi
Command not found
ubuntu-drivers devices

sudo apt update
sudo apt install nvidia-driver-535

nvidia-smi
NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver. Make sure that the latest NVIDIA driver is installed and running.

sudo reboot