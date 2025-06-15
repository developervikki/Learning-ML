#group data by categorical colomn 

import pandas as pd

data={
    "class":["A","B","C","D","E"],
    "Score":[85,90,88,72,95,80],
    "Age":[15,16,15,17,16,15]
    
}


df=pd.DataFrame(data)
print("Original Dataset:\n",df)


grouped=df.groupby("class").mean()
print(grouped)


