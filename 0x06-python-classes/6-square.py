#!/usr/bin/python3
"""This is a demo module for square class with private size"""


class Square:
    """Square class with size"""

    def __init__(self, size=0, position=(0, 0)):
        """initalize a new square

            Args:
                size(int): The size of square
                position(tuple): poistion of the square
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """Return the size of square"""

        return self.__size

    @size.setter
    def size(self, val):
        """Validate the size"""

        if not isinstance(val, int):
            raise TypeError('size must be an integer')
        elif val < 0:
            raise ValueError('size must be >= 0')
        self.__size = val

    @property
    def position(self):
        """return the position of the square"""

        return self.__position

    @position.setter
    def position(self, value):
        """set the position correctly"""

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """Return the size of square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square"""

        for i in range(self.__size):
            if not self.__position[1] > 0:
                print(" " * self.__position[0], end='')
            for j in range(self.__size):
                print('#', end='')
            print('')
        if self.__size == 0:
            print('')
