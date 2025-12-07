import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt

x_t = torch.linspace(-6, 6, 200)
gelu = F.gelu(x_t)
plt.plot(x_t, gelu); plt.title("GELU"); plt.grid(); plt.show()