# Count occurrences of an element in a list
numbers = [1, 2, 3, 1, 2, 1, 4]
element = 1
count = 0
for num in numbers:
    if num == element:
        count += 1
print(f"The element {element} occurs {count} times in the list.")