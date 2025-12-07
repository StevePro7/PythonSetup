import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import torch
import torch.nn
import torch.optim
from collections import defaultdict
import pandas as pd

import tensorflow as tf


print(torch.cuda.device_count())
print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU detected")

print(torch.version.cuda)
print(torch.cuda.is_available())

print(tf.__version__)
print(tf.config.list_physical_devices())
# [PhysicalDevice(name='/physical_device:CPU:0', device_type='CPU')]

print('the end')