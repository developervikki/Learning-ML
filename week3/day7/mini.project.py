import numpy as np

# Generate synthetic data
np.random.seed(42)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)  # Corrected np.randn to np.random.randn

# Add bias term to feature matrix
x_b = np.c_[np.ones((100, 1)), x]

# Initialize parameters
theta = np.random.randn(2, 1)
learning_rate = 0.1
iterations = 1000

# Define prediction function
def predict(x, theta):
    return np.dot(x, theta)

# Task 2: Use gradient descent to optimize the model parameters
def gradient_descent(x, y, theta, learning_rate, iterations):
    m = len(y)
    for _ in range(iterations):
        gradients = (1 / m) * np.dot(x.T, (np.dot(x, theta) - y))  # Fixed np.dot(x,T) to np.dot(x.T, ...)
        theta -= learning_rate * gradients
    return theta

# Task 3: Calculate evaluation metrics
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def r_squared(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - (ss_res / ss_tot)

# Perform gradient descent
theta_optimized = gradient_descent(x_b, y, theta, learning_rate, iterations)

# Predictions and evaluations
y_pred = predict(x_b, theta_optimized)
mse = mean_squared_error(y, y_pred)
r2 = r_squared(y, y_pred)

print("Optimized parameters (Theta):", theta_optimized)
print("MSE:", mse)
print("R²:", r2)
