import pandas as pd
#load Dataset
url="data.csv"
df=pd.read_csv(url)
#define Features and target

features=df[['record_id' , 'AverageTemperatureFahr']]
target=df['day']

print("Features: \n",features.head())
print("Target: \n",target.head())