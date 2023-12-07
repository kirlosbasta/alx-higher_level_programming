#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    all_weight = [x * y for x, y in my_list]
    weights = [y for x, y in my_list]
    return list_sum(all_weight) / list_sum(weights)


def list_sum(lis):
    sum = 0
    for i in lis:
        sum += i
    return sum
