"""
Fundamentals: Working with Strings
"""

# "Addition" and "multiplication" of strings
print('hello' * 3)
print('hello' + 'world')

# Convert strings to numbers
print(int('22') + float(1.35))

# We can't convert floating point strings to integers
# int('22.3') # error

# Convert numbers to strings
print(str(22.3) + 'hello') # when we need to combine strings and numbers together


"""
Streamline Your Print Statements
================================
"""

# String interpolation is just a fancy way of saying that you want to insert some 'stuff' - i.e., variables - into a string.
name = 'Zaphod'
num_heads = 2
num_arms = 3

print('{} has {} heads and {} hands'.format(name, num_heads, num_arms)) # sequence
print('{2} has {1} heads and {0} hands'.format(name, num_heads, num_arms)) # indexes
print('{0} has {1} heads and {0} hands'.format(name, num_heads)) # repeating indexes

# assign objects right inside format, any order
print('{name} has {heads} heads and {hands} hands'.format(heads=2, name='Zaphod', hands=3))


"""
Find a String in a String
=========================
"""
phrase = "the surprise is in here somewhere"
print(phrase.find('surprise')) # 4, zero based, case sensitive starting symbol position (first appearence)
print(phrase.find('ololo')) # -1, not found
print(phrase.replace('surprise', 'ololo')) # don't change string, returns new string. Strings are immutable

