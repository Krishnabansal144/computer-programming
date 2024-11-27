#Q18 = Create a function flatten_list that takes a nested list and returns a flat list.
#=>
# Define a function named 'flatten_list' that takes one parameter 'nested_list'
def flatten_list(nested_list):
    # Initialize an empty list to store the flattened elements
    flat_list = []
    # Iterate over each item in the nested list
    for item in nested_list:
        # Check if the item is a list itself
        if isinstance(item, list):
            # If the item is a list, recursively flatten it and extend the flat_list
            flat_list.extend(flatten_list(item))
        else:
            # If the item is not a list, append it directly to the flat_list
            flat_list.append(item)
    # Return the flattened list
    return flat_list

# Call the 'flatten_list' function with a nested list as the argument and store the result
result = flatten_list([[1, 2, 3], 2, 4, [4, 5, 6]])

# Print the flattened list
print(result)

