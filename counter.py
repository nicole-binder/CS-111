'''
    counter.py
    Nicole Binder, 15 September 2018
	Adapted from a program written by Jeff Ondich

    This program counts the number of lines in a file specified by the user.
    It also counts the number of lines that contain at least 80 characters.

    To test this program, create a text file (called, say, testdata.txt)
    with a bunch of lines, plus at least one line that's longer than
    80 characters.  Then run

       python3 counter.py
       File name, please: testdata.txt
       ...

    to see how many lines and how many long (>= 80) lines are in the file.
'''

input_file_name = input('File name, please: ')
input_file = open(input_file_name)

number_of_lines = 0
number_of_long_lines = 0
number_of_blank_lines = 0
number_of_short_lines = 0
number_of_the_lines = 0

for line in input_file:
    number_of_lines = number_of_lines + 1
    if len(line) >= 80:
        number_of_long_lines = number_of_long_lines + 1
    if len(line) == 1:
        number_of_blank_lines = number_of_blank_lines + 1
    if len(line) < 80:
        number_of_short_lines = number_of_short_lines + 1
    if line.startswith('the '):
        number_of_the_lines = number_of_the_lines + 1
    if line.startswith('The '):
        number_of_the_lines = number_of_the_lines + 1




input_file.close()

print('The number of lines in', input_file_name, 'is', number_of_lines)
print('The number of long lines (80 chars or more) is', number_of_long_lines)
print('The number of empty lines is', number_of_blank_lines)
print('The number of short lines (80 chars or less) is', number_of_short_lines)
print('The number of lines beginning with "The" or "the" is', number_of_the_lines)
