#1. Nested Dictionary: Accessing Values in Nested Dictionaries

#Problem: You have a dictionary with nested dictionaries. You need to access values from the nested dictionaries.

my_dict = {
    'person1': {'name': 'John', 'age': 25},
    'person2': {'name': 'Alice', 'age': 30}
}
print(my_dict['person1']['name'])  # Output: John
print(my_dict['person2']['age'])   # Output: 30
