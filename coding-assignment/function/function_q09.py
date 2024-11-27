#Q9 = Define a function sum_list that takes a list of numbers and returns their sum.
#=>
# Define a function named 'sum_list' that takes one parameter 'numbers'
def sum_list(numbers):
    # Print the sum of the numbers in the list 'numbers'
    print(sum(numbers))

# Prompt the user to enter a list of numbers, split the input string, convert each part to an integer, and store it in the list 'numbers'
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Call the 'sum_list' function with the list of numbers as the argument
sum_list(numbers)
