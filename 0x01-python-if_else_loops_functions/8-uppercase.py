#!/usr/bin/python3
def uppercase(str):
    print('{}'.format(''.join([chr(ord(a) - 32) if ord(a)
          in range(97, 123) else a for a in str])))
