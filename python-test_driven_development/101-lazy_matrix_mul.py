#!/usr/bin/python3
"""
This module defines a function for lazy matrix multiplication
using NumPy's dot function, with proper error handling and formatting.
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
    # Check if any element in m_a or m_b is a string
    try:
        # Convert both matrices to numpy arrays to check for type validity
        a = np.array(m_a, dtype=float)
        b = np.array(m_b, dtype=float)
    except ValueError:
        raise ValueError("invalid data type for einsum")

    try:
        # Now perform matrix multiplication with np.dot
        if a.ndim < 2 or b.ndim < 2:
            raise ValueError(
                "Scalar operands are not allowed, use '*' instead")

        return np.dot(a, b)  # Return the result as a NumPy array

    except TypeError:
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    except ValueError as e:
        # Let NumPy's error message be raised for shape mismatch
        raise
