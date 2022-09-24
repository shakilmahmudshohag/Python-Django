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





# String slicing in python to check if a string can become empty by recursive deletion
def checkEmpty(input, pattern):
    # If both are empty
    if len(input) == 0 and len(pattern) == 0:
        return 'true'

    # If only pattern is empty
    if len(pattern) == 0:
        return 'true'

    while (len(input) != 0):

        # find sub-string in main string
        index = input.find(pattern)

        # check if sub-string founded or not
        if (index == (-1)):
            return 'false'

        # slice input string in two parts and concatenate
        input = input[0:index] + input[index + len(pattern):]
    return 'true'


# Driver program
if __name__ == "__main__":
    input = 'Moonlight'
    pattern = 'kilmu'
    print(checkEmpty(input, pattern))

#FInd all duplicate character in string
from collections import Counter
def find_dup_char(input):
    #now create dictionary using counter method which will have string as key and their frequencies as value
    wc = Counter(input)
#Finding no of occurrence of ac character and get the index of it
    for letter,count in wc.items():
        if(count>1):
           print(letter)
#Driver class
if __name__=="__main__":
    input ="kilmulovemoonlight"
    find_dup_char(input)

#using count() method
def find_dup_char(input):
    x=[]
    for i in input:
        if i not in x and input.count(i)>1:
            x.append(i)
    print("".join(x))
#DRiver program
if __name__=="__main__":
    input ='kilmulovemoonlight'
    find_dup_char(input)

#Reverse string in python (6 different ways)
#Reverse a string in python using a loop
def reverse(s):
    str =""
    for i in s:
         str = i + str
    return str
s = "Moonlight"
print("The original string is:",end="")
print(s)
print("The reversed string(using loops) is:",end="")
print(reverse(s))

#Reverse a string in python using recursion
def reverse(s):
    if len(s) ==0:
        return s
    else:
        return reverse(s[1:]) +s[0]
s ="Moonlight"
print("The original string is:",end="")
print(s)
print("The reversed string(using recursion) is :",end="")
print(reverse(s))

#Reverse sting in python using stack
#function to create an empty stack.It initializes size of stack as 0
def createStack():
    stack =[]
    return stack
#Function to determine the size of the stack
def size(stack):
    return len(stack)
#Stack is empty if the size is 0
def isEmpty(stack):
    if size(stack) ==0:
        return true
#Function to add an item to stack.It increases size by 1
def push(stack,item):
    stack.append(item)
#Function to remove an item from stack It decreases size by 1
def pop(stack):
    if isEmpty(stack):
        return
    return stack.pop()
#A stack based function to reverse a string
def reverse(string):
    n = len(string)
    #create a empty stack
    stack =createStack()
    #Push all character of string to stack
    for i in range(0,n,1):
        push(stack,string[i])
    #Making the string empty since all characters are saved in stack
    string=""
    #pop all characters of string and put them back to string
    for i in range(0,n,1):
        string +=pop(stack)
    return string
#Driver code
s ="moonlight"
print("The original string is:",end="")
print(s)
print("The reversed string(using stack) is:",end="")
print(reverse(s))

#Reverse string in python using an extended slice
#Function to reverse a string
def reverse (string):
    string = string[::-1]
    return string
s ="Moonlight"
print("The original string is:",end="")
print(s)
print("The reversed string(using extended slice syntax) is:",end="")
print(reverse(s))

#Reverse strig in python using reversed() method
#python code to reverse a string using reversed()
#Function to reverse a stirng
def reverse(string):
    string ="".join(reversed(string))
    return string
s="Moonlight"
print("The original string is:",end="")
print(s)
print("The reversed string (using reversed) is:",end="")
print(reverse(s))

#Reverse string in python using list comprehension
#Function to reverse a string
def reverse(string):
    string=[string[i] for i in range(len(string)-1,-1,-1)]
    return "".join(string)
s="Moonlight"
print("The original string is:",s)
print("The reversed string(using reversed) is:",reverse(s))

#Reverse string in python usingthe function call
#function to reverse a string by converting string to list then reversed it and again convert it to string
def reverse(string):
    string =list(string)
    string.reverse()
    return "".join(string)
