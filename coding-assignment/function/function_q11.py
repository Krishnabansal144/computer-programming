#Q11 = Write a function greet that takes a name and a greeting message with a default value.
#=>
# Define a function named 'greet' that takes two parameters 'name' and 'message'
def greet(name, message):
    # Print the greeting message and the name
    print(f"{message}, {name}!")

# Prompt the user to enter a name
name = input("Enter the name: ")

# Prompt the user to enter a message
message = input("Enter the message: ")

# Call the 'greet' function with the user's inputs as arguments
greet(name, message)
