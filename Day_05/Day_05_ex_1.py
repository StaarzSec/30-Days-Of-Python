# 1 :


empty_list =  []


# 2 :


fruits = ['apple','banana','orange','lemon','ananas']


# 3 :


print(len(fruits))


# 4 :


print(fruits[0])

print(fruits[2])

print(fruits[4])


# 5 :

mixed_data_list = ['Woupeyi','16','1st year','Switzerland']


# 6 :

it_companies = ['Facebook','Google','Apple','Microsoft','IBM','Oracle','Amazon']
print(it_companies)


# 7 :
print(it_companies)


# 8 :
print(len(it_companies))


# 9 :

print(it_companies[0])

print(it_companies[3])

print(it_companies[6])


# 10 :

it_companies[0] = "X"
print(it_companies)

# 11:

it_companies.insert('Nvidia')
print(it_companies)


# 12 :

it_companies.insert(3,'SpaceX')
print(it_companies)


# 13 :

it_companies[2] = 'APPLE'
print(it_companies)


# 15 :

does_exist = 'Nvidia' in it_companies

print(does_exist)


# 16 :

it_companies.sort()
print(it_companies)


# 17 :

it_companies.reverse()
print(it_companies)


# 18 :

first_slice_it = it_companies[0:3]
print(first_slice_it)

# 19 :

second_slice_it = it_companies[4:7]
print(second_slice_it)


# 20 : 

middle_slice_it = it_companies[3:4]
print(middle_slice_it)

# 21 :

it_companies.pop(0)
print(it_companies)

# 22 :

it_companies.pop(3)
print(it_companies)

# 23 :

it_companies.pop(5)
print(it_companies)

# 24 :

it_companies.clear()
print(it_companies)

# 25 :

del it_companies

# 26 :

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)
