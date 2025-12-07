# 6. TENSORFLOW
import tensorflow as tf
import numpy as np

#print("TensorFlow version:", tf.__version__)
#print("Eager Execution:", tf.executing_eagerly())
#TensorFlow version: 2.19.0
#Eager Execution: True

# Creating tensors
a = tf.constant([[1, 2], [3, 4]])
#print("Tensor a:\n", a)

# Creating a tensor from a NumPy array
b = tf.convert_to_tensor(np.array([[5, 6], [7, 8]]), dtype=tf.int32)
#print("Tensor b:\n", b)

# Tensor operations
# print(tf.add(a, b))     # element-wise addition
# print(tf.matmul(a, b))  # matrix multiplication

# Build simple Neural Network
# MNIST classifier

# Step 1: load dataset
mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# # Step 2: normalize data
X_train = X_train / 255.0
X_test = X_test / 255.0

# Step 3: build model
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Flatten, Dense, Dropout

model = Sequential([
    Input(shape=(28, 28)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.2),
    Dense(10, activation='softmax')
])

# Step 4: compile model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Step 5: train model
model.fit(X_train, y_train, epochs=5)

# Step 6 evaluate model
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test accuracy: {test_accuracy:.2f}")
# Test accuracy: 0.98