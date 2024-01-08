#!/usr/bin/python3
"""Contain lookup function"""


def lookup(obj):
    """
    returns the list of available attributes
    and methods of an object
    Args:
        obj: Any object type
    Return: list of available attributes and methods
    """
    return dir(obj)
