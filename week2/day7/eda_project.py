#data manipulation and vizualization for EDA

import pandas as pd
#load titanic dataset
url="data.csv"
df=pd.read_csv(url)



#inspect the data

print(df.info())
print(df.describe())


#handle the missing values

df["Age"]=df["Age"].fillna(df["Age"].median())
df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])



#remove dublicates

df=df.drop_duplicates()

#filter data : 

