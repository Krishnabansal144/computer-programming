#Q17 = Define a recursive function fibonacci that returns the nth Fibonacci number.
#=>
# Define a function named 'fibonacci' that takes one parameter 'n'
def fibonacci(n):
    # Initialize the first two terms of the Fibonacci sequence
    a = 0
    b = 1
    # Check if the user wants only the first term
    if n == 1:
        print(a)
    else:
        # Print the first two terms of the sequence
        print(a, end=", ")
        print(b, end=", ")
        # Generate and print the remaining terms of the sequence
        for i in range(n - 2):
            c = a + b
            # Print each term, and add a comma and space only if it is not the last term
            if i == n - 3:
                print(c)
            else:
                print(c, end=", ")
            a, b = b, c

# Prompt the user to enter the number of terms they want in the Fibonacci sequence
number = int(input("Enter the number of terms you want: "))
# Call the 'fibonacci' function with the user's input as the argument
fibonacci(number)

