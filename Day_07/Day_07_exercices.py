# Set variables
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


# Exercice: level 1

# 1
print(len(it_companies)) # 7

# 2
it_companies.add("Twitter")

# 3
it_companies.update(["LinkedIn", "Snapchat"])

# 4
it_companies.remove("IBM")

# 5
# the difference between remove and discard is that remove will raise a KeyError if the item does not exist in the set, while discard will not raise an error if the item does not exist.

# Exercice: level 2

# 1
A.union(B)

# 2
A.intersection(B)

# 3
A.issubset(B)

# 4
A.isdisjoint(B)

# 5
A.union(B)
B.union(A)

# 6
print(A.symmetric_difference(B))

# 7
del A
del B


# Exercice: level 3

# 1
age_set = set(age)
len(age_set) # 5
len(age) # 8

# 2
# The difference between the length of the list and the length of the set is that the list can contain duplicate values, while the set only contains unique values. In this case, the list has 8 elements, while the set has 5 unique elements.

# 3
word = ["I", "am", "a", "teacher", "and", "I", "love", "to", "inspire", "and", "teach", "people"] 
split_word = set(word)
# How many unique words are in the list?
print(len(split_word))
