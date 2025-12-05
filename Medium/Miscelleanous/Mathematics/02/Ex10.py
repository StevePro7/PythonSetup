# ================================
# Convex vs Non-Convex on MNIST
# ================================
# Shows how convexity affects optimization outcomes.

import os, random, numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models, optimizers

# Enable eager execution
# Use experimental_run_eagerly for newer TensorFlow versions
# tf.config.experimental_run_eagerly(True) # This caused an error
tf.compat.v1.enable_eager_execution()


# --------------------------------
# Reproducibility helpers
# --------------------------------
def set_seed(seed=42):
    random.seed(seed); np.random.seed(seed); tf.random.set_seed(seed)

set_seed(42)

# --------------------------------
# DATA: MNIST (fallback available)
# --------------------------------
USE_SKLEARN_FALLBACK = False  # set True if offline

if not USE_SKLEARN_FALLBACK:
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
    X_train = X_train.reshape(-1, 28*28).astype("float32") / 255.0
    X_test  = X_test.reshape(-1, 28*28).astype("float32") / 255.0
    n_features, n_classes = 784, 10
else:
    # Fallback: sklearn digits (8x8)
    from sklearn.datasets import load_digits
    from sklearn.model_selection import train_test_split
    digits = load_digits()
    X = digits.data.astype("float32") / 16.0
    y = digits.target.astype("int64")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    n_features, n_classes = X_train.shape[1], len(np.unique(y))

# --------------------------------
# Utils
# --------------------------------
def build_softmax_model():
    # Convex model: linear logits + softmax (no hidden layers)
    model = models.Sequential([
        layers.Input(shape=(n_features,)),
        layers.Dense(n_classes, activation='softmax', use_bias=True)
    ])
    return model

