#!/usr/bin/python3
"""Matrix Element Division Module"""


def matrix_divided(matrix, div):
    """Function to divide a matrix by div"""

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    len_e = 0
    msg_size = "Each row of the matrix must have the same size"

    new_matrix = []

    for elm in matrix:
        if not elm or not isinstance(elm, list):
            raise TypeError(msg_type)

        if len_e != 0 and len(elm) != len_e:
            raise TypeError(msg_size)

        new_row = []

        for val in elm:
            if not type(val) in (int, float):
                raise TypeError(msg_type)

            len_e = len(elm)

            new_row.append(round(val/div, 2))
        new_matrix.append(new_row)

    return new_matrix
