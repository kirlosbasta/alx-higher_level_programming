#!/usr/bin/python3
"""Module contain a class Mylist"""


class MyList(list):
    """Class that inhirite from list class
    function:
        print_sorted: prints the sorted list
    """
    def print_sorted(self):
        """print a sorted list"""

        print(sorted(self))
