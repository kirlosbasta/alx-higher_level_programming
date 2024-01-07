#!/usr/bin/python3
"""Say may name module contain one function
say_my_name(first_name, last_name="")
"""


def say_my_name(first_name, last_name=""):
    """Print a string contain first and last name

        My name is <first name> <last name>

        Args:
            first_name: str
            last_name: str
    """
    if first_name is None or not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print(f'My name is {first_name} {last_name}')
