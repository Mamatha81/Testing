import requests
response=requests.get("https://www.google.com/")
print(response.status_code)
print(response.text)
print("          ****************              ")
print(response.json)
print("          ****************              ")
print(response.headers)
print("          ****************              ")
print(response.url)
print("          ****************              ")
print(response.request)
print("          ****************              ")


response_1=requests.get("https://api.thecatapi.com/v1/breedz").json()
print()
print(response_1.status_code)
