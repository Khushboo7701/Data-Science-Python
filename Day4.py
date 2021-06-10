#Classes and objects
# 1. Define a class MyClass and create its object
class MyClass:
    name="Khushboo" 
    domain="Data Science"

    def intern(self):
        print(self.name, "is interning in", self.domain)

obj = MyClass() #object
print("Name: ", obj.name)
print("Domain: ",obj.domain)
obj.intern()

# 2. Initialize object using init
class Internship:
    def __init__(self, name, domain):
        self.name = name
        self.domain = domain
    
    def intern(self):
        print(self.name, "is interning in", self.domain)

i = Internship("Khushboo","Data Science")
i.intern()
print("Name: ",i.name)
print("Domain: ",i.domain)

# 3. Create a class variable named foundation in the above defined class and demonstrate the difference between class and instance variables
class Internship:
    foundation = "Internity"
    def __init__(self, name, domain):
        self.name = name
        self.domain = domain
    
    def intern(self):
        print(self.name, "is interning in", self.domain)

i = Internship("Khushboo","Data Science")
i.intern()
print("Name: ",i.name)
print("Domain: ",i.domain)
print("Foundation: ", Internship.foundation)

i2 = Internship("Aakriti", "Graphic Designing")
i2.intern()
print("Name: ",i.name)
print("Domain: ",i.domain)
print("Foundation: ", Internship.foundation)

# Here the values of foundation for both objects remains same and it is accessed by using class name

# 4. Define functions to set and print the value of instance variables name, domain and age in above class
class Internship:
    foundation = "Internity"
    def __init__(self):
        pass

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setDomain(self, domain):
        self.domain = domain

    def getDomain(self):
        return self.domain
    
    def setAge(self, age):
        self.age = age
    
    def getAge(self):
        return self.age
    
    def intern(self):
        print(self.name, "aged", self.age, "is interning in", self.domain)

i = Internship()
i.setName("Khushboo") #access functions using object name
i.setDomain("Data Science") 
i.setAge(20) 
i.intern()
print("Name: ",i.getName())
print("Age: ",i.getAge())
print("Domain: ", i.getDomain())
print("Foundation: ", Internship.foundation)


# 5. Delete the attribute domain for object i in program 3.
class Internship:
    foundation = "Internity"
    def __init__(self, name, domain):
        self.name = name
        self.domain = domain
    
    def intern(self):
        print(self.name, "is an intern")

i = Internship("Khushboo","Data Science")
i.intern()
del i.domain
print("Name: ",i.name)
# the statement print("Domain: ",i.domain) will now show error since the attribute domain doesnt exist now
print("Foundation: ", Internship.foundation)

i2 = Internship("Aakriti", "Graphic Designing")
i2.intern()
print("Name: ",i.name) # deleting the attribute deletes it for all objects so the statement print("Domain: ",i1.domain)will also show error.
print("Foundation: ", Internship.foundation)

# Closures and decorators
# 1. Use closure to invoke add function outside its scope
def addition(num1,num2):
    def add():
        print("Sum is:", (num1+num2))
    return add

if __name__ == '__main__':
    outer = addition(20,30)
    outer()

# 2. Implement closure to invoke print_func outside its scope
def operation(func):
    def print_func(*args):
        print("Result of operation is: ", func(*args))

    return print_func

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

add1 = operation(add)
add1(5,3)

sub1 = operation(subtract)
sub1(5,3)

# 3. Implement decorator with simple function
def decorator(func):
    def inner_func():
        print("Before calling test")
        func()
        print("After calling test")
    return inner_func

@decorator
def test():
    print("Inside test")

test = decorator(test)
test()

# 4. Implement decorator to print the sum of two numbers
def decorator(func):
    def inner_func(a,b):
        print("Before calculating sum")
        func(a,b)
        print("After calculating sum")
    return inner_func
@decorator
def add(x,y):
    print("Sum is: ", (x+y))

add = decorator(add)
add(5,3)

# 5. Implement decorator with a function that returns the result of subtracting two numbers
def decorator(func):
    def inner_func(a,b):
        print("Before subtracting")
        value = func(a,b)
        print("After subtracting")
        return value
    return inner_func

@decorator
def sub(x,y):
    print("Subtracting")
    return x-y

sub = decorator(sub)
print("Difference is: ", sub(5,3))

# 6. WAP showing chaining of three decorators
def decorator1(func):
    def inner():
        x=func()
        return 2*x
    return inner
def decorator2(func):
    def inner():
        x=func()
        return 3*x
    return inner
def decorator3(func):
    def inner():
        x=func()
        return 4*x
    return inner   

@decorator1
@decorator2
@decorator3
def num():
    return 10

print(num())

# Descriptors and properties
# 1. Descriptor - an object attribute with binding behaviour
class DescriptorClass:
    def  __init__(self, initial_value=None, name='var'):
        self.val = initial_value
        self.name = name 

    def __get__(self, obj, objtype):
        print("Retrieving", self.name)
        return self.val
    
    def __set__(self, obj, val):
        print("Setting", self.name)
        self.val = val

class A:
    x = DescriptorClass(1, 'variable "x"')
    y = 2

a = A()
print(a.x)
print(a.y)
a.x = 4
print(a.x)

# 2. Use descriptor to get value of an attribute and raise error if we try to set a new value to it
class DescriptorClass:
    def  __init__(self, initial_value=None, name='var'):
        self.val = initial_value
        self.name = name 

    def __get__(self, obj, objtype):
        print("Retrieving", self.name)
        return self.val

    def __set__(self, obj, val):
        raise Exception("Cannot modify value")


class A:
    x = DescriptorClass(1, 'variable "x"')
    y = 2

a = A()
print(a.x)
print(a.y)
# If we try to change the value of x using statement a.x = 4, it raises exception
print(a.x)

# had problem implementing the property in descriptor