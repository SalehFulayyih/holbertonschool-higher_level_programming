#!/usr/bin/python3
"""
This module defines a function for lazy matrix multiplication
using NumPy's dot function to match specific output expectations.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy's dot function.

    Args:
        m_a: First matrix
        m_b: Second matrix

    Returns:
        The product of the two matrices as a NumPy array.

    Raises:
        ValueError: For invalid types, dimensions, or contents
    """
    # Check if either of the inputs is a scalar (string or non-list-like)
    if not isinstance(m_a, (list, tuple)) or not isinstance(m_b, (list, tuple)):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    # Try to convert matrices to NumPy arrays with dtype=float
    try:
        a = np.array(m_a, dtype=float)
        b = np.array(m_b, dtype=float)
    except ValueError:
        raise ValueError("invalid data type for einsum")

    # Ensure that the matrices have compatible shapes for multiplication
    if a.shape[1] != b.shape[0]:
        raise ValueError(
            f"shapes {a.shape} and {b.shape} not aligned: {a.shape[1]} (dim 1) != {b.shape[0]} (dim 0)")

    # Perform matrix multiplication using np.dot
    return np.dot(a, b)
