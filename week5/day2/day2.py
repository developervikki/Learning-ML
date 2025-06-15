import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(2)
x = np.random.rand(100, 1) * 100
y = 3 * x + np.random.randn(100, 1) * 2  # Adding small noise

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Fit Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# Make Predictions
y_pred = model.predict(X_test)

# Print Slope and Intercept
print("Slope: ", model.coef_[0][0])
print("Intercept: ", model.intercept_[0])

# Plot Actual vs Predicted
plt.scatter(X_test, y_test, color="red", label="Actual Data")
plt.plot(X_test, y_pred, color="blue", label="Predicted Line")
plt.title("Linear Regression Model")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()

# Evaluate Performance
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error (MAE): ", mae)
print("Mean Squared Error (MSE): ", mse)
print("R-Squared Score: ", r2)
