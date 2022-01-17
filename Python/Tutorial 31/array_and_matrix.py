from numpy import *
array1 =array([
    [1,2,3],
    [4,5,6]
])
array1 = array1.flatten()
array1 = array1.reshape(3,2)
matrix1 = matrix(array1)
print(matrix1)
print()
print(array1)
print(array1.shape)
print(array1.size)