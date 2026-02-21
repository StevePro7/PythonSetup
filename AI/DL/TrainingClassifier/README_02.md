Training a Classifier 02
21-Feb-2026

https://docs.pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html

Follow up notes

Define Convolutional Neural Network
useful for image classifiers

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)
		
		
IMPORTANT
self.fc1

FC
Fully Connected

A fully connected layer (also called a linear layer or dense layer) is a layer where:

* Every input neuron is connected to every output neuron.
* It is typically used after convolution and pooling layers.
* It helps combine extracted features to perform classification or regression.


Optimizer
SDG
Stochastic Gradient Descent
e.g.
torch.nn.optim.SGD()

optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

lr = learning rate	step size
momentum			90% of previous update velocity