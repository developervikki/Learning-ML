import numpy as np

a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])

#addition and subtraction

print("Addition: \n ",a+b)
print("subtraction: \n ",a-b)



# scalar multiplication
c=2*a
print("Scalar multiplication :\n",c)

# Matrix Multiplication
    # Formula: (a.b)ij=summetion of kAikBkj



result=np.dot(a,b)
print("matrix multiplication: \n",result)
  #indentity matrix
I=np.eye(3)
print("Indentity Matrix: \n", I)



#zero matrix

z=np.zeros((2,3))
print("Zero Matrix: \n",z)


#digonal matrix
d=np.diag([1,2,3])
print("Diagonal matrix: \n",d)

