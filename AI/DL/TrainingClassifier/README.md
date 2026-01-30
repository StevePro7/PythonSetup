Training a Classifier
29-Jan-2026

https://docs.pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html

uv init --python 3.11.11
uv venv --python 3.11.11
source .venv/bin/activate

uv add torch torchvision torchaudio

uv add matplotlib


#  Ex01
1. Load and normalize CIFAR10

UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown
  plt.show()

plt.savefig("Ex01.png", bbox_inches="tight", dpi=300)
plt.close()
    

#  Ex02
2. Define a Convolutional Neural Network


#  Ex03
3. Define a Loss function and optimizer


#  Ex04
4. Train the network


#  Ex05
5. Test the network on the test data


CPU
[1,  2000] loss: 2.235
[1,  4000] loss: 1.856
[1,  6000] loss: 1.684
[1,  8000] loss: 1.532
[1, 10000] loss: 1.490
[1, 12000] loss: 1.442
[2,  2000] loss: 1.371
[2,  4000] loss: 1.341
[2,  6000] loss: 1.335
[2,  8000] loss: 1.300
[2, 10000] loss: 1.266
[2, 12000] loss: 1.280
Finished Training
GroundTruth:  cat   ship  ship  plane
Predicted:  cat   ship  ship  ship 
Accuracy of the network on the 10000 test images: 54 %
Accuracy for class: plane is 55.0 %
Accuracy for class: car   is 71.4 %
Accuracy for class: bird  is 30.1 %
Accuracy for class: cat   is 31.7 %
Accuracy for class: deer  is 69.3 %
Accuracy for class: dog   is 38.6 %
Accuracy for class: frog  is 55.6 %
Accuracy for class: horse is 60.9 %
Accuracy for class: ship  is 78.5 %
Accuracy for class: truck is 52.3 %
End5!!

Process finished with exit code 0



GPU
repeat process but on CPU
make the following changes

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print(device)

# cuda:0
net = Net()
net.to(device)


    for i, data in enumerate(trainloader, 0):
        # get the inputs; data is a list of [inputs, labels]
        # inputs, labels = data
        inputs, labels = data[0].to(device), data[1].to(device)