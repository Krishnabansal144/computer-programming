# 8. Replace the second element of a tuple without modifying it directly:
t = (5, 10, 15)
new_tuple = t[:1] + (20,) + t[2:]  # Output: (5, 20, 15)
