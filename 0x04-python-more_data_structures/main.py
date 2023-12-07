#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "MCMXII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MMXXIII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MCM"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XXXIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MMMCMXCIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))