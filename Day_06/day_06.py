# 1
tpl = ()
# 2
brother = ('Kenji')
sister = ('Thais')
# 3
siblings = brother + sister
print(siblings)

# 4
len(siblings)

# 5 
family_members = siblings = ('Thais', 'Kenji', 'Céline', 'Michel')
print(family_members)


# Exercise 2: 

# 1 
siblings = family_members[:2]
parents = family_members[2:4]
print("Siblings:", siblings)
print("Parents:", parents)

# 2 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'eggs', 'meat')
food_stuff_tp = fruits + vegetables + animal_products
print("Food stuff (tuple):", food_stuff_tp)

# 3 Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("Food stuff (list):", food_stuff_lt)

# 4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_lt) // 2
middle_items = food_stuff_lt[middle_index]
print("Middle item(s):", middle_items)

# 5 Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First three items:", first_three)
print("Last three items:", last_three)

# 6 Delete the food_stuff_tp tuple completely
del food_stuff_tp

# 7 Check if estonia exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia in nordic countries:", 'Estonia' in nordic_countries)

# 8 Check if 'Iceland' is a nordic country
print("Iceland in nordic countries:", 'Iceland' in nordic_countries)


