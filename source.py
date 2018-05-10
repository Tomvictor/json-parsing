import requests

print("start parsing. . . .")



r = requests.get('https://buildfromzero.com/tutorials/api/?format=json')

print("status code :")
print(r.status_code)

print("body : ")


print(r.text)