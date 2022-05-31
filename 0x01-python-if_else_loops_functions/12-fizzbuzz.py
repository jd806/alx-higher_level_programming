#!/usr/bin/env python3
def fizzbuzz():
    print(' '.join(['Fizz' if a % 3 == 0 else 'Buzz' if a %
                    5 == 0 else str(a) for a in range(1, 101)]), end=' ')
