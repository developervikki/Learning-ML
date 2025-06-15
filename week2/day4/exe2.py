import pandas as pd
import numpy as np



df1=pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Vikash","Satish","Rajan"],
    "Age":[25,30,35]
})

df2=pd.DataFrame({
    "ID":[1,2,3],
    "score":[58,90,88],
    
})



print("dataset 1: \n",df1)
print("dataset 2: \n",df2)


merged=pd.merge(df1,df2, how="inner",on="ID")
print("Merged Dataset: \n",merged)

merged["score_percentage"]=(merged["score"]/100)*100
print("Transformed Dataset \n",merged)