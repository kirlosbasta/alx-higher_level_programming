#!/usr/bin/python3
def uppercase(str):
    """convert a string to uppercase"""
    new_str = ""
    for i in range(len(str)):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            new_str += chr(ord(str[i]) - 32)
        else:
            new_str += str[i]
    print("{:s}".format(new_str))
