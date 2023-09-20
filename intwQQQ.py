l1 =['1','22','3','5']
l1=[int(i)for i in l1]
l1.sort()
print(l1)

# creat a dict with two lists
keys=[1,2,3,4]
values=["a","b","c","d"]
print(dict(zip(keys,values)))

#  print list with 1 to 10 numbers
list1=[x for x in range (1,11)]
print(list1)

# # palindrome
x="madam"
y=x[::-1]
print(y)
if x==y:
    print("it is palindrome")
else:
    print("it is not palindrome")


# programme to write even number 1 to 10
for x in range (1,10):
    if x%2==0:
        print(x)


# ******************    FOR LOOP   *************
i=1
for x in range(1,10):
    print(x)

i=1
for i in range(1,12):
    if i==5:
        break
    print(i)
print("its break")

i=1
for i in range (1,10):
    if i==6:
        continue
    print(i)
print("its done")

# i=1
# for i in range (1,12):
#     if x==3:
#         pass
#     print("hii")
#     print(x)

# **************    WHILE     ***************
x=1
while(x<20):
    print("hello")
    x+=1

x=1
while(x<=10):
    print(x)
    if x==5:
        break
    x+=1
print("hhhh")

# x=1
# while(x<10):
#     print(x)
#     if x==3:
#      continue
#     x+=1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


# **********  iter   ***********
x="BANANA"
y=iter(x)
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))


# ************* date time  *********
import datetime
x=datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
print(x.strftime("%p"))


import json
x = {"name": "John","age": 30,"city": "New York"}
y=json.dumps(x)
print(y)

y={
    "std":[
        {"name":"mama",
    "age":22,
    "yr":202
    },
    {"name":"mama",
    "age":22,
    "yr":12
    },
    {"name":"mama",
    "age":22,
    "yr":12
     }


    ]
}