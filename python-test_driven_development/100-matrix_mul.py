#!/usr/bin/python3
"""
Module for matrix multiplication.
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices after validating inputs.

    Args:
        m_a (list of lists): First matrix (2D list of integers/floats).
        m_b (list of lists): Second matrix (2D list of integers/floats).

    Returns:
        list of lists: Result of matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
                  contains non-integer/float elements, or is irregular.
        ValueError: If m_a or m_b is empty or matrices can't be multiplied.
    """
    # Error messages
    ERR_MA_NOT_LIST = "m_a must be a list"
    ERR_MB_NOT_LIST = "m_b must be a list"
    ERR_MA_NOT_LIST_OF_LISTS = "m_a must be a list of lists"
    ERR_MB_NOT_LIST_OF_LISTS = "m_b must be a list of lists"
    ERR_MA_EMPTY = "m_a can't be empty"
    ERR_MB_EMPTY = "m_b can't be empty"
    ERR_MA_INVALID_ELEMS = "m_a should contain only integers or floats"
    ERR_MB_INVALID_ELEMS = "m_b should contain only integers or floats"
    ERR_MA_NOT_RECTANGULAR = "each row of m_a must be of the same size"
    ERR_MB_NOT_RECTANGULAR = "each row of m_b must be of the same size"
    ERR_CANNOT_MULTIPLY = "m_a and m_b can't be multiplied"

    # Validate m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError(ERR_MA_NOT_LIST)
    if not isinstance(m_b, list):
        raise TypeError(ERR_MB_NOT_LIST)

    # Validate m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError(ERR_MA_NOT_LIST_OF_LISTS)
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError(ERR_MB_NOT_LIST_OF_LISTS)

    # Validate m_a and m_b are not empty
    if not m_a or any(not row for row in m_a):
        raise ValueError(ERR_MA_EMPTY)
    if not m_b or any(not row for row in m_b):
        raise ValueError(ERR_MB_EMPTY)

    # Validate all elements are integers or floats
    for row in m_a:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(ERR_MA_INVALID_ELEMS)
    for row in m_b:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(ERR_MB_INVALID_ELEMS)

    # Validate matrices are rectangular
    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError(ERR_MA_NOT_RECTANGULAR)
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError(ERR_MB_NOT_RECTANGULAR)

    # Validate if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError(ERR_CANNOT_MULTIPLY)

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(len(m_b[0])):
            dot_product = 0
            for k in range(len(m_b)):
                dot_product += m_a[i][k] * m_b[k][j]
            row_result.append(dot_product)
        result.append(row_result)

    return result
