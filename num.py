'''
NumPy is a Python library.

NumPy is used for working with arrays.

NumPy is short for "Numerical Python".
'''

import numpy

a = numpy.array([1,2,3,4,5])

print(a)


import numpy as np

b = np.array([0,9,8,7,6])

print(b)

print(np.__version__)
#numpy versions

print(type(b))
#type(): This built-in Python function tells us the type of the object passed to it

'''
Dimensions in Array

A dimension in arrays is one level of array depth (nested arrays).

nested array: are arrays that have arrays as their elements.

0-D Arrays
0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
'''

import numpy as np

arr = np.array(42)

print(arr)


'''
1-D Arrays
An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

These are the most common and basic arrays.
'''

import numpy as np

ar = np.array([1, 2, 3, 4, 5])

print(ar)


'''
2-D Arrays
An array that has 1-D arrays as its elements is called a 2-D array.

These are often used to represent matrix or 2nd order tensors.
'''

import numpy as np

brr = np.array([[1, 2, 3], [4, 5, 6]])

print(brr)

'''
3-D arrays
An array that has 2-D arrays (matrices) as its elements is called 3-D array.

These are often used to represent a 3rd order tensor.
'''

import numpy as np

crr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(crr)

'''
Check Number of Dimensions?
NumPy Arrays provides the ndim attribute 
that returns an integer that tells us how many dimensions the array have.
'''

import numpy as np

x = np.array(42)
y = np.array([1, 2, 3, 4, 5])
z = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(x.ndim)
print(y.ndim)
print(z.ndim)
print(d.ndim)