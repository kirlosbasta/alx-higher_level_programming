#!/usr/bin/python3
def islower(c):
    """Return True if c is lowercase"""
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False
