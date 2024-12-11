import numpy as np
# 1D Array
arr_1d = np.array([1, 2, 3, 4, 5])

# 2D Array
arr_2d = np.array([[1, 2], [3, 4], [5, 6]])

print("1D Array:", arr_1d)
print("2D Array:\n", arr_2d)

# Creating a 3D array 
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) 
print(arr_3d) 

# Indexing
print("Element at index 2:", arr_1d[2])

# Slicing
print("Sliced Array (1:4):", arr_1d[1:4])

# Boolean Indexing
arr3=arr_1d>3 
print("Elemnets greater  than 3=",arr_1d[arr3])   

# Adding elements
arr = np.append(arr_1d, [6, 7])

# Removing elements
arr = np.delete(arr, 0)

# Sorting
arr_sorted = np.sort(arr)

print("Modified Array:", arr)
print("Sorted Array:", arr_sorted)

# Basic Operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Data Types
# Numerical Data
numerical_data = [1, 2, 3, 4, 5]
print("Numerical Data:", numerical_data)

# Categorical Data
categorical_data = ['Red', 'Blue', 'Green']
print("Categorical Data:", categorical_data)

# Cardinal Data
cardinal_data = ['12345', '67890', '54321']
print("Cardinal Data:", cardinal_data)

#Creating a Matrix
matrix1 = np.array([[1, 2], [3, 4]]) 
matrix2 = np.array([[5, 6], [7, 8]]) 

#Addition
matrix_sum = matrix1 + matrix2 
print(matrix_sum) 

#Subtration
matrix_diff = matrix2 - matrix1 
print(matrix_diff) 

#Multiplication
matrix_prod = matrix1 * matrix2 
print(matrix_prod) 