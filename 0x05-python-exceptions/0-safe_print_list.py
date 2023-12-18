#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x == 0 or x < 0:
        return 0
    try:
        i = 0
        while i < x:
            print("{}".format(my_list[i]), end="")
            i += 1
        print("")
        return i
    except IndexError:
        if i > 0:
            print('')
        return i
