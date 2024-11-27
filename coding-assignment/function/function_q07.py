#Q7 = Create a function max_of_three that takes three numbers and returns the largest one.
#=>
# Define a function named 'max_of_three' that takes three parameters 'a', 'b', and 'c'
def max_of_three(a, b, c):
    # Print the maximum of the three numbers using the 'max' function
    print(max(a, b, c))

# Prompt the user to enter the first number and convert the input to an integer
number1 = int(input("Enter the number1: "))

# Prompt the user to enter the second number and convert the input to an integer
number2 = int(input("Enter the number2: "))

# Prompt the user to enter the third number and convert the input to an integer
number3 = int(input("Enter the number3: "))

# Call the 'max_of_three' function with the user's inputs as arguments
max_of_three(number1, number2, number3)

