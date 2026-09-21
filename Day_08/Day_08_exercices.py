import os
os.system('cls')


# 1
dog = {}

# 2
dog = {
    "name": "Buddy",
    "color": "Brown",
    "breed": "Labrador",
    "legs": 4,
    "age": 4
}

# 3 
student = {
    "first_name": "Liam",
    "last_name": "Woupeyi",
    "gender": "Male",
    "age": 15,
    "country": "Switzerland",
    "city": "Zurich",
    "address": "Bahnhofstrasse 1",
    "is_married": False,
    "skills": ["Python", "JavaScript"]
}

# 4
print(len(student)) # 9

# 5
values = student.values()
print(values)
print(type(values))

# 6 
student['skills'].append('HTML')

# 7
keys = student.keys()
print(keys)

# 8
values = student.values()
print(values)

# 9
print(student.items())

# 10
del student["address"]
student.pop("city")

# 11
del student