#!/usr/bin/env python3

"""
This module multiplies two matrices
"""


def mat_mul(mat1, mat2):
    """
    This function multiplies two matrices
    """
    if len(mat1[0]) != len(mat2):
        return None
    else:
        result_matrix = [[0 for _ in range(len(mat2[0]))]
                         for _ in range(len(mat1))]
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in range(len(mat1[0])):
                    result_matrix[i][j] += mat1[i][k] * mat2[k][j]
    return result_matrix
