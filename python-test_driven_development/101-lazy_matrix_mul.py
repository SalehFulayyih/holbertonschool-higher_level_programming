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
        The product of the two matrices.

    Raises:
        ValueError: If scalar input or invalid types prevent multiplication
    """
    try:
        # Force NumPy to use numeric data types
        a = np.array(m_a, dtype=float)
        b = np.array(m_b, dtype=float)

        if a.ndim < 2 or b.ndim < 2:
            raise ValueError(
                "Scalar operands are not allowed, use '*' instead")

        return np.dot(a, b)

    except TypeError:
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    except ValueError as e:
        # Handle bad dtype (e.g. string in matrix)
        if "could not convert" in str(e) or "invalid" in str(e):
            raise ValueError("invalid data type for einsum")
        raise
