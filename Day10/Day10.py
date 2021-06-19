import pandas as pd
import numpy as np

#accessing series
d = {'a':'1.2', 'b':'2.0', 'c':'3.9', 'd':'5.3', 'e':'6.2'}
s = pd.Series(d) 
print(s) 

print("Series element at position 3: ", s[3])
print("Series element at index d: ", s['d']) 

#Accessing a multiple element using index label
print(s[[0,2,4]])
print(s[['a','b','c']])

#accessing data frame 
d = {'EmpId' : ['E01','E02','E03','E04'],    
       'EmpName' : ['Raj','Atul','Reena','Ayushi'],    
       'Department' : ['IT','IT','HR','Accounts']}    
df = pd.DataFrame(d, index=['First','Second','Third','Fourth']) 


#selecting columns
print(df.EmpName['Third']) #Accessing using row name
print(df.EmpName[2]) #accessing using row index  

print(df.at['Second','Department']) #using at function
print(df.iat[1,2]) #using iat function

print(df["EmpName"]) #accessing whole column
print(df.EmpName)

print(df[['EmpName','Department']])
print(df.EmpName,df.Department)

#accessing rows
print(df.loc[['Second']])
print(df.iloc[[2]])

#reading and writing data
#read_csv is used to read data from a csv file
data = pd.read_csv('GamesSales.csv', index_col=0)
# df = pd.DataFrame(data)
print("Values in file are :-----------------------------", df)

print(df.columns)
print(df.index)
print(df.head(5))
print(df.tail(5))

#to_csv is used to store data to a new csv file
s = df.to_csv('data2.csv')
with open('data2.csv','r') as newfile:
       print("Contents of new file are: ",newfile.read())

#reading from a text file
with open("data.txt","r") as file:
       df = pd.DataFrame(file, index=None)
print(df)


#indexing and slicing pandas data frames
d = {'EmpId' : ['E01','E02','E03','E04','E05'],    
       'EmpName' : ['Raj','Atul','Reena','Ayushi','Khushi'],    
       'Department' : ['IT','IT','HR','Accounts','Sales'],
       'Gender': ['Male','Male','Female','Female','Female']}
df = pd.DataFrame(d, index=[1,2,3,4,5]) 
print(df['EmpId'])
print(df[['EmpId','EmpName']])
print(df.EmpName[2])

#using loc and iloc
print(df.loc[:])
print(df.loc[0:2,:])
print(" ....", df.loc[2:4,'EmpId':'Department'])

print(df.iloc[2:5,0:2])
print(df.iloc[:,1:4])

#changing data using iloc
df.iloc[1]={'EmpId':'E02', 'EmpName':'Rajat','Department':'Marketing','Gender':'Male'}
print(df)

print(df.loc[1:3])

#cleaning data
'''
Bad data could be:
Empty cells
Data in wrong format
Wrong data
Duplicates
We can deal with bad data in pandas using following methods:
'''

data = pd.read_csv('GamesSales.csv', index_col=0)
df = pd.DataFrame(data)

# drop missing values
print(df.dropna(subset=["Year"],axis=0))
print(df.dropna(axis=1))

# removing rows
print(df.dropna(inplace=True))
df=df[~df.isna().any(axis=1)]
print(df)

# replacing values
meanval = df["Year"].mean()
df["Year"].replace(np.nan, meanval)
print(df)
modeval = df["Year"].mode()[0]
df["Year"].replace(np.nan, modeval)
print(df)
medianval = df["Year"].median()
df["Year"].replace(np.nan, medianval)
print(df)

# removing duplicates
df.drop_duplicates(inplace=True)

#Data aggregation
'''Dataframe.aggregate() function is used to apply some aggregation across one or more column. 
Aggregate using callable, string, dict, or list of string/callables.
Most frequently used aggregations are:
sum: Return the sum of the values for the requested axis
min: Return the minimum of the values for the requested axis
max: Return the maximum of the values for the requested axis
'''

data = pd.read_csv('GamesSales.csv', index_col=0)
df = pd.DataFrame(data)
print(df.aggregate(['sum','min','max']))
print(df.aggregate({"Year":['min','max'],
              "Rest of World":['min', 'max'],
              "Global":['min', 'max','sum'], 
              }))

#Data merging
'''merge() for combining data on common columns or indices
'''
d = {'EmpId' : ['E01','E02','E03','E04','E05'],    
       'EmpName' : ['Raj','Atul','Reena','Ayushi','Khushi'],    
       'Department' : ['IT','IT','HR','Accounts','Sales'],
       'Gender': ['Male','Male','Female','Female','Female']}
df1 = pd.DataFrame(d, index=[1,2,3,4,5]) 
d = {'EmpId' : ['E06','E07','E03','E08','E09'],    
       'EmpName' : ['Rahul','Rohit','Reena','Swati','Payal'],    
       'Department' : ['Sales','IT','HR','Marketing','Sales'],
       'Gender': ['Male','Male','Female','Female','Female']}
df2 = pd.DataFrame(d, index=[6,7,3,8,9]) 
print(df1)
print(df2)

print("Using key:\n", pd.merge(df1,df2,on='EmpId'))   #
print("Using multiple keys:\n", pd.merge(df1,df2,on=['EmpId','EmpName']))   #Merging 2 dataframe on multiple key

print("Using left join:\n", pd.merge(df1, df2, on='EmpName', how='left'))    
print("Using right join:\n", pd.merge(df1, df2, on='EmpName', how='right'))   
print("Using intersection keys:\n", pd.merge(df1, df2, on='EmpName', how='inner'))   
print("Using union of keys:\n", pd.merge(df1, df2, on='EmpName', how='outer'))   

