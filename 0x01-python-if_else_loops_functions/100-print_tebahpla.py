#!/usr/bin/python3
print('{}'.format(''.join([chr(a - 32) if a % 2 != 0 else chr(a)
      for a in range(122, 96, -1)])), end='')