s="Moonlight"
print("The reversed string(using reversed) is:",end="")
print(reverse(s))

#python program to check if a string is palindrome or not
#function which return reverse of a string
def isPalindrome(s):
    return s == s[::-1]
#driver code
s="malayalam"
ans =isPalindrome(s)
if ans:
    print("yes")
else:
    print("NO")

#Iterative method to check string is palindrome or not
def isPalindrome(str):
    #Run loop from 0 to len/2
    for i in range(0,int(len(str)/2)):
        if str[i] !=str[len(str)-i-1]:
            return False
    return True
#main function
s="malayalam"
ans = isPalindrome(s)
if (ans):
    print("yes")
else:
    print("NO")

#Method using the inbuilt function to reverse a string
def isPalindrome(s):
    rev =''.join(reversed(s))

    if(s==rev):
        return True
    return False
#main function
s="malayalam"
ans =isPalindrome(s)
if(ans):
    print("Yes")
else:
    print("no")

#Method using one extra variable
x="malayalam"
w=""
for i in x:
    w=i+w
if (x==w):
    print("Yes")
else:
    print("NO")

#Method using flag
# Python program to check
# if a string is palindrome
# or not
st = 'malayalam'
j = -1
flag = 0
for i in st:
	if i != st[j]:
		flag = 1
		break
	j = j - 1
if flag == 1:
	print("NO")
else:
	print("Yes")

#Method using recursion
# Recursive function to check if a
# string is palindrome
def isPalindrome(s):

	# to change it the string is similar case
	s = s.lower()
	# length of s
	l = len(s)

	# if length is less than 2
	if l < 2:
		return True

	# If s[0] and s[l-1] are equal
	elif s[0] == s[l - 1]:

		# Call is palindrome form substring(1,l-1)
		return isPalindrome(s[1: l - 1])

	else:
		return False

# Driver Code
s = "MalaYaLam"
ans = isPalindrome(s)

if ans:
	print("Yes")

else:
	print("No")
#using extend and reverse methods
def palindrome(s):
	x=list(s)
	y=[]
	y.extend(x)
	x.reverse()
	if(x==y):
		return True
	return False
#Driver code
s="malayalam"
ans =isPalindrome(s)
if ans:
	print("Yes")
else:
	print("NO")

#Interesting facts about strings in python set 1
#strings are immutable
#python3 program to show that string cannot be changed
a='moonlight'
#output is displayed
print(a)
a[2]='K'
print(a)
#cauese error

#python3 program to show that a string can be appended to a string
a="moonlight"
print(a)
a= a + ' my love'
print(a)

#Python3 program to show that both string hold same identity
string1 ="Hello"
string2 ="Hello"
print(id(string1))
print(id(string2))

#Modifying a string
string1 ="hello"
print(id(string1))
string1 +=" World"
print(string1)
print(id(string1))

#python3 program to create strings in three different ways and concatenate them
a='moon'
b="light"
c='''My'''
d='''love,"but"'''
print(a)
print(b)
print(c)
print(d)
print(a+b+c+d)

#How to print single quote or double quote in screen?
print("Hi I am kilmu")
#use of escape sequence
print("she said,\"she cann't love me\"")
print('I will love her forever')
#use of mix quotes
print('one day,"she will love me too"')

#print Escape character
print("\\ is back slash")

#Intersting facts about strings in python set 2(slicing)
#A python to illustrate slicing in string
x = "Moonlight my Love"
#prints 3rd character beginning from 0
print(x[2])
#print 7th character
print(x[6])
#prints 3rd character from the rear beginning from -1
print(x[-3])
#Length of string is 14 so it is out of bound
print(x[15])


#Slicing string_name[beginning:end:step]
#A python program to illustrate print substrings of string
x ="I love you Moonnlight"
#prints substring from 2nd to 5th character
print(x[2:5])
#prints substring stepping up 2nd character from 4th to 10th character
print(x[4:10:2])
#print 3rd character from rear from 3 to 5
print(x[-5:-3])


