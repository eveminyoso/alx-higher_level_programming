#!/usr/bin/python3
import sys
length = len(sys.argv)
if __name__ == '__main__':
    if length == 1:
        print("0 arguments.")
    elif length == 2:
        print("1 argument:")
        print("{:d}:".format(1) + " {:s}".format(sys.argv[1]))
    else:
        print("{:d}".format(length - 1) + " arguments:")
        for i in range(length):
            if i != 0:
                print("{:d}:".format(i) + " {:s}".format(sys.argv[i]))
