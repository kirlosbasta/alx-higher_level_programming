#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev_list = my_list
    rev_list.reverse()
    for x in rev_list:
        print("{:d}".format(x))
