#!/usr/bin/python3
def uppercase(str):
    result = [chr(ord(i) - 32) if 'a' <= i <= 'z' else i for i in str]
    print(''.join(result))
