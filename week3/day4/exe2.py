import numpy as np

# Generate synthetic data
np.random.seed(42)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)

# Add bias term to x
x_b = np.c_[np.ones((100, 1)), x]

# SGD implementation
def stochastic_gradient_descent(x, y, theta, learning_rate, n_epochs):
    m = len(y)
    for epoch in range(n_epochs):
        for i in range(m):
            random_index = np.random.randint(m)
            xi = x[random_index:random_index + 1]
            yi = y[random_index:random_index + 1]
            gradients = 2 * xi.T @ (xi @ theta - yi)
            theta -= learning_rate * gradients
    return theta

# Initialize parameters
theta = np.random.randn(2, 1)  # Random initialization with correct shape
learning_rate = 0.01
n_epochs = 50

# Perform SGD
theta_opt = stochastic_gradient_descent(x_b, y, theta, learning_rate, n_epochs)

print("Optimized Parameters: ", theta_opt)
