#!/usr/bin/python3
"""Module contain a funtion"""


def add_attribute(self, var, value):
    """
    set a new attribute to obj if possible
    Args:
        var: new variable
        value: value of var
    """
    if hasattr(self, '__dict__'):
        self.__dict__[var] = value
    else:
        raise TypeError("can't add new attribute")
