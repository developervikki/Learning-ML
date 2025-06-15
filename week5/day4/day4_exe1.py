import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report


#generate synthetic dataset

np.random.seed(42)
n_samples=200
x=np.random.rand(n_samples,2)*10

y = (x[:, 0] * 1.5 + x[:, 1] > 15).astype(int)




#create a dataframe
df=pd.DataFrame(x, columns=['Age', 'salary'])
df['Purchase']=y


#split data
X_train, X_test, Y_train, Y_test=train_test_split(df[['Age','salary']],df['Purchase'],test_size=0.2, random_state=42)

#train the logistic regression model

model=LogisticRegression()
model.fit(X_train,Y_train)

#make predictions
y_pred=model.predict(X_test)

#evalute
print("Accuracy: ", accuracy_score(Y_test,y_pred))
print("Precision: ", precision_score(Y_test,y_pred))
print("Recall: ", recall_score(Y_test,y_pred))
print("F1 Score: ", f1_score(Y_test,y_pred))
print("\nClassification Report: ", classification_report(Y_test,y_pred))



import matplotlib.pyplot as plt

#plot decision boundary
x_min, x_max= x['Age'].min()-1,x['Age'].max()+1
y_min, y_max= x['Salary'].min()-1,x['Salary'].max()+1
xx,yy =np.meshgrid(np.arrange(x_min, x_max, 0.1), np.arrange(y_min, y_max, 0.1))
#predict prob