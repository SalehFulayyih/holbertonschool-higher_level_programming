#!/usr/bin/python3
"""
Module for lazy matrix multiplication using NumPy.
This module defines a function lazy_matrix_mul that multiplies two matrices using NumPy.
"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    This function performs matrix multiplication on two matrices `m_a` and `m_b`
    using NumPy's `matmul` function. It raises an exception if the matrices have
    incompatible shapes or contain invalid data types.

    Args:
        m_a (list of list of int/float): The first matrix.
        m_b (list of list of int/float): The second matrix.

    Returns:
        numpy.ndarray: The result of multiplying matrices `m_a` and `m_b`.

    Raises:
        ValueError: If the matrices contain invalid data types or their shapes
                    do not align for multiplication.
    """
    
    # Ensure the matrices contain only numeric data
    try:
        m_a = np.array(m_a, dtype=np.float64)
        m_b = np.array(m_b, dtype=np.float64)
    except ValueError:
        raise ValueError("invalid data type for einsum")
    
    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        # If the matrices' shapes do not align, raise an error with details
        raise ValueError(
            f"shapes {m_a.shape} and {m_b.shape} not aligned: {m_a.shape[1]} (dim 1) != {m_b.shape[0]} (dim 0)"
        ) from e
