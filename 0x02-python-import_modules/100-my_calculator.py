#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    len_ = len(sys.argv)
    if len_ < 3:
        sys.stdout.write("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        sys.stdout.flush()
        sys.exit(1)
    else:
        for i in range(len_):
            if i > 1:
                if sys.argv[i] == '+':
                    a = int(sys.argv[1])
                    b = int(sys.argv[3])
                    print("{:d} + {:d} = {:d}".format(a, b,  add(a, b)))
                    sys.exit(0)
                elif sys.argv[i] == '-':
                    a = int(sys.argv[1])
                    b = int(sys.argv[3])
                    print("{:d} - {:d} = {:d}".format(a, b,  sub(a, b)))
                    sys.exit(0)
                elif sys.argv[i] == '*':
                    a = int(sys.argv[1])
                    b = int(sys.argv[3])
                    print("{:d} * {:d} = {:d}".format(a, b,  mul(a, b)))
                    sys.exit(0)
                elif sys.argv[i] == '/':
                    a = int(sys.argv[1])
                    b = int(sys.argv[3])
                    print("{:d} / {:d} = {:d}".format(a, b,  div(a, b)))
                    sys.exit(0)
                elif sys.argv[i] != '+' or sys.argv[i] != '-' or sys.argv[i] != '*' or sys.argv[i] != '/':
                    sys.stdout.write(
                        "Unknown operator. Available operators: +, -, * and /\n")
                    sys.stdout.flush()
                    sys.exit(1)
