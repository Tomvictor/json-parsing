import requests

print("start parsing. . . .")



r = requests.get('https://buildfromzero.com/tutorials/api/?format=json')

print("status code :")
print(r.status_code)

# print("body : ")

# raw_data = r.text
# print("raw string. .. . ")
# print(raw_data)

# print("raw data type")

# print(type(raw_data))


print("parsing json. . .. ")

json_data = r.json()
print(json_data)


print("printing type. . . . .")
print(type(json_data))


print("\r\n\r\n")
print(json_data['count'])
print("\r\n\r\n")
print(json_data['results'][0])


print("\r\n\r\n")

temp = json_data['results'][0]

print(temp)

print("\r\n\r\n")

print(temp['title'])






# print("tesig . . . . .")



# req = requests.get('https://buildfromzero.com/tutorials/api/?format=json')

# print("status code :")
# print(r.status_code)

# temp_data = r.text

# print(temp_data)

# print(r)





