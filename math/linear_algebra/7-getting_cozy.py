#!/usr/bin/env python3

"""
This module provides a function to concatenate two 2D matrices
along a specific axis.
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two 2D matrices along a specific axis.
    Args:
        mat1 (list of list of int/float): The first matrix.
        mat2 (list of list of int/float): The second matrix.
        axis (int): The axis along which to concatenate (0 for rows,
        1 for columns).
    Returns:
        list of list of int/float: The resulting matrix after concat
        enation.
        None: If the matrices cannot be concatenated.
    """
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return mat1 + mat2
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    else:
        return None
