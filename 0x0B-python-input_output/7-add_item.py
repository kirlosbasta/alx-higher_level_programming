#!/usr/bin/python3
'''
Write a script that adds all arguments to a Python list,
and then save them to a file:

You must use your function save_to_json_file from 5-save_to_json_file.py
You must use your function load_from_json_file from 6-load_from_json_file.py
The list must be saved as a JSON representation in a file named add_item.json
If the file doesn’t exist, it should be created
You don’t need to manage file permissions / exceptions.

'''
import json
import sys
import os


def main():
    '''entry point'''
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').\
        load_from_json_file
    arg_list = sys.argv[1:]
    filename = 'add_item.json'
    if os.path.exists(filename):
        old_list = load_from_json_file(filename)
    else:
        old_list = []
    old_list.extend(arg_list)
    save_to_json_file(old_list, filename)


if __name__ == '__main__':
    main()
