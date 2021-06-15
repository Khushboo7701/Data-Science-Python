#1. Linear Algebra in Numpy
'''NumPy package contains numpy.linalg module that provides all the functionality required for linear algebra.
This module offers various methods to apply linear algebra on any numpy array.
We can find:
rank, determinant, trace, etc. of an array.
eigen values of matrices
matrix and vector products (dot, inner, outer,etc. product), matrix exponentiation
solve linear or tensor equations and much more!
'''

import numpy as np
 
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
 
# Rank of a matrix
print("Rank of A:", np.linalg.matrix_rank(A))
 
# Trace of matrix A
print("\nTrace of A:", np.trace(A))
 
# Determinant of a matrix
print("\nDeterminant of A:", np.linalg.det(A))
 
# Inverse of matrix A
print("\nInverse of A:\n", np.linalg.inv(A))
 
print("\nMatrix A raised to power 3:\n",
           np.linalg.matrix_power(A, 3))

'''
This function returns the dot product of two arrays.
For 2-D vectors, it is the equivalent to matrix multiplication.
For 1-D arrays, it is the inner product of the vectors. 
For N-dimensional arrays, it is a sum product over the last axis
of a and the second-last axis of b.
'''
a = np.array([[1,2],[3,4]]) 
b = np.array([[11,12],[13,14]]) 
np.dot(a,b) 

'''This function returns the dot product of the two vectors.
If the first argument is complex, then its conjugate is used for calculation.
If the argument id is multi-dimensional array, it is flattened.
'''
a = np.array([[1,2],[3,4]]) 
b = np.array([[11,12],[13,14]]) 
print (np.vdot(a,b))

'''This function returns the inner product of vectors for 1-D arrays. 
For higher dimensions, it returns the sum product over the last axes.
'''
print (np.inner(np.array([1,2,3]),np.array([0,1,0])))

'This function calculates the determinant of the input matrix.'
a = np.array([[1,2], [3,4]]) 
print (np.linalg.det(a))

'This function calculates the inverse of a matrix'
x = np.array([[1,2],[3,4]]) 
y = np.linalg.inv(x) 
print (x) 
print (y)
print (np.dot(x,y))

'This  function returns the matrix product of two arrays'
a = [[1,0],[0,1]] 
b = [[4,1],[2,2]] 
print (np.matmul(a,b))


#2.Using numpy arrays
#ndarrays, indexing, slicing and copying already covered.
a = np.arange(1, 10) #fills array with numbers from 1 to 9
print(a) 
a = a.reshape((3, 3)) #if we want to reshape the array and put it in a 3x3 matrix
print(a)

a = np.random.randint(100,200,10) #fills the array with 10 random integer values between 100 and 200
print(a)

#concatenation
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
print(np.concatenate([x, y]))

x = np.array([1, 2, 3])
y = np.array([[9, 8, 7],
                 [6, 5, 4]])

# vertically stack the arrays
print(np.vstack([x, y]))

# horizontally stack the arrays
z = np.array([[10],
              [11]])
print(np.hstack([y,z]))

#splitting
x = [1, 2, 3, 5, 7, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 6])
print(x1, x2, x3)

#vertical splitting
g = np.array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]])
x,y = np.vsplit(g, [2])
print(x)
print(y)

#horizontal splitting
x,y = np.hsplit(g, [2])
print(x)
print(y)

# 3.Vectorized Operations
'''The concept of vectorized operations on NumPy allows the use of more
optimal and pre-compiled functions and mathematical operations on NumPy
array objects and data sequences, thus resulting in greater speed.
'''
#vectorized sum
print(np.sum(np.arange(150)))

#vectorized exponential
print(np.exp(np.arange(150)))

#vectorized difference
print(np.diff(np.array([1,5,8,9])))

#vectorized product
a = np.array([1, 2, 4, 8])
b = np.array([5, 6, 2, 9])
print(np.prod([a, b], axis=1))

# 4. Broadcasting and shape manipulation
'''The term broadcasting refers to the ability of NumPy
to treat arrays of different shapes during arithmetic operations.
Arithmetic operations on arrays are usually done on corresponding elements.
If two arrays are of exactly the same shape, then these operations are smoothly performed.
Operations on arrays of non-similar shapes is still possible in NumPy, because of the broadcasting capability.
'''
a = np.array([1,2,3,4]) 
b = np.array([10,20,30,40]) 
c = a * b 
print (c)

a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]]) 
b = np.array([1.0,2.0,3.0]) 
print("Sum of arrays: ", (a+b))

'The reshape() function is used to give a new shape to an array without changing its data.'
print(np.reshape(a, (6,2)))

# 5. Boolean Masks
'Boolean arrays can be used as masks, to select particular subsets of the data themselves.'
a = np.array([[5, 0, 3, 3],
       [7, 9, 3, 5],
       [2, 4, 7, 6]])
print(a<5)
'To select these values from the Boolean array, this is known as a masking operation:'
print(a[a < 5])
#or
filter_a = a<5
new_a = a[filter_a]
print(filter_a)
print(new_a)

# 6. Universal function
'''Universal functions in Numpy are simple mathematical functions. 
It is just a term that we gave to mathematical functions in the Numpy library. 
Numpy provides various universal functions that cover a wide variety of operations.
'''
a = np.array([50.7, 52.5, 50, 58, 55.63, 73.25, 49.5, 45])

#returns minimum or maximum of an array or along an axis
print(np.amin(a), np.amax(a))

#returns range of values (maximum-minimum) of an array or along an axis
print(np.ptp(a))

#calculate pth percentile of array or along specified axis
print(np.percentile(a, 70))

#compute mean of data along specified axis
print(np.mean(a))

#compute median of data along specified axis
print(np.median(a))

#compute standard deviation of data along specified axis
print(np.std(a))

#compute variance of data along specified axis
print(np.var(a))

#compute average of data along specified axis
print(np.average(a))

a= np.array([0, 2, 4, 6, 8, 16, 32])
b = np.array([1, 3, 5, 7, 9, 17, 33])

#performs bitwise and operation on two array elements
print(np.bitwise_and(a, b))

#performs bitwise or operation on two array elements
print(np.bitwise_or(a, b))

#performs bitwise xor operation on two array elements
print(np.bitwise_xor(a, b))

#performs bitwise inversion of an array elements
print(np.invert(a))

#shift the bits of elements to left
print(np.left_shift(a, 1))

#shift the bits of elements to left
print(np.right_shift(a, 1))

# 7. Date and time
'''With the help of numpy.datetime64() method,
we can get the date in a numpy array in a particular format 
i.e year-month-day by using numpy.datetime64() method.
'''

g = np.array(np.datetime64('2019-08-26'))
  
print(g)
print(type(g))

g = np.array(np.datetime64('2019-08', 'D'))
print(g)
print(type(g))

#using the dateutil module, we can parse dates from a variety of string formats
from dateutil import parser
date = parser.parse("4th of July, 2019")
print(date)

#date time arithmetic
np.datetime64('2000-05') + np.timedelta64(15, 'D')
date = np.datetime64('2000-05-16')
print(date)