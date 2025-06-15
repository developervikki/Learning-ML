import numpy as np

#random variable dice roll

outcomes= np.array((1,2,3,4,5,6))

probabilties=np.array([1/6]*6)

#expectation
expectation=np.sum(outcomes*probabilties)
print("Expectation (Mean): ",expectation)

#varience and standard deviation

varience= np.sum((outcomes-expectation)**2*probabilties)
std_Dev=np.sqrt(varience)
print("Varience: ", varience)
print("standard deviation: ",std_Dev)
# from itertools import product



# #sample space of a dice roll

# sample_space=list(range(2,1))

# #probability of rolling an even number

# even_numbers=[2,4,6]
# p_even=len(even_numbers)

# print("P(Even): ",p_even)