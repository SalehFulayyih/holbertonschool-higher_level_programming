import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy."""

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
            f"shapes {m_a.shape} and {m_b.shape} not aligned: {m_a.shape[1]} (dim 1) != {m_b.shape[0]} (dim 0)") from e
