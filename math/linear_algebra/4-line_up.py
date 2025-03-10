#!/usr/bin/env python3

"""
This module adds two arrays (1D or 2D) together.
"""


def add_arrays(arr1, arr2):
    '''
        A function that adds two arrays element-wise
    '''
    if len(arr1) == len(arr2):
        return [arr1[i] + arr2[i] for i in range(len(arr1))]
    else:
        return None
