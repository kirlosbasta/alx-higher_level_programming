#!/usr/bin/python3
"""Module for locked Class only"""


class LockedClass:
    """Class that can set only first_name as it attribute any thing
        else raise attribute error
    """

    __slots__ = ["first_name"]
