# 1 *** comments

#  2 *** keywords
import keyword

print(keyword.kwlist)

# 3 *******  variable
# a variable is nothing but reserved memory location to store values
# variables are used to store the data
# memory allocated when the value are stored in variable
# every variable must have some type
x = 5
a, b, c = 10, 20, 30
d = e = f = 1

# 4 ******  datatypes
# ** numbers,string,boolean,     list, tuple,dictionary
# numbers ---int, float
x = 5  # int type
y = 5.2  # float type
bt = True  # boolean type
bf = False  # boolean type
string = "welcome"  # string type

# concatenation
print(10 + 10)  # v 20
print(10.2 + 10.5)  # V 20.7
print(10 + 10.5)  # V 20.5
print(10 + True)  # V 11
print(10 + False)  # V 10
print("welcome" + "python")  # V  welcomepython
print(True + True)  # V 2
# print(10+"python") # NV
# print(True+"welcome") # NV
# print(10.5+"Welcome") # NV


# *** swapping
x = 5
y = 10
print("before sapping", x, y)
y, x = x, y
print("after swapping", x, y)

# *** Redeclaration
# in other programming language we can't declare same values but in python we can redeclare the values
a = 10
print(a)

a = 20
print(a)

# *** deleting variables
a = 1
print(a)

# del a  # delete the variable
# print(a) # it will shows name error  name a is not defined

# *** How to take input from user in python
#  * string to int
# n1 = input("enter first number: ")  # 10 treated as string
# n2 = input("enter second number: ")  # 20 treated as string
# print(n1+n2)

# n1 = input("enter first number: ")  # 10 treated as string
# n2 = input("enter second number: ")  # 20 treated as string
# print(int(n1)+int(n2)) before print we can convert into int

# s1 = int(input("enter first number: ")) # 10 treated as number
# s2 = int(input("enter second number: ") ) # 20 treated as number
# print(s1+s2)

#  * string to float
# n1 = input("enter first decimal number: ")  # 10.5 treated as string
# n2 = input("enter second  decimal number: ")  # 10.5 treated as string
# print(n1 + n2)
#
# n1 = input("enter first number: ") # 10 treated as string
# n2 = input("enter second number: ")  # 20 treated as string
# print(float(n1)+float(n2)) #before print we can convert into float

# n1 = input("enter first number: ") # 10 treated as string
# n2 = input("enter second number: ")  # 20 treated as string
# print(float(n1)+float(n2)) #before print we can convert into float

# convert string to int and float
# n1 = input("enter first int number: ")  # 10 treated as string
# n2 = input("enter second decimal number: ")  # 20.5 treated as string
# print(int(n1) + float(n2))  # before print we can convert into float and int at the same time


#  **** formatting output
# * approach 1
name = "praveen"
age = 28
sal = 123.45
print(name, age, sal)
# * approach 2
print("name is : ", name)
print("age is : ", age)
print("salary is : ", sal)
# * approach 3     using % operator
print("name:%s age:%d sal:%f" % (name, age, sal))
# * approach 4
print("name:{} age:{} sal:{}".format(name, age, sal))
# * approach 5
print("name:{0} age:{1} sal:{2}".format(name, age, sal))

# **** flow control statement in python
# * conditional statement --- if else
a = 20
if a > 20:
    print("yes")
else:
    print("no")

b = 10
if b % 2 == 0:
    print("10 is even")
else:
    print("10 is odd")

# multiple statement under if else statement
if True:
    print("Statement 1")
    print("Statement 2")  # if True
    print("Statement 3")
else:
    print("statement5")
    print("statement6")  # if False
print("this is not part of if or else block")

# single statements in single line
print("Hello") if True else print("bye")
print("Yes") if 10 < 20 else print("no")

# multiple statements in single line
x = {print("hello"), print("friend")} if True else {print("Bye"), print("Friend")}
y = {print("hello"), print("friend")} if False else {print("Bye"), print("Friend")}

# elif statement
a = 10
if a == 10:
    print("ten")
elif a == 20:
    print("twenty")
elif a == 30:
    print("thirty")
else:
    print("it is not in list")

# * iterative statement  ( loops ) ---- for, while
# forloop is always used with range()
# print 1 to 10 even numbers
print(list(range(10)))  # (0,1,2,3,4,5,6,7,8,9)
for i in range(10):
    print(i)  # print 0,1,2............9
for i in range(0, 10, 2):  # print even numbers
    print(i)

for i in range(1, 10, 2):  # print odd numbers
    print(i)

