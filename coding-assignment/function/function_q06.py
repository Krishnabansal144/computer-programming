#Q6 = Write a function power that takes a base and an exponent and returns the base raised to the exponent.
#=>
# Define a function named 'power' that takes two parameters 'base' and 'exp'
def power(base, exp):
    # Print the result of 'base' raised to the power of 'exp'
    print(base ** exp)

# Prompt the user to enter the base and convert the input to an integer
base = int(input("Enter the base: "))

# Prompt the user to enter the exponent and convert the input to an integer
exp = int(input("Enter the exponent: "))

# Call the 'power' function with the user's inputs as arguments
power(base, exp)
