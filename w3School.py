print("Hello world")

x = "mamatha"
if "mamatha":
    print("yes")
else:
    print("no")

x = 5
y = "variables"
print(x, y)

x, y, z = "apple", "banana", "cherry"
print(x)
print(y)
print(z)

x = y = z = "orange"
print(x)
print(y)
print(z)

flowers = "rose", "lilly", "hibiscus"
x, y, z = flowers
print(x)
print(y)
print(z)

x = "pyhton is awesome"
print(x)

x = "python"
y = "is"
z = "awesome"
print(x, y, z)
x = "python"
y = "is"
z = "awesome"
print(x + y + z)

"""
data types
    int,float,complex
    str
    list,tuple,dict,set
    bool
"""

"""
numbers
     int,float,complex (ex: int change into float change into complex change into int)
"""

import random  # 1 to 10 means give the one random number

print(random.randrange(1, 10))

for x in "banana":
    print(x)

txt = "my name is mamatha praveen"
print("is" in txt)
print("as" not in txt)

x = "hello my world"
print(x[1:6])
print(x[:8])
print(x[1:])
print(x[-7:-2])
print(x[-1:-6])

x = "Hello World"
print(x.upper())
print(x.lower())
print(x.strip())  # strip means remove white space from the begining or end
print(x.replace("H", "J"))
print(x.split(","))  # split means separated with comma

a = "hi"  # concatenate means mixing
b = "hello"
c = a + b
print(c)
c = a + " " + b
print(c)

age = 15
txt = "my name is john i am {}"
print(txt.format(age))

name = "johny"
age = 20
school = "ABC"
std = "my name is {} schooling in {} i am {} old "
print(std.format(name, school, age))
std = "my name is {0} schooling in {1} i am {2} old "
print(std.format(name, school, age))

# booleans ( True , False )

# Python operators
#  +, -, *, /, %, &, //, <, > ......

# List ( ordered, changeble, allow duplicates )
x = ["apple", "banana", "cherry", "apple", "banana"]
print(x)
print(len(x))
print(x[2])
x[1] = "hi"
print(x)
# add ---- append,exstend,insert
# remove ---- remove,pop,del
x = ["apple", "banana", "cherry"]
print(x)

thislist = ["apple", "banana", "berry"]
for x in thislist:
    print(thislist)

# loop

# list comprehension
x = ["apple", "banana", "cherry", "mango", "kiwi"]
y = [x for x in x if "n" in x]
print(y)

# sort
x = ["apple", "banana", "cherry", "mango", "kiwi", "orange"]
x.sort()
print(x)
x.sort(reverse=True)
print(x)
x = ["apple", "Banana", "cherry", "mango", "Kiwi", "orange"]
x.sort()
print(x)
x.sort(reverse=True)
print(x)

# copy
x = ["apple", "banana", "cherry"]
y = x.copy()
print(y)
x = ["apple", "banana", "cherry"]
y = list(x)
print(y)

# joins
x = [1, 2, 3]
y = [4, 5, 6]
z = x + y
print(z)

x = [1, 4, 3]
y = [4, 5, 6]
x.extend(y)
print(x)

# tuples  (ordered ,unchangeble , allow duplicates )
# access means indexing like1:5,:4......
"""
we cant add, change, remove but we can do tuple to tuple if we want change, we should change 
into list and again change into tuple
"""

x = ("yellow", "green", "red", "cheery", "berry")
(mango, grape, *apple) = x
print(mango)
print(grape)
print(apple)

# loop
# join

# set ( unorder,unchangeble,duplicates not allowed )

x = "hello\
user"
print(x)
x = '''hello
to
world'''
print(x)

# ***********if statement
# num=int(input('enter the value'))
# if num%2==0:
#     print("it is even number")

# *********if else statement
# vote=int(input("enter your age"))
# if age>=18:
#     print("you are eligble for vote")
# else:
#     print("you are not")

# *********** else if or elif
# num=int(input("enter the values"))
# if num==10:
#     print("it is equal to 10")
# elif num==50:
#     print("it is equal to 50")
# elif num == 20:
#     print("it is equal to 100")
# else:
#     print("those are not equal to 10,50,20")

x = "helomapa"
for i in x:
    print(i)
x = range(6)  # x=range(1,8) x=range(1,30,3)
for i in x:
    print(i)

