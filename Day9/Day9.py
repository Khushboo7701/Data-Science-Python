#Introduction to Pandas
'''Pandas is a free open source library written for the Python programming language for 
data manipulation and analysis. 
It offers data structures and operations for manipulating numerical tables and time series.
'''

#Pandas data structures
'''Pandas deals with the following three data structures −
Series - 1D labeled homogeneous array, size is immutable.
DataFrame - General 2D labeled, size-mutable tabular structure with potentially heterogeneously typed columns.
Panel - General 3D labeled, size-mutable array.
These data structures are built on top of Numpy array, which means they are fast.
'''

from numpy.lib.index_tricks import AxisConcatenator
import pandas as pd
import numpy as np
#Series
'''Series is a one-dimensional array like structure with homogeneous data.'''

s= pd.Series(dtype='float64') #empty series of type float
print(s) #Series([], dtype: float64)
print(s.index) #Index([], dtype='object')

s = pd.Series(np.arange(5), index=['a','b','c','d','e']) #creating series from ndarray
print(s)
print(s.index)

d = {'a':'1.2', 'b':'2.0', 'c':'3.9', 'd':'5.3', 'e':'6.2'}
s = pd.Series(d) #creating series from dictionary
print(s) 
print(s.index)

print("Series element at position 3: ", s[3]) #accessing element in series
print(s[3:]) 
print("Series element at index d: ", s['d']) #accessing element using index

s = pd.Series(6, index=['a','b','c','d','e']) #creating series from scalar value
print(s) 
print(s.index)

#Dataframe
'''DataFrame is a two-dimensional array with heterogeneous data.'''
l = ['english','computer','mathematics'] #from list
df = pd.DataFrame(l)
print(df)

l = [['english','literature'],['hindi','sanskrit'],['computer','mathematics']] #from list of lists
df = pd.DataFrame(l)
print(df)

d = {"one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]), "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),}
df = pd.DataFrame(d) #from dict of Series
print(df)
df = pd.DataFrame(d, index=["d", "b", "a","c"], columns=["two", "one"])
print(df)

d = {"one": [1.0, 2.0, 3.0, 4.0], "two": [4.0, 3.0, 2.0, 1.0]} #from dict of ndarrays
df = pd.DataFrame(d)
print(df)

#selecting columns
print(df["one"])
#indexing a dataframe using loc
d = {"one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]), "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),}
df = pd.DataFrame(d, index=["d", "b", "a"], columns=["two", "one"])
first = df.loc["a"]
second = df.loc["d"]
print(first,"-",second)

#Panel
'''Panel is a three-dimensional data structure with heterogeneous data. 
It is hard to represent the panel in graphical representation. 
But a panel can be illustrated as a container of DataFrame.'''

# d = np.random.rand(2,4,5)
# p = pd.Panel(d) #from ndarrays
# print(p)

# #from dict of dataframes
# d = {"one" : pd.DataFrame(np.random.randn(4, 3)), "two" : pd.DataFrame(np.random.randn(4, 2))}
# p = pd.Panel(d)
# print(p)

# #accessing element
# print(p["one"])

# #accessing using major axis
# print(p.major_xs(1))
# #accessing using minor axis
# print(p.minor_xs(1)) 

#creating dataframe from text file
with open("data.txt","r") as file:
    df = pd.DataFrame(file, index=None)
print(df)

#creating dataframe from csv file
df = pd.read_csv('GamesSales.csv')
print(df.to_string())

#creating dataframe from database
import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="8179",
    database="db2")

df = pd.read_sql("select * from employee;", con)
print(df)

# #creating dataframe from api
# import requests
# r = requests.get('https://api.box.com/2.0/files/:file_id/content/')
# x = r.json()
# df = pd.DataFrame(x['content'])
# print(df)

#creating dataframe from dataframe object
d1 = pd.DataFrame(df)
d2 = pd.DataFrame({'EMPNO':['17'], 'ENAME':['Khushboo'],'JOB':['MANAGER'],'HIREDATE':['2021-03-06'],'SAL':['30000'],'COMM':['None'],'DEPTNO':['3']})
df2=d1.append(d2)
print(df2)

#Examining the data
data = pd.read_csv('GamesSales.csv')
print(data.head())
print(data.head(4))
print(data.tail(5))

#describing and summarizing the data
print(data.describe())
print(data.describe(include=['object']))
print(data.describe(include='all'))
print(data.info())
print(data.shape)
print(data.columns)
print("Count ",data.count)
print("Minimum ",data.min())
print("Maximum ",data.max())
print("Mean ",data.mean())
print("Median ",data.median())

