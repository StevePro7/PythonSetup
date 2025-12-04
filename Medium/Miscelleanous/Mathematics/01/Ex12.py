# groupnorm_why_demo.py
import torch, torch.nn as nn, torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import numpy as np, random
from pathlib import Path

# ----------------------------
# Repro & device
# ----------------------------
def set_seed(s=42):
    random.seed(s); np.random.seed(s)
    torch.manual_seed(s); torch.cuda.manual_seed_all(s)
set_seed(42)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Device:", device)

# ----------------------------
# Data (CIFAR-10)
# ----------------------------
tfm = transforms.Compose([transforms.ToTensor()])
data_root = "./data"
train_ds = datasets.CIFAR10(root="./data", train=True,  download=True, transform=tfm)
val_ds   = datasets.CIFAR10(root="./data", train=False, download=True, transform=tfm)

def make_loaders(batch):
    return (DataLoader(train_ds, batch_size=batch, shuffle=True,  num_workers=2, pin_memory=(device.type=="cuda")),
            DataLoader(val_ds,   batch_size=batch, shuffle=False, num_workers=2, pin_memory=(device.type=="cuda")))

# ----------------------------
# Model family (same params; BN or GN)
# ----------------------------
class SmallCNN(nn.Module):
    def __init__(self, norm_type="bn"):
        super().__init__()
        C1, C2 = 32, 64
        if norm_type == "bn":
            n1, n2 = nn.BatchNorm2d(C1), nn.BatchNorm2d(C2)
        elif norm_type == "gn":
            n1, n2 = nn.GroupNorm(8, C1), nn.GroupNorm(8, C2)   # 8 groups divides 32, 64
        else:
            raise ValueError("norm_type must be 'bn' or 'gn'")
        self.block1 = nn.Sequential(nn.Conv2d(3, C1, 3, padding=1), n1, nn.ReLU())
        self.block2 = nn.Sequential(nn.Conv2d(C1, C2, 3, padding=1), n2, nn.ReLU())
        self.head   = nn.Sequential(nn.AdaptiveAvgPool2d((1,1)), nn.Flatten(), nn.Linear(C2, 10))
    def forward(self, x):
        x = self.block1(x); x = self.block2(x); x = self.head(x)
        return x

# ----------------------------
# Train / eval
# ----------------------------
def run_epoch(model, loader, opt=None):
    """If optimizer is None -> eval; else -> train."""
    is_train = opt is not None
    model.train(is_train)
    loss_fn = nn.CrossEntropyLoss()
    total_loss, total_correct, total = 0.0, 0, 0
    for xb, yb in loader:
        xb, yb = xb.to(device), yb.to(device)
        if is_train:
            opt.zero_grad()
        logits = model(xb)
        loss = loss_fn(logits, yb)
        if is_train:
            loss.backward()
            opt.step()
        total_loss += loss.item()*xb.size(0)
        total_correct += (logits.argmax(1) == yb).sum().item()
        total += xb.size(0)

    return total_loss / total, total_correct / total

def train_model(norm_type, train_loader, val_loader, epochs=1, lr=1e-3):
    model = SmallCNN(norm_type).to(device)
    opt = optim.Adam(model.parameters(), lr=lr)
    hist = {"train_loss":[], "train_acc":[], "val_loss":[], "val_acc":[]}
    for ep in range(1, epochs+1):
        tl, ta = run_epoch(model, train_loader, opt)
        vl, va = run_epoch(model, val_loader,   None)
        hist["train_loss"].append(tl); hist["train_acc"].append(ta)
        hist["val_loss"].append(vl);   hist["val_acc"].append(va)
        print(f"[{norm_type}][epoch {ep}] train_acc={ta:.3f} val_acc={va:.3f}")
    return model, hist

