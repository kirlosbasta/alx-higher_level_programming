#!/usr/bin/python3
"""This is a demo module for square class with private size"""


class Square:
    """Square class with size"""

    def __init__(self, size=0):
        """initalize a new square

            Args:
                size(int): The size of square
        """

        self.size = size

    @property
    def size(self):
        """Return the size of square"""

        return self.__size

    @size.setter
    def size(self, val):
        """Validate the size"""

        if not isinstance(val, int) or not isinstance(val, float):
            raise TypeError('size must be a number')
        elif val < 0:
            raise ValueError('size must be >= 0')
        self.__size = val

    def area(self):
        """Return the size of square"""
        return self.__size ** 2

    def __eq__(self, other):
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
