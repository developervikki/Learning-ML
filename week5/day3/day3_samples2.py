from sklearn.linear_model import Ridge,Lasso
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

#generate Synthetic Data
np.random.seed(2)
x=np.random.rand(100,1)*10
y=3*x**2+2*x+np.random.randn(100,1)*5
#transform features to polynomials
poly_features= PolynomialFeatures(degree=2, include_bias=False)
x_poly=poly_features.fit_transform(x)


x_train, x_test, y_train, y_test=train_test_split(x_poly,y, test_size=0.2, random_state=42)

#ridge  Regression
ridge_model=Ridge(alpha=1)
ridge_model.fit(x_train,y_train)
ridge_predictions=ridge_model.predict(x_test)






#lasso Regression
lasso_model=Lasso(alpha=1)
lasso_model.fit(x_train,y_train)
lasso_predictions=lasso_model.predict(x_test)

#evaluate Ridge
ridge_mse=mean_absolute_error(y_test,ridge_predictions )
print("Ridge Regression MSE: ",ridge_mse)


#Evaluate Lasso
lasso_mse=mean_absolute_error(y_test,lasso_predictions )
print("Lasso Regression MSE: ",lasso_mse)