#5. Dictionary Comprehension

#Problem: You need to create a dictionary from a list of keys, with values being their squares.

numbers = [1, 2, 3, 4, 5]
squares_dict = {num: num**2 for num in numbers}
print(squares_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
