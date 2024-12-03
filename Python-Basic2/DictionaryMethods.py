person = {"name ": "Sazid","adress": "Maheshpur" , "age": "17", "job" : "Student"}

print(person)
print(person["job"])
print(person.keys())
print(person.values())
person ["language"] = "Python"
# print(person)
del person["age"]
print(person)

for key,value in person.items():
    print(key,value)
    

for key,value in enumerate(person):
    print(key,value)