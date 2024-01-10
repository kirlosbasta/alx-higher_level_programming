#!/usr/bin/python3
'''Pascal's Triangle'''


def pascal_triangle(n):
    '''
    returns a list of lists of integers representing the
    Pascal’s triangle of n
    Args:
        n: integer greater than 0
    '''
    tri = []
    if n is None or n <= 0:
        return tri
    for i in range(n):
        s_list = []
        if i == 0:
            s_list.append(1)
        elif i == 1:
            s_list = [1, 1]
        else:
            prev = tri[i - 1]
            for x in range(len(prev)):
                if x == 0 or x == len(prev) - 1:
                    s_list.append(prev[x])
                if x != len(prev) - 1:
                    s_list.append(prev[x] + prev[x + 1])
        tri.append(s_list)
    return tri
