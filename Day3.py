#Functions and modules
# 1. User defined function to check if a string is palindrome
def isPalindrome(s):
    st = s[::-1]

    if st==s:
        return "Yes"
    else:
        return "NO"

print(isPalindrome("3200"))

# 2. Function with default values
def intern(firstname,lastname,domain='Data Science'):
     print(firstname, lastname, ' is an intern in ', domain)

intern('Khushboo','Gupta','Data Science')
intern('Khushboo','Gupta')    

# 3. Define a module for finding factorial of 5
import factorial 
f = factorial.fact(5)
print(f)

# 4. Find factorial of 5 by importing fact function from factorial module
from factorial import fact
f = fact(5)
print(f)

# 5. Import module factorial and use it by renaming it as facto
import factorial as facto
f = facto.fact(10)
print("Factorial of 10 is ",f)


#List comprehension
# 1. Store the squares of numbers from 1 to 5 in a list.
squares = [x**2 for x in range(1,6)]
print("Squares of numbers from 1 to 5: ", squares) # [1,4,9,16,25]

# 2. Store tuples in new list based on given condition
d = [(x,y) for x in [1,2,3,4] for y in [1,2,3,4] if x!=y]
print(d) #[(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]

# 3. Nested list comprehension
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
d = [[row[i] for row in matrix] for i in range(4)]
print(d) #[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


# 4. Store the characters of a string in upper case in a list 
str = "Hello World"
str = [x.upper() for x in str]
print(str)

# 5. Store the names of, if its Khushboo store "name"
list1 = ["Khushboo","Nancy","Aakriti","Omkar","Sripad"]
newlist = [x if x!="Khushboo" else "name" for x in list1]
print(newlist)


#Iterators
# Program to create an iterator for an iterable string object and print the values
str ="Khushboo"
myit = iter(str)
print(next(myit)) #K
print(next(myit)) #h
print(next(myit)) #u
print(next(myit)) #s
print(next(myit)) #h
print(next(myit)) #b
print(next(myit)) #o
print(next(myit)) #o

#Create an iterator to print a sequence of numbers
class SequenceNum():
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x


myit = SequenceNum()
myiter = iter(myit)
print("Values are: ")
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


#Create an iterator that returns sequence of numbers from 1 to 10 using StopIteration
class SequenceNum():
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a<=10:
        x = self.a
        self.a += 1
        return x
    else:
        raise StopIteration

myit = SequenceNum()
myiter = iter(myit)
print("Values are: ")
for value in myit:
    print(value)


#Generators
# Generator function to print list of prime numbers till 20

def prime(num):
    x=2
    while x<num:
        if (num%x==0):
            return False
        x+=1
    return True

def primeGen(limit):
    a=2
    while a<limit:
        if (prime(a)):
            yield a
        a+=1

for value in primeGen(20):
    print(value)

# generator function for printing fibonacci series
def fib(limit):
    a,b = 0,1
    while a<limit:
        yield a
        a,b = b,a+b

for value in fib(5):
    print(value)
