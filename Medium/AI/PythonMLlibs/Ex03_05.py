# 5. TENSORFLOW
from pickletools import optimize

import tensorflow as tf
from tensorflow.keras import layers, Model
import numpy as np
from tensorflow.python.keras.utils.version_utils import training

from Ex03_03 import X_train

# 1. load + preprocess data (MNIST)
(x_train, y_train), _ = tf.keras.datasets.mnist.load_data()
x_train = x_train.astype("float32") / 255.0
x_train = x_train[:10000]   # Use subset for speed
y_train = y_train[:10000]

# 2. define custom dense-like layer
class MyLayer(layers.Layer):
    def __init__(self, units=64):
        super(MyLayer, self).__init__()
        self.units = units

    def build(self, input_shape):
        self.w = self.add_weight(shape=(input_shape[-1], self.units),
                                 initializer='random_normal',
                                 trainable=True)
        self.b = self.add_weight(shape=(self.units,),
                                 initializer='zeros',
                                 trainable=True)

    def call(self, inputs):
        return tf.matmul(inputs, self.w) + self.b

# 3. build the model using function API
inputs = tf.keras.Input(shape=(28, 28))
x = layers.Flatten()(inputs)
x = MyLayer(64)(x)
x = layers.Activation('relu')(x)  # Correct use inside Functional API
outputs = layers.Dense(10, activation='softmax')(x)
model = Model(inputs, outputs)

# 4. define loss function optimizer and accuracy metric
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy()
optimizer = tf.keras.optimizers.Adam()
train_acc = tf.keras.metrics.SparseCategoricalAccuracy()

# 5. training parameters
EPOCHS = 5
BATCH_SIZE = 64

# 6. prepare dataset
dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(1000).batch(BATCH_SIZE)

# 7. custom training loop
for epoch in range(EPOCHS):
    print(f"\nEpoch {epoch + 1}/{EPOCHS}")

    for step, (x_batch, y_batch) in enumerate(dataset):
        with tf.GradientTape() as tape:
            logits = model(x_batch, training=True)
            loss = loss_fn(y_batch, logits)

        gradients = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))
        train_acc.update_state(y_batch, logits)

        if step % 100 == 0:
            print(f"Step {step}: Loss = {loss:.4f} | Accuracy = {train_acc.result():.4f}")

    # Reset metric state after each epoch
    print(f"Epoch {epoch + 1} Accuracy: {train_acc.result():.4f}")
    train_acc.reset_state()

# Epoch 5 Accuracy: 0.9514