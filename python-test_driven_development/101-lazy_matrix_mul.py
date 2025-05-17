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
    # First, reject scalar-like inputs (like strings or numbers)
    if not isinstance(m_a, (list, tuple)) or not isinstance(m_b, (list, tuple)):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    try:
        # Try converting to float to catch invalid strings like "6"
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
        raise  # Let NumPy's shape error message show