# ----------------------------
# (A) Sweep: val accuracy vs batch size
# ----------------------------
batch_sizes = [2, 4, 8, 32]
bn_scores, gn_scores = [], []
for b in batch_sizes:
    tr, va = make_loaders(b)
    # 1 epoch to keep it quick — we compare sensitivity to batch size
    _, bn_hist = train_model("bn", tr, va, epochs=1)
    _, gn_hist = train_model("gn", tr, va, epochs=1)
    bn_scores.append(bn_hist["val_acc"][-1])
    gn_scores.append(gn_hist["val_acc"][-1])

plt.figure(figsize=(7,5))
plt.plot(batch_sizes, bn_scores, marker="o", label="BatchNorm")
plt.plot(batch_sizes, gn_scores, marker="s", label="GroupNorm")
plt.xscale("log") # Removed basex=2
plt.xlabel("Batch size"); plt.ylabel("Validation accuracy")
plt.title("Validation accuracy vs. batch size (BN vs GN)")
plt.legend(); plt.tight_layout()
plt.savefig("gn_vs_bn_valacc_vs_batch.png"); plt.show()

# ----------------------------
# (B) Tiny batch stability: curves at batch=4 ### try this for batch=8 as well
# ----------------------------
tr4, va4 = make_loaders(4)
_, bn_hist4 = train_model("bn", tr4, va4, epochs=3)
_, gn_hist4 = train_model("gn", tr4, va4, epochs=3)

epochs = range(1, 4)
import matplotlib.pyplot as plt
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.plot(epochs, bn_hist4["val_loss"], marker="o", label="BN Val Loss")
plt.plot(epochs, gn_hist4["val_loss"], marker="s", label="GN Val Loss")
plt.xlabel("Epoch"); plt.ylabel("Loss"); plt.title("Tiny batch=4: Validation Loss"); plt.legend()
plt.subplot(1,2,2)
plt.plot(epochs, bn_hist4["val_acc"], marker="o", label="BN Val Acc")
plt.plot(epochs, gn_hist4["val_acc"], marker="s", label="GN Val Acc")
plt.xlabel("Epoch"); plt.ylabel("Accuracy"); plt.title("Tiny batch=4: Validation Accuracy"); plt.legend()
plt.tight_layout(); plt.savefig("gn_vs_bn_curves_batch4.png"); plt.show()

# ----------------------------
# (C) WHY: activation-statistics stability snapshot
#     We record channel-wise means from block1 for a tiny batch
# ----------------------------
@torch.no_grad()
def channel_means_of_block1(model, loader, n_batches=5):
    model.eval()
    means = []
    for i, (xb, _) in enumerate(loader):
        if i >= n_batches: break
        xb = xb.to(device)
        # forward until end of block1
        x = model.block1[0](xb)  # conv
        x = model.block1[1](x)   # norm (BN or GN)
        # x: [B, C, H, W]
        m = x.mean(dim=(0,2,3)).detach().cpu().numpy()  # per-channel mean across this tiny batch
        means.append(m)
    return np.stack(means, axis=0)  # shape: [n_batches, C]

bn_means = channel_means_of_block1(SmallCNN("bn").to(device), tr4, n_batches=6)
gn_means = channel_means_of_block1(SmallCNN("gn").to(device), tr4, n_batches=6)

plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.plot(bn_means, alpha=0.7); plt.title("BN: per-channel means across mini-batches (batch=4)")
plt.xlabel("mini-batch idx"); plt.ylabel("mean activation (channel-wise)")
plt.subplot(1,2,2)
plt.plot(gn_means, alpha=0.7); plt.title("GN: per-channel means across mini-batches (batch=4)")
plt.xlabel("mini-batch idx"); plt.ylabel("mean activation (channel-wise)")
plt.tight_layout(); plt.savefig("gn_vs_bn_channel_means_stability.png"); plt.show()

print("Saved plots:",
      Path("gn_vs_bn_valacc_vs_batch.png").resolve(),
      Path("gn_vs_bn_curves_batch4.png").resolve(),
      Path("gn_vs_bn_channel_means_stability.png").resolve())
