import numpy as np
import matplotlib.pyplot as plt

# Simulate unnormalized activations
np.random.seed(42)
original = np.random.randn(1000) * 5 + 10   # shifted, high variance
shifted  = np.random.randn(1000) * 20 - 30  # extreme shift/scale

# Apply BatchNorm-style normalization (mean=0, var=1)
def batchnorm(x, eps=1e-5):
    mu, sigma = x.mean(), x.std()
    return (x - mu) / np.sqrt(sigma**2 + eps)

normed1 = batchnorm(original)
normed2 = batchnorm(shifted)

# Plot distributions
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.hist(original, bins=40, alpha=0.5, label="Original")
plt.hist(normed1, bins=40, alpha=0.5, label="Normalized")
plt.legend(); plt.title("Moderate Scale Shift")

plt.subplot(1,2,2)
plt.hist(shifted, bins=40, alpha=0.5, label="Original Extreme")
plt.hist(normed2, bins=40, alpha=0.5, label="Normalized")
plt.legend(); plt.title("Extreme Scale Shift")
plt.tight_layout()
plt.show()