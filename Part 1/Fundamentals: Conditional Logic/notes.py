"""
Fundamentals: Conditional Logic
"""

"""
Compare Values
==============
"""
# True is 1, False is 0:
print(1 + True - False)

print(1 <= 1)  # True
print(1 != 1)  # False
print(1 != 2)  # True

print("good" != "bad")  # True
print("good" != "Good")  # True

print(123 == "123")  # False

"""
Add Some Logic
==============
"""
print((1 <= 1) and (1 != 1))  # False
print(not (1 != 2))  # False
print(("good" != "bad") or False)  # True
print(("good" != "Good") and not (1 == 1))  # False

"""
Control the Flow of Your Program
================================
"""
# word = input('Enter a word: ')
word = 'hello'
if len(word) < 5:
    print('Less than 5 symmbols')
elif len(word) > 5:
    print('More than 5 symbols')
else:
    print('Equals to 5')

"""
Break Out of the Pattern
========================
"""
# for and while loops could use else:
phrase = "it marks the spot"
for letter in phrase:
    if letter == 'X':
        break
else:
    print("There was no 'X' in the phrase")  # prints if no breaks reached

tries = 0

while tries < 3:
    password = input('Password: ')
    if password == 'I<3Bieber':
        break
    else:
        tries += 1
else:
    print("Suspicious activity. The authorities have been alerted.") # always prints unless break reached

"""
Recover from errors
===================
"""
# see review_ex_try.py

"""
Simulate Events and Calculate Probabilities
===========================================
"""
# see random_examples.py
