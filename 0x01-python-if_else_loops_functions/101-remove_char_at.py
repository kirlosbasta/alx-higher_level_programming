#!/usr/bin/python3
def remove_char_at(str, n):
    """Remove char at n and print the remaining"""
    if (n > len(str)):
        return str
    new_str = ""
    for i in range(len(str)):
        if i != n:
            new_str += str[i]
    return new_str
