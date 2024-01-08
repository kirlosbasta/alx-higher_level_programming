#!/usr/bin/python3
"""Module has is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of or inhirited
    from a_class
    Args:
        obj: an object
        a_class: a class
    """
    return isinstance(obj, a_class)
