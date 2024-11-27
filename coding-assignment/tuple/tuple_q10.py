# 10. Flatten a nested tuple into a single tuple:
nested_tuple = ((1, 2), (3, 4), (5, 6))
flattened_tuple = tuple(x for subtuple in nested_tuple for x in subtuple)  # Output: (1, 2, 3, 4, 5, 6)