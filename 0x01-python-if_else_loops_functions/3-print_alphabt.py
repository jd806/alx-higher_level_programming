#!/usr/bin/python3
print(''.join([chr(a) for a in range(97, 123)
               if a not in [101, 113]]), end="")
