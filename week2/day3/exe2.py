#select specific coloumns and filter rows

import pandas as pd


df=pd.read_csv("data.csv")

selected_coloumns=df[["record_id","month"]]
print("Selected coloumns: ",selected_coloumns)


#filter
filtered_rows=df[(df["month"]>6)]
print("filtered rows: ",filtered_rows)