# Retry with a smaller, faster experiment to avoid timeouts:
# - 2000 samples, 20 epochs

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import torch
import torch.nn as nn
import torch.optim as optim
from collections import defaultdict
import pandas as pd
from pathlib import Path

rng = np.random.RandomState(42)
torch.manual_seed(42)

X, y = make_moons(n_samples=2000, noise=0.25, random_state=rng)
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.25, random_state=rng, stratify=y)

scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train).astype(np.float32)
X_val   = scaler.transform(X_val).astype(np.float32)
y_train = y_train.astype(np.int64)
y_val   = y_val.astype(np.int64)

X_train_t = torch.from_numpy(X_train)
y_train_t = torch.from_numpy(y_train)
X_val_t   = torch.from_numpy(X_val)
y_val_t   = torch.from_numpy(y_val)

class MLP(nn.Module):
    def __init__(self, activation: nn.Module):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(2, 64),
            activation,
            nn.Linear(64, 32),
            activation.__class__() if isinstance(activation, (nn.ReLU, nn.LeakyReLU, nn.Tanh, nn.Sigmoid, nn.GELU)) else activation,
            nn.Linear(32, 2)
        )
    def forward(self, x):
        return self.net(x)

def train_model(activation_module, epochs=20, lr=1e-3, batch_size=128, device='cpu'):
    model = MLP(activation_module).to(device)
    opt = optim.Adam(model.parameters(), lr=lr)
    loss_fn = nn.CrossEntropyLoss()

    n = X_train_t.shape[0]
    history = defaultdict(list)

    for epoch in range(epochs):
        idx = torch.randperm(n)
        Xb = X_train_t[idx]
        yb = y_train_t[idx]

        model.train()
        running_loss = 0.0
        correct = 0
        total = 0
        for i in range(0, n, batch_size):
            xb = Xb[i:i+batch_size]
            ybb = yb[i:i+batch_size]
            opt.zero_grad()
            logits = model(xb)
            loss = loss_fn(logits, ybb)
            loss.backward()
            opt.step()
            running_loss += loss.item() * xb.size(0)
            pred = logits.argmax(dim=1)
            correct += (pred == ybb).sum().item()
            total += xb.size(0)
        train_loss = running_loss / total
        train_acc = correct / total

        model.eval()
        with torch.no_grad():
            logits_val = model(X_val_t)
            val_loss = loss_fn(logits_val, y_val_t).item()
            val_acc = (logits_val.argmax(dim=1) == y_val_t).float().mean().item()

        history['epoch'].append(epoch+1)
        history['train_loss'].append(train_loss)
        history['val_loss'].append(val_loss)
        history['train_acc'].append(train_acc)
        history['val_acc'].append(val_acc)

    return model, pd.DataFrame(history)

activations = {
    'Sigmoid': nn.Sigmoid(),
    'Tanh': nn.Tanh(),
    'ReLU': nn.ReLU(),
    'LeakyReLU(0.1)': nn.LeakyReLU(0.1),
    'GELU': nn.GELU(),
}

histories = {}
for name, act in activations.items():
    _, hist = train_model(act, epochs=20, lr=1e-3, batch_size=128)
    hist['activation'] = name
    histories[name] = hist

df_hist = pd.concat(histories.values(), ignore_index=True)

plt.figure(figsize=(8,5))
for name in activations.keys():
    sub = df_hist[df_hist['activation']==name]
    plt.plot(sub['epoch'], sub['val_loss'], label=name)
plt.xlabel("Epoch")
plt.ylabel("Validation Loss")
plt.title("Activation Function Comparison: Validation Loss")
plt.legend()
plt.tight_layout()
loss_path = Path("activation_val_loss_fast.png")
plt.savefig(loss_path)
plt.show()

plt.figure(figsize=(8,5))
for name in activations.keys():
    sub = df_hist[df_hist['activation']==name]
    plt.plot(sub['epoch'], sub['val_acc'], label=name)
plt.xlabel("Epoch")
plt.ylabel("Validation Accuracy")
plt.title("Activation Function Comparison: Validation Accuracy")
plt.legend()
plt.tight_layout()
acc_path = Path("activation_val_acc_fast.png")
plt.savefig(acc_path)
plt.show()

summary = df_hist.sort_values('epoch').groupby('activation').tail(1)[['activation','train_loss','val_loss','train_acc','val_acc']]
summary = summary.sort_values('val_acc', ascending=False).reset_index(drop=True)


(loss_path.as_posix(), acc_path.as_posix())