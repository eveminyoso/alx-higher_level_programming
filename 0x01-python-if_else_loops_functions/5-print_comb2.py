#!/usr/bin/python3
for i in range(100):
    if i < 10:
        print("{:2d}".format(i), end=", ")
    elif i == 99:
        print("{:d}".format(i))
    else:
        print("{:d}".format(i), end=", ")
