# 9. Transpose a Matrix (2D List)
rows, cols = 3, 4
matrix = []
for i in range(rows):
    row = [i + j for j in range(cols)]  # Example: Filling with i + j
    matrix.append(row)

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix)
print(transposed)
