#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise ValueError("Both m_a and m_b must be lists")
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise ValueError("Both m_a and m_b must be lists of lists")
    if not all(isinstance(item, (int, float)) for row in m_a for item in row):
        raise ValueError("m_a must be a list of lists of integers or floats")
    if not all(isinstance(item, (int, float)) for row in m_b for item in row):
        raise ValueError("m_b must be a list of lists of integers or floats")

    return np.matmul(m_a, m_b)
