from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report


#load Iris Datase

data=load_iris()
x,y=data.data, data.target

#split dataset

x_train, x_test, y_train, y_test= train_test_split(x,y,test_size=0.2, random_state=42)


#scale the features

scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)


#Experiment with different alues for k

for k in range (1,11):
    #initiliaze K-NN Model
    knn=KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    
    #predict on test data
    y_pred=knn.predict(x_test)
    accuracy=accuracy_score(y_test, y_pred)
    print(f"K={k}, Accuracy={accuracy:.2f}")