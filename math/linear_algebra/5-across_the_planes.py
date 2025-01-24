#!/usr/bin/env python3

"""
This module provides a function to add two 2D matrices element-wise.
"""


def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise.
    Args:
        mat1 (list of list of int/float): The first matrix.
        mat2 (list of list of int/float): The second matrix.
    Returns:
        list of list of int/float: The resulting matrix after addition.
        None: If the matrices are not the same shape.
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    result_matrix = [[0 for _ in range(len(mat1[0]))]
                     for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            result_matrix[i][j] = mat1[i][j] + mat2[i][j]
    return result_matrix