def build_mlp(hidden=128):
    # Non-convex model: ReLU introduces non-linearity → rugged loss
    model = models.Sequential([
        layers.Input(shape=(n_features,)),
        layers.Dense(hidden, activation='relu'),
        layers.Dense(hidden//2, activation='relu'),
        layers.Dense(n_classes, activation='softmax')
    ])
    return model

def compile_and_train(model, optimizer_factory, X_train, y_train, epochs=6, batch_size=128, val_split=0.1, verbose=0):
    # Create a new optimizer instance for this model
    opt = optimizer_factory()
    model.compile(optimizer=opt,
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    hist = model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size,
                     validation_split=val_split, verbose=verbose)
    return hist

def evaluate(model, X_test, y_test):
    loss, acc = model.evaluate(X_test, y_test, verbose=0)
    return loss, acc

def plot_history(histories, title):
    # histories: dict(name -> History.history)
    plt.figure(figsize=(7,5))
    for name, H in histories.items():
        plt.plot(H['val_loss'], label=f"{name} val_loss")
    plt.title(title)
    plt.xlabel("Epoch")
    plt.ylabel("Validation Loss")
    plt.legend()
    plt.grid(True)
    plt.show()

# --------------------------------
# A) CONVEX: Softmax Regression
# --------------------------------
# Define optimizer factories
optimizer_factories = {
    "SGD(eta=0.1)": lambda: optimizers.SGD(learning_rate=0.1),
    "SGD+Momentum(0.9)": lambda: optimizers.SGD(learning_rate=0.05, momentum=0.9),
    "Adam(1e-3)": lambda: optimizers.Adam(learning_rate=1e-3),
}


convex_histories = {}
convex_results = {}

for name, opt_factory in optimizer_factories.items():
    set_seed(42)  # reset weights → fair comparison
    model = build_softmax_model()
    # Pass the factory to compile_and_train
    H = compile_and_train(model, opt_factory, X_train, y_train, epochs=8, batch_size=256, val_split=0.1, verbose=0)
    loss, acc = evaluate(model, X_test, y_test)
    convex_histories[name] = H.history
    convex_results[name] = (loss, acc)

plot_history(convex_histories, "Convex model (Softmax) — different optimizers")

print("=== Convex model (Softmax) results ===")
for name, (loss, acc) in convex_results.items():
    print(f"{name:20s}  Test loss={loss:.4f}  Test acc={acc:.4f}")

# NOTE (what to observe):
# - All optimizers converge to essentially the SAME solution (convex bowl → unique minimum).
# - Speed may differ (Adam often faster), but the final performance is very similar.

# --------------------------------
# B) NON-CONVEX: 2-layer ReLU MLP
# --------------------------------
nonconvex_histories = {}
nonconvex_results = {}

for name, opt_factory in optimizer_factories.items():
    set_seed(42)  # same seed for optimizer comparison
    model = build_mlp(hidden=128)
    # Pass the factory to compile_and_train
    H = compile_and_train(model, opt_factory, X_train, y_train, epochs=8, batch_size=256, val_split=0.1, verbose=0)
    loss, acc = evaluate(model, X_test, y_test)
    nonconvex_histories[name] = H.history
    nonconvex_results[name] = (loss, acc)

plot_history(nonconvex_histories, "Non-convex model (MLP) — different optimizers")

print("\n=== Non-convex model (MLP) results ===")
for name, (loss, acc) in nonconvex_results.items():
    print(f"{name:20s}  Test loss={loss:.4f}  Test acc={acc:.4f}")

# NOTE (what to observe):
# - Final metrics can differ across optimizers (no unique minimum).
# - Adam often finds good minima quickly; SGD may need more tuning/schedule.

# --------------------------------
# C) NON-CONVEX: Sensitivity to initialization
# --------------------------------
init_results = []
for seed in [0, 1, 2, 3, 4]:
    set_seed(seed)
    model = build_mlp(hidden=128)
    # Pass the factory to compile_and_train
    H = compile_and_train(model, lambda: optimizers.Adam(1e-3), X_train, y_train, epochs=6, batch_size=256, val_split=0.1, verbose=0)
    loss, acc = evaluate(model, X_test, y_test)
    init_results.append((seed, loss, acc))

print("\n=== Non-convex (MLP) — different random initializations (Adam) ===")
for seed, loss, acc in init_results:
    print(f"seed={seed:2d}  Test loss={loss:.4f}  Test acc={acc:.4f}")

# Expectation:
# - Different seeds → different minima → small but real variation in final performance.

# --------------------------------
# D) BONUS: Weight interpolation curve (non-convex evidence)
# --------------------------------
def get_flat_weights(model):
    # Flatten all weights + biases into one vector
    vecs = []
    for w in model.weights:
        vecs.append(tf.reshape(w, [-1]).numpy())
    return np.concatenate(vecs)

def set_flat_weights(model, flat):
    # Write a flat vector back into keras variables (same shapes/order)
    idx = 0
    for w in model.weights:
        size = np.prod(w.shape)
        new_vals = flat[idx:idx+size].reshape(w.shape)
        w.assign(new_vals)
        idx += size

# Train two MLPs with different seeds (two different minima)
set_seed(100)
mlp_A = build_mlp(128)
compile_and_train(mlp_A, lambda: optimizers.Adam(1e-3), X_train, y_train, epochs=6, batch_size=256, val_split=0.1, verbose=0)

set_seed(777)
mlp_B = build_mlp(128)
compile_and_train(mlp_B, lambda: optimizers.Adam(1e-3), X_train, y_train, epochs=6, batch_size=256, val_split=0.1, verbose=0)

wA = get_flat_weights(mlp_A)
wB = get_flat_weights(mlp_B)

# Probe along the straight line between A and B in parameter space
alphas = np.linspace(0, 1, 31)
probe = build_mlp(128)
# Compile with a dummy optimizer, as we manually set weights
probe.compile(optimizer='sgd', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
interp_losses = []

for a in alphas:
    w = (1 - a) * wA + a * wB
    set_flat_weights(probe, w)
    loss, _ = probe.evaluate(X_test, y_test, verbose=0)
    interp_losses.append(loss)

plt.figure(figsize=(7,5))
plt.plot(alphas, interp_losses, marker='o')
plt.title("Non-convex evidence: Loss along weight interpolation path")
plt.xlabel(r"Interpolation $\alpha$  (0 = A, 1 = B)")
plt.ylabel("Test Loss")
plt.grid(True)
plt.show()