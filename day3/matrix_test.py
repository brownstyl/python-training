import numpy as np

# 1. Create a 2D NumPy array (Matrix) with 2 rows and 4 columns
matrix = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80]
])

# 2. Print the shape to verify it is exactly (2, 4)
print("Matrix Shape:", matrix.shape)
print("---")

# 3. Perform the vector operation (divide everything by 2)
modified_matrix = matrix / 2

# 4. Print the final modified matrix
print("Original Matrix:\n", matrix)
print("\nDivided Matrix:\n", modified_matrix)
