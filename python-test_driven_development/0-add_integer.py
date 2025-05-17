#!/usr/bin/python3
"""
Module that adds two integers or floats.
"""


def add_integer(a, b=98):
    """
    Returns the sum of two integers or floats after casting them to integers.

    Args:
        a (int, float): The first number.
        b (int, float): The second number (default is 98).

    Raises:
        TypeError: If either a or b is not an integer or float.

    Returns:
        int: The sum of a and b after casting them to integers.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
