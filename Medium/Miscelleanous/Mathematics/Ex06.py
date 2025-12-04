import numpy as np

logits = np.array([2.0, 1.0, 0.1])
exp = np.exp(logits)
softmax = exp / exp.sum()
print(softmax)  # probability distribution