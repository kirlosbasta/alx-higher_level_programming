#!/usr/bin/python3
"""Module contain BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
