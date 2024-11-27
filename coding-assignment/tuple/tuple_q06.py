# 6. Count occurrences of each element in a tuple:
t = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
count_dict = {x: t.count(x) for x in set(t)}  # Output: {1: 1, 2: 2, 3: 3, 4: 4}

