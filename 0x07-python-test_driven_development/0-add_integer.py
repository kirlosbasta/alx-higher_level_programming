#!/usr/bin/python3
"""This module about add_integer and how to set up
doctest for this matter
and perpare for the real world
task and think of all the possible edge cases
"""


def add_integer(a, b=98):
    """Return the sum of two integer a and b
    Args:
        a: integer or float
        b: integer or float
    """
    if a is None or not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError('a must be an integer')
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