#Python string Methods set 1 (find,rfind,startwith,endwith,islower,isupper,lower,upper,swapcase,title)
#python code to demonstrate working of find() and rfind()
str ="Moonlight the love of my life"
str2="kilmu"
#using find() to find first occurence of st2 returns 8
print("The first occurrence of str2 is at :",end="")
print(str.find(str2,4))
#using rfind () to find last occurrence of str2
#returns2
print("The last occurrence of str2 is at :",end="")
print(str.rfind(str2,4))

#python code to demonstrate working of startswith() and endswith()
str ="kilmu"
str1 ="Monlight the love of my life"
#using startswith() to find if str starts with st1
if str1.startswith(str):
    print("str1 begins with:"+str)
else: print("str1 does not begin with :"+ str)
#using endswith () to find if str ends with str1
if str1.endswith(str):
    print("str1 ends with:"+str)
else:print("str1 does not ends with:"+str)

#python code to demonstrate working of isupper() and islower()
str ="Moonlight the love of my life"
str1 ="KILMU"
#checking if all character in str1 are upper cased
if str1.isupper():
    print("All character in str1 is upper cased")
else:print("All character in str1 are not upper cased")

#checking if all charcters in str are lower case
if str.islower():
    print("All character in str is lower cased")
else:print("All charcter in str are not lower cased")

#python code to demonstrate working of upper(),lower(),swapcase() and title()
str ="Moonlight the Love of my Life"
str1=str.lower();
print("The lower case converted string:"+str1)
str2=str.upper();
print("The upper case converted string:"+str2)
str3=str.swapcase();
print("The swaps case converted string:"+str3)
str4=str.title();
print("The lower case converted string:"+str4)


#python string Methods set 2(len,count,center,ljust,rjust,isalpha,isalnum,isspace and join)
#python code to demonstrate working of len() and count()
str ="Moonlight the love of my life"
#printing length of string using len()
print("The length of string is:",len(str))
#printing occurrence of "Moonlight" in string prints 2 as it only checks till 15th element
print("Number of apperance of ""Moonlight"" is:",end="")
print(str.count("Moonlight",0,29))


# Python code to demonstrate working of
# center(), ljust() and rjust()
str = "Moonlight"

# Printing the string after centering with '-'
print ("The string after centering with '-' is : ",end="")
print ( str.center(20,'-'))

# Printing the string after ljust()
print ("The string after ljust is : ",end="")
print ( str.ljust(20,'-'))

# Printing the string after rjust()
print ("The string after rjust is : ",end="")
print ( str.rjust(20,'-'))

# Python code to demonstrate working of
# isalpha(), isalnum(), isspace()
str = "Moonlight"
str1 = "123"

# Checking if str has all alphabets
if (str.isalpha()):
	print ("All characters are alphabets in str")
else : print ("All characters are not alphabets in str")

# Checking if str1 has all numbers
if (str1.isalnum()):
	print ("All characters are numbers in str1")
else : print ("All characters are not numbers in str1")

# Checking if str1 has all spaces
if (str1.isspace()):
	print ("All characters are spaces in str1")
else : print ("All characters are not spaces in str1")

#python code to demonstrate working of join()
str="_"
str1 =("Moonlight","my","love")
#using join() to join sequence str1 with str
print("The string after joining is:",end="")
print(str.join(str1))

#python string method set 3(strip,istrip,rstrip,min,max,maketrans,translate,replace,& expandtabs())
#python code to demonstrate working of strip(),lstrip() and rstrip()
str="----Moonlight----"
#using strip() to delete all '-'
print("String after stripping all '-' is:",end="")
print(str.strip('-'))
#using lstrip() to delete all trailing '-'
print("String after stripping all leading '-' is:",end="")
print(str.lstrip('-'))
#using rstrip() to delete all leading '-'
print("String after stripping all leading '-' is:",end="")
print(str.rstrip('-'))

#python code to demonstrate working of min() and max()
str ="Moonlight"
print("The minimum value character is:" + min(str))
print("The maximum value character is:" + max(str))

# Python code to demonstrate working of
# maketrans() and translate()
from string import maketrans # for maketrans()

str = "moonlight"

str1 = "moo"
str2 = "kil"

