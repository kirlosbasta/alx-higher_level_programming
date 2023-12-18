#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Return the result of division of two list"""
    result = []
    for i in range(list_length):
        try:
            item = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            item = 0
        except TypeError:
            print("wrong type")
            item = 0
        except ZeroDivisionError:
            print('division by 0')
            item = 0
        finally:
            result.append(item)
    return result
