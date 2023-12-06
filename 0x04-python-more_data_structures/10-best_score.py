#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return
    else:
        count = 0
        for x, y in a_dictionary.items():
            if count == 0:
                biggest = y
                name = x
            if y > biggest:
                biggest = y
                name = x
            else:
                count += 1
    return name
