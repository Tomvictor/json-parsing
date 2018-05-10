import requests

print("start parsing. . . .")



r = requests.get('https://buildfromzero.com/tutorials/api/?format=json')

print("status code :")
print(r.status_code)

print("body : ")

raw_data= r.text
print(raw_data)

json_data = r.json()

print(type(json_data))

