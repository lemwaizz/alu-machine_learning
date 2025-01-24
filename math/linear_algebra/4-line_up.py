#!/usr/bin/env python3

"""
This module adds two arrays (1D or 2D) together.
"""


def add_arrays(arr1, arr2):
    """
    This function checks array dimensionality then proceeds to add them.
    Args:
        arr1 (list of int/float or list of list of int/float): The first
        array.
        arr2 (list of int/float or list of list of int/float): The second
        array.
    Returns:
        list of int/float or list of list of int/float: The resulting array
        after addition.
    Raises:
        ValueError: If the arrays have incompatible dimensions.
    """
    if isinstance(arr1[0], list) and isinstance(arr2[0], list):
        if len(arr1) != len(arr2) or len(arr1[0]) != len(arr2[0]):
            return None
        result_matrix = [[0 for _ in range(len(arr1[0]))]
                         for _ in range(len(arr1))]
        for i in range(len(arr1)):
            for j in range(len(arr1[0])):
                result_matrix[i][j] = arr1[i][j] + arr2[i][j]
    else:
        if len(arr1) != len(arr2):
            return None
        result_matrix = [0 for _ in range(len(arr1))]
        for i in range(len(arr1)):
            result_matrix[i] = arr1[i] + arr2[i]
    return result_matrix
