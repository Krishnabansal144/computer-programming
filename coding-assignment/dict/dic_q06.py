#6. Removing Key-Value Pairs Conditionally

#Problem: You need to remove key-value pairs from a dictionary where the value meets a certain condition (e.g., value is greater than 30).

my_dict = {'John': 25, 'Alice': 35, 'Bob': 40, 'Eve': 22}
my_dict = {k: v for k, v in my_dict.items() if v <= 30}
print(my_dict)  # Output: {'John': 25, 'Eve': 22}