# using maketrans() to map elements of str2 with str1
mapped = maketrans( str1, str2 )

# using translate() to translate using the mapping
print ="The string after translation using mapped elements is : "
print =str.translate(mapped)

#python code to demonstrate working of replace()
str ="Moon_light the love of my life"
str1 ="Moon_"
str2 ="kilmu"
#using replace () to replace str2 with str1 in str only changes 2 occurrences
print("The string after replacing strings is:",end="")
print(str.replace(str1,str2,2))

#python code to illustrate expandtabs()
string ='Moon\tthe_love\tof_my_life'

#No parameters,by default size is 8
print(string.expandtabs())
#tab size taken as 2
print(string.expandtabs(2))
#tab size taken as 5
print(string.expandtabs(5))

# Regular Expressions in Python – Set 2 (Search, Match and Find All)
# A Python program to demonstrate working of re.match().
import re

# Lets use a regular expression to match a date string
# in the form of Month name followed by day number
regex = r"([a-zA-Z]+) (\d+)"

match = re.search(regex, "I was born on June 24")

if match != None:

	# We reach here when the expression "([a-zA-Z]+) (\d+)"
	# matches the date string.

	# This will print [14, 21), since it matches at index 14
	# and ends at 21.
	print ("Match at index %s, %s" % (match.start(), match.end()))

	# We us group() method to get all the matches and
	# captured groups. The groups contain the matched values.
	# In particular:
	# match.group(0) always returns the fully matched string
	# match.group(1) match.group(2), ... return the capture
	# groups in order from left to right in the input string
	# match.group() is equivalent to match.group(0)

	# So this will print "June 24"
	print ("Full match: %s" % (match.group(0)))

	# So this will print "June"
	print ("Month: %s" % (match.group(1)))

	# So this will print "24"
	print ("Day: %s" % (match.group(2)))

else:
	print ("The regex pattern does not match.")


# A Python program to demonstrate working
# of re.match().
import re


# a sample function that uses regular expressions
# to find month and day of a date.
def findMonthAndDate(string):
    regex = r"([a-zA-Z]+) (\d+)"
    match = re.match(regex, string)

    if match == None:
        print("Not a valid date")
        return

    print("Given Data: %s" % (match.group()))
    print("Month: %s" % (match.group(1)))
    print("Day: %s" % (match.group(2)))


# Driver Code
findMonthAndDate("Jun 24")
print("")
findMonthAndDate("I was born on June 24")

# A Python program to demonstrate working
# of re.match().
import re


# a sample function that uses regular expressions
# to find month and day of a date.
def findMonthAndDate(string):
    regex = r"([a-zA-Z]+) (\d+)"
    match = re.match(regex, string)

    if match == None:
        print("Not a valid date")
        return

    print("Given Data: %s" % (match.group()))
    print("Month: %s" % (match.group(1)))
    print("Day: %s" % (match.group(2)))


# Driver Code
findMonthAndDate("Jun 24")
print("")
findMonthAndDate("I was born on June 24")



#Python string title method
#python string title() Method Example
print("moonlight_the_love_of_my_Life".title())

#Basic usages of python string title() method
#conversion from mixed case
str1 ="moonLight"
print(str1,'converted to using title():',str1.title())

#conversion from all lower case
str4 ="moonlight".title()
print(str4,'converted to using title():',str4.title())
#conversion from all upper case
str5 ="MOONLIGHT".title()
print(str5,'converted to using title():',str5.title())

#title() method considers any non-alphabet as a word boundary
string = "He's smarter."
expected_string ="He's Smarter"
print("Expected:",expected_string,",Actual:",string.title())

#Different word boundaries other than space,when using title() Method
string ="moonlight-mylove"
print(string,"converted using title():",string.title())

#using Regex to fix the unexpected behavior of python string title() Method
import re


def to_title(string):
	regex = re.compile("[a-z]+('[a-z]+)?", re.I)
	return regex.sub(lambda grp: grp.group(0)[0].upper() + grp.group(0)[1:].lower(),
					string)


print(to_title("I will love you forever Meri moonlight"))
"""


#Python | Swap commas and dots in a String
