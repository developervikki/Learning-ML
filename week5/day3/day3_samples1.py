import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

#generate Synthetic Data
np.random.seed(2)
x=np.random.rand(100,1)*10
y=3*x**2+2*x+np.random.randn(100,1)*5
#transform features to polynomials
poly_features= PolynomialFeatures(degree=2, include_bias=False)
x_poly=poly_features.fit_transform(x)

#fit polynomial Regression

model=LinearRegression()
model.fit(x_poly,y)
y_pred=model.predict(x_poly)

#plot the result

plt.scatter(x,y, color="blue", label="actual")
plt.scatter(x,y_pred, color="red", label="Predicted Data")
plt.title("Polynomial Regression")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()


#evaluate Model
mse=mean_absolute_error(y,y_pred)
print("Mean Square Error (MSE): ",mse)