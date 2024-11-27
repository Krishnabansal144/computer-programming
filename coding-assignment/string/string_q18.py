#q18
# program to find most frequent character
def most_frequent_char(s):
    from collections import Counter
    s = s.replace(" ", "")  # Remove spaces
    counts = Counter(s)
    most_frequent = counts.most_common(1)[0][0]
    return most_frequent


# Example
input_string = "banana"
print("Most Frequent Character:", most_frequent_char(input_string))