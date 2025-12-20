# Step 1: Install Required Libraries
# Step 2: Import Libraries
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt


# Step 3: Load and Preprocess Data
# Load MNIST dataset (images of digits)
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Reshape the images to 28x28 pixels and normalize them to [0, 1] range
x_train = x_train.reshape((x_train.shape[0], 28, 28, 1)).astype('float32') / 255
x_test = x_test.reshape((x_test.shape[0], 28, 28, 1)).astype('float32') / 255

# Convert labels to one-hot encoding
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)


# Step 4: Build the Model
model = Sequential()

# Add a convolutional layer with 32 filters, a 3x3 kernel, and ReLU activation
model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))

# Add a max-pooling layer to reduce the spatial dimensions
model.add(tf.keras.layers.MaxPooling2D((2, 2)))

# Flatten the output of the previous layer to a 1D array
model.add(tf.keras.layers.Flatten())

# Add a fully connected (dense) layer with 128 units and ReLU activation
model.add(Dense(128, activation='relu'))

# Output layer with 10 units for 10 classes (digits 0-9) and softmax activation
model.add(Dense(10, activation='softmax'))


# Step 5: Compile the Model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])


# Step 6: Train the Model
history = model.fit(x_train, y_train, epochs=5, batch_size=64, validation_data=(x_test, y_test))


# Step 7: Evaluate the Model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc}')


# Step 8: Make Predictions
predictions = model.predict(x_test)
print(f'Predicted label for the first test image: {np.argmax(predictions[0])}')


# Step 9: Visualize the Results
plt.imshow(x_test[0].reshape(28, 28), cmap='gray')
plt.title(f'Predicted label: {np.argmax(predictions[0])}')
plt.show()