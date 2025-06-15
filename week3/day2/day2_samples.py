import numpy as np

a=np.array([[2,3],[1,4]])

detement=np.linalg.det(a)
# print("Determinant: \n",detement)

U,S,vt= np.linalg.svd(a)
print("U: \n",U)
print("Singular Values: \n",S)
print("V Transpose: \n",vt)

#inverse of a determinant


# inverse=np.linalg.inv(a)
# print("Inverse of A: \n",inverse)


# #eigenvalues and eigenvectors

# eigenvalues, eigenvectors =np.linalg.eig(a)
# print("Eigenvalues :\n",eigenvalues)
# print("Eigenvvectors :\n",eigenvectors)