#!/usr/bin/python3
"""Module contain print square function"""


def print_square(size):
    """prints a square with the character #
        Args:
            size: size length of the square
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print('')
