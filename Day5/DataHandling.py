import pandas as pd
data = pd.read_csv("students.csv")
type(data)

len(data)
data.head()
data.tail()
data.info()
data.describe()
data.value_counts()
data.loc[data['Name']=='Hema']

st = pd.Series(["Hema","Ishita","Shivangi","Shivansh"], index=[1,2,3,4])
st
import numpy as np
n1 = np.array([10,20,30,40,50])
n1
type(n1)

n2 = np.array([[10,20,30],[30,20,10]])
n2
type(n2)


n1= np.array([10,20])
n2= np.array([30,40])
np.sum([n1,n2])
