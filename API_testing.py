from urllib.request import urlopen
import json
url="https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
response=urlopen(url)
data_json=json.loads(response.read())
print(data_json)

dates=[]
for cods in data_json["list"]:
       # print(cods["main"]["temp"])
       # print(cods["main"]["pressure"])
       # print(cods["wind"])
       keys=dates.append(cods["dt_txt"][0:10])
       values=dates.append(cods["dt_txt"][12:])
print((dates))
# print(dict(zip(keys,values)))






# option=input("""
# Please choose an option from below
# 1. Get Temperature
# 2. Get Wind Speed
# 3. Get Pressure
# 0. Exit
# """)

# for cods in data_json["list"]:
#      if int(option)==1:
#        print(cods["main"]["temp"])
#      elif int(option) == 2:
#        print(cods["wind"])
#      elif int(option)==3:
#        print(cods["main"]["pressure"])
#      elif int(option)==0:
#           pass


dates="2019-03-27 18:00:00"
print(dates[0:10])