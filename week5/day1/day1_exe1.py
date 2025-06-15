

import pandas as pd
from sklearn.model_selection import train_test_split
#load Dataset
url="data.csv"
df=pd.read_csv(url)
#define Features and target

features=df[['record_id' , 'AverageTemperatureFahr']]
target=df['day']

print("Features: \n",features.head())
print("Target: \n",target.head())

X_train, X_test, Y_train, Y_test = train_test_split(features, target, test_size=0.2, random_state=42)



print("Training dataset is : ", X_train.shape)
print("Testing dataset is : ", X_test.shape)