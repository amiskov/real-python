"""
Fundamentals: Lists and Dictionaries
"""

colors = ['red', 'green', 'blue']
print(colors[0])
print(colors[0:2])

# lists are mutable
colors[2] = 'grey'

# add items
colors.append('fuchsia')
print(colors)

# add several items
colors.extend(['brown', 'black', 'silver'])
print(colors)

# remove items
colors.remove('red')
print(colors)

# get item's index
print(colors.index('black'))

# lists variable is a pointer to an object
clrs = colors
clrs.append('#f00')
print('\n', colors)

# if we need to copy every items of a list to another list here's the trick:
new_colors = colors[:]
new_colors.remove('#f00')
print('\nnew_colors = ', new_colors)
print('colors =     ', colors)

# another way via .extend():
new_colors2 = []
new_colors2.extend(colors)
print('\nnew_colors2 = ', new_colors2)

# sort alphabetically
colors.sort() # changes the list itself
print(colors)

# create list from string
str_list = "hello world".split()
print('\n', str_list)

other_str_list = 'one, two, three'.split(',') # using delimiter
print('\n', other_str_list)


def numbers_up_to_20(list):
    """
    Takes a list of numbers as the argument and then outputs only the numbers from the list
    that fall between 1 and 20 (inclusive)
    """
    output = []

    for n in list:
        if 1 <= n <= 20:
            output.append(n)
    return output

print(numbers_up_to_20([2, 4, 8, 16, 32, 64]))
