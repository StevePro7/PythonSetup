import torch.nn as nn

model_bn = nn.Sequential(
    nn.Conv2d(3, 32, kernel_size=3, padding=1),
    nn.BatchNorm2d(32),  # BatchNorm applied after convolution
    nn.ReLU(),
    nn.Linear(128, 64),
    nn.BatchNorm1d(64),  # for fully connected layers
    nn.ReLU()
)