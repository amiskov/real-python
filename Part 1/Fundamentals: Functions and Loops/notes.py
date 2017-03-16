"""
Fundamentals: Functions and Loops
"""

"""
Create Your Own Functions
=========================
"""


# Docstrings example. It has to come at the very beginning of a function, right after the first definition line:
def return_difference(n1, n2):
    """Return the difference between two numbers.
       Subtracts n2 from n1."""
    return n1 - n2


# with docstrings we can use command help(return_difference)
help(return_difference)


def cube(number):
    return number * number * number


print(cube(3), cube(4), cube(2))


def multiply(a, b):
    return a * b


print(multiply(2, 5))

"""
Run in circles
==============
"""
n = 1
while n < 5:
    print(n)
    n += 1

for n in range(1, 5): # starts from 1, stops before 5
    print('n = ', n)

for j in ['a', 'b', 'c', 'd']:
    print(j)


def doubles(n):
    for i in range(1, 4):
        n *= 2
        print(n)

doubles(2)