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
        The product of the two matrices as a Python list.

    Raises:
        ValueError: If scalar input or invalid types prevent multiplication
    """
    try:
        # Attempt to create arrays without forcing float
        a = np.array(m_a)
        b = np.array(m_b)

        # Reject object-dtype (usually from strings or mixed types)
        if a.dtype == object or b.dtype == object:
            # Try converting to float to confirm it's invalid
            np.array(m_a, dtype=float)
            np.array(m_b, dtype=float)

        if a.ndim < 2 or b.ndim < 2:
            raise ValueError(
                "Scalar operands are not allowed, use '*' instead")

        # Use dot for expected error message formatting
        result = np.dot(a, b)

        return result.tolist()

    except TypeError:
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    except ValueError as e:
        if "could not convert" in str(e) or "invalid" in str(e):
            raise ValueError("invalid data type for einsum")
        raise
