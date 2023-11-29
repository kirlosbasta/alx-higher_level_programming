#!/usr/bin/python3
def print_last_digit(number):
    """Print and return the last digit of number"""
    digit = abs(number) % 10
    print("{:d}".format(digit), end="")
    return digit
