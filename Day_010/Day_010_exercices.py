# Exercice Level 1 :

# 1 :
for i in range(11):
    print(i)


# 2 :
i = 0
while i < 11:
    print(i)
    i+=1


# 3 : Write a loop that makes seven calls to print(), so we get on the output the following triangle

for idx in range(1, 8):
    print('#' * idx)

# 4 : 
for idx in range(8):
    print("#"*8)

# 5 :
for idx in range(1, 11):
    print(idx, "x", idx, "=", idx*idx)

# 6 :
languages = ['Python', 'Numpy','Pandas','Django', 'Flask']
for language in languages:
    print(language)

# 7 :
for i in range(0, 101, 2):
    print(i)

# 8 :
for i in range(1, 101, 2):
    print(i)

# Exercice Level 2 :

# 1 :
sum = 0
for i in range(1, 101):
    sum += i
    print("The sum of all numbers is:", sum)
# 2 :
sum_even = 0
sum_odd = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(f"The sum of all evens is {sum_even} and the sum of all odds is {sum_odd}")
