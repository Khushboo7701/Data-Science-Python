#Slicing:
# 1.Slicing list
a = [1,2,'okay',2.4,7,10,'last']
print(a[1:3]) # [2,'okay']
print(a[0:]) #prints full list i.e. [1,2,'okay',2.4,7,10)]
print(a[0:len(a)]) #prints full list
print(a[:]) #prints full list
print(a[-4:-1]) # [2.4,7,10]
#To slice with a jump value of 2:
print(a[1:7:2]) # [2,2,4,10]
#To step backward during slicing:
print(a[7:1:-2]) # ['last',7,'okay']

# 2.Slicing String
str = "Hello World"
print(str[1:3]) #el
print(str[0:]) #prints whole string i.e. Hello World
print(str[0:len(str)]) #prints whole string
print(str[:]) #prints whole string
print(str[-5:]) #World
print(str[0:8:2]) #slices by a stride of 2. output-HloW 

# 3.Slicing tuple
a = (1,2,'okay',2.4,7,10,'last')
print(a[1:3]) # (2,'okay')
print(a[0:]) #prints full tuple i.e. (1,2,'okay',2.4,7,10)
print(a[0:len(a)]) #prints full tuple
print(a[:]) #prints full tuple
print(a[-4:-1]) # (2.4,7,10)
#To slice with a jump value of 2:
print(a[1:7:2]) # (2,2,4,10)
#To step backward during slicing:
print(a[7:1:-2]) # ('last',7,'okay')


#Indexing:
# 1.Indexing list
a = [1,2,6,'hello',3.5, 'world']
x = a[3] #hello
y = a[-1] #world
print(x+" " +y) # hello world

# 2.Indexing strings
str = "Khushboo"
print(str[1]) #h
print(str[-1]) #starts from back of string. Output- o
print(str[-4]) #h

# 3.Indexing tuple
b = (1,2,6,'hello',3.5, 10)
x = b[2] #6
y = b[-1] #10
print(y-x) # 4

# 4.Indexing dictionary
#since dictionary is unordered, indexing is done using the key
d = {"name":"Khushboo", "domain":"data science"}
myName = d['name']
print("My name is ", myName) #My name is Khushboo

#Exception handling
# 1.try except
a= int(input("Enter a"))
b= int(input("Enter b"))
try:
    c = a/b
except:
    print("Division unsuccessful")
   
    
# 2.many excepts
a= int(input("Enter a "))
b= int(input("Enter b"))
try:
    c = a/b
except NameError:
    print("c is not defined")
except ZeroDivisionError:
    print("Zero Division Error")
except:
    print("Some other error occurred")

# 3.try except else
#else defines block of code to be executed if no errors are raised
a= int(input("Enter a "))
b= int(input("Enter b"))
try:
    c = a/b
except:
    print("Division unsuccessful")
else:
    print("Division result: ",c)
    
# 4.try except finally
a= int(input("Enter a"))
b= int(input("Enter b"))
try:
    c = a/b
except:
    print("Division unsuccessful")
else:
    print("Division result: ",c)
finally:
    print("a: ",a,"b: ",b)
    
# 5.try except raise
#to define error ourselves
a= int(input("Enter a"))
b= int(input("Enter b"))
try:
    c=a/b
    if b>a:
        raise DivisionError("second number should be less than first")
    else:
        print("Division result: ",c)
except:
    print("Division not possible")


#Regular Expressions
# 1. Check if the string starts with He and ends with d
import re
str = "Hello world"
x = re.search("^He.+d$", str)
if x:
    print("Match found")
else:
    print("Match not found")
    
# 2. Difference between ^[] and [^]
str = "Hello World"
x= re.findall("^[h-o]", str)
print(x) #[]
x = re.findall("[^hio]",str) 
print(x) #['H', 'e', 'l', 'l', ' ', 'W', 'r', 'l', 'd']

# 3. split the string at occurrence of a digit
str = input("Enter the input")
x= re.split("\d", str)
print("The resulting list is: ",x)

# 4. Split the string at first two occurrences of whitespace
str = input("Enter the input")
x= re.split("\s", str, 2)
print("The resulting list is: ",x)


# 5. Replace the matching characters
str = "Today is a bad day"
x= re.sub("bad","good", str)
print(x)#Today is a good day

# 6. Search for an upper case "S" character in the beginning of a word, and print the word:

str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.group()) #Spain