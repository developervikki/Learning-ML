import numpy as np

import matplotlib.pyplot as plt


#sigmoid function
def sigmoid(z):
    return 1/(1+np.exp(-z))

#generate values
z=np.linspace(-10,10,100)
sigmoid_values=sigmoid(z)

#plot
plt.plot(z,sigmoid_values)
plt.title("sigmoid Function")
plt.xlabel("z")
plt.ylabel("sigma(z)")
plt.grid()
plt.show()