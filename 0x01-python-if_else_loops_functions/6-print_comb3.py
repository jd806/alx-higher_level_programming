#!/usr/bin/python3
print(', '.join([f'{i:d}{j:d}' for i in range(0, 8)
      for j in range(i+1, 10)] + ['89']))
