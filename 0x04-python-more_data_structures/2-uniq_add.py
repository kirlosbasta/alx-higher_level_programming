#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set(my_list)
    sum = 0
    for dig in uniq:
        sum += dig
    return sum
