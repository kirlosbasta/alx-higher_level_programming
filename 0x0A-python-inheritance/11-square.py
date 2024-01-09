#!/usr/bin/python3
"""Module contain BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class that has Square feature and inherits
    from rectangle
    """
    def __init__(self, size):
        """initalize each instantiation with size"""

        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        """return the area of square"""

        return self.__size ** 2

    def __str__(self):
        """print user friendly representation of square"""

        return "[Square] {}/{}".format(self.__size, self.__size)
