# Find the index of an element in a list
numbers = [10, 20, 30, 40, 50]
element = 30
index = -1
for i in range(len(numbers)):
    if numbers[i] == element:
        index = i
        break
if index != -1:
    print(f"The element {element} is at index {index}")
else:
    print(f"The element {element} is not found in the list.")