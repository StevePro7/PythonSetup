import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))


class SingleNeuron:
    def __init__(self, w, b):
        self.w = w
        self.b = b

    def forward(self, x):
#        z = w * x + b
        z = np.dot(self.w, x) + self.b
        y = sigmoid(z)
        return y


w = np.array([0.4, -1.2, 0.7])
b = 0.1
neuron: SingleNeuron = SingleNeuron(w, b)
x = np.array([1.0, 2.0, -0.5])
y = neuron.forward(x)
print(f"Output: {y:.4f}")
# Output: 0.0953


# # Example: one input, one weight, one bias
# x = 0.8
# w = 1.5
# b = -0.9
# neuron: SingleNeuron = SingleNeuron(w, b)
# y = neuron.forward(x)
# print(f"Output: {y:.4f}")   # value between 0 and 1
# # Output: 0.5744