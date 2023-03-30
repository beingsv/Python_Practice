person = {"name": "Shiwam", "age": 23, "city": "Varanasi"}

print(person["name"])

#changing value
person["age"] = 26

#add new
person["gender"] = "male"

#print via loop
for key, value in person.items():
    print(key, value)