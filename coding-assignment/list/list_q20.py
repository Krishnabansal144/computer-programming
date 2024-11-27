# spiral matrix reversal
def spiral_traversal(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)  # Take the first row
        if matrix and matrix[0]:  # Rotate the rest counter-clockwise
            matrix = [list(row) for row in zip(*matrix)][::-1]
    return result

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(spiral_traversal(matrix))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]