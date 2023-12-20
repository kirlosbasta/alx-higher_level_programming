#!/usr/bin/python3
"""This is a demo module for square class with private size"""


class Square:
    """Square class with size"""

    def __init__(self, size=0):
        """initalize a new square

            Args:
                size(int): The size of square
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Return the size of square"""
        return self.__size ** 2
