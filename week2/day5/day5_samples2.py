#calculating summary statics for grouped Data
#common satatics
#mean
#max
#min



def rang_func(x):
    return x.max()-x.min()


df.groupby("category_coloumn")["numeric_coloumn"].mean(rang_func)
df.groupby("category_coloumn")["numeric_coloumn"].max(rang_func)
df.groupby("category_coloumn")["numeric_coloumn"].min(rang_func)


df.groupby("category_coloumn").agg({"numeric_coloumn": ["mean","max","min"]})




