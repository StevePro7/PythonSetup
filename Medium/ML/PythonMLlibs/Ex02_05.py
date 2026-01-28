# 6. TENSORFLOW
import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

# 1. load + prepare data with validation split
mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train, X_val = X_train[:50000] / 255.0, X_train[50000:] / 255.0
y_train, y_val = y_train[:50000], y_train[50000:]

# 2. define model (same as basic for continuity
from tensorflow.keras import layers, Sequential

model = Sequential([
    layers.Input(shape=(28, 28)),       # define input here
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(10, activation='softmax')
])

# 3. custom callback example: early stopping
early_stop = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss', patience=3, restore_best_weights=True
)

# compile model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# train model with validation and callback
history = model.fit(X_train, y_train,
                    epochs=20,
                    validation_data=(X_val, y_val),
                    callbacks=[early_stop])

# save + load model
model.save('mnist_model.h5')

# load the model later
new_model = tf.keras.models.load_model('mnist_model.h5')

# plot training history (optional visualization)
import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Val Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()