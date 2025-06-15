import scipy.stats as stats

data= [10,20,30,40,50]
mean=sum(data)/len(data)


varience = sum((x-mean)**2 for x in data)/len(data)

std_dev=varience**0.5


sampele_mean=mean

z_score=1.96
ci=(sampele_mean- z_score*(std_dev /len(data)**0.5),
    sampele_mean +z_score *(std_dev/len(data)**0.5))

print("95 % confidence level ",ci)




# from statistics import mode

# data= [10,20,30,40,50]
# mean=sum(data)/len(data)
# print("Mean: ",mean)



# sorted_data= sorted(data)
# median=sorted_data[len(data)//2] if len(data) %2!=0 else \
#     (sorted_data[len(data)//2-1]+sorted_data[len(data)//2])/2
# print("Median: ",median)

# print("Mode: ",mode(data))

# #dispersion


# varience = sum((x-mean)**2 for x in data)/len(data)
# print("varience: ", varience)

# std_dev=varience**0.5

# print("Standard deviation: ",std_dev)




