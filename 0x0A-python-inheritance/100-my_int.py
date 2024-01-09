#!/usr/bin/python3
"""Module that has MyInt class"""


class MyInt(int):
    """class that inherits from int and extend it features"""

    def __eq__(self, other):
        """return true if both are not equal"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """return True if both equal"""
        return int.__eq__(self, other)
