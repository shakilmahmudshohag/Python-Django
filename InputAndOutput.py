"""
# Ctrl+Alt+I =Indents
# a use of input
val = input("Enter a value:")
print("The value is:",val)
name=input("What is your name?\n")
print(name)
print("type of value",type(val))
print("type of value",type(name))

num1 = int(input())
num2 = int(input())
print(num1+num2)

num1 = float(input())
num2 = float(input())
print(num1+ num2)

string = str(input())
print(string)

#Taking multiple inputs from user
# Taking three inputs at a time
x,y,z =input("Enter three values:").split()
print("total number of students:",x)
print("Number of boys is:",x)
print("Number of girls is:",x)
print()

#taking two inputs at a time
a,b =input("Enter two values:").split()
print("First number is {} and second number is {}".format(a,b))
print()

#taking multiple inputs at a time
# and type casting using list() function
x = list(map(int,input("Enter multiple values:").split()))
print("List of students:",x)

# Python program showing
# how to take multiple input
# using List comprehension

# taking two input at a time
x, y = [int(x) for x in input("Enter two values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print()

# taking three input at a time
x, y, z = [int(x) for x in input("Enter three values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print("Third Number is: ", z)
print()

# taking two inputs at a time
x, y = [int(x) for x in input("Enter two values: ").split()]
print("First number is {} and second number is {}".format(x, y))
print()

# taking multiple inputs at a time
x = [int(x) for x in input("Enter multiple values: ").split()]
print("Number of list is: ", x)

# taking multiple inputs at a time separated by comma
x = [int(x) for x in input("Enter multiple value: ").split(",")]
print("Number of list is: ", x)

print("shakil\n mahmud")
print("shakil mahmud")
print("shakil mahmud", end="**")
print("welcome to codna house")

import time
count_second =10
for i in reversed(range(count_second+1)):
    if i > 0:
        print(i,end='>>>')
        time.sleep(1)
    else:
        print('Start')

import time
count_second = 2
for i in reversed(range(count_second + 1)):
    if i > 0:
        print(i, end='>>>',flush=True)
        time.sleep(1)
    else:
        print('Start')

#separator
a =12
b =12
c = 2022
print(a,b,c,sep="-")

#file argument
import io

# declare a dummy file
dummy_file = io.StringIO()

# add message to the dummy file
print('Hello Geeks!!', file=dummy_file)

# get the value from dummy file
dummy_file.getvalue()


# Python 3.x program showing
# how to print data on
# a screen

# One object is passed
print("shakil")

x = 5
# Two objects are passed
print("x =", x)

# code for disabling the softspace feature
print('S', 'A', 'L', sep='-')

# using end argument
print("Python", end='@')
print("shakil")

#print without newline in python
print("shakil",end=" ")
print("mahmud")
a=[1,2,3,4]
for i in range(4):
    print(a[i],end=" ")

#print without newline in python without using for loop
l=[1,2,3,4,5,6]
print(*l)

#python end parameter
print("welcome to",end='@')
print("codna house",end=' ')

#sep parameter
print('S','A', sep='',end='')
print('L')
print('01','08','2022',sep='_',end='\n')
print('red','green','blue',sep=',',end='@')
print('shakil')

#python output formating
print("shakil:%2d,portal:%5.2f"%(1,05.333))
print("Total students: %3d,boys:%2d"%(240,120))
print("%7.3o"%(25))
print("%10.3E"%(356.08977))


#using format() method
print('I love {} for"{}!"'.format('you','me'))

# a position of the object
print('{0} and {1}'.format('me','you'))
print('{1} and {0}'.format('me','you'))

#the above formatting can also be done by using f-strings
print(f"I love {'you'} for \"{'me'}!\"")
print(f"{'you'} and {'me'}")


#combining positional and keyword argument
print('Number one portal is {0},{1},and {other}.'.format('shakil,'for',other='mahmud'))
#using format() method with number
print("Geeks :{0:2d}, Portal :{1:8.2f}".
      format(12, 00.546))
# Changing positional argument
print("Second argument: {1:3d}, first one: {0:7.2f}".
      format(47.42, 11))

print("Geeks: {a:5d},  Portal: {p:8.2f}".
      format(a=453, p=59.058))
"""
# Python program to
# show format() is
# used in dictionary

tab = {'geeks': 4127, 'for': 4098, 'geek': 8637678}

# using format() in dictionary
print('Geeks: {0[geeks]:d}; For: {0[for]:d}; '
      'Geeks: {0[geek]:d}'.format(tab))

data = dict(fun="GeeksForGeeks", adj="Portal")

# using format() in dictionary
print("I love {fun} computer {adj}".format(**data))

# Python program to
# format a output using
# string() method

cstr = "I love geeksforgeeks"

# Printing the center aligned
# string with fillchr
print("Center aligned string with fillchr: ")
print(cstr.center(40, '#'))

# Printing the left aligned
# string with "-" padding
print("The left aligned string is : ")
print(cstr.ljust(40, '-'))

# Printing the right aligned string
# with "-" padding
print("The right aligned string is : ")
print(cstr.rjust(40, '-'))