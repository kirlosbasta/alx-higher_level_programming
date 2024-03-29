#!/usr/bin/python3
'''Search and update'''


def append_after(filename="", search_string="", new_string=""):
    '''
    inserts a line of text to a file, after each line containing
    a specific string
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        old_lines = f.readlines()
        new_lines = []
        for line in old_lines:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
