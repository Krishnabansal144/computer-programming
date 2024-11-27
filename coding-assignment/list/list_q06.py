# Remove duplicates from a list
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(f"The list after removing duplicates is {unique_numbers}")