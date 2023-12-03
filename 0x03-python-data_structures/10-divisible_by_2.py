#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None
    result = []
    for x in my_list:
        if x % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
