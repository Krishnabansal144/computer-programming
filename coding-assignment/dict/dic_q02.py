#2. Default Dictionary Values using get()

#Problem: You need to safely access values from a dictionary, but the key may not exist. Use get() to avoid KeyError if the key is missing.

my_dict = {'name': 'Bob', 'age': 22}
print(my_dict.get('age'))         # Output: 22
print(my_dict.get('city', 'N/A')) # Output: N/A (default value if key doesn't exist)
