#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    dir_list = dir(hidden_4)
    for i in range(len(dir_list)):
        if dir_list[i][0] != '_' and dir_list[i][1] != '_':
            print("{:s}".format(dir_list[i]))
