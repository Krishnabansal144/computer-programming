# 9. Sort a tuple of tuples by the second element:
t = ((1, 3), (2, 1), (3, 2))
sorted_tuple = tuple(sorted(t, key=lambda x: x[1]))  # Output: ((2, 1), (3, 2), (1, 3))

