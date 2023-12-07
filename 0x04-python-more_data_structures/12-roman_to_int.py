#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str) or \
            len(roman_string) == 0:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    key_list = list(roman)
    sum = 0
    for c in range(len(roman_string)):
        for i in range(len(key_list)):
            if roman_string[c] == key_list[i]:
                if c != len(roman_string) - 1 and \
                        roman[roman_string[c]] < roman[roman_string[c + 1]]:
                    sum -= roman[key_list[i]]
                else:
                    sum += roman[key_list[i]]
    return sum
