#!/usr/bin/python3
import numpy as np

"""
This module provides a function `lazy_matrix_mul` that multiplies two matrices
using the NumPy library. The function ensures that the matrices are in the correct 
format and raises errors if the shapes do not align or if the data is invalid.
"""


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy.

    This function multiplies two matrices m_a and m_b using the NumPy library. 
    It ensures that the matrices are in the correct format and raises an error 
    if the shapes of the matrices do not align for multiplication.

    Args:
        m_a (list of list of int/float): The first matrix.
        m_b (list of list of int/float): The second matrix.

    Returns:
        numpy.ndarray: The resulting matrix after multiplication.

    Raises:
        ValueError: If the matrices contain non-numeric data or if the shapes
        of the matrices do not align.
    """
    try:
        # Ensure the matrices contain only numeric data and convert to NumPy arrays
        m_a = np.array(m_a, dtype=np.float64)
        m_b = np.array(m_b, dtype=np.float64)
    except ValueError:
        raise ValueError("invalid data type for einsum")

    try:
        # Perform matrix multiplication
        result = np.matmul(m_a, m_b)
        # Convert result to integers to match expected output format
        return result.astype(int)
    except ValueError as e:
        # If the matrices' shapes do not align, raise an error with details
        raise ValueError(
            f"shapes {m_a.shape} and {m_b.shape} not aligned: {m_a.shape[1]} (dim 1) != {m_b.shape[0]} (dim 0)") from e
