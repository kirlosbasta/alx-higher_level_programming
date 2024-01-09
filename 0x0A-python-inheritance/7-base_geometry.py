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
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
