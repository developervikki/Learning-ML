import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import uniform


#discrete random variable : dice roll

# outcomes=[1,2,3,4,5,6]

# probabilities=[1/6]*6
# plt.bar(outcomes,probabilities,color="Red", alpha=0.7)
# print("PMF of a Dice roll")
# plt.xlabel("outcomes")
# print("probability")
# plt.show()



#continuous random variable: uniform distributions
x = np.linspace(0, 1, 100)
pdf = uniform.pdf(x, loc=0, scale=1)

# Plot the PDF
plt.plot(x, pdf, color="red")
plt.title("PDF of Uniform(0,1)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()

