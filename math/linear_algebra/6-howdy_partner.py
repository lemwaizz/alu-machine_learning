#!/usr/bin/env python3

"""
This module concatenates two lists
"""


def cat_arrays(arr1, arr2):
    """
    This function concatenates two strings
    """
    if not isinstance(arr1, list) or not isinstance(arr2, list):
        return None
    else:
        ans = arr1 + arr2
        return ans
