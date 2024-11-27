#Q19 = Write a function palindrome that checks if a given string is a palindrome and print the reversed string as well.
#=>
# Define a function named 'palindrome' that takes one parameter 's'
def palindrome(s):
    # Print the reversed string
    print("Reversed string is:", s[::-1])
    # Return True if the string 's' is equal to its reverse, otherwise False
    return s == s[::-1]

# Prompt the user to enter a string
s = input("Enter string: ")

# Call the 'palindrome' function with the user's input as the argument and print the result
print(palindrome(s))
