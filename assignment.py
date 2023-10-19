a = (10, 20, 30)
print(type(a))

A = 1, 2, 3, 4
a, b, c, d = A
print(d)  # this type of assgnment is called tuple unpacking

# a=int(input("enter value of A: "))
# b=int(input("enter value B: "))
# print("A={} and B={}".format(a,b))
# a=a+b
# b=a-b
# a=a-b
# print("now A={} and B={}" .format(a,b)) # this kind of assignment is called parellel assignment

a = 1
b = a
a = 2
print(b)

x = 10
y = id(x)
print(type(x))
print(y)

# x=0101
# y=2
# c=x+y
# print(c)    SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

print(1 + 2)
print(2 - 1)
print(2 * 3)
print(3 // 2)  # 1
print(3 / 2)  # 1.5
print(-3 // 2)  # answer -1.5 it will do round figure -2
print(-3 / 2)  # -1.5

# what are the basic data type supported by python
# numeric dt: int,float,long,none type
# string:str
# boolean : T, F
# none type: none

a = "Hello world"
print(id(a))
# here the values of id get different values because of change the H h
a = "hello world"
b = a
print(a is b)
print(id(a))
print(id(b))

a = [1, 2, 3]
for i in a:
    print("in for loop")
else:
    print("not in for loop")

import sys

print(sys.version)

x = "mamathapraveen"
y = x
print(sys.getrefcount(x))

# l="bahubali"
# k=l
# print(sys.getrefcount(l))
# del l
# print(sys.getrefcount(l))  #NameError: name 'l' is not defined


x = range(1, 10)
print(type(x))

# a=xrange(1,10)
# print(type(a)) xrang is not working in version 3 range and xrange work only range

# ****** what happend in the background when you run the python file
# when we run the .py file it undergoes 2 phases one phase is syntax and second phase is it compiles to byte code
# using python virtual machine, loads the byte code into memory and runs

# ******** what is a module in python
# a module is a.py in python in which variable, functions, and classes can be defined
# it can also have a ruunable code

# *********  how do you include a module in your python file
# the keyword "import" is used to import a module into the current file
# ex: import sys here sys is a predefined module

# ***** how do you reload a python module
# there is function reload() in a python. which take module name as an argument and reload the module

# ******* what is list in python
# the list is one of the built in datastructure in python. list is order,changeble allow duplicates immutable
# elements are separated by comma and closed with square brackets

# **** when do you choose list over a tuple

# **** how do you get last value in a list or tuple
# when we pass -1 to the index operator of the list or tupleit returns the last value
a = (1, 2, 3, 4)
print(a[-1])
b = [1, 2, 3, 4]
print(b[-1])

# **** what is the index out of range error
# when the value is given greater than the actual size list or tuple, index out of range error
# x=[1,2,3,4,5]
# print(x[5])
#
# x=(1,2,3,4,5)
# print(x[5])

# what is slice notation in python to access element in iterator
# access to more than one element fromlist or a tuple we can use ':' operator syntax is
# a[strtindex:endindex:step]

x = [1, 2, 3, 4, 5, 6, 7, 8]
print(x[1:8:2])

# *** how do you convert a list of integers to acomma separated string
# list elements can be turned into a string using join function
x = [1, 2, 3, 4]
print(x)
numbers = ",".join(str(i) for i in x)
print(numbers)

#  28 *** what is the difference between python append() and extend() function
# extend function takes an iterable and adds each element of the iterable to the list.
# takes the value and adds to the list as single object
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)

a = [1, 2, 3]
a.append(5)
print(a)

# tell me about a few string operations in python
a = "name"
b = "c"
print(a)  # a string
print(b)  # a char

name = str()
print(name)
name_ = str("new string")
print(name_)

# *** strings are immutable
s1 = "welcome"
s2 = "welcome"
print(id(s1), id(s2))
s3 = s2 + "to python"
print(s3)
s4 = (s2 * 3)
print(s4)
# **** slicing
s = "welcome to python"
print(s[1:6])
print(s[1:])
print(s[:6])
print(s[::-1])  # it will come back
print(s[1:-2])  # eliminate two char from end

# *** string functions in python
print(len("abcd"))
print(max("abcd"))
print(min("abcd"))

# *** in and not in operator
x = "welcome"
print("come" in x)
print("come" not in x)

#  **** string comparison
print("tim" == "tie")
print("free" != "freedom")
print("yellow" <= "fellow")

# **** testing strings
x = "welcome"
print(x.isalnum())
print("welcome".isalpha())
print("2012".isdigit())
print("ABC".isupper())
print("ABC".isdigit())

# *** searching for substring
x = "i am indian"
print(x.endswith("an"))
print(x.startswith("am"))
print(x.find("am"))  # am strts from second position so 2
print(x.find("bind"))  # bind is not in x so -1
print(x.count("i"))

# *** string converting
y = "my name IS MAMATHA"
print(y.upper())
print(y.lower())
print(y.title())
print(y.capitalize())
print(y.swapcase())

# **** how do you create a list which is  a reverse version on another list in python
x = [1, 2, 3, 4, 5, 6]
y = list(reversed(x))
print(y)

# ********** what is a dictionary in a python
# dictionary is a kind of hash or map in another language. dictionary contains keys and values keys are unique values
# are accessed using keys
data = {"name": "mamatha", "age": 21, "color": "red"}
print(data)
print(data["name"])
data["year"] = 2001
print(data)
data["year"] = 2002
print(data)
del data["age"]
print(data)

# *** how do you merge one dictionary with the other
# python provide update() method we can use that for merge one to other
a = {'name': "mama"}
b = {'age': 21}
a.update(b)
print(a)

# **** how to walk through a list in a sorted order without sorting the actual list
a = [5, 3, 4, 1, 2]
a.sort()  # using sort method
print(a)
print(sorted(a))

a = [5, 3, 4, 1, 2]
print("original list", a)
for i in range(0, len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print("sorted list", a)

name = ['john', 'fan', 'can', 'jam', 'joy', 'tom', 'tan']
jname = [i for i in name if i[1] == 'a']
print(jname)

# **** what is a set
# set is unordered collection of unique objects

# *** find how many different characters are present in this string
a = "this is a sample string with many characters"
print(len(a))
print(len(set(a)))

# ***** name some standard error in python
# type error      expected type doesn't match with the given type of variable
# value error     expected value not given if you are expecting 4, you have given 2
# name error      trying to access a variable or function that is not defined
# IO error        trying to access a file that doesn't exist
# index error     accessing a invalid index   of a sequence will through
# key error       when invalid key is used t access a value in the dictionary

# **** how python support encapsulation with respect to function
# python supports inner function, a function define inside a function is called inner function whose behaviour is not hidden.

# how do you open an already existing file and add content to it
# f=open("simple-file.txt","a") open the file in append mode
# f.write("some content") append content to the file
# f.close() closes the file

# ***** what is bult in type does python provide
# there are mutable and immutable data built in data types are there
# Mutable builtin data types            #immutable built in data types
#  list                                     # string
#  set                                      #  tuple
#  dictionaries



