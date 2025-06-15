from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, KFold
from sklearn.ensemble import RandomForestClassifier

#load datset
data=load_iris()
x,y= data.data, data.target

#initiliaze classifier 
model=RandomForestClassifier(random_state=2)

#perform K-Fold Cross-validation

kf=KFold(n_splits=5,shuffle=True, random_state=42)
cv_scores=cross_val_score(model,x, y, cv=kf, scoring="accuracy" )


# print result 
print("Cross-Validation score: ",cv_scores)
print("Mean Accuracy: ", cv_scores.mean())