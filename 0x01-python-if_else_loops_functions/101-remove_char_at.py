#!/usr/bin/python3
def remove_char_at(str, n):
    """Remove char at n and print the remaining"""
    new_str = ""
    for i in range(len(str)):
        if i != n:
            new_str += str[i]
    print("{}".format(new_str))
