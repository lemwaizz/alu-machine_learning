#!/usr/bin/env python3

def matrix_shape(matrix):
    if not matrix or not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise ValueError("Input must be a non-empty 2D list")
    
    rows = len(matrix)
    columns = len(matrix[0])
    
    return [rows, columns]
