#!/usr/bin/python3
'''
reads stdin line by line and computes metrics
'''
import sys


def print_result(status, file_size):
    '''print the meterics'''
    print('File size: {}'.format(file_size))
    for key in sorted(status):
        if status[key] != 0:
            print(f'{key}: {status[key]}')


def main():
    file_size = 0
    status = {'200': 0, '301': 0, '400': 0, '401': 0,
              '403': 0, '404': 0, '405': 0, '500': 0}
    counter = 0
    try:
        for line in sys.stdin:
            splited_line = line.split(' ')
            status[splited_line[7]] += 1
            file_size += int(splited_line[8])
            counter += 1
            if counter == 10:
                print_result(status, file_size)
                counter = 0

    finally:
        print_result(status, file_size)


if __name__ == '__main__':
    main()
