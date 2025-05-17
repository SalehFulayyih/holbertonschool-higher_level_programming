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
        ValueError: If the inputs are invalid or cannot be multiplied
    """
    try:
        a = np.array(m_a)
        b = np.array(m_b)

        # Raise custom error if scalar-like input
        if a.ndim < 2 or b.ndim < 2:
            raise ValueError(
                "Scalar operands are not allowed, use '*' instead")

        # Let NumPy raise its native ValueError if shapes don't match
        return np.matmul(a, b)

    except TypeError:
        raise ValueError("Scalar operands are not allowed, use '*' instead")
