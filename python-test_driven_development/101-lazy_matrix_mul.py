#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices."""
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("Both m_a and m_b must be lists")
    if isinstance(m_a, str) or isinstance(m_b, str):
        raise ValueError("Scalar operands are not allowed, use '*' instead")
    return np.matmul(m_a, m_b)
