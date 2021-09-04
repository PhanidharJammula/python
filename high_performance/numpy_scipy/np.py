import numpy as np

array1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(array1)

print(array1.shape)
print(type(array1))
print(np.arange(0, 6, 0.5))

# slicing
print(array1[:, :2])
print(array1[0:2, 1:3])

# numpy functions
print(np.zeros([3, 4]))
print(np.eye(3))
print(np.eye(2, 1))

# integer indexing
print(array1[[0, 1, 2], [1, 2, 3]])

# boolean masking
bool_mask = array1%2==0
print(bool_mask)
print(array1[bool_mask])

# operations
print(array1 *2)
print(array1 ** 4)
array2 = np.array([0, 7, 8, 3])
print(array1+array2)
print(np.multiply(array1, array2))

# broadcasting
arr2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr2d*2)
add_array = np.array([1, 2, 3, 4])
print(array1+add_array)

print("===")

def do_some_op(arr1, arr2):
    #arr3 = []
    #for idx in range(0, len(arr1)):
    #    arr3.append(arr1[idx] + arr2[idx] + idx)

    idx_array = np.arange(arr1.size)
    arr3 = arr1 + arr2 + idx_array

    return arr3

arr1 = np.random.random(500)
arr2 = np.random.random(500)

print(len(do_some_op(arr1, arr2)))

