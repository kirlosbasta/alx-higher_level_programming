#!/usr/bin/python3
"""Module for locked Class only"""


class LockedClass:
    """Class that can set only first_name as it attribute any thing
        else raise attribute error
    """
    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError('object has no attribute {}'.format(name))
        self.__dict__[name] = value