for i in range(10, 1, -1):
    print(i)  # print 10 to 1 in reverse

# while loop
i = 1
while i <= 5:
    print(i)
    i = i + 1

i = 5
while i >= 1:
    print(i)
    i = i - 1

# * jumping statement    (Transfer statements)---- Break, Continue
#  for Break
for i in range(1, 10):
    if i == 5:
        break
    print(i)
#  for continue
for i in range(1, 10):
    if i == 5:
        continue
    print(i)

#  while Break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
# while continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# **** number types
x = 10
print(type(x))
y = 10.5
print(type(y))
# **** number type conversion
x = 5.4
print(int(x))
print(type(int(x)))
y = 5
print(float(y))
print(type(float(x)))
x = 5
y = float(x)
print(y)
# *** Built-in function on  number type
big = max(10, 20, 30, 40)
print(big)
small = min(10, 20, 30, 40)
print(small)

# ***** python strings
# * creating string ---- strings are immutable
name = 'mamatha'
print(name)
name1 = str('praveen')
print(name1)

# * strings in python are immutable
str1 = "welcome"
print(id(str1))
str2 = "welcome"
print(id(str2))
str2 = str2 + "to python"
print(id(str1))
print(id(str2))

# *operation on string
str1 = "welcome"
print(str1 * 3)
print(str1 + " to python")

# * slicing
x = "welcome to"
print(x[1:5])
print(x[:5])
print(x[1:])
print(x[1:-1])

# * ord() and chr() functions
# ord() = this function returns the ascii code of the character
# chr() = this function returns the ascii character of the number
print(ord('L'))  # 65
print(chr(77))  # M
print(chr(80))  # P

# * string function in python
# len() ---- returns length of the string
# max() ---- returns character having highest ascii value
# min() ---- returns character having lowest ascii value
print(len("hello"))
print(max("hello"))
print(min("hello"))

# * in and not in operstors
x = "welcome"
print("we" in x)
print("come" not in x)

# * string comparison
# { >, <, >=, <=, ==, != }
print("tim" > "time")
print("man" < "woman")
print("child" >= "time")
print("tim" <= "time")
print("second" == "time")
print("baby" != "child")

# * iterating string using for loop
s = "python"
for i in s:
    print(i)  # python in char will print one by one
s = "python"
for i in s:
    print(s)  # python will print 6 times

# * Testing strings
s = "welcome to PYTHON"
print(s.isalnum())
print("welcome".isalpha())
print("welcome".isupper())
print("123".isdigit())
print("welCome".islower())
print("1".isidentifier())

# * searching for substring
s = "welcome to python"
print(s.startswith("we"))
print(s.endswith("o"))
print(s.find("to"))
print(s.rfind("k"))  # returns lowest index from where s1 starts in string not found return -1
print(s.count("e"))  # returns highest index from where s1 starts in string not found return -1

# * converting strings
s = "welcome to PYTHON"
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.replace("PYTHON", "PYTHON1"))

# ****** python lists
# list is another type of list sequence defined list class of python
# list allows to add, delete
# list is very similar to arrays
# * creating list
l1 = [1, 2, 3, 4, 5]
print(l1)
l2 = ['mama', 'prav', 'saty', 'madh']
print(l2)
l3 = []
print(l3)
l4 = ['python']
print(l4)
# * access elements from the list
l1 = [1, 2, 3, 4, 5]
print(l1[3])

# * list common operations
l1 = [1, 2, 3, 4, 5]
print(2 in l1)
print(6 not in l1)
print(len(l1))
print(min(l1))
print(max(l1))
print(sum(l1))

# * list slicing
l1 = [12, 13, 23, 34, 5, 45, 56, 6]
print(l1[1:4])
print(l1[:4])
print(l1[1:])

# * [+ and * operator
l1 = [12, 13, 23, 34]
l2 = [5, 45, 56, 6]
print(l1 + l2)
print(l1 * 3)

# * in or not in operator

l1 = [12, 13, 23, 34]
print(12 in l1)
print(12 not in l1)

# * traversing list using for loop
l1 = [12, 13, 23, 34, 8]
for i in l1:
    print(i)
l1 = [12, 13, 23, 34, 8]
for i in l1:
    print(i, end=" ")  # if you want the number continuously side by side we should use end=

