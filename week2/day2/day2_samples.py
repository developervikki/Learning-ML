import numpy as np


np.random.seed(42)

random_array=np.random.rand(3,3)
print("Random Array: \n",random_array)



random_integers=np.random.randint(0,10, size=(2,3))
print("Random Integers: ",random_integers)











# #bolean indexing

# arr=np.array([1,2,3,4,5,6])
# even=arr[arr%2==0]
# print("Evens: ",even)



# arr[arr>3]=0
# print("Modified Arrays: ",arr)


# arr=np.array([[1,2,3],[4,5,6]])

# print("sum: ",np.sum(arr))

# print("Mean", np.mean(arr))
# print("Max", np.max(arr))
# print("Min", np.min(arr))
# print("Standard Deviation", np.std(arr))
# print("sum along rows", np.sum(arr,axis=1))
# print("sum along coloumn", np.sum(arr,axis=0))



# #array and scaler broadcasting
# arr=np.array([1,2,3])
# print(arr+10)


# matrix=np.array([[1,2,3],[4,5,6]])
# vector=np.array([1,0,1])
# print(matrix+vector)