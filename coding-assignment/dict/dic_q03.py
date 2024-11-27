#3. Merging Multiple Dictionaries Using update()

#Problem: You need to merge multiple dictionaries into one, with the values from later dictionaries overwriting earlier ones.

dict1 = {'name': 'Steve', 'age': 40}
dict2 = {'age': 45, 'city': 'London'}
dict1.update(dict2)  # Merges dict2 into dict1
print(dict1)  # Output: {'name': 'Steve', 'age': 45, 'city': 'London'}
