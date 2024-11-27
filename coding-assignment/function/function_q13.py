#Q13 = Define a function all_even that takes a list of numbers and returns True if all numbers are even, otherwise False.
#=>
# Define a function named 'all_even' that takes one parameter 'numbers'
def all_even(numbers):
    # Check if all numbers in the list are even using a generator expression
    if all(num % 2 == 0 for num in numbers):
        # If all numbers are even, print True
        print(True)
    else:
        # If any number is not even, print False
        print(False)

# Prompt the user to enter a list of numbers, split the input string, convert each part to an integer, and store it in the list 'numbers'
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Call the 'all_even' function with the list of numbers as the argument
all_even(numbers)
