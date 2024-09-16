import numpy as np


def print_matrix(matrix):
    # Find the maximum width considering two decimal places for formatting
    max_width = max(len(f"{item:.2f}") for row in matrix for item in row)

    # Iterate over each row in the matrix
    for row in matrix:
        # Create a formatted string for the row with numbers rounded to two decimal places
        formatted_row = ' '.join(f'{float(item):>{max_width}.2f}' for item in row)
        print(f'| {formatted_row} |')

# Generate an identity matrix
size = 4  # Specify the size of the identity matrix
identity_matrix = np.eye(size)

print_matrix(identity_matrix)
