
#Q4 = Define a function is_even that takes a number and returns True if it's even, otherwise False.
#=>
# Define a function named 'is_even' that takes one parameter 'num'
def is_even(num):
    # Check if the number is divisible by 2 with no remainder
    if num % 2 == 0:
        # If true, print True
        print(True)
    else:
        # If false, print False
        print(False)

# Prompt the user to enter a number and convert the input to an integer
num = int(input("Enter the number: "))

# Call the 'is_even' function with the user's input as the argument
is_even(num)
