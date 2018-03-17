"""
Multiline comment
"""

print(
"""
Mess Around with Your Words
===========================
"""
)

# Multiline string
long_string = """Multiline string variable
with many words"""

print(long_string)

# String function
print(len(long_string))

# Concatenation
print('hello' + ' ' + 'world')

# Combine several strings
print(long_string, 'hello world')

# String is just a sequence of characters, so:
print('hello'[1]) # prints 'e' (0-based numbering)
print(long_string[3:5]) # section of string. From 3rd to 5th (not including 5th) - 'ti`
print(long_string[:5], long_string[5]) # 'Multi', not including 5th
print(long_string[36], long_string[36:]) # 'words', from 36th
print(long_string[:]) # whole line


# Strings are immutable
# long_string[3] = 'j' # error


print(
"""
Use Objects and Methods
=======================
"""
)

# Strings are objects
print(long_string.upper())

# Catch user input
user_input = input('What\'s up?')
print('You sad:', user_input)

