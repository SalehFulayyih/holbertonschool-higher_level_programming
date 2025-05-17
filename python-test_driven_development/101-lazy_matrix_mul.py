#!/usr/bin/python3
"""
This module defines a function for lazy matrix multiplication
using NumPy's matmul. It is part of test-driven development
in higher level programming.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy's matmul function.

    Args:
        m_a: First matrix
        m_b: Second matrix

    Returns:
        The product of the two matrices.

    Raises:
        ValueError: If the matrices can't be multiplied
    """
    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e
