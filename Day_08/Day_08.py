empty_dict = {}

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

print(len(person)) # 7

print(person['first_name']) # Asabeneh
print(person['skills']) # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0]) # JavaScript

print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None

dct['key5'] = 'value5'
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)


person['first_name'] = 'Eyob'
person['age'] = 252

print('key2' in dct) # True
print('key5' in dct) # False

dct.pop('key1')
dct.popitem() # removes the last item
del dct['key2']

person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_married']        # Removes the is_married item

print(dct.items())

print(dct.clear()) # {}

dct_copy = dct.copy( ) # creates a copy of dct
keys = dct.keys() # returns a list of all the keys in the dictionary
print(keys)

values = dct.values() # returns a list of all the values in the dictionary
print(values)
