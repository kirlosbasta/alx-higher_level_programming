#!/usr/bin/python3
"""Magic class demo"""
import math


class MagicClass:
    """Magic class demo"""

    def __init__(self, radius=0):
        """initialize the radius"""
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        self.radius = radius

    def area(self):
        """Calculate the area"""
        return math.pi * self.radius ** 2

    def circumference(self):
        """Calculate the circumference"""
        return math.pi * self.radius * 2
