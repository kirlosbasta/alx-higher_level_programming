#!/usr/bin/python3
"""Module contain Rectangle class"""


class Rectangle:
    """Define a Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """return the area of rectangle"""
        return self.height * self.width

    def perimeter(self):
        """return the perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        rec = ""
        for i in range(self.height):
            for j in range(self.width):
                rec += str(self.print_symbol)
            if i != self.height - 1:
                rec += '\n'
        return rec

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
