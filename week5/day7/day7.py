#task: Perform EDA and Preprocessing


import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing 

#load Data
data=fetch_california_housing(as_frame=True)
df=data.frame

#inspect data

print(df.info())
print(df.describe())


#visualize relationships
sns.pairplot(df, vars=['MedInc','AveRooms','HouseAge', 'MedHouseVal'])
plt.show()

#check For Missing Values
print("Missing Values: \n", df.isnull().sum())


