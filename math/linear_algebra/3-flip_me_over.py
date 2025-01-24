#!/usr/bin/env python3

"""
This module provides a function that transposes a matrix
"""


def matrix_transpose(matrix):
    """
    Returns the transpose of a matrix
    """
    result_matrix = [[0 for _ in range(len(matrix))]
                     for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result_matrix[j][i] = matrix[i][j]
    return result_matrix
