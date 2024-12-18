import numpy as np
# 2D array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Accessing elements
print(arr[0, 1])  # Element at first row, second column

# Slicing
print(arr[:, 1])  # Second column
print(arr[0:2, 1:3])  # Subarray
