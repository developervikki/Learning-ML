#grouping Data by categories

grouped=df.groupby("Coloumn_name")

for name, group in grouped:
    print(name)
    print(group)
    
grouped.mean()
grouped.sum()


#aggregation 

df.groupby("Category_coloumn")["numeric_coloumn"].mean()
df.groupby("category_coloumn").agg({"numeric_coloumn": ["mean","max","min"]})




pivot=df.pivot_table(
    values="numeric_coloumn",
    index="category_coloumn",
    aggfunc="mean"
)






def rang_func(x):
    return x.max()-x.min()


df.groupby("category_coloumn")["numeric_coloumn"].agg(rang_func)
