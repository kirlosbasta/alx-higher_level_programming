#!/usr/bin/python3
import sys
argv = sys.argv
if __name__ == '__main__':
    length = len(argv)
    sum = 0
    if length > 1:
        for i in range(1, length):
            sum += int(argv[i])
        print("{:d}".format(sum))
    else:
        print("0")
