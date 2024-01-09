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
