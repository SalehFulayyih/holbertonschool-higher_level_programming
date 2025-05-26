#!/usr/bin/python3
"""
a class MyInt that inherits from int
"""


class MyInt(int):
    """Inherit Class"""

    def __eq__(self, other):
        return int(self) != int(other)

    def __ne__(self, other):
        return int(self) == int(other)