# * commonly used in list method with return type
# append,extend,insert, remove,pop,del,,clear, change
l3 = [12, 13, 23]
print(l3.append(4))
print("append", l3)
l1 = [12, 13, 23]
l2 = [1, 2, 3]
l1.extend(l2)
print("extend", l1)
l1 = [12, 13, 23]
l1.insert(1, 5)
print("insert", l1)

l1 = [12, 13, 23, 1, 2, 3]
l1.remove(2)
print("remove value2", l1)
l1.pop()
print("pop last value", l1)
l1.pop(1)
print("pop the index number 1 ", l1)
l1.clear()
print(l1)
# del l1
# print(l1)  # it will shows " name error "
l1 = [12, 13, 23, 1, 2, 3]
l1.reverse()
print(l1)
l1.sort()
print(l1)
l1 = [12, 13, 23, 1, 1, 1, 2, 3]
l2 = l1.count(1)
print(l2)
l1 = [1, 2, 3, 4, 5]
l2 = l1.index(3)
print(l2)
# * list comprehension
l1 = [x for x in range(10)]
print(l1)
l1 = [x + 1 for x in range(10)]
print(l1)
l1 = [x for x in range(10) if x % 2 == 0]
print(l1)

# ******* creating dictionary
# dict is a python data type is used to store key value pair
# it enable to quickly retrive, add, remove using keyband pair
# dict are very similar hashmap in java
# dict are mutable
# dict can be created using a pair of curly braces
# eac item in the dict consist of key ,followed by a colon which is followed by value
# each item using separated by comma
# key must be hashable type, but value can be anytype
# each key in the dictionary must be unique
data = {"name": "mamaprav",
        "age": 21,
        "dob": 2003}
print(data)

# * retrieving elements in the dictionary
print(data["name"])
# * adding elements in the dictionary
data["college"] = 1234
print(data)
# * modify elements in the dictionary
data["dob"] = 2002
print(data)
# * delete elements in the dictionary
del data["college"]
print(data)
# * looping items in the dictionary
alpha = {'a': 1,
         'b': 2,
         'c': 3,
         'd': 4,
         'e': 5, }
for x in alpha:
    print(x, ':', alpha[x])

# * find the length of the dictionary
print(len(alpha))

# * equality test in dictionary
keys = {"a": 10, "b": 20}
values = {"b": 20, "a": 10}
print(keys == values)
print(keys != values)

# * dictionary methods
alpha = {'a': 1,
         'b': 2,
         'c': 3,
         'd': 4,
         'e': 5, }
print(alpha.keys())
print(alpha.values())
print(alpha.popitem())
print(alpha.pop('b'))
print(alpha.get('d'))
print(alpha.clear())

# ****** python tuples
# tuples are very similar to list but in tuple we cant add remove delate
# tuples are immutable
t1 = (1, 2, 3)
print(type(t1))
t2 = ()
t3 = ([9, 8, 7, 6, 5, 4])
print(type(t3))
# * tuples functions
t3 = (9, 8, 7, 6, 5, 4)
print(max(t3))
print(min(t3))
print(sum(t3))
print(len(t3))

# iterating through tuple
t3 = (9, 8, 7, 6, 5, 4)
for i in t3:
    print(i)
for i in t3:
    print(i, end=' ')

# * slicing tuple
t3 = (9, 8, 7, 6, 5, 4)
print(t3[0:3])
print(t3[0:])
print(t3[:3])
print(t3[1:-2])
# * in and not in operator
print(8 in t3)
print(8 not in t3)


# **** list vs dictionary vs tuple


# ****** file handling
# * we can use file handling to read and write data to and from the file
# *opening a file
# f=open(filename,mode)
# three modes are there in opening file
# 'r'=open a file for read only
# 'w'=open a file for writing if already exist data will be cleared before opening otherwise new data will be created
# 'a'=open a file in append mode to write the data end of the file
# # closing a file
# f.close()
# writing
# # file = open('D:/Basics/filehandling', 'w')
# file = open('D:/filehandling', 'w')
# file.write('this is my first file handling ')
# file.write(' i created first time dile handling')
# file.close()
# data into file
# reading data from a file
# appending data
# looping through the data using for loop

# **** classes and object
# * creating basic class and objects which include methods
class myclass:
    def myfun(self):
        pass

    def display(self, name):
        print("my name is: ", name)


o = myclass()
o.myfun()
o.display('mamatha')


# * instance method and static method
# instance method should have self  static method no need
class types_methods:
    def insta(self):
        print("this is instance method")

        @staticmethod
        def stati():
            print('this is static method')


m = types_methods()
m.insta()
types_methods.stati()