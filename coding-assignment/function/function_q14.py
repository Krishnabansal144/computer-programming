#Q14 = Write a function filter_even that takes a list and returns a list of only the even numbers.
#=>
# Define a function named 'filter_even' that takes one parameter 'numbers'
def filter_even(numbers):
    # Initialize an empty list to store even numbers
    even = []
    # Iterate over each number in the list 'numbers'
    for i in numbers:
        # Check if the number is even
        if i % 2 == 0:
            # If the number is even, append it to the 'even' list
            even.append(i)
        else:
            # If the number is not even, continue to the next iteration (this 'else' is not necessary, but included for clarity)
            continue
    # Print the filtered list of even numbers
    print("Filtered list is:", even)

# Prompt the user to enter a list of numbers, split the input string, convert each part to an integer, and store it in the list 'numbers'
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Call the 'filter_even' function with the list of numbers as the argument
filter_even(numbers)
