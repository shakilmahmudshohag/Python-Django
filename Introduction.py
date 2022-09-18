"""mynumber=3
print(mynumber)
mynumber2=4.5
print(mynumber2)
mynumber3="hello"
print(mynumber3)

#creating an empty list
nums=[]

#appending in the list
nums.append(4)
nums.append(3.5)
nums.append("string")
print(nums)

#getting input from user

name=input("Enter your name:")
print("hello", name)

num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))

num3=num1*num2
print("product is:",num3)

#selecting statement
num1=32
if(num1>12):
    print("num1 is good")
elif(num1>35):
    print("num1 is not good")
else:
    print("num2 is great")

    #function
    def hello():
        print("hello")
        print("hello again")
        hello()

        #calling function
        hello()

        #function with main
        def getinteger():
            result=int(input("Enter integer:"))
            return result
        def Main():
            print("Started")
            output=getinteger()
            print(output)

            if __name__=="__main__":
                Main()

# a simple for loop
for step in range(143):
    print(step)


# Python program to illustrate
# math module
import math


def Main():
    num = -85

    # fabs is used to get the absolute
    # value of a decimal
    num = math.fabs(num)
    print(num)


if __name__ == "__main__":
    Main()

tup=('shakil','mahmud')
print(tup)
# define a set and it's element
myset=set(["shakil","mahmud"])
print(myset)

#python keyword list
import keyword
print("The list of keyword is:")
print(keyword.kwlist)

print(False == 0)
print((True == 1)
print(True + True + True)
print(True + False + False)
print(None == 0)
print(None == [])

print(True or False)
print(False and True)
print(not True)

if 's' in 'shakil':
    print("s is part of shakil ")
else:
    print(" s is not part of shakil")
for i in 'shakil':
    print(i, end="")
print("\r")
print(' ' is ' ')
print({} is {})

# Using for loop
for i in range(10):

    print(i, end=" ")

    # break the loop as soon it sees 6
    if i == 6:
        break

print()

# loop from 1 to 10
i = 0
while i < 10:

    # If i is equals to 6,
    # continue to next iteration
    # without printing
    if i == 6:
        i += 1
        continue
    else:
        # otherwise print the value
        # of i
        print(i, end=" ")

    i += 1

i =22
if (i == 10):
    print("i is 10")
elif(i == 20):
    print("i is 20")
else:
    print("i is not present")


def fun():
    print("Inside Function")
fun()

#Return Keyword
def fun():
    S=0
    for i in range(10):
        S += i
    return S
print(fun())

#Yield Keyword
def fun():
    S=0

    for i in range(10):
        S += i
        yield S
for i in fun():
    print(i)


# A class
class Dog:
    #attribute
     attr1 ="mammal"
     attr2 ="dog"
# A simple method
     def fun(self):
         print("I'am a",self.attr1)
         print("I'am a",self.attr2)

#Driver code object instantiation
Rodger = Dog()

#Accessing class attributes and method through objects
print(Rodger.attr1)
Rodger.fun()


#with Keyword
with open('file_path','w') as file:
    file.write('hello world!')

# as Keyword
import math as sha
print(sha.factorial(5))


#pass keyword
n=10
for i in range(n):
 pass

#Lambda keyword
g = lambda x:x*x*x
print(g(7))
#import from keyword
import math
print(math.factorial(10))

from math import factorial
print(factorial(10))

#Exception handling keyword
a =4
b=0
try:
 k=a/b
 print(k)

except ZeroDivisionError:
 print("can't divide by zero")

finally:
 print("This is always excuted")

print("The value of a/b is:")
assert b != 0, "Divide by 0 error"
print (a / b)

#del keyword
my_variable1 =20
my_variable2 ="shakil"

print(my_variable1)
print(my_variable2)

del my_variable1
del my_variable2
print(my_variable1)
print(my_variable2)

#Global and nonlocal keywords
a = 15
b = 10

def add():
    c=a+b
    print(c)
add()

def fun():
    var1 =10
    def gun():
        nonlocal var1
        var1=var1+10
        print(var1)

    gun()
fun()

#namespaces and scope in python

#var1 is in the goble namespace

var1 = 5
def some_func():
    #var2 is in the local namespace
    var2 = 6
    def some_innner_func():
        #var3 is in the nested local namespace
        var3 = 7


count = 5
def some_method():
    global count
    count = count+1
    print(count)
some_method()



# Python program showing
# a scope of object

def some_func():
    print("Inside some_func")

    def some_inner_func():
        var = 10
        print("Inside inner function, value of var:", var)

    some_inner_func()
    print("Try printing var from outer function: ", var)


some_func()

# statement ,indentation,and comment
#statement
#Declared using Continuation Character (\):
s = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9

#Declared using parentheses () :
n = (1 * 2 * 3 + 7 + 8 + 9)

#Declared using square brackets [] :
footballer = ['MESSI',
          'NEYMAR',
          'SUAREZ']

#Declared using braces {} :
x = {1 + 2 + 3 + 4 + 5 + 6 +
     7 + 8 + 9}

#Declared using semicolons(;) :
flag = 2; ropes = 3; pole = 4

# Python program showing
# indentation


site = 'gfg'

if site == 'gfg':
    print('Logging on to the heart...')
else:
    print('retype the URL.')
print('All set !')

j = 1
while(j<=5):
    print(j)
    j=j+1

#comment
'''Docstrings are written in the functions and classes to show how to use the program.
   
Multi-line comments are used to show how a block of code works.  '''
"""
# How to assign values to variable in python

# Direct Initialisation Method
a = 5
print("The value of a is:"+ str(a))

#Using Conditional operator
a=1 if 20>10 else 0
print("The value of a is:",str(a))