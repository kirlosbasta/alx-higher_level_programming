#!/usr/bin/pyhton3
"""Module contain Text_indentation function"""


def text_indentation(text):
    """prints a text with 2 new lines after each of
        these characters: ., ? and :
        Args:
            text: Str
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    to_print = ""
    start = 0
    for i in range(len(text)):
        if text[i] != ' ' or start != 0:
            start = 1
            to_print += text[i]

        if text[i] in '.?:':
            print(to_print + '\n')
            to_print = ""
            start = 0
        elif i == len(text) - 1:
            print(to_print, end='')
