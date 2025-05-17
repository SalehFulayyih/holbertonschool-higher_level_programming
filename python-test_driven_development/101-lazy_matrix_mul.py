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
        ValueError: If the matrices can't be multiplied or input is invalid.
    """
    try:
        # Convert to NumPy arrays and validate types
        a = np.array(m_a)
        b = np.array(m_b)

        # If inputs are scalar or not at least 2D (like string or int), raise ValueError
        if a.ndim < 2 or b.ndim < 2:
            raise ValueError(
                "Scalar operands are not allowed, use '*' instead")

        return np.matmul(a, b)
    except TypeError:
        raise ValueError("Scalar operands are not allowed, use '*' instead")
    except ValueError as e:
        # Handle shape mismatch or invalid dimensions
        if "matmul" in str(e):
            raise ValueError("m_a and m_b can't be multiplied")
        raise
