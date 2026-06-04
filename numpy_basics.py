
import numpy as np

# 1D Array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(array_1d)

# 2D Array
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6]])
print("\n2D Array:")
print(array_2d)

# 3D Array
array_3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print("\n3D Array:")
print(array_3d)

# Arrays for Operations
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([2, 4, 5, 8])

# Addition
print("\nAddition:")
print(arr1 + arr2)

# Subtraction
print("\nSubtraction:")
print(arr1 - arr2)

# Multiplication
print("\nMultiplication:")
print(arr1 * arr2)

# Division
print("\nDivision:")
print(arr1 / arr2)