#Q2 = Write a function add that takes two numbers and returns their sum.
#=>
# Define a function named 'add' that takes two parameters 'a' and 'b'
def add(a, b):
    # Print the sum of 'a' and 'b'
    print(a + b)

# Prompt the user to enter the first number and convert it to an integer
first_number = int(input("Enter the first number: "))

# Prompt the user to enter the second number and convert it to an integer
second_number = int(input("Enter the second number: "))

# Call the 'add' function with 'first_number' and 'second_number' as arguments
add(first_number, second_number)
