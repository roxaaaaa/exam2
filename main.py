# -*- coding: utf-8 -*-

import numpy as np

def matrix_norm(matrix):
    # Calculate the column norms (sum of absolute values in each column)
    return np.max(np.sum(np.abs(matrix), axis=0))

def find_min_norm_matrix(matrices):
    norms = [matrix_norm(matrix) for matrix in matrices]
    min_index = norms.index(min(norms))
    return matrices[min_index]

# Example matrices
matrix1 = np.array([[1, -2, 3], [-4, 5, -6]]) # 1+4 = 5 , 2+5 = 7 , 3+6 = 9 .... max = 9 = norma
matrix2 = np.array([[2, 3, -1], [-3, -2, 1]])
matrix3 = np.array([[0, 1, 2], [3, -1, 4]])

# List of matrices
matrices = [matrix1, matrix2, matrix3]

print(matrix_norm(matrix1))
print(matrix_norm(matrix2))
print(matrix_norm(matrix3))
# Find and print the matrix with the smallest norm
min_norm_matrix = find_min_norm_matrix(matrices)
print("Matrix with the smallest norm:")
print(min_norm_matrix)