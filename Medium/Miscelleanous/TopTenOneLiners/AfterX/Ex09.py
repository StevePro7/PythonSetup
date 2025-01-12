# 9. Transpose a Matrix (2D List)
rows, cols = 3, 4
matrix = []
for i in range(rows):
    row = [i + j for j in range(cols)]  # Example: Filling with i + j
    matrix.append(row)

transposed = [list(row) for row in zip(*matrix)]
print(matrix)
print(transposed)
