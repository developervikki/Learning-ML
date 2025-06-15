import matplotlib.pyplot as plt


#scatter plot
x=[1,2,3,4,5]
y=[10,12,25,30,45]

plt.scatter(x,y, label="Trend" , color="red", linestyle="--",marker="o")
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(["Dataset 1"])
plt.show()














#basic plot

# x=[1,2,3,4]
# y=[10,20,30,40]
# plt.plot(x,y)
# plt.show

#basic plot

#line plot
# plt.plot([1,2,3],[10,20,30],label="Trend")
# plt.title("Line Plot")

# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.legend()
# plt.show()



#bar chart
# categories=["A","B","C"]
# values=[10,15,7]
# plt.bar(categories,values,color="red")
# plt.title("Bar Chart")
# plt.show()


#histogram

# data=[1,2,2,3,3,3,4,4,4,4]
# plt.hist(data, bins=4,color="green",edgecolor="black")
# plt.title("Histogram")
# plt.show()