x = ['hi', 'hel', 'oy']
y = ['ap', 'ba', 'ch']

for i in x:
    for n in y:
        print(x, y)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

x = 'hello'
del x
print("{} and {} both are friends ".format("mam", "bha"))
print("{0} and {1} both are friends ".format("swa", "van"))
x = ['john', 1, 2, 3, 4, 1]
print(type(x))
print(x)

names = {1: "ananth", 2: "krish", 3: "aman"}
y = {v: k for k, v in names.items()}
print(y)

num = [1, 3, 4, 7, 5]
print(sorted(num, reverse=True)[1])

# ***********list add
x = [1, 2, 3, 4, 5, 6]
x[2] = 9
print(x)
x[1:3] = [1, 2]
print(x)
x = ['app', 'banaa', 'cher', 'mango']
y = ['hi', 'bye']
x.insert(2, 'boy')
print(x)
x.append('berr')
print(x)
x.extend(y)
print(x)

# ********** list remove
x = [1, 2, 9, 4, 7, 6]
x.remove(1)
print(x)
x.pop()
print(x)
x.clear()  # del.x means del entire list, clear means clear the data
print(x)

# ************ TUPLE
x = (1, 8, 7, 6, 5, 4, 3)
y = list(x)
y.append(9)
x = tuple(y)
print(x)
z = (10,)
x += z
print(x)
x = (1, 8, 7, 6, 5, 4, 3)
y = list(x)
y.remove(6)
x = tuple(y)
print(x)

# **********sets
x = {'app', 'banaa', 'cher', 'mango'}
y = {'hi', 'hoo'}
x.add('hello')
print(x)
x.update(y)
print(x)
x.remove('banaa')
print(x)
x.pop()
print(x)
x.clear()
print(x)
# x={'app','cher','mango'}
# del x
# print(x)
x = {'app', 'banaa', 'cher', 'mango'}
y = {'one', 'two', 'three'}
z = x.union(y)  # union,intersection,substraction
print(z)

# ***********dictionaries
dicts = {'name': 'mama', 'age': 22, 'year': 2002, 'clg': 'vgd'}
print(dicts)
print(dicts['age'])
dicts['color'] = 'blue'
print(dicts)
dicts.pop('age')
print(dicts)
for x in dicts:
    print(dicts[x])


def func(name):
    print('hi', name)


func('prama')


# ****************** required arguments
# def fun(name):
#     values='hello'+name
#     return values
# name=input("enter the name:" )
# print(fun(name))

# ****************** default arguments
def func(name, age=20):
    print('my name is', name, 'age is', age)


func(name='prama')
func(age=9, name='mapra')

# ****************lambda
x = lambda a: a + 6
print(x(9))
x = lambda a, b: a * b
print(x(9, 6))

# ************use lambda filter
value = (10, 19, 34, 68, 123, 324)
filt_val = tuple(filter(lambda x: (x % 3 == 0), value))
print(filt_val)

# ***************lambda map
values = (1, 2, 3, 4, 5)
map_val = list(map(lambda x: x ** 2, values))
print(map_val)

i = 0
while i < 6:
    print(i)
    i += 1

i = 0
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# ************   math
x = min(1, 2, 3)
y = max(1, 2, 3)
print(x)
print(y)

x = abs(-9.8)
print(x)

x = pow(2, 3)
print(x)

import math

x = math.sqrt(81)
print(x)

import math

x = math.ceil(2.4)
y = math.floor(2.4)
print(x)
print(y)

import math

x = math.pi
print(x)

# x=input("enter username:")
# print("username is:" + x)


k = ['a', 'b', 'c']
v = [1, 2, 3]
z = {}
for k, v in z.items():
    print(z)

x = [1, 2, 3, 4, 3, 2]
y = set(x)
print(list(y))

x = "2019-03-27 18:00:00"
print(len(x))

x = 1, 2, 3
y = 10, 20, 30
print(dict(zip(x, y)))

# *************** modify strings ******************
x = 'heLLo python, programming'
print(x.upper())
print(x.lower())
print(x.strip())
print(x.split(","))
print(x.replace('h', 'H'))

# ************* concatenate strings ***************
x = 'hello'
y = 'mamatha'
z = x + ' ' + y
print(x + y)
print(z)

# *********** string format ***************
x = 'mamatha'
y = 81
z = 73
form = "my name is {} bought {} quantity rupees are {}"
print(form.format(x, y, z))

