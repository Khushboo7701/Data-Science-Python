#1. This is a python comment.
import os


str = input("Enter your input:") # input function to read data from keyboard
print ("Received input is: ", str)

#2. IO using files
fo = open("file1.txt", "w+")
str = "We are learning IO in python.\nPython is a great language.\n"
fo.write(str)
str=fo.read()
print("Read String is: ",str)
str=fo.readline()
print("First line of file: ", str)
str=fo.readline()
print("Second line of file: ", str)
print("Contents of file:")
for line in fo:
    print(line, end='')
    
print ("Name of file: ", fo.name)
print ("Closed or not: ", fo.closed)
print ("Opening mode: ", fo.mode)
print ("Current position: ", fo.tell())



fo.close()

os.rename('file1.txt', 'file2.txt')
os.remove('file2.txt')

#3. Operators
a = 20 #assignment 
b = 10
print(a+b) #addition
print(a-b) #subtraction
print(a*b) #multiplication
print(a/b) #division

a = 10
b = 3
print(a%b) #modulus
print(a//b) #floor division

a+=2
print(a)
a-=2
print (a)
a*=2
print (a)
a/=2
print (a)

a = 10
b = 3
#logical operators
print(a>5 and b>5)
print(a>5 or b>5)
print(not(a>5 and b>5))


#4. namespace
#built-in
a=2
print("Id of a:", id(a))


a=10 #global
def fun(): #local
    a=2
    print(a)

fun()
print(a)

#To access global inside local
a=10
def fun():
    global a
    a=a+2
    print(a)
    
fun()
print(a)


#5. Some Useful Functions
a = 'Hello'
print(len(a))
a.upper()
print(a)
a.lower()
print(a)

print(abs(-4/3))
print(round(4/3))
print(min(2,5,1))
print(max(2,4,1))
a=[3,5,6,1,9]
print(sum(a))
print(sorted(a))
print(sorted(a, reverse=True))

#Find mean of given numbers using above functions
num = [1,2,5,6,4]
m = sum(num)/len(num)
print("Mean is: ", m)

a=2
type(a)

#6. Flow and loop

#Check if the number is odd or even
n=int(input("Enter the number"))
if n%2==0:
    print("Number is even")
else:
    print("Number is odd")

str = 'hello'
for i in str:
    print(i)

a=[1,4,2,5,6,9]
for x in a:
    print(x)

n=2
print("Printing table of 2:")
for x in range(1,11):
    print(n," * ",x, " = ", x*n)

#Print odd numbers less than 10
print("Odd numbers less than 10:")
n=1
while n<11:
    if n%2!=0:
        print(n)
    n+=1


#7. Data Types: str, bool, int, float, list, tuple, set
a=5 
print(type(a))
b=6.4
print(type(b))
#Type conversion
b=int(b)
print(b)

#8. List
a=[1,4,5,3,6,10]
#access
print(a[1])
for x in a:
    print (x)

a[1]=5
print(a[2:5])
a.append("last")
print(a)
b=[3,"second list"]
a.extend(b)
print(a)
a.remove("last")
print(a)
a.pop(1)
print(a)


#9. Tuple
a=[1,4,5,3,6,10]
#access
print(a[1])
for x in a:
    print (x)
print(a[2:5])
print(a)

#program to change a tuple value
x= ("v",1,2,"b")
y= list(x)
y[1] = "a"
x=tuple(y)
print(x)

#Program to join two tuples
a= (1,2,4)
b=(3,2,6)
c = a+b
print(c)

#unpack a tuple
fruits = ("apple","mango","cherry","banana")
(first, second, *third) = fruits
print(first)
print(second)
print(third)


#10. Dictionary
#Use dictionary to store an employee details
emp = {
"id":100,
"name":"Harry",
"email": "harry@gmail.com"
}
print(emp)
#accessing items
print(emp["name"])
for x in emp:
    print(emp[x])
#changing dictionary items
emp["id"]=101
print(emp)
#Program to add Harry's Dob in dictionary
emp.update({"dob":"20-04-1998"})
print(emp)
#Program to remove Harry's email from dictionary
emp.pop("email")
print(emp)

#Use nested dictionary to store details of 3 employees

emp1 = {
"id":100,
"name":"Harry",
"email": "harry@gmail.com"
}
emp2 = {
"id":101,
"name":"James",
"email": "james@gmail.com"
}
emp3 = {
"id":102,
"name":"John",
"email": "john@gmail.com"
}
emp = {"emp1":emp1, "emp2":emp2, "emp3":emp3}
print(emp)


#11. Strings
str = "Hello"
#accessing characters in a string
print(str[1])
for x in str:
    print(x)
#To find length of string
print(len(str))
#slice
a="Hello"
print(a[1:3])
print(a[1:])
print(a[:len(a)])
print(a[:])

a="Hello World"
print(a.upper())
print(a.lower())
a.replace('H','W')
print(a)

#program to concatenate two strings
a="Hello"
b="World"
print(a+b)

#string formatting
age=20
a='My age is: {}'
a.format(age)
print(a)