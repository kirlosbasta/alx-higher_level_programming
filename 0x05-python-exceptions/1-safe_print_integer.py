#!/usr/bin/python3
def safe_print_integer(value):
    """print and return True if value is intger and false if not"""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
