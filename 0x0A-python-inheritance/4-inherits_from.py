#!/usr/bin/python3
"""Module has inherits_from function"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance inhirited
    from a_class directly or indirectly otherwise False
    Args:
        obj: an object
        a_class: a class
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
