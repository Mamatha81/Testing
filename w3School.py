print("Hello world")

x="mamatha"
if "mamatha":
    print("yes")
else:
    print("no")

x=5
y="variables"
print(x,y)

x,y,z="apple","banana","cherry"
print(x)
print(y)
print(z)

x=y=z="orange"
print(x)
print(y)
print(z)

flowers="rose","lilly","hibiscus"
x,y,z=flowers
print(x)
print(y)
print(z)

x="pyhton is awesome"
print(x)

x="python"
y="is"
z="awesome"
print(x,y,z)
x="python"
y="is"
z="awesome"
print(x+y+z)

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

import random    # 1 to 10 means give the one random number
print(random.randrange(1,10))

for x in "banana":
    print(x)

txt="my name is mamatha praveen"
print("is" in txt)
print("as" not in txt)

x="hello my world"
print(x[1:6])
print(x[:8])
print(x[1:])
print(x[-7:-2])
print(x[-1:-6])

x="Hello World"
print(x.upper())
print(x.lower())
print(x.strip()) # strip means remove white space from the begining or end
print(x.replace("H","J"))
print(x.split(",")) # split means separated with comma

a="hi" # concatenate means mixing
b="hello"
c=a+b
print(c)
c=a+" "+b
print(c)

age=15
txt="my name is john i am {}"
print(txt.format(age))

name="johny"
age=20
school="ABC"
std="my name is {} schooling in {} i am {} old "
print(std.format(name,school,age))
std="my name is {0} schooling in {1} i am {2} old "
print(std.format(name,school,age))

# booleans ( True , False )

# Python operators
#  +, -, *, /, %, &, //, <, > ......

# List ( ordered, changeble, allow duplicates )
x=["apple","banana","cherry","apple","banana"]
print(x)
print(len(x))
print(x[2])
x[1]="hi"
print(x)
# add ---- append,exstend,insert
# remove ---- remove,pop,del
x=["apple","banana","cherry"]
print(x)

thislist=["apple","banana","berry"]
for x in thislist:
    print(thislist)

#loop

#list comprehension
x=["apple","banana","cherry","mango","kiwi"]
y=[x for x in x if "n" in x]
print(y)

# sort
x=["apple","banana","cherry","mango","kiwi","orange"]
x.sort()
print(x)
x.sort(reverse=True)
print(x)
x=["apple","Banana","cherry","mango","Kiwi","orange"]
x.sort()
print(x)
x.sort(reverse=True)
print(x)

# copy
x=["apple","banana","cherry"]
y=x.copy()
print(y)
x=["apple","banana","cherry"]
y=list(x)
print(y)

#joins
x=[1,2,3]
y=[4,5,6]
z=x+y
print(z)

x=[1,4,3]
y=[4,5,6]
x.extend(y)
print(x)

# tuples  (ordered ,unchangeble , allow duplicates )
# access means indexing like1:5,:4......
"""
we cant add, change, remove but we can do tuple to tuple if we want change, we should change 
into list and again change into tuple
"""

x=("yellow","green","red","cheery","berry")
(mango,grape,*apple)=x
print(mango)
print(grape)
print(apple)

#loop
#join

# set ( unorder,unchangeble,duplicates not allowed )

x="hello\
user"
print(x)
x='''hello
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

#*********** else if or elif
# num=int(input("enter the values"))
# if num==10:
#     print("it is equal to 10")
# elif num==50:
#     print("it is equal to 50")
# elif num == 20:
#     print("it is equal to 100")
# else:
#     print("those are not equal to 10,50,20")

x="helomapa"
for i in x:
    print(i)
x=range(6) #x=range(1,8) x=range(1,30,3)
for i in x:
    print(i)



x=['hi','hel','oy']
y=['ap','ba','ch']

for i in x:
    for n in y:
      print(x,y)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

x='hello'
del x
print("{} and {} both are friends ".format("mam","bha"))
print("{0} and {1} both are friends ".format("swa","van"))
x=['john',1,2,3,4,1]
print(type(x))
print(x)




names={1:"ananth",2:"krish",3:"aman"}
y={v:k for k,v in names.items()}
print(y)

num=[1,3,4,7,5]
print(sorted(num,reverse=True)[1])

# ***********list add
x=[1,2,3,4,5,6]
x[2]=9
print(x)
x[1:3]=[1,2]
print(x)
x=['app','banaa','cher','mango']
y=['hi','bye']
x.insert(2,'boy')
print(x)
x.append('berr')
print(x)
x.extend(y)
print(x)

# ********** list remove
x=[1,2,9,4,7,6]
x.remove(1)
print(x)
x.pop()
print(x)
x.clear() # del.x means del entire list, clear means clear the data
print(x)

# ************ TUPLE
x=(1,8,7,6,5,4,3)
y=list(x)
y.append(9)
x=tuple(y)
print(x)
z=(10,)
x+=z
print(x)
x=(1,8,7,6,5,4,3)
y=list(x)
y.remove(6)
x=tuple(y)
print(x)


# **********sets
x={'app','banaa','cher','mango'}
y={'hi','hoo'}
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
x={'app','banaa','cher','mango'}
y={'one','two','three'}
z=x.union(y)          # union,intersection,substraction
print(z)


#***********dictionaries
dicts={'name':'mama','age':22,'year':2002,'clg':'vgd'}
print(dicts)
print(dicts['age'])
dicts['color']='blue'
print(dicts)
dicts.pop('age')
print(dicts)
for x in dicts:
    print(dicts[x])

def func(name):
    print('hi' ,name)
func('prama')


#****************** required arguments
# def fun(name):
#     values='hello'+name
#     return values
# name=input("enter the name:" )
# print(fun(name))

#****************** default arguments
def func(name,age=20):
    print('my name is',name,'age is',age )
func(name='prama')
func(age=9,name='mapra')


# ****************lambda
x=lambda a:a+6
print(x(9))
x=lambda a,b:a*b
print(x(9,6))

# ************use lambda filter
value=(10,19,34,68,123,324)
filt_val=tuple(filter(lambda x:(x%3==0),value))
print(filt_val)

# ***************lambda map
values=(1,2,3,4,5)
map_val=list(map(lambda x:x**2,values))
print(map_val)

i=0
while i<6:
    print(i)
    i+=1

i=0
while i<6:
    print(i)
    if i==3:
        break
    i+=1

i=0
while i<6:
    i += 1
    if i==3:
        continue
    print(i)


# ************   math
x=min(1,2,3)
y=max(1,2,3)
print(x)
print(y)

x=abs(-9.8)
print(x)

x=pow(2,3)
print(x)

import math
x=math.sqrt(81)
print(x)

import math
x=math.ceil(2.4)
y=math.floor(2.4)
print(x)
print(y)

import math
x=math.pi
print(x)

# x=input("enter username:")
# print("username is:" + x)


k=['a','b','c']
v=[1,2,3]
z={}
for k,v in z.items():
    print(z)

x=[1,2,3,4,3,2]
y=set(x)
print(list(y))

x="2019-03-27 18:00:00"
print(len(x))

x=1,2,3
y=10,20,30
print(dict(zip(x,y)))

