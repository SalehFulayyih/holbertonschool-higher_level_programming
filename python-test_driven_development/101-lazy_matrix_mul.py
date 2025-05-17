#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy's matmul function.
    
    Args:
        m_a: First matrix
        m_b: Second matrix

    Returns:
        The product of the two matrices.
    """
    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e
