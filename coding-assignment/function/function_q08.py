#Q8 = Write a function reverse_string that takes a string and returns it reversed.
#=>
# Define a function named 'reverse_string' that takes one parameter 's'
def reverse_string(s):
    # Return the reverse of the string 's' using slicing
    return s[::-1]

# Prompt the user to enter a string
string = input("Enter the string: ")

# Call the 'reverse_string' function with the user's input as the argument
reversed_string = reverse_string(string)

# Print the reversed string
print(reversed_string)

