'''What is Numpy?
Numpy is the fundamental package for scientific computing in python. It is a python library that provides
a multidimensional array object and various derived objects. It offers comprehensive mathematical functions,
random number generators and linear algebra routines and more

Why Numpy arrays?
Numpy offers powerful n-dimensional arrays, which are fast and versatile, and facilitate advanced mathematical
and other types of operations on large numbers of data. Numpy ararays perform better than Lists in:
Size, performance and functionality. Numpy arrays take up less space, provide optimized functions and are faster
than lists.

Limitations of Numpy?
1. Using “nan” in Numpy: “Nan” stands for “not a number”. It was designed to address the problem of missing values. 
NumPy itself supports “nan” but lack of cross-platform support within Python makes it difficult for the user. 
That’s why we may face problems when comparing values within the Python interpreter.
2. Require a contiguous allocation of memory: Insertion and deletion operations become costly as data is stored 
in contiguous memory locations as it requires shifting.

Installation requirement?
To install numpy, run the command- pip install numpy.
'''

#Creating numpy arrays
import numpy as np
a = np.array([1,2,3,5])
print(a)
a = np.array([10,20,30,40,50,60], dtype=object) #1D array
print("1D array\n",a)
a = np.zeros((1,2),dtype='i') #creates a 1x2 array filled with zeros
print(a)


#nd array objects
print(type(a)) #prints <class 'numpy.ndarray'> since its a nd array object
a = np.array([[10,20,30,40],[50,60,70,80]], dtype=object) #2D array
print("2D array\n",a)
print(type(a))
a = np.array([[[10,20,40,]],[[40,50,60]],[[60,70,80]]], dtype=object) #3-D array
print("3D array\n",a)
print(type(a))

#Memory layout of ndarray
'''An instance of class ndarray consists of a contiguous one-dimensional segment of 
computer memory (owned by the array, or by some other object), combined with an indexing
scheme that maps N integers into the location of an item in the block. 
The ranges in which the indices can vary is specified by the shape of the array. 
How many bytes each item takes and how the bytes are interpreted is defined by the 
data-type object associated with the array.
'''
n1 = np.array([[[1,2,5,7]],[[3,6,8,2]],[[3,3,6,8]]])
print("Array dimensions:", n1.shape) #returns a tuple of array dimensions
print("Number of elements in the array: ",n1.size)
print("Length of one array element in bytes:",n1.itemsize)
print("memory layout of the array: ",n1.flags)

#Indexing
n1 = np.array([10,20,30,60]) 
print("Indexing a one dimensional array: ", n1[2])
n2 = np.array([[10,20,40],[40,50,60]])
print("Indexing a two dimensional array: ",n2[1,2])
n3 = np.array([[[1,2,5,7]],[[3,6,8,2]],[[3,3,6,8]]])
print("Indexing a three dimensional array: ", n3[0,0,1])

#Slicing
a = np.array([10,20,40,70,50])
print(a[0:3]) 
print(a[-3:-1]) 
print(a[1:5:2]) 
print(a[1:]) 
print(a[:])

#Views and copies
'''The main difference between a copy and a view of an array is 
that the copy is a new array, i.e. a new reference of the original array 
is created and any changes made to the original array will not affect the copy
whereas the view is just a view of the original array, and changes made in it 
will affect the original array.
'''
a = np.array(['a','b','f','d','e'])
b = a.copy()
b[2] = 'c'
print(a) #['a' 'b' 'f' 'd' 'e']
print(b) #['a' 'b' 'c' 'd' 'e']
print(b.base) #None

'''Every NumPy array has the attribute base that returns None if the array owns the data.
Otherwise, the base  attribute refers to the original object.
'''
a = np.array([10,20,30,40,50])
b = a.view()
a[0] = 100
print(a) #[100  20  30  40  50]
print(b) #[100  20  30  40  50]
print(b.base) #[100  20  30  40  50]

#Array datatypes
'''NumPy has some extra data types, and refer to data types with one character,
like i for integers, u for unsigned integers etc.
The data types in Numpy are:
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
'''
a = np.array([10,20,30,40,50,60]) # we use dtype property to check the data type of a numpy array
print(a.dtype) #int32
print(type(a))

b = np.array(['a', 'b', 'c'])
print(b.dtype) #<U1

#while creating array using array() function, we can also specify the data type of the array elements
a = np.array([1, 2, 3, 4], dtype='S') #takes the given numbers in string
print(a.dtype) #|S1

#We can change the data type of an existing array, by making a copy of the array
#and using astype() method.
a = np.array([10,20,30,40,50,60]) # we use dtype property to check the data type of a numpy array
print(a.dtype) #int32
b = a.astype('float')
a = a.astype('float')
print(a.dtype)
print(b.dtype) #float64
b = np.array([1, 0, 3])
b = b.astype(bool)
print(b.dtype) #bool #here b refers to a copy, ie. a different reference of the original array b
