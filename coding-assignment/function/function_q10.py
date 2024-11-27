#Q10 = Create a function count_vowels that takes a string and returns the number of vowels in it.
#=>
# Define a function named 'count_vowels' that takes one parameter 's'
def count_vowels(s):
    # Define a string containing all the vowels (both lowercase and uppercase)
    vowels = 'aeiouAEIOU'
    # Initialize a counter variable to 0
    count = 0
    # Iterate over each character in the string 's'
    for i in s:
        # If the character is in the 'vowels' string, increment the counter
        if i in vowels:
            count += 1
        else:
            continue  # This 'else' is not necessary, but it's fine to include it for clarity
    # Print the total count of vowels in the string
    print("The number of vowels in given string is:", count)

# Prompt the user to enter a string
s = input("Enter the string: ")

# Call the 'count_vowels' function with the user's input as the argument
count_vowels(s)
