st = set()
st = {'item1', 'item2', 'item3','item4'}
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}

len(st)
len(fruits)

print("Does set st contain item3?", 'item3' in st)

print('mango' in fruits)

st.add('item5')
fruits.add('lime')

st.update(['item5', 'item6', 'item7'])
print(st)
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
fruits.update(vegetables)
print(fruits)

st.remove('item2')
fruits.pop()

removed_item = st.pop()

st.clear()

fruits.clear()
print(fruits) # set()
del st
del fruits
lst = ['item1', 'item2', 'item3','item4', 'item1']
st = set(lst) # {'item1', 'item2', 'item3', 'item4'} - the order is random, because sets are unordered collections

fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits = set(fruits) # {'banana', 'orange', 'mango', 'lemon'} - the order is random, because sets are unordered collections

st1 = {'item1', 'item2', 'item3','item4'}
st2 = {'item5', 'item6', 'item7','item8'}
st3 = st1.union(st2)

print(fruits.union(vegetables))
st1 = {'item1', 'item2', 'item3','item4'}
st2 = {'item5', 'item6', 'item7','item8'}
st1.update(st2)

fruits.update(vegetables)
print(fruits)


whole_numbers = {0, 1, 2, 3, 4, 5,6, 7, 8, 9,10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.intersection(dragon) # {'o', 'n'}
python & dragon # {'o', 'n'}
whole_numbers = {0, 1, 2, 3, 4, 5,6, 7, 8, 9,10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False
even_numbers.issubset(whole_numbers) # True

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.issubset(dragon) # False


whole_numbers = {0, 1, 2, 3, 4, 5,6, 7, 8, 9,10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}
python.difference(dragon) # {'p', 'y', 't', 'h'}
dragon.difference(python) # {'d', 'r', 'a', 'g'}

python.symmetric_difference(dragon) # {'p', 'y', 't', 'h', 'd', 'r', 'a', 'g'}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True
