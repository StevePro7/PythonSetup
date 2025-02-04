# Step 1: Install Required Libraries
# Step 2: Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


# Step 3: Load and Prepare Data
# Sample data: Square footage (X) and House price (Y)
data = {'SquareFootage': [1500, 1800, 2400, 3000, 3500, 4000, 5000],
        'Price': [400000, 450000, 500000, 600000, 650000, 700000, 800000]}
df = pd.DataFrame(data)

# Split the data into input (X) and output (Y)
X = df[['SquareFootage']]
Y = df['Price']


# Step 4: Split the Data into Training and Testing Sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Step 5: Train the Model
model = LinearRegression()
model.fit(X_train, Y_train)


# Step 6: Make Predictions
Y_pred = model.predict(X_test)


# Step 7: Evaluate the Model
mse = mean_squared_error(Y_test, Y_pred)
print("Mean Squared Error:", mse)

# Plot the results
plt.scatter(X_test, Y_test, color='blue', label='True values')
plt.plot(X_test, Y_pred, color='red', label='Predicted values')
plt.xlabel('Square Footage')
plt.ylabel('Price')
plt.legend()
plt.show()

