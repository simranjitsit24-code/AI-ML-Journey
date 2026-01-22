import numpy as np
#creating the array
arr  = np.array([1, 2, 3, 4, 5])
print("Original Array:")
print(arr)

#Array Operations
arr  = arr*10
print("Array after multiplication by 10:")
print(arr)

arr = arr + 5
print("Array after addition of 5:")
print(arr)

#Statistical Functions
mean_value = np.mean(arr)
print("Mean of the array:", mean_value)

std_dev = np.std(arr)
print("Standard Deviation of the array:", std_dev)

sum_value = np.sum(arr)
print("Sum of the array elements:", sum_value)
max_value = np.max(arr)
print("Maximum value in the array:", max_value)
min_value = np.min(arr)
print("Minimum value in the array:", min_value)


#Reshaping the array
reshaped_arr = arr.reshape(1, 5)
print("Reshaped Array (1x5):")
print(reshaped_arr)


#Slicing the array

sliced_arr = arr[1:4]
print("Sliced Array (elements from index 1 to 3):")
print(sliced_arr)

#Boolean Indexing
bool_index = arr > 20
filtered_arr = arr[bool_index]
print("Filtered Array (elements greater than 20):")
print(filtered_arr)

#Advanced Indexing
advanced_indexed_arr = arr[[0, 2, 4]]
print("Advanced Indexed Array (elements at index 0, 2, and 4):")
print(advanced_indexed_arr)

#Matrix Operations
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
matrix_sum = matrix_a + matrix_b
print("Matrix Sum:")
print(matrix_sum)
matrix_product = np.dot(matrix_a, matrix_b)
print("Matrix Product:")
print(matrix_product)
print (matrix_a @ matrix_b)  # Alternative way to do matrix multiplication
transpose_a = np.transpose(matrix_a)
print("Transpose of Matrix A:")
print(transpose_a)
inverse_a = np.linalg.inv(matrix_a)
print("Inverse of Matrix A:")
print(inverse_a)
determinant_a = np.linalg.det(matrix_a)
print("Determinant of Matrix A:")
print(determinant_a)

#Broadcasting
arr_c = np.array([[1, 2, 3], [4, 5, 6]])
arr_d = np.array([10, 20, 30])
broadcasted_sum = arr_c + arr_d
print("Broadcasted Sum of arr_c and arr_d:")
print(broadcasted_sum)
#column broadcasting
A = np.array([[1, 2, 3],
              [4, 5, 6]])
print(A.shape)

C = np.array([[10],
              [20]])
print(C.shape)
broadcasted_sum_col = A + C
print("Broadcasted Sum of A and C (column broadcasting):")
print(broadcasted_sum_col)

#Time Complexity Comparison 
import time
import array as arr
time_start = time.time()
arr1 = np.arange(1000000)
time_end = time.time()
print("Time taken to create NumPy array of 1,000,000 elements:", time_end - time_start)
time_start = time.time()
arr2 = arr.array('i', range(1000000))
time_end = time.time()
print("Time taken to create array module array of 1,000,000 elements:", time_end - time_start)
time_start = time.time()
arr3 = [i for i in range(1000000)]
time_end = time.time()
print("Time taken to create Python list of 1,000,000 elements:", time_end - time_start)