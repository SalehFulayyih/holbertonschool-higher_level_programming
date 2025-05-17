#!/usr/bin/python3
"""
This module defines a function for lazy matrix multiplication
using NumPy's dot function to preserve expected error messages.
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
    try:
        # Try converting to float arrays first to catch string data like "6"
        np.array(m_a, dtype=float)
        np.array(m_b, dtype=float)
    except Exception:
        raise ValueError("invalid data type for einsum")

    try:
        a = np.array(m_a)
        b = np.array(m_b)

        if a.ndim < 2 or b.ndim < 2:
            raise ValueError(
                "Scalar operands are not allowed, use '*' instead")

        return np.dot(a, b)

    except TypeError:
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    except ValueError as e:
        # Let NumPy raise shape errors naturally
        raise
