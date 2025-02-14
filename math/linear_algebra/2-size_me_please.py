#!/usr/bin/env python3

"""
This module provides a function to determine the shape of a matrix.
"""


def matrix_shape(matrix):
    """calculate shape of all dimensional matrices"""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0] if matrix else []
    return shape
