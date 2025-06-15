import pandas as pd





#loading data from CSV, EXCEL, and other sources

df=pd.read_csv("data.csv")
df=pd.read_excel("data.xlsx")


# #saving data 

# df.to_csv("data.csv")
# df.to_excel("data.xlsx")

# # s=pd.Series([10,20,30], index=["a","b","c"])
# # print(s)


# # data = {"Name": ["Vikash","Satish"],"Age": [25,30]}
# # df=pd.DataFrame(data)
# # print(df)


#basic dataframe operations

#viewing data
print(df.head())
print(df.tail(3))



print(df.info())
print(df.describe())


print(df[["Name","Age"]])

Print(df[df["Age"]>25])


print(df.iloc[0])
print(df.iloc[:,0])




print(df.loc[0])
print(df.loc[:,"Name"])