"""
Make Permanent Lists
"""

# Tuples are like lists but they can't be changed (are immutable objects)
months = (
    'January'
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
)

# Functions can return multiple values as tuples


def adder_subtractor(num1, num2):
    # returns addition and subtraction of 2 numbers
    add = num1 + num2
    subtract = num1 - num2
    return add, subtract

test = adder_subtractor(3, 5)
print(test, type(test))

# parentheses are optional for creating tuples

# Tuple Packing — packing several objects into tuple:
coordinates = 1.3232, 4.2323

# Tuple Unpacking — retrieving values from tuple:
x, y = coordinates
print("x = {}, y = {}".format(x, y))

# Tuple packing/unpacking not using very frequently. Code becomes harder to read.
