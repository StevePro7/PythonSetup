import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# 1. Dataset: MNIST (handwritten digits 0–9)
transform = transforms.ToTensor()
train_ds = datasets.MNIST(root="./data", train=True, download=True, transform=transform)
val_ds   = datasets.MNIST(root="./data", train=False, download=True, transform=transform)

train_loader = DataLoader(train_ds, batch_size=128, shuffle=True)
val_loader   = DataLoader(val_ds, batch_size=512, shuffle=False)

# 2. Define two models (same architecture, with/without BN)
class MLPPlain(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28*28, 256), nn.ReLU(),
            nn.Linear(256, 128), nn.ReLU(),
            nn.Linear(128, 10)
        )
    def forward(self, x): return self.net(x)

class MLPWithBN(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28*28, 256), nn.BatchNorm1d(256), nn.ReLU(),
            nn.Linear(256, 128), nn.BatchNorm1d(128), nn.ReLU(),
            nn.Linear(128, 10)
        )
    def forward(self, x): return self.net(x)

# 3. Training helper
def train_model(model, epochs=5, lr=1e-3):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    opt = optim.Adam(model.parameters(), lr=lr)
    loss_fn = nn.CrossEntropyLoss()

    for epoch in range(epochs):
        model.train()
        total_loss, correct, n = 0,0,0
        for xb, yb in train_loader:
            xb, yb = xb.to(device), yb.to(device)
            opt.zero_grad()
            out = model(xb)
            loss = loss_fn(out, yb)
            loss.backward()
            opt.step()
            total_loss += loss.item()*xb.size(0)
            correct += (out.argmax(1)==yb).sum().item()
            n += xb.size(0)
        train_loss, train_acc = total_loss/n, correct/n

        # validation
        model.eval()
        val_loss, val_correct, val_n = 0,0,0
        with torch.no_grad():
            for xb,yb in val_loader:
                xb, yb = xb.to(device), yb.to(device)
                out = model(xb)
                val_loss += loss_fn(out,yb).item()*xb.size(0)
                val_correct += (out.argmax(1)==yb).sum().item()
                val_n += xb.size(0)
        val_loss, val_acc = val_loss/val_n, val_correct/val_n

        print(f"Epoch {epoch+1}: Train Loss={train_loss:.3f}, Acc={train_acc:.3f}, Val Loss={val_loss:.3f}, Acc={val_acc:.3f}")

    return model

# 4. Run training
print("=== Training Plain MLP ===")
plain_model = train_model(MLPPlain(), epochs=5)

print("\n=== Training MLP with BatchNorm ===")
bn_model = train_model(MLPWithBN(), epochs=5)
