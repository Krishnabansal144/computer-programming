# Sort a list in ascending order
numbers = [5, 2, 9, 1, 5, 6]
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print(f"The sorted list is {numbers}")