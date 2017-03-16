"""
Store Relationships in Dictionaries
"""

# Order of objects in dictionary is unimportant. They store data as key-value pairs
phonebook = {
    'Vasya': '8 909 434 32 32',
    'Petya': '+7 323 894 32 48',
    'Svetlana Petrovna': '8 909 323 38 29',
    'Mike Jordan': '+7 333 233 84 88'
}
print(phonebook, type(
    phonebook))  # Order is other, than we created because of hashing (storing values in memory for speed retrieving)

# retrieve item
print(phonebook['Vasya'])

# add item
phonebook['Putin'] = '+7 000 00 00'
print(phonebook)

# Can't store various values for the same keys:
phonebook['Vasya'] = '02'  # new number for Vasya
print(phonebook['Vasya'])

# delete key-value pair
del (phonebook['Vasya'])
print(phonebook)

# Loop over keys of a dictionary
print(phonebook.keys(),
      type(phonebook.keys()))  # special type of object: dict_keys (like list, but haven't lists' methods)

# To manipulate dict_keys objects we need to convert them into lists
keys_list = list(phonebook.keys())  # list functions converts something into list
print(keys_list, type(keys_list))

# Get each dictionary key and it's value in loop
print('\n')
for name in phonebook:
    print(name, phonebook[name])

# Check if key exists in dictionary. We need this to prevent e.g. retrieving non existed keys
print('\n')
print('Vasya' in phonebook)
print('Petya' in phonebook)

# Use dictionary sorted by keys
print('\n')
for name in sorted(phonebook):
    print(name, phonebook[name])

# sorted do not change existing dictionary
print(phonebook)

# Dictionary keys must be immutable (strings or numbers)
updated_phonebook = {
    2.25: 'Hello',
    'a': ['test', 2]
}
print(updated_phonebook['a'][0])

# Create dictionaries with dict()
# when keys are like variables (letters and numbers in names)
simple_dict = dict(my_key_1='hello', my_other_key='test')

# Dict from list of tuples (non limited for key names)
dict_with_tuples = dict([('string one', 'value one'), (2323, 'value 3')])

print(simple_dict)
print(dict_with_tuples)

# Review exercises
birthdays = {'Luke Skywalker': '5/24/19',
             'Obi-Wan Kenobi': '3/11/57',
             'Darth Vader': '4/1/41'}

if 'Yoda' in birthdays:
    print(birthdays['Yoda'])
else:
    print('unknown')

if 'Darth Vader' in birthdays:
    print(birthdays['Darth Vader'])
else:
    print('unknown')


for name in ['Yoda', 'Darth Vader']:
    if name not in birthdays:
        print('=> unknown')
    else:
        print('=>', name)


for name in birthdays:
    print(name, birthdays[name])

del (birthdays['Darth Vader'])

other_birthdays = dict([
    ('Luke Skywalker', '5/24/19'),
    ('Obi-Wan Kenobi', '3/11/57'),
    ('Darth Vader', '4/1/41')
])

print('\n', other_birthdays)
