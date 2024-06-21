'''
NumPy is a Python library.

NumPy is used for working with arrays.

NumPy is short for "Numerical Python".
'''

# import numpy

# a = numpy.array([1,2,3,4,5])

# print(a)


# import numpy as np

# b = np.array([0,9,8,7,6])

# print(b)

# print(np.__version__)
#numpy versions

# print(type(b))
#type(): This built-in Python function tells us the type of the object passed to it

'''
Dimensions in Array

A dimension in arrays is one level of array depth (nested arrays).

nested array: are arrays that have arrays as their elements.

0-D Arrays
0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
'''

# import numpy as np

# arr = np.array(42)

# print(arr)


'''
1-D Arrays
An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

These are the most common and basic arrays.
'''

# import numpy as np

# ar = np.array([1, 2, 3, 4, 5])

# print(ar)


'''
2-D Arrays
An array that has 1-D arrays as its elements is called a 2-D array.

These are often used to represent matrix or 2nd order tensors.
'''

# import numpy as np

# brr = np.array([[1, 2, 3], [4, 5, 6]])

# print(brr)

'''
3-D arrays
An array that has 2-D arrays (matrices) as its elements is called 3-D array.

These are often used to represent a 3rd order tensor.
'''

# import numpy as np

# crr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(crr)

'''
Check Number of Dimensions?
NumPy Arrays provides the ndim attribute 
that returns an integer that tells us how many dimensions the array have.
'''

# import numpy as np

# x = np.array(42)
# y = np.array([1, 2, 3, 4, 5])
# z = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(x.ndim)
# print(y.ndim)
# print(z.ndim)
# print(d.ndim)


'''
Higher Dimensional Array

An array can have any number of dimensions.

When the array is created, you can define the number of dimensions by using the ndmin argument.

'''

# import numpy as np

# arr = np.array([1, 2, 3, 4], ndmin=5)

# print(arr)
# print('number of dimensions :', arr.ndim)

'''
Access Array Elements
Array indexing is the same as accessing an array element.

You can access an array element by referring to its index number.

The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.
'''

# import numpy as np

# arr = np.array([1, 2, 3, 4])

# print(arr[0])
##############################################
'''
add two elements in the array
'''
# import numpy as np

# arr = np.array([1, 2, 3, 4])

# print(arr[2] + arr[3])

'''
Access 2-D Arrays
To access elements from 2-D arrays we can use comma separated 
integers representing the dimension and the index of the element.

Think of 2-D arrays like a table with rows and columns, 
where the dimension represents the row and the index represents the column.
'''
# import numpy as np

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print('2nd element on 1st row: ', arr[0, 1])

'''
what is the output of this
'''
# import numpy as np

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print('5th element on 2nd row: ', arr[1, 4])


'''
Access 3-D Arrays
To access elements from 3-D arrays we can use 
comma separated integers representing the dimensions and the index of the element.
'''

# import numpy as np

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# print(arr[0, 1, 2])


'''
Example Explained
arr[0, 1, 2] prints the value 6.

And this is why:

The first number represents the first dimension, which contains two arrays:
[[1, 2, 3], [4, 5, 6]]
and:
[[7, 8, 9], [10, 11, 12]]
Since we selected 0, we are left with the first array:
[[1, 2, 3], [4, 5, 6]]

The second number represents the second dimension, which also contains two arrays:
[1, 2, 3]
and:
[4, 5, 6]
Since we selected 1, we are left with the second array:
[4, 5, 6]

The third number represents the third dimension, which contains three values:
4
5
6
Since we selected 2, we end up with the third value:
6
'''

'''
Negative Indexing
Use negative indexing to access an array from the end.
'''

# import numpy as np

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print('Last element from 2nd dim: ', arr[1, -1])

'''
Numpy array Slicing
'''

'''
Slicing arrays
Slicing in python means taking elements from one given index to another given index.

We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].

If we don't pass start its considered 0

If we don't pass end its considered length of array in that dimension

If we don't pass step its considered 1

'''

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[1:5])


'''
Negative slicing
'''
# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[-3:-1])


'''
STEP
Use the step value to determine the step of the slicing:
'''

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[1:5:2])


'''
Slicing 2d array
'''
# import numpy as np

# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print(arr[1, 1:4])


'''
Data Types in Python
By default Python have these data types:

strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
integer - used to represent integer numbers. e.g. -1, -2, -3
float - used to represent real numbers. e.g. 1.2, 42.42
boolean - used to represent True or False.
complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j
Data Types in NumPy
NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )


'''


# import numpy as np

# arr = np.array(['apple', 'banana', 'cherry'])

# print(arr.dtype)


'''
Creating Arrays With a Defined Data Type
We use the array() function to create arrays, 
this function can take an optional argument: dtype 
that allows us to define the expected data type of the array elements:
'''

# import numpy as np

# arr = np.array([1, 2, 3, 4], dtype='S')

# print(arr)
# print(arr.dtype)

# import numpy as np

# arr = np.array([1, 2, 3, 4], dtype='i4')

# print(arr)
# print(arr.dtype)

'''
Random Numbers in Numpy

Random number does NOT mean a different number every time. 
Random means something that can not be predicted logically.
'''

'''
Generate Random Number
NumPy offers the random module to work with random numbers.
'''

# from numpy import random

# x = random.randint(100)

# print(x)

'''
Generate Random Float
The random module's rand() method returns a random float between 0 and 1.

Generate a random float from 0 to 1:
# '''
# from numpy import random

# x = random.rand()

# print(x)

'''
Generate Random Array
In NumPy we work with arrays, and you can use the two methods from the above examples to make random arrays.

Integers
The randint() method takes a size parameter where you can specify the shape of an array.

Example
Generate a 1-D array containing 5 random integers from 0 to 100:
'''
# from numpy import random

# x=random.randint(100, size=(5))

# print(x)

'''
generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
'''
# from numpy import random

# x = random.randint(100, size=(3, 5))

# print(x)

'''
Floats
The rand() method also allows you to specify the shape of the array.

Example
Generate a 1-D array containing 5 random floats:
'''
# from numpy import random

# x = random.rand(5)

# print(x)

'''
Generate Random Number From Array
The choice() method allows you to generate a random value based on an array of values.

The choice() method takes an array as a parameter and randomly returns one of the values.
'''

# from numpy import random

# x = random.choice([3, 5, 7, 9])

# print(x)



'''
The choice() method also allows you to return an array of values.

Add a size parameter to specify the shape of the array.

'''
# from numpy import random

# x = random.choice([3, 5, 7, 9], size=(3, 5))

# print(x)