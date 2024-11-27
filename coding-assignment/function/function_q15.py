#Q15 = Create a nested function make_greeting that returns a greeting function customized with a given greeting message.
#=>
# Define a function named 'make_greeting' that takes one parameter 'greeting'
def make_greeting(greeting):
    # Define an inner function named 'greet' that takes one parameter 'name'
    def greet(name):
        # Return a formatted greeting message using the 'greeting' and 'name'
        return f"{greeting}, {name}!"
    # Return the 'greet' function
    return greet

# Prompt the user to enter a greeting message and store it in the variable 'greeting'
greeting = input("Enter the greeting message: ")

# Prompt the user to enter a name and store the input in the variable 'name'
name = input("Enter the name: ")

# Call the 'make_greeting' function with the 'greeting' input and store the returned function in 'greeting_function'
greeting_function = make_greeting(greeting)

# Call the 'greeting_function' with the 'name' input and store the result in the variable 'message'
message = greeting_function(name)

# Print the personalized greeting message
print(message)

