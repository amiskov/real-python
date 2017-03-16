""""""

"""
Read and write simple files
===========================
"""

# open/create file for writing.
# If the file exists then it's contents will be overwritten:
my_output_file = open('hello.txt', 'w') # variable now contains file object
my_output_file.writelines('This is my first file')
my_output_file.close() # always close file after working with it dur to buffering issues

# Passing list of lines
line_to_write = ['First line', '\nSecond line']
file = open('hello_multiline.txt', 'w')
file.writelines(line_to_write)
file.close()

# Add to the end of file - 'a' param:
file_to_add = open('hello_multiline.txt', 'a')
file_to_add.writelines('\nThird line')
file_to_add.close()

# Read contents - 'r' param (returns list with visible line breaks):
file_to_read = open('hello_multiline.txt', 'r')
print(file_to_read.readlines())
file_to_read.close()

# Common way to go through text file
file_to_read = open('hello_multiline.txt', 'r')
print('Print with for-loop:')
for line in file_to_read.readlines():
    print(line, end='') # don't print extra new-line-symbol

file_to_read.close()

# readline() method reads line-by-line saving position
file_to_read = open('hello_multiline.txt', 'r')
print('\n\nPrint with while loop line-by-line:')
line = file_to_read.readline()

while line != '':
    print(line, end='')
    line = file_to_read.readline() # update position
file_to_read.close()

# Using code blocks with `with` keyword so we don't need to close file.
# After running block Python cleans things up:
print('\n\nPrint with `with` blocks:')
with open('hello_multiline.txt') as file: # Prepare new variable environment inside block
    for line in file:
        print(line, end='')

# Read from one wile and append to another with `with`:
with open('hello.txt', 'r') as input, open('hello_multiline.txt', 'a') as output:
    for line in input.readlines():
        output.write('\n' + line)

# Find a certain place in a file with seek():
print('\n\nPlaying with seek() method:\n')
file = open('hello_multiline.txt', 'r')
file.seek(11) # go to 12th symbol (byte)
print(file.read(3)) # read 3 symbols from current position and print it
