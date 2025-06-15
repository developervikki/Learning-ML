import pandas as pd

df=df.rename(coloumns={"old_name": "new_name"})

df["coloumn_name"]= df["coloumn_name"].astype("float")

df["coloumn_name"]= pd.to_datetime(df["coloumn_name"]).astype("float")

df["new_coloumn"]=df["existing_coloumn"]*2



#combining and merging Dataframes

combined=pd.concat([df1,df2], axis=0)
combined=pd.concat([df1,df2], axis=1)

merged=pd.merge(df1, df2, on="common_coloumn")
merged=pd.merge(df1,df2, how="left", on="common_coloumn")
merged=pd.merge(df1,df2, how="left", on="common_coloumn")


joined=df1.join(df2, how="inner")











df=df.dropna()
df=df.dropna(axis=1)

df["coloumn_name"]=df["coloumn_name"].fillna(0)

df.fillna(method="ffill")
df.fillna(method="bfill")

df["coloumn_name"]=df["coloumn_name"].interpolate()

