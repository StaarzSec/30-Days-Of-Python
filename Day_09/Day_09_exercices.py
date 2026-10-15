# # Exercises: Level 1

# # 1
# age = int(input("Enter your age : "))

# if age >= 18:
#     message = f"You are old enough to learn to drive."
# else:
#     more_years = 18 - age
#     message = f"You need {more_years} more years to learn to drive"

# print(message)

# # 2

# MY_AGE = 15

# your_age = int(input("Enter your age : "))

# if your_age > MY_AGE:
#     difference = your_age - MY_AGE
#     if difference == 1:
#         print(f"You are {difference} year older than me.")
#     else:
#         print(f"You are {difference} years older than me.")
# elif your_age == MY_AGE:
#     print(f"We have the same age !")
# else:
#     if your_age < MY_AGE:
#         difference = MY_AGE - your_age
#         if difference == 1:
#             print(f"You are {difference} year younger than me.")
#         else:
#             print(f"You are {difference} years younger than me.")

# 3

# nbr1 = int(input("Enter number one : "))
# nbr2 = int(input("Enter number two : "))

# if nbr1 > nbr2:
#     print(f"{nbr1} is greater than {nbr2}")
# elif nbr2 > nbr1:
#     print(f"{nbr2} is greater than {nbr1}")


# Exercises: level 2


# On demande le score directement
score = int(input("Score : "))

# Pas besoin de "and", l'ordre du haut vers le bas suffit !
if score <= 59:
    grade = "F"
elif score <= 69:   # Si on arrive ici, le score est forcément > 59
    grade = "D"
elif score <= 79:   # Si on arrive ici, le score est forcément > 69
    grade = "C"
elif score <= 89:
    grade = "B"
else:               # "else" capture tout le reste (90 et plus)
    grade = "A"

message = f"Your grade is : {grade}"
print(message)

2.


season = ""
month_choose = input("Choose a month : ")
if month_choose == "december" or month_choose == "january" or month_choose == "february":
    season = "Winter"
else:
    if month_choose == "march" or month_choose == "april" or month == "may":
        season = "Spring"
    else:
        if month_choose == "june" or month_choose == "july" or month_choose == "august":
            season = "Summer"
        else:
            if month_choose == "september" or month_choose == "october" or month_choose == "november":
                season = "Autumn"

message = f"We are in {season} this month" 

3. 
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit : ") 
if fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(fruit)
    fruits.sort()

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if skills in person:
    if 'Python' in person['skills']:
        print("The person has Python skill")
    else:
        print("The person does not have Python skill")
        