import numpy as np

#simulating 10,000 dice rolls

rolls=np.random.randint(1,7, size=10000)


#calculate probability
p_even=np.sum(rolls%2==0)/len(rolls)
p_generator_than_4=np.sum(rolls>4)/len(rolls)


print("P(Even): ",p_even)
print("P(Greater than 4): ",p_generator_than_4)