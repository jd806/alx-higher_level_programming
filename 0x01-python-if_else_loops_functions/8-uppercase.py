def uppercase(str):
    print(''.join([chr(ord(a) - 32) if ord(a)
          in range(97, 123) else a for a in str]))
