#clean a dataset by handling missing values and remaining columns

import pandas as pd
import numpy as np

#create a dataset
data={
    "Name":["Vikash", "Satish", np.nan, "Rajan"],
    "Age": [25,np.nan, 30,35],
    "score": [85,90,np.nan,88],
}

df=pd.DataFrame(data)

print("original dataset: \n ",df)

df["Age"]=df["Age"].fillna(df["Age"].mean)
df["score"]=df["score"].interpolate()





df=df.rename(columns={"Name":"Student_Name","score": "Exam:score"})

print("Dataset : \n", df)