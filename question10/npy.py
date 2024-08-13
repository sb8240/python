''' 
Numpy provides efficient storage (takes less space)
it is fast
provides better ways of handlig data for processing

'''
import numpy as np
my_arr = np.array([[2,4,5,7]], np.int8) # int8 specifies 8 bit of space for each element
print(my_arr[0,2])
print(my_arr.shape) # (1, 4) 1row 4columns
print(my_arr.dtype) # int8

# array creation from other python structures
list_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(list_array)
print(list_array.dtype)
print(list_array.size)
print(list_array.shape)

rng = np.arange(99)
print(rng)
reshape = rng.reshape(3, 33) # 3 x 33 = 99 
print(reshape)
zeros = np.zeros((2,3))
print(zeros)

lnspace = np.linspace(1,5,10) # will give elements beteween 1-5 linearly spaced by 10
print(lnspace)

identity = np.identity(6)
print(identity) # will return a identity matrix of 6 X 6

# numpy axis
# axis 0 = columns, axis 1 = rows

x = [[1,2,3],[6,5,4],[7,8,9]]
arry = np.array(x)
print(arry.argmax(axis=0))
print(arry.argsort()) # arrange elements in ascending oder
# you can perform matrics operations here
print(np.sqrt(arry))
print(arry*arry)
print(arry.sum())
print(arry.max()) # similarly min()
print(np.where(arry>5)) # returns an array of tuples consists of [column,row] where element >5
print(np.count_nonzero(arry)) # count how nmany non zero elements are there

print(arry)
print(arry.sum(axis=0))
print(arry.sum(axis=1))
print(arry.T) # transpose

# array.flat --> function is used as a 1_D iterator over N-dimensional arrays
for item in arry.flat:
    print(item)

print(arry.ndim)
print(arry.size) # print how many elements in the array
print(arry.nbytes) # shows how many bytes
one = np.array([1,2,3,4567,5,8])
print(one.argmax()) # return the index where the max value is, similarly argmin() return the index of min value
print(one.argsort()) # returns the index oder in which the original array will be sorted

import sys
py_ar = [0,45,6,7]
np_ar = np.array(py_ar)

print(sys.getsizeof(1)*len(py_ar))
print(np_ar.itemsize*np_ar.size)


