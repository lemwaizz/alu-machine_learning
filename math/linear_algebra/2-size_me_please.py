#!/usr/bin/env python3
def matrix_shape(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    shape = []
    shape.append(rows)
    shape.append(columns)
    print(shape)
