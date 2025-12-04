# layernorm_rnn_demo.py
# Show LayerNorm benefit on a variable-length sequence classification task.

import math, random, numpy as np
import torch, torch.nn as nn, torch.optim as optim
from torch.nn.utils.rnn import pad_sequence, pack_padded_sequence, pad_packed_sequence
import matplotlib.pyplot as plt
from pathlib import Path

# ---------------------------
# Reproducibility & device
# ---------------------------
def set_seed(seed=42):
    random.seed(seed); np.random.seed(seed)
    torch.manual_seed(seed); torch.cuda.manual_seed_all(seed)
set_seed(42)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ---------------------------
# Synthetic sequence dataset
# ---------------------------
# Each sequence is a list of real numbers in [-1, 1].
# Label = 1 if final cumulative sum > 0, else 0 (order matters).
def make_example(min_len=20, max_len=60):
    L = random.randint(min_len, max_len)
    x = torch.rand(L, 1)*2 - 1  # values in [-1,1]
    y = torch.tensor([1 if x.sum().item() > 0 else 0], dtype=torch.long)
    return x, y

def make_split(n, min_len=20, max_len=60):
    data = [make_example(min_len, max_len) for _ in range(n)]
    return data

train_data = make_split(4000)
val_data   = make_split(800)

def collate(batch):
    xs, ys = zip(*batch)
    lengths = torch.tensor([len(x) for x in xs], dtype=torch.long)
    xs_pad = pad_sequence(xs, batch_first=True)          # (B, T, 1)
    ys = torch.cat(ys, dim=0)                            # (B,)
    return xs_pad, lengths, ys

# ---------------------------
# RNN cells
# ---------------------------
class PlainRNNCell(nn.Module):
    def __init__(self, in_dim, hid_dim):
        super().__init__()
        self.Wx = nn.Linear(in_dim, hid_dim, bias=True)
        self.Wh = nn.Linear(hid_dim, hid_dim, bias=False)
        self.act = nn.Tanh()
    def forward(self, x_t, h):
        pre = self.Wx(x_t) + self.Wh(h)       # no normalization
        return self.act(pre)

class LayerNormRNNCell(nn.Module):
    def __init__(self, in_dim, hid_dim):
        super().__init__()
        self.Wx = nn.Linear(in_dim, hid_dim, bias=True)
        self.Wh = nn.Linear(hid_dim, hid_dim, bias=False)
        self.ln = nn.LayerNorm(hid_dim)       # LayerNorm on pre-activation
        self.act = nn.Tanh()
    def forward(self, x_t, h):
        pre = self.Wx(x_t) + self.Wh(h)
        pre = self.ln(pre)                    # normalize per time step, per sample
        return self.act(pre)

# ---------------------------
# RNN wrappers
# ---------------------------
class SimpleRNN(nn.Module):
    def __init__(self, cell_cls, in_dim=1, hid_dim=64, num_classes=2):
        super().__init__()
        self.cell = cell_cls(in_dim, hid_dim)
        self.out  = nn.Linear(hid_dim, num_classes)
    def forward(self, x_pad, lengths):
        B, T, D = x_pad.shape
        h = torch.zeros(B, self.cell.Wx.out_features, device=x_pad.device)
        # iterate time with masking (small & clear for demo)
        for t in range(T):
            x_t = x_pad[:, t, :]
            mask = (t < lengths).float().unsqueeze(1)     # (B,1)
            h = self.cell(x_t, h) * mask + h * (1 - mask) # keep old h beyond length
        return self.out(h)  # classify using final hidden state

# ---------------------------
# Training loop
# ---------------------------
def run_epoch(model, data, optimizer=None, batch_size=64):
    is_train = optimizer is not None
    if is_train: model.train()
    else: model.eval()

    total_loss, total_correct, total = 0.0, 0, 0
    loss_fn = nn.CrossEntropyLoss()

    # small batch size emphasizes LayerNorm’s batch-size independence
    for i in range(0, len(data), batch_size):
        batch = data[i:i+batch_size]
        xs, ls, ys = collate(batch)
        xs, ls, ys = xs.to(device), ls.to(device), ys.to(device)

        if is_train:
            optimizer.zero_grad()
        logits = model(xs, ls)
        loss = loss_fn(logits, ys)
        if is_train:
            loss.backward()
            optimizer.step()

        total_loss += loss.item() * ys.size(0)
        total_correct += (logits.argmax(1) == ys).sum().item()
        total += ys.size(0)

    return total_loss/total, total_correct/total

def train_model(model, epochs=15, lr=3e-3):
    model = model.to(device)
    opt = optim.Adam(model.parameters(), lr=lr)
    history = {"train_loss":[], "train_acc":[], "val_loss":[], "val_acc":[]}
    for ep in range(1, epochs+1):
        tr_loss, tr_acc = run_epoch(model, train_data, optimizer=opt, batch_size=32)  # small batches
        va_loss, va_acc = run_epoch(model, val_data,   optimizer=None, batch_size=64)
        history["train_loss"].append(tr_loss); history["train_acc"].append(tr_acc)
        history["val_loss"].append(va_loss);   history["val_acc"].append(va_acc)
        print(f"Epoch {ep:2d}: Train Loss={tr_loss:.3f}, Acc={tr_acc:.3f} | Val Loss={va_loss:.3f}, Acc={va_acc:.3f}")
    return history

# ---------------------------
# Run: Plain vs LayerNorm
# ---------------------------
plain = SimpleRNN(PlainRNNCell)
ln    = SimpleRNN(LayerNormRNNCell)

print("=== Training Plain RNN (no normalization) ===")
hist_plain = train_model(plain, epochs=15)

print("\n=== Training LayerNorm RNN ===")
hist_ln = train_model(ln, epochs=15)

# ---------------------------
# Plot results
# ---------------------------
epochs = range(1, len(hist_plain["train_loss"])+1)
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.plot(epochs, hist_plain["train_loss"], marker='o', label="Plain Train Loss")
plt.plot(epochs, hist_plain["val_loss"],   marker='o', linestyle='--', label="Plain Val Loss")
plt.plot(epochs, hist_ln["train_loss"],    marker='s', label="LN Train Loss")
plt.plot(epochs, hist_ln["val_loss"],      marker='s', linestyle='--', label="LN Val Loss")
plt.xlabel("Epoch"); plt.ylabel("Loss"); plt.title("Loss: Plain vs LayerNorm RNN"); plt.legend()

plt.subplot(1,2,2)
plt.plot(epochs, hist_plain["train_acc"], marker='o', label="Plain Train Acc")
plt.plot(epochs, hist_plain["val_acc"],   marker='o', linestyle='--', label="Plain Val Acc")
plt.plot(epochs, hist_ln["train_acc"],    marker='s', label="LN Train Acc")
plt.plot(epochs, hist_ln["val_acc"],      marker='s', linestyle='--', label="LN Val Acc")
plt.xlabel("Epoch"); plt.ylabel("Accuracy"); plt.title("Accuracy: Plain vs LayerNorm RNN"); plt.legend()

plt.tight_layout()
out_path = Path("layernorm_rnn_curves.png")
plt.savefig(out_path)
plt.show()
print(f"Saved plot to: {out_path.resolve()}")
