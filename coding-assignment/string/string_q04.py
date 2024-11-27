#q4
# You are given a name and a positive integer. You are required to print a greeting message using the 
# name and a number of exclamation marks equal to the given integer. For example, if the given 
# name is 'John' and the integer is 3, the output should be 'Hello, John!!!'. 
# You will first take a string as input representing the name and then take an integer
# as input representing the number of exclamation marks

# The Python built-in function 'input' is used to read a line of text from standard input.

# First we need to take the name as string from user input
name = input()

# Now, we need to take an integer representing the number of exclamation marks
num = int(input())

# TODO: Now you need to print the greeting message using the name and the number of exclamation marks. 
# You need to use the String formatting techniques here. There are several ways to 
# format strings in python, choose the one you are most comfortable with.
print(f'Hello, {name}{"!" * num}')