forms = "my name is {2} bought {0} quantity rupees are {1}"
print(forms.format(y, z, x))

# ************** list access  *************
x = ['a', 'b', 'c', 'd', 'e', 'f']
print(x[1:3])
print(x[1:])
print(x[:3])
print(x[-4:-1])
print(x[-5])
print(x[1])

# ********** change list items ************
x = ['a', 'b', 'c', 'd', 'e', 'f']
x[1] = 'z'
print(x)
x[1:3] = ['y', 'x']
print(x)
x[1:3] = ['w']
print(x)

# ********** add list items append, exstend, insert ************
x = ['a', 'b', 'c', 'd', 'e', 'f']
x.append('w')
print(x)
x.insert(2, 'l')
print(x)
y = [1, 2, 3]
x.extend(y)
print(x)

# ********** remove list items remove, pop, clear,del ************
x = ['a', 'b', 'c', 'd', 'e', 'f']
x.remove('c')
print(x)
x.pop()
print(x)
x.pop(3)
print(x)
x.clear()
print(x)
# del x
# print(x)

# ********** loop list items  for, while ************
x = ['d', 'e', 'f']
for i in x:
    print(i)
x = ['a', 'b', 'c']
for i in range(len(x)):
    print(x[i])

x = ['z', 'y', 'x', 'w', 'v', 'u']
i = 0
while i < len(x):
    print(x[i])
    i = i + 1

# ************ list comprehension ***************
name = ['apple', 'banana', 'cat', 'dog', 'egg', 'fish']
y = []
for x in name:
    if "g" in x:
        y.append(x)
print(y)

name = ['apple', 'banana', 'cat', 'dog', 'egg', 'fish']
new = [x for x in name if 'a' in x]
print(new)

new = [x for x in name]
print(new)

name = ['apple', 'banana', 'cat', 'dog', 'egg', 'fish']
new = [x for x in name if x != 'cat']
print(new)

x = [i for i in range(1, 10)]
print(x)

x = [i for i in range(10) if i < 5]
print(x)

x = ['hello' for i in name]
print(x)

x = [i if i != 'banana' else 'bat' for i in name]
print(x)

# ************* list sort  *****************
name = ['egg', 'banana', 'apple', 'dog', 'zebra', 'fish']
name.sort()
print(name)
name.sort(reverse=True)
print(name)
name = ['egg', 'Banana', 'apple', 'dog', 'zebra', 'fish']
name.sort()
print(name)
name.reverse()
print(name)

# *********** list copy ************
name = ['egg', 'Banana', 'apple', 'dog']
names = name.copy()
print(names)
names = list(name)
print(names)

# ************** list join *****************
name = ['egg', 'Banana', 'apple']
nums = [1, 2, 34]
vals = name + nums
print(vals)
name.extend(nums)
print(name)

# ************ dictionary **************
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car["model"]
print(y)
x = car.get("year")
print(y)

x = car.keys()
print(x)
car["color"] = "red"
print(x)

x = car.values()
print(x)
car["ac"] = "working"
print(x)
# *******change dict vals ******************
x = car.values()
print(x)
car["color"] = "white"
print(x)
# *******change dict keys ******************
x = car.keys()
print(x)
car["top"] = car["color"]
del car["color"]
print(x)

x = car.items()
print(x)

if "model" in car:
    print("yes model in car")
else:
    print("no model is not in this")

if "color" in car:
    print("yes color in car")
else:
    print("no color is not in this")
# ************** pop the dict ****************
car.pop("top")
print(car)

car.clear()
print(car)

# **************** loop dict  **************
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in car:
    print(x)

for x in car.keys():
    print(x)

for x in car:
    print(car[x])

for x in car.values():
    print(x)

for x, y in car.items():
    print(x, y)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
cars = car.copy()
print(cars)

cars = dict(car)
print(cars)

# ********* nested dict *************
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily)
print(myfamily["child1"]["name"])

# ***************** Tuple update *******************
x = ('egg', 'Banana', 'apple', 'dog')
y = list(x)
y.append("fish")
x = tuple(y)
print(x)
x = ['egg', 'Banana', 'apple', 'dog']
y = ("orange",)
x += y
print(x)

x = ['egg', 'Banana', 'apple', 'dog']
y = list(x)
y.remove("apple")
print(y)

