#expolre special matrix


import numpy as np

#identity matrix
I=np.eye(3)
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("A X I: \n", np.dot(a,I))




#diagonal matrix and zero matrix 

d=np.diag([1,2,3])
z=np.zeros((3,3))

print("Diagonal Matrix: \n",d)
print("Zero Matrix: \n",z)