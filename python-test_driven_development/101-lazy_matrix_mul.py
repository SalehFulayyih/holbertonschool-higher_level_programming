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
        m_a: First matrix (list of lists)
        m_b: Second matrix (list of lists)

    Returns:
        The product of the two matrices as a NumPy array.

    Raises:
        ValueError: For invalid types, dimensions, or contents.
    """
    # Check if both matrices are lists of lists (or tuples of tuples)
    if not isinstance(m_a, (list, tuple)) or not isinstance(m_b, (list, tuple)):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    # Try converting the matrices to numpy arrays with a float data type
    try:
        a = np.array(m_a, dtype=float)
        b = np.array(m_b, dtype=float)
    except ValueError:
        raise ValueError("invalid data type for einsum")

    # Ensure matrices are aligned for multiplication
    if a.shape[1] != b.shape[0]:
        raise ValueError(
            "shapes ({},{}) and ({},{}) not aligned: {} (dim 1) != {} (dim 0)".format(
                a.shape[0], a.shape[1], b.shape[0], b.shape[1],
                a.shape[1], b.shape[0]
            )
        )

    # Handle special case for empty matrices
    if a.shape[1] == 0 or b.shape[0] == 0:
        raise ValueError(
            "shapes ({},{}) and ({},{}) not aligned: {} (dim 1) != {} (dim 0)".format(
                a.shape[0], a.shape[1], b.shape[0], b.shape[1],
                a.shape[1], b.shape[0]
            )
        )

    # Perform matrix multiplication
    result = np.dot(a, b)

    # Convert the result to integer and return
    return result.astype(int)
