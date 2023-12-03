#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) == 0:
        return None
    elif idx < 0 or idx >= len(my_list):
        return my_list
    my_list.remove(my_list[idx])
    return my_list
