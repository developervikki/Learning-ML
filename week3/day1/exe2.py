#matrix vector multiplication


import numpy as np

#create matrix and vector

m=np.array([[1,2,3],[4,5,6],[7,8,9]])
v=np.array([1,0,-1])


# matrix vector multiplication

result=np.dot(m,v)
print("matrix vector multiplication: \n",result)