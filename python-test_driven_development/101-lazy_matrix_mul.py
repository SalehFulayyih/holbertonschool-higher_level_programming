#!/usr/bin/python3
"""
This module defines a function for lazy matrix multiplication
using NumPy's dot function to preserve expected error messages
used in test-driven development.
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
        ValueError: If the inputs are scalars or if dot cannot multiply them
    """
    try:
        a = np.array(m_a)
        b = np.array(m_b)

        if a.ndim < 2 or b.ndim < 2:
            raise ValueError(
                "Scalar operands are not allowed, use '*' instead")

        return np.dot(a, b)

    except TypeError:
        raise ValueError("Scalar operands are not allowed, use '*' instead")