x = ['egg', 'Banana', 'apple', 'dog']
(e, b, a, d) = x
print(e)
print(b)
print(a)
print(d)

x = ['egg', 'Banana', 'apple', 'dog']
(*food, animal) = x
print(food)
print(animal)

# *********** set *************
x = {'egg', 'Banana', 'apple'}
y = {1, 2, 3, 3}
x.update(y)
print(x)

x = {'egg', 'Banana', 'apple'}
y = [1, 2, 3, 3]
x.update(y)
print(x)

x = {'egg', 'Banana', 'apple'}
y = (1, 2, 3, 3)
x.update(y)
print(x)

x = {'egg', 'Banana', 'apple'}
x.remove("Banana")  # discard, clear
print(x)

x = {'egg', 'Banana', 'apple'}
for i in x:
    print(i)

x = {'egg', 'Banana', 'apple'}
y = (1, 2, 3, 3)
z = x.union(y)
print(z)

x = {'egg', 'Banana', 'apple'}
y = (1, 2)
x.update(y)
print(x)

prices = ['24,999', '34,999', '24,999']
for i in prices:
    print(i)
three = [int(x.replace(",", "")) for x in prices]
print(three)

cart_count = "84,997.00".replace(",", "")

bal = float(cart_count)
total = int(bal)

print(total)

x = [111, 22, 13, 45]
y = x.copy()
print(y)

n1 = 20
n2 = 30
mul = n1 * n2
print(mul)
add = n1 + n2
print(add)

num = list(range(10))
previous = 0
for i in num:
    sum = previous + i
    print('Current Number ' + str(i) + ' Previous Number ' + str(previous) + ' is ' + str(sum))
    previous = i


s = "pynative"
for i in s[::2]:
    print(i)

s = "pynative"
x=s[2:]
print(x)

x = [10, 20, 30, 40, 10]
if x[0]==x[-1]:
    print("result is true")
else:
    print("result is false")
y = [75, 65, 35, 75, 30]
if x[0]==x[-1]:
    print("result is true")
else:
    print("result is false")

z=[10, 20, 33, 46, 55]
for i in z:
    if i%5==0:
        print(i)


x = "Emma is good developer. Emma is a writer"
y=x.count("Emma")
print("emma is appeared", y," times")


n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()


x=121
y=str(x)
z=y[::-1]
if z==y:
    print("Yes. given number is palindrome number")
else:
    print("No. given number is not palindrome number")


x=125
y=str(x)
z=y[::-1]
if z==y:
    print("Yes. given number is palindrome number")
else:
    print("No. given number is not palindrome number")


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
values=[]
for i in list1:
    if i%2!=0:
        values.append(i)
for i in list2:
    if i%2==0:
        values.append(i)
print(values)

for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=" ")
    print("\t")

# rows = int(input("Enter number of rows: "))
#
# for i in range(rows, 0, -1):
#     for j in range(0, i):
#         print("* ", end=" ")
#
#     print("\n")

# m=int(input("enter first number"))
# p=int(input("enter second number"))
# mul=m*p
# print(mul)


print('Name', 'Is', 'James', sep='**')

num = 458.541315
print('%.3f'% num)

i=0
while i<11:
    print(i)
    i+=1

for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=" ")
    print("\t")


numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i> 500:
        break
    elif i>150:
        continue
    elif i%5==0:
        print(i)

lis = [10, 20, 30, 40, 50]
l=reversed(lis)
for x in l:
    print(x)


for i in range(-10,0,1):
    print(i)

for i in range(5):
    print(i)
else:
    print("Done!")


x= 5 * 4 * 3 * 2 * 1
print(x)

def data(name,age):
    # print(name,age)
    print("my  name is ", name, "and ", age, " years old" )
data("mam",22)

x= [100, 200, 300, 400, 500]
y=reversed(x)
for i in y:
    print(i)

x = ["M", "na", "i", "Ke"]
y = ["y", "me", "s", "lly"]
z=[i + j for i,j in zip (x,y) ]
print(z)

x=[1, 2, 3, 4, 5, 6, 7]
y=[]
for i in x:
    y.append(i*i)
print(y)


x = [10, 20, 30, 40]
y = [100, 200, 300, 400]
z=[i + j for i,j in zip (x,y) ]
print(z)

x=float(2.8)
print(type(x))


x={1,2,3,2}
print(x)

x=15*12
print(x)

