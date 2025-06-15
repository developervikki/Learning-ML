

# def byes_therorem(prior, likelihood,evidence):
#     return (likelihood*prior)/evidence



import numpy as np
import matplotlib.pyplot as plt  # Correct import

# # Parameters for Gaussian distribution
# mu, sigma = 0, 1

# # Generate x values
# x = np.linspace(-4, 4, 100)

# # Gaussian (normal) distribution formula
# y = (1 / (np.sqrt(2 * np.pi * sigma**2))) * np.exp(-0.5 * ((x - mu) / sigma)**2)

# # Plot the distribution
# plt.plot(x, y)
# plt.title("Gaussian Distribution")
# plt.xlabel("x")
# plt.ylabel("Probability Density")
# plt.grid(True)
# plt.show()



# # Parameters for Bernoulli distribution
# p = 0.6  # Probability of success

# # Plotting the Bernoulli distribution
# plt.bar([0, 1], [1 - p, p], color="blue", tick_label=["0 (Failure)", "1 (Success)"])
# plt.title("Bernoulli Distribution")
# plt.xlabel("Outcome")
# plt.ylabel("Probability")
# plt.grid(axis="y", linestyle="--", alpha=0.7)
# plt.show()


# from scipy.stats import binom

# n,p= 10, 0.5
# x=np.arange(0, n+1)
# y=binom.pmf(x,n,p)
# plt.bar(x,y, color="green")
# plt.title("Binomial Distribution")
# plt.show()


from scipy.stats import poisson

lam=3
x=np.arange(0,10)
y=poisson.pmf(x,lam)
plt.bar(x,y, color="blue")
plt.title("Poisson Distribution")
plt.show()
