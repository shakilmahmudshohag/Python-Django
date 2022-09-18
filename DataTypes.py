"""
#Assingning string to a variable
a= "This is a string"
print(a)
b="This is a string"
print(b)
c='''This is a String'''
print(c)

# Declaring a list
L = [1, "a" , "string" , 1+2]
print(L)
#Adding an element in the list
L.append(6)
print(L)
#Deleting last element from a list
L.pop()
print(L)
#Displaying Second element of the list
print(L[1])

#Tuples in python
tup =(1,"a","string",1+2)
print(tup)
print(tup[1])


#Iteration by while loop for a condition
i = 1
while (i<10):
   print(i)
   i +=1

#Iterration by for loop on the string
s ="Hello world"
for i in s:
   print(i)

#Iterration by for loop on list
L =[1,4,5,7,8,9]
for i in L:
   print(i)


#Iteration by for loop for range
for i in range(0,10):
    print(i)

#python program for creation of string
#creating a string with single quotes
String1 ='Welcome to the world'
print("string with the use of single Quotes:")
print(String1)


#creating a string with double Quotes
String1 ="I' am shakil"
print("\nString with the use of Double quotes:")
print(String1)

#creating a string with triple Quotes
String1='''I'm shakil mahmud and I live in the world'''
print("\nString with the use of triple Quotes:")
print(String1)

#creating string with triple quotes allows multiple lines
String1 =  '''shakil
              mahmud
              shohag'''
print("\nCreating a multiple String:")
print(String1)

#python program to access Characters of string
String1 ="Moonlight"
print("Initial String:")
print(String1)

#printing First character
print("\nFirst character of string is:")
print(String1[0])

#printing Last character
print("\nLast character of string is:")
print(String1[-1])

#program to reverse a string
sha ="Moonlight"
print(sha[::-1])

#program to reverse a string
sha ="Moonlight"

#Reverse the string using reversed and join function
sha ="".join(reversed(sha))
print(sha)

#python program to demonstrate string slicing
#creating a string
string1 ="Moonlight"
print("Initial string:")
print(string1)

#printing 3rd to 12th character
print("\nSlicing character from 3-12:")
print(string1[3:12])

#printing character between 3rd and 2nd last character
print("\nSlicing character between" +
      "3rd and 2nd last character")
print(string1[3:-2])

#python program to update character of a string
string1 ="Hello, I am shakil mahmud"
print("Initial string:")
print(string1)
#updating a character of the string as a python strings are immutable they don't support item updation directly there are following two ways
#1
list1 = list(string1)
list1[2] = 'p'
string2 =''.join(list1)
print("\nupdating charcter at 2nd Index:")
print(string2)
#2
string3 =string1[0:2] + 'p' +string1[3:]
print(string3)

#python program to update entire string
string1 ="hello, I am kilmu"
print("Initial String:")
print(string1)

#updating a string
string1 ="Welcome to the world !"
print("\nupdated string:")
print(string1)

#python program to delete character from a string
string1 ="Hello , I am kilmu"
print("Initial string:")
print(string1)
#Deleting a character of the string
string2 =string1[0:2] +string1[3:]
print("\nDeleting character at 2nd Index:")
print(string2)

#python program to Delete entire String
string1 ="Hello, I am kilmu"
print("Intial string:")
print(string1)
#Deleting a string with the use of del
del string1
print("\nDeleting entire string:")
print(string1)

#python program for Escape Sequencing of string
#Initial string
string1 = '''I'm kilmu'''
print("Initial string with use of Triple Quotes:")
print(string1)

#Escaping single Quotes
string1 ='I\'m "kilmu"'
print("\nEscaping single Quotes:")
print(string1)

# Escaping Double Quotes
String1 = "I'm a \"kilmu\""
print("\nEscaping Double Quotes: ")
print(String1)

# Printing Paths with the
# use of Escape Sequences
String1 = "C:\\Python\\kilmu\\"
print("\nEscaping Backslashes: ")
print(String1)

# Printing Paths with the
# use of Tab
String1 = "Hi\tkilmu"
print("\nTab: ")
print(String1)

# Printing Paths with the
# use of New Line
String1 = "Python\nkilmu"
print("\nNew Line: ")
print(String1)

#printing hello in octal
string1 ="\110\145\154\154\157"
print("\nPrinting in octal with the use of Escape Sequence:")
print(string1)

#using raw string to ignore escape sequences
string1 =r"This is \110\145\154\154\157"
print("\nPrinting Raw string in octal format:")
print(string1)

#printing hex in hex
string1="\x48\x45\x58"
print("\nPrinting in hex with the use of escape sequence:")
print(string1)

#using raw string to ignore escape sequences
string1=r"\x48\x45\x58"
print("\nPrinting in hex with the use of escape sequence:")
print(string1)

#python program for formatting of string
#Default order
string1="{} {} {}".format('shakil','mahmud','shohag')
print("print string in default order:")
print(string1)

#positinal formatting
string1="{1} {2} {0}".format('shakil','mahmud','shohag')
print("print string in default order:")
print(string1)

#keyword formatting
string1="{S} {m} {s}".format(s='shakil',m='mahmud',S='shohag')
print("print string in default order:")
print(string1)

#formatting of integers
string1 = "{0:b}".format(16)
print("\nBinary representration of 16is:")
print(string1)

#formatting of floats
string1 ="{0:e}".format(165.6458)
print("\nExponent representration of 165.6458 is:")
print(string1)

#Rounding off integers
string1 ="{0:.2f}".format(1/6)
print("\none-sixth is:")
print(string1)

#String aligment
string1 ="|{:<10}|{:^10}|{:>10}|".format('shakil','mahmud','sohag')
print(string1)

String2 = "\n{0:^16} you destroyed {1:<4}!".format("My love",
                                                    2022)
print(String2)

# Python Program for
# Old Style Formatting
# of Integers

Integer1 = 12.3456789
print("Formatting in 3.2f format: ")
print('The value of Integer1 is %3.2f' % Integer1)
print("\nFormatting in 3.4f format: ")
print('The value of Integer1 is %3.4f' % Integer1)

#USEFUL PYTHON STRING OPERATIONS
#logical operator on string in python
str1 =''
str2 ='kilmu'
#repr is used to print the string along with the quotes
#Returns str1
print(repr(str1 and str2))

#returns str1
print(repr(str2 and str1))

#returns str2
print(repr(str1 or str2))
#returns str2
print(repr(str2 or str1))
#returns true
print(repr(not str1))

#string formatting in python using %
#python program to demonstrate the use of formatting useing %
#Initialize variable as a string
variable ='15'
string="Variable as string=%s"%(variable)
print(string)

#printing as raw data
print("variable as raw data = %r"%(variable))

#convert the variable to integer and perform check other formatting options
variable =int(variable)
#without this below statement will give error
string ="variable as integer =%d "%(variable)
print(string)
print("Variable as float =%f"%(variable))

#printing as any string or char after a mark here i use mayank as a string
print("Variable as printing with special char=%c"%(variable))
print("variable as octal=%o"%(variable))
print("variable as hexadecimal=%x"%(variable))

#String template class in python
#A simple python template example
from string import Template
#create a template that has placeholder for value of x
t =Template('x is $x')
#Substitute value of x in above template
print(t.substitute({'x':1}))


#A python program to demonstrate the working of the string template
from string import Template
#List student stores the name and marks of three students
student =[('Ram',90),('Ankit',78),('Bob',92)]
#we are creating a basic structure to print the name and amrks of the students
t=Template('Hi $name,you have got $marks marks')
for i in student:
    print(t.substitute(name=i[0],marks=i[1]))

#Example of the safe_substitute method
from string import Template
template =Template('$name is the $job of $company')
string =template.safe_substitute(name='raju Kumar',job ='TCE')
print(string)

#printing the template string
string import Template
t = Template('I am $name from $city')
print('Template String =', t.template)

#Escaping $sign
template = Template('$$ is the symbol for $name')
string =template.substitube(name='Dollar')

#The ${Identifier}
template =Template('That $noun looks ${nounly}y')
string =template.substitube(noun='fish')

#how to split a string in python
line = "shakil \nmahmud \nsohag"
print(line.split())
print(line.split(' ', 1))

#Python docstring
#The below examples demosnstarte hoe to declare and access  a docstring using triple single quotes
def my_function():
	'''Demonstrates triple double quotes
	docstrings and does nothing really.'''

	return None

print("Using __doc__:")
print(my_function.__doc__)

print("Using help:")
help(my_function)

#Using triple double quotes
def my_function():
	"""Demonstrates triple double quotes
	docstrings and does nothing really."""

	return None

print("Using __doc__:")
print(my_function.__doc__)

print("Using help:")
help(my_function)

#One line Docstrings
def power(a, b):
	"""Returns arg1 raised to power arg2."""

	return a**b

print(power.__doc__)
"""
#Multi line docstring

