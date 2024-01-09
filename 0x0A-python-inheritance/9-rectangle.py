#!/usr/bin/python3
"""Module contain BaseGeometry class"""


class BaseGeometry:
    """Class that has basic geometry features"""

    def area(self):
        """raise an Exception message"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validate value
        Args:
            name: string
            value: must be more that 0
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """Class that has Rectangle features"""

    def __init__(self, width, height):
        """initalize each instantiation with"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """return the area of rectangle"""

        return self.__height * self.__width

    def __str__(self):
        """print user friendly representation of Rectangle"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
