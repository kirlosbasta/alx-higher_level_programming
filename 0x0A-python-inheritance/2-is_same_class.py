#!/usr/bin/python3
"""Exact same object"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly
    an instance of the specified class otherwise False
    Args:
        obj: any object
        a_class: any class
    Return: True or False
    """
    return type(obj) is a_class
