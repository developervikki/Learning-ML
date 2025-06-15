#load andExplore a sample dataset


import pandas as pd

#load dataset
df=pd.read_csv("data.csv")

#explore the structure

# print("First 5 Rows: \n",df.head())
# print("Last 5 Rows: \n",df.tail())

print(df.info())

print(df.describe())