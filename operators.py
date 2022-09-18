"""

#Example of arithmetic operator
a=9
b=4
add = a + b
sub= a - b
mul = a * b
div1 = a / b
div2 = a // b
mod = a % b
p= a**b
print(add)
print(sub)
print(mul)
print(div1)
print(div2)
print(mod)
print(p)
#comparison operators
# Examples of Relational Operators
a = 13
b = 33

# a > b is False
print(a > b)

# a < b is True
print(a < b)

# a == b is False
print(a == b)

# a != b is True
print(a != b)

# a >= b is False
print(a >= b)

# a <= b is True
print(a <= b)

# AND: True if both the operands are true	x and y
# OR: True if either of the operands is true 	x or y
# NOT: True if the operand is false 	not x
# Examples of Logical Operator
a = True
b = False

# Print a and b is False
print(a and b)

# Print a or b is True
print(a or b)

# Print not a is False
print(not a)

#bitwise operators
# Examples of Bitwise operators
a = 10
b = 4

# Print bitwise AND operation
print(a & b)

# Print bitwise OR operation
print(a | b)

# Print bitwise NOT operation
print(~a)

# print bitwise XOR operation
print(a ^ b)

# print bitwise right shift operation
print(a >> 2)

# print bitwise left shift operation
print(a << 2)

# Examples of Assignment Operators
a = 10

# Assign value
b = a
print(b)

# Add and assign value
b += a
print(b)

# Subtract and assign value
b -= a
print(b)

# multiply and assign
b *= a
print(b)

# bitwise lishift operator
b <<= a
print(b)

#identity operator
a = 10
b = 20
c = print( a is not b)
print(a is c)

#Membership operators
x = 24
y = 20
list=[10,20,30,40,50]
if( x not in list):
    print("x is Not present in given list")
else:
    print("x is present in given list")

if(y in list):
    print("y is present in given list")
else:
    print("y is not present in given list")


#operator precedence
expr = 10+20*30
print(expr)

name="Alex"
age= 0

if name =="Alex" or name =="John" and age>=2:
    print("Hello! welcome")
else:
    print("good bye")

#operator Associativity
# Examples of Operator Associativity

# Left-right associativity
# 100 / 10 * 10 is calculated as
# (100 / 10) * 10 and not
# as 100 / (10 * 10)
print(100 / 10 * 10)

# Left-right associativity
# 5 - 2 + 3 is calculated as
# (5 - 2) + 3 and not
# as 5 - (2 + 3)
print(5 - 2 + 3)

# left-right associativity
print(5 - (2 + 3))

# right-left associativity
# 2 ** 3 ** 2 is calculated as
# 2 ** (3 ** 2) and not
# as (2 ** 3) ** 2
print(2 ** 3 ** 2)
#python operators
# "//" for integers
print(5//2)
print(-5//2)

# "/" for floating point numbers
print(5.0/2)
print(-5.0/2)

# A Python program to demonstrate use of
# "//" for both integers and floating points
print (5//2)
print (-5//2)
print (5.0//2)
print (-5.0//2)


#ternary operator
a,b = 10,20
min = a if a < b else b
print(min)

#Direct Method by using tuples, Dictionary, and lambda
# Python program to demonstrate ternary operator
a, b = 10, 20

# Use tuple for selecting an item
# (if_test_false,if_test_true)[test]
# if [a<b] is true it return 1, so element with 1 index will print
# else if [a<b] is false it return 0, so element with 0 index will print
print( (b, a) [a < b] )

# Use Dictionary for selecting an item
# if [a < b] is true then value of True key will print
# else if [a<b] is false then value of False key will print
print({True: a, False: b} [a < b])

# lambda is more efficient than above two methods
# because in lambda we are assure that
# only one expression will be evaluated unlike in
# tuple and Dictionary
print((lambda: b, lambda: a)[a < b]())


# Python program to demonstrate nested ternary operator
a, b = 10, 20

print ("Both a and b are equal" if a == b else "a is greater than b"
		if a > b else "b is greater than a")


# Python program to demonstrate nested ternary operator
a, b = 10, 20

if a != b:
	if a > b:
		print("a is greater than b")
	else:
		print("b is greater than a")
else:
	print("Both a and b are equal")


a=5
b=7

# [statement_on_True] if [condition] else [statement_on_false]

print(a,"is greater") if (a>b) else print(b,"is Greater")

# Program to demonstrate conditional operator
a, b = 10, 20

# If a is less than b, then a is assigned
# else b is assigned (Note : it doesn't
# work if a is 0.
min = a < b and a or b

print(min)


#operator overloading
print(1+2)
print("shakil" + "Mahmud")
print(3*4)
print("I Love you" * 4)

# Python Program illustrate how
# to overload an binary + operator

class A:
	def __init__(self, a):
		self.a = a

	# adding two objects
	def __add__(self, o):
		return self.a + o.a
ob1 = A(1)
ob2 = A(2)
ob3 = A("shakil")
ob4 = A("For")

print(ob1 + ob2)
print(ob3 + ob4)

class complex:
	def__init__(self,a,b):
	self.a = a
	self.b = b


	def__add__(self, other):
	return self.a + other.a,self.b +other.b

ob1 = complex(1,2)
ob2 = complex(2,3)
ob3 = ob1 + ob2
print(ob3)

#a comparison operators
class A:
	def __init__(self,a):
	     self.a = a
	def __gt__(self, other):
		if(self.a>other.a):
			return True
		else:
			return False
ob1 = A(2)
ob2 = A(3)
if(ob1>ob2):
	print("ob1 is greater than ob2")
else:
	print("ob2 is greater than ob1")


# Python program to overload equality
# and less than operators

class A:
	def __init__(self, a):
		self.a = a

	def __lt__(self, other):
		if (self.a < other.a):
			return "ob1 is lessthan ob2"
		else:
			return "ob2 is less than ob1"

	def __eq__(self, other):
		if (self.a == other.a):
			return "Both are equal"
		else:
			return "Not equal"


ob1 = A(2)
ob2 = A(3)
print(ob1 < ob2)

ob3 = A(4)
ob4 = A(4)
print(ob1 == ob2)


# Python program which attempts to
# overload ~ operator as binary operator

class A:
	def __init__(self, a):
		self.a = a

	# Overloading ~ operator, but with two operands
	def __invert__(self, other):
		return "This is the ~ operator, overloaded as binary operator."


ob1 = A(2)
ob2 = A(3)

print(ob1~ob2)

#Any all in python
# All T= T,T
#All F=F,F
#one T all F=T,F
#one F all T=T,F
#Empty iterable = F,T
# Since all are false, false is returned
print (any([False, False, False, False]))

# Here the method will short-circuit at the
# second item (True) and will return True.
print (any([False, True, False, False]))

# Here the method will short-circuit at the
# first (True) and will return True.
print (any([True, False, False, False]))


# Here all the iterables are True so all
# will return True and the same will be printed
print (all([True, True, True, True]))

# Here the method will short-circuit at the
# first item (False) and will return False.
print (all([False, True, True, False]))

# This statement will return False, as no
# True is found in the iterables
print (all([False, False, False]))


# This code explains how can we
# use 'any' function on list
list1 = []
list2 = []

# Index ranges from 1 to 10 to multiply
for i in range(1,11):
	list1.append(4*i)

# Index to access the list2 is from 0 to 9
for i in range(0,10):
	list2.append(list1[i]%5==0)

print('See whether at least one number is divisible by 5 in list 1=>')
print(any(list2))

# Illustration of 'all' function in python 3

# Take two lists
list1=[]
list2=[]

# All numbers in list1 are in form: 4*i-3
for i in range(1,21):
	list1.append(4*i-3)

# list2 stores info of odd numbers in list1
for i in range(0,20):
	list2.append(list1[i]%2==1)

print('See whether all numbers in list1 are odd =>')
print(all(list2))


#operator functions in python set 1
#python code to demonstrate working of add(),sub(),mul()
#importing operator madule
import operator
#initializing variables
a=4
b=3
#using add() to add two numbers
print("The addtionof numbers is :",end="");
print(operator.add(a, b))
#using sub() to subtract two numbers
print("The difference of number is:", end="")
print(operator.sub(a,b))
#using mul() to multiply two numbers
print("The product of number is:",end="")
print(operator.mul(a,b))

# Python code to demonstrate working of
# truediv(), floordiv(), pow(), mod()

# importing operator module
import operator

# Initializing variables
a = 5

b = 2

# using truediv() to divide two numbers
print ("The true division of numbers is : ",end="");
print (operator.truediv(a,b))

# using floordiv() to divide two numbers
print ("The floor division of numbers is : ",end="");
print (operator.floordiv(a,b))

# using pow() to exponentiate two numbers
print ("The exponentiation of numbers is : ",end="");
print (operator.pow(a,b))

# using mod() to take modulus of two numbers
print ("The modulus of numbers is : ",end="");
print (operator.mod(a,b))

#uing It() to check if a is less than b
if(operator.lt(a,b)):
    print("5 is less than 2")
else:print("5 is not less than 2")

#using le() to check if a is less than or equal to b
if(operator.le(a,b)):
    print("5 is less than or equal to 2")
else:print("5 is not less than or equal to 2")

#using eq to check if a is equal to b
if(operator.eq(a,b)):
    print("5 is equal to 2")
else:print("5 is not equal to 2")

# using gt() to check if a is greater than b
if (operator.gt(a, b)):
    print("5 is greater than 2")
else:
    print("5 is not greater than 2")

# using ge() to check if a is greater than or equal to b
if (operator.ge(a, b)):
    print("5 is greater than or equal to 2")
else:
    print("5 is not greater than or equal to 2")

# using ne() to check if a is not equal to b
if (operator.ne(a, b)):
    print("5 is not equal to 2")
else:
    print("5 is equal to 2")


#operator Function in python -set 2
#python code to demonstrate working of setitem(),delitem(),and getitem()

#importing operator module
import operator
#initializing list
li =[1,5,6,7,8]
#printing original list
print("The original list is:", end="")
for i in range(0,len(li)):
    print(li[i],end="")
print("\r")

#using setitem() to assign 3 at 4th position
operator.setitem(li,3,3)
#printing modified lsit after setitem()
print("The modified lsit after setitem() is :",end="")
for i in range(0,len(li)):
    print(li[i],end="")
print("\r")

#using delitem() to delete value at 2nd index
operator.delitem(li,1)
#printing modified list after delitem()
print("The modified lsit after delitem()is :",end="")
for i in range(0,len(li)):
 print(li[i],end="")
print("\r")

#using getitem() to access 4th element
print("The 4th item of the list is:",end="")
print(operator.getitem(li,3))

#using setitem to assign 2,3,4 at 2nd,3rd and 4th index
operator.setitem(li,slice(1,4),[2,3,4])

print("The modified lsit after setitem()is :",end="")
for i in range(0,len(li)):
 print(li[i],end="")
print("\r")

# using delitem() to delete value at 3rd and 4th index
operator.delitem(li, slice(2, 4))

# printing modified list after delitem()
print("The modified list after delitem() is : ", end="")
for i in range(0, len(li)):
    print(li[i], end=" ")

print("\r")

# using getitem() to access 1st and 2nd element
print ("The 1st and 2nd element of list is : ",end="")
print (operator.getitem(li,slice(0,2)))

#python code to demonstrate working of concat() and contains()
#importing operator module
import operator
#Initializing string 1
s1="MoonLight"
#Initializing string 2
s2="Moon"

#using concat() to concatenate two strings
print("The concatenated string is:",end="")
print(operator.concat(s1,s2))

#using contains() to check if s1 contains s2
if(operator.contains(s1,s2)):
    print("MoonLight contains Moon")
else:print("MoonLight does not contains Moon")

# Python code to demonstrate working of
# and_(), or_(), xor(), invert()

# importing operator module
import operator

# Initializing a and b

a = 1

b = 0

# using and_() to display bitwise and operation
print ("The bitwise and of a and b is : ",end="")
print (operator.and_(a,b))

# using or_() to display bitwise or operation
print ("The bitwise or of a and b is : ",end="")
print (operator.or_(a,b))

# using xor() to display bitwise exclusive or operation
print ("The bitwise xor of a and b is : ",end="")
print (operator.xor(a,b))

# using invert() to invert value of a
operator.invert(a)

# printing modified value
print ("The inverted value of a is : ",end="")
print (operator.invert(a))

#Difference between == and is operator in pyton
#[] is an empty list
list1=[]
list2=[]
list3=list1
if (list1 == list2):
    print("True")
else:
    print("False")

if (list1 is list2):
    print("True")
else:
    print("False")

if(list1 is list3):
    print("True")
else:print("False")
list3 = list3 + list2

if (list1 is list3):
    print("True")
else:
    print("False")

list1 = []
list2 = []

print(id(list1))
print(id(list2))

#python Membership and identity operators
#python program to illustrate finding common member in list using in operator
list1 =[1,2,3,4,5]
list2 =[6,7,8,9]
for item in list1:
    if item in list2:
        print("overlapping")
    else:print("Not overlapping")

#The same example without using in operator
#Define a funcion() that takes two lists

def overlapping(list1,list2):
    c=0
    d=0
    for i in list1:
        c +=1
    for i in list2:
        d +=1
    for i in range(0,c):
        for j in range(0,d):
            if(list1[i] == list2[j]):
                return 1
    return 0

list1 =[1,2,3,4,5]
list2 =[6,7,8,9]
if(overlapping(list1,list2)):
    print("overlapping")
else:print("Not overlapping")


#python program to illustrate not in operator
x =24
y =20
list = [10,20,30,40,50]
if (x not in list):
    print("x is not present in the list")
else:print("x is present in the list")
if (y  in list):
    print("y is present in the list")
else:print("y is not present is the list")



#python program to illustrate the use of is identity operator
x=5
y=5
print(x is y)
print(id(x))
print(id(y))

#python program to illustrate the use of is not identity operator
x=5
if(type(x) is not int):
    print("True")
else:print("False")

#prints true
x=5.6
if (type(x) is not int):
    print("true")
else:print("False")
